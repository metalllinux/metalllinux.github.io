---
title: "Setting Up Keepalived For Load Balancing"
category: "general-linux"
tags: ["setting", "keepalived", "load", "balancing"]
---

* Install the `keepalived` package:
```
sudo dnf install -y keepalived
```
* Else, build from source:
* Install pre-requisitive building packages:
```
sudo dnf install -y gcc openssl-devel
```
* Get the latest tarball (version `2.3.2` at the time of writing):
```
wget https://www.keepalived.org/software/keepalived-2.3.2.tar.gz
```
* Extract the tarball:
```
tar -xvf keepalived-2.3.2.tar.gz
```
* Change into the tarball directory:
```
cd keepalived-2.3.2/
```
* Run `./configure`:
```
./configure
```
* Build and install the package:
```
make
sudo make install
```
* Check the `keepalived` version:
```
keepalived --version
```
* As an example, create two servers that will share the same IP address.
* Below is the configuration for Server1:
```
sudo tee -a /etc/keepalived/keepalived.conf <<EOF
vrrp_instance VI_1 {
        state MASTER
        interface enp8s0
        virtual_router_id 51
        priority 100
        advert_int 1
        authentication {
              auth_type PASS
              auth_pass 12345
        }
        virtual_ipaddress {
              10.25.96.10/20
        }
}

virtual_server 10.25.96.10 22 {
    delay_loop 10
    lvs_sched lc
    lvs_method DR
    persistence_timeout 9600
    protocol TCP

    real_server 10.25.96.5 22 {
        weight 1
        TCP_CHECK {
            connect_timeout 10
            connect_port 22
        }
    }
}
EOF
```
* This is the configuration for Server 2, the only differences are `state` is set to `BACKUP` and `priority` is set to `99`.
```
sudo tee -a /etc/keepalived/keepalived.conf <<EOF
vrrp_instance VI_1 {
        state BACKUP
        interface enp8s0
        virtual_router_id 51
        priority 99
        advert_int 1
        authentication {
              auth_type PASS
              auth_pass 12345
        }
        virtual_ipaddress {
              10.25.96.10/20
        }
}

virtual_server 10.25.96.10 22 {
    delay_loop 10
    lvs_sched lc
    lvs_method DR
    persistence_timeout 9600
    protocol TCP

    real_server 10.25.96.5 22 {
        weight 1
        TCP_CHECK {
            connect_timeout 10
            connect_port 22
        }
    }
}
EOF
```
* Allow `vrrp` traffic via `Firewalld`:
```
firewall-cmd --permanent --add-rich-rule='rule protocol value="vrrp" accept' 
firewall-cmd --reload
```
* Start and enable the `keepalived` service on both Load Balancers:
```
systemctl enable --now keepalived
```
* Check the IP address information of each Load Balancer server, to ensure the `vrrp` address has been assigned to the `MASTER` server and not the `BACKUP` server.
```
ip -brief address show
```
* The `MASTER` server will look like the below example:
```
[root@Rocky-Linux-8-10-Load-Balancer-1 keepalived-2.3.2]# ip -brief address show
lo               UNKNOWN        127.0.0.1/8 ::1/128 
enp1s0           UP             64.176.44.36/23 fe80::5400:5ff:fe38:ccd2/64 
enp8s0           UP             10.25.96.3/20 10.25.96.10/24 fe80::5800:5ff:fe38:ccd2/64
```
* The `BACKUP` server will look like this:
```
[root@Rocky-Linux-8-10-Load-Balancer-2 keepalived-2.3.2]# ip -brief address show
lo               UNKNOWN        127.0.0.1/8 ::1/128 
enp1s0           UP             64.176.37.104/23 fe80::5400:5ff:fe38:ccf8/64 
enp8s0           UP             10.25.96.4/20 fe80::5800:5ff:fe38:ccf8/64
```
* To test failover functionality, stop the `keepalived` service on the `MASTER` server:
```
systemctl stop keepalived
```
* Then check each server's IP information and you see that the `vrrp` address has been assigned to the `BACKUP` server:
```
[root@Rocky-Linux-8-10-Load-Balancer-1 keepalived-2.3.2]# ip -brief address show
lo               UNKNOWN        127.0.0.1/8 ::1/128 
enp1s0           UP             64.176.44.36/23 fe80::5400:5ff:fe38:ccd2/64 
enp8s0           UP             10.25.96.3/20 fe80::5800:5ff:fe38:ccd2/64
```
```
[root@Rocky-Linux-8-10-Load-Balancer-2 keepalived-2.3.2]# ip -brief address show
lo               UNKNOWN        127.0.0.1/8 ::1/128 
enp1s0           UP             64.176.37.104/23 fe80::5400:5ff:fe38:ccf8/64 
enp8s0           UP             10.25.96.4/20 10.25.96.10/24 fe80::5800:5ff:fe38:ccf8/64
```
* Install the `ipvsadm` package on both Load Balancer servers, to help setup the Virtual Server Table in the kernel:
```
sudo dnf install -y ipvsadm
```
* Create the `/etc/modules-load.d/ipvs.conf` file in both Load Balancer servers and add the `ip_vs` module:
```
tee -a /etc/modules-load.d/ipvs.conf <<EOF
ip_vs
EOF
```
* Enable IP Forwarding and the binding of non-local IP addresses on each Load Balancer server:
```
tee -a /etc/sysctl.conf <<EOF
net.ipv4.ip_forward = 1
net.ipv4.ip_nonlocal_bind = 1
EOF
```
* Make sure that IP Forwarding is set and loopback devices are hidden on any servers behind the Load Balancers:
```
tee -a /etc/sysctl.conf <<EOF
net.ipv4.ip_forward = 1
# Enable configuration of hidden devices
net.ipv4.conf.all.hidden = 1
# Make the loopback interface hidden
net.ipv4.conf.lo.hidden = 1
EOF
```
* `reboot` both Load Balancer servers and any servers behind the Load Balancers.
* Check that IP Forwarding and non-local binding work as expected. Each command should return the value of `1`:
```
/usr/sbin/sysctl net.ipv4.ip_forward
/usr/sbin/sysctl net.ipv4.ip_nonlocal_bind 
```
* Add the following script to the Login Node server behind the Load Balancers:
```
vim /usr/local/sbin/virtual_ip_setup.sh
```
```
_VIP=10.25.96.10
case $1 in
    start)
        echo "Configure loopback real IP from loadbalancer"
        echo '1' > /proc/sys/net/ipv4/conf/lo/arp_ignore
        echo '2' > /proc/sys/net/ipv4/conf/lo/arp_announce
        echo '1' > /proc/sys/net/ipv4/conf/all/arp_ignore
        echo '2' > /proc/sys/net/ipv4/conf/all/arp_announce
        /sbin/ip addr add ${_VIP}/32 dev lo
                ;;
    stop)
        echo "Unconfigure loopback real IP from loadbalancer"
        /sbin/ip addr del ${_VIP}/32 dev lo
        echo '0' > /proc/sys/net/ipv4/conf/lo/arp_ignore
        echo '0' > /proc/sys/net/ipv4/conf/lo/arp_announce
        echo '0' > /proc/sys/net/ipv4/conf/all/arp_ignore
        echo '0' > /proc/sys/net/ipv4/conf/all/arp_announce
        ;;
      *)
        echo "Usage: $0 {start|stop}"
        exit 1
esac
EOF
```
* Made the script executable:
```
chmod +x /usr/local/sbin/virtual_ip_setup.sh
```
* Run the script:
```
/usr/local/sbin/virtual_ip_setup.sh start
```
* Attempt to `ssh` into the server behind the Load Balancer servers, via the `virtual_server` IP set on the Load Balancers.
```
# From the client machine that wants to ssh into the Login Server
ssh 10.25.96.5 
```

