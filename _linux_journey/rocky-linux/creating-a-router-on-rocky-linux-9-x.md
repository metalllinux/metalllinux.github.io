---
title: "Creating A Router On Rocky Linux 9.X"
category: "rocky-linux"
tags: ["rocky-linux", "creating", "router", "rocky", "linux"]
---

* Enable IP Forwarding:
```
cat << "EOF" | sudo tee -a /etc/sysctl.conf
net.ipv4.ip_forward = 1
EOF
```
* Ensure Receive Offloading is disabled:
```
sudo ethtool -k ethX | grep -e lro -e gro
```
* Disable Reverse Path Filtering:
```
cat << "EOF" | sudo tee -a /etc/sysctl.conf
net.ipv4.conf.all.rp_filter = 0
net.ipv4.conf.default.rp_filter = 0
EOF
```
* Apply the changes:
```
sudo sysctl -p
```
* Check for any existing Reverse Path Filtering:
```
sudo sysctl -a | egrep "\.rp_filter"
```
* Escalate to `root`:
```
sudo su -
```
* Disable Reverse Path Filtering on those interfaces:
```
for TUNABLE in $(sysctl -a | awk '/\.rp_filter/{print $1}'); do sysctl -w "$TUNABLE=0"; done
```
* Exit out of `root`:
```
exit
```
* Add the external interface to the `external` `firewalld` zone:
```
sudo nmcli con add type ethernet autoconnect yes ifname enp4s0 con-name enp4s0 connection.zone external
```
* Check that the interface was set correctly:
```
nmcli -f connection.zone con show enp4s0
```
* Make sure that `masquerade` is equal to `yes`:
```
sudo firewall-cmd --list-all --zone=external | grep masquerade
```
* Assign static IPs to the internal interfaces:
```
sudo nmcli connection modify enp1s0f3 ipv4.addresses 192.168.1.108/24 ipv4.method manual

sudo nmcli connection modify enp1s0f2 ipv4.addresses 192.168.1.109/24 ipv4.method manual
```
* Configure the local interface:
```
sudo nmcli con modify enp1s0f3  ipv4.dns 9.9.9.9 autoconnect yes connection.zone internal

sudo nmcli con modify enp1s0f2  ipv4.dns 9.9.9.9 autoconnect yes connection.zone internal
```
* Check the connection was set to `internal`:
```
nmcli -f connection.zone con show enp1s0f3

nmcli -f connection.zone con show enp1s0f2
```
* Bring the internal connections up:
```
sudo nmcli connection up enp1s0f3

sudo nmcli connection up enp1s0f2
```