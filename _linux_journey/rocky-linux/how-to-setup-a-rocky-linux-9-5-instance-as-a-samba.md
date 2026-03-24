---
title: "How To Setup A Rocky Linux 9.5 Instance As A Samba"
category: "rocky-linux"
tags: ["rocky-linux", "setup", "rocky", "linux", "instance"]
---

* Create the user `test`:
```
useradd -m test
```
* Set a password:
```
passwd test
```
* Add the user to the `wheel` group:
```
usermod -aG wheel test
```
* Switch to the `test` user:
```
su - test
```
* Logged in to the VM as my `test` user and updated all packages in the VM:
```
sudo dnf upgrade -y
```
* Installed the required build tools:
```
sudo dnf groupinstall -y "Development Tools"
```
* Downloaded the latest samba tarball:
```
wget https://download.samba.org/pub/samba/samba-latest.tar.gz
```
* Extracted the tarball:
```
tar -xf ./samba-latest.tar.gz
```
* Changed into the directory:
```
cd samba-4.21.3/
```
* Bootstrapped further dependencies for Rocky Linux 9.5:
```
sudo ./bootstrap/generated-dists/centos9s/bootstrap.sh
```
* Built the package:
```
./configure
make
sudo make install
```
* Added to my $PATH:
```
export PATH=/usr/local/samba/bin/:/usr/local/samba/sbin/:$PATH
```
```
tee -a ~/.bashrc << EOF
export PATH=/usr/local/samba/bin/:/usr/local/samba/sbin/:$PATH
EOF
```
```
source ~/.bashrc
```
* Created the `systemd` service:
```
cat << "EOF" | sudo tee /etc/systemd/system/samba-ad-dc.service
[Unit]
Description=Samba Active Directory Domain Controller
After=network.target remote-fs.target nss-lookup.target

[Service]
Type=forking
ExecStart=/usr/local/samba/sbin/samba -D
PIDFile=/usr/local/samba/var/run/samba.pid
ExecReload=/bin/kill -HUP $MAINPID

[Install]
WantedBy=multi-user.target
EOF
```
* Reloaded the `systemd` configuration:
```
sudo systemctl daemon-reload
```
* Disabled `resolvconf` in `NetworkManager`:
```
sudo tee -a /etc/NetworkManager/conf.d/90-dns-none.conf << EOF
[main]
dns=none
EOF
```
* Restarted `NetworkManager`:
```
sudo systemctl reload NetworkManager
```
* Added the IP and information of my VM to `/etc/hosts`:
```
sudo tee -a /etc/hosts << EOF
45.32.54.22   rockyvm.metalinux.online   rockyvm
EOF
```
* Change to the `root` user:
```
su - root
```
* Add the Samba path:
```
tee -a ~/.bashrc << EOF
export PATH=/usr/local/samba/bin/:/usr/local/samba/sbin/:$PATH
EOF
```
* Source it:
```
source ~/.bashrc
```
* I provisioned Samba AD in Non-interactive Mode:
```
samba-tool domain provision --server-role=dc --use-rfc2307 --dns-backend=SAMBA_INTERNAL --realm=rockyvm.metalinux.online --domain=rockyvm --adminpass=<PASSWORD_HERE>
```
* I observed my credentials were available:
```
INFO 2025-01-21 07:43:13,462 pid:97089 /usr/local/samba/lib64/python3.9/site-packages/samba/provision/__init__.py #497: Server Role:           active directory domain controller
INFO 2025-01-21 07:43:13,462 pid:97089 /usr/local/samba/lib64/python3.9/site-packages/samba/provision/__init__.py #498: Hostname:              rocky-linux-95-vm
INFO 2025-01-21 07:43:13,462 pid:97089 /usr/local/samba/lib64/python3.9/site-packages/samba/provision/__init__.py #499: NetBIOS Domain:        ROCKYVM
INFO 2025-01-21 07:43:13,462 pid:97089 /usr/local/samba/lib64/python3.9/site-packages/samba/provision/__init__.py #500: DNS Domain:            rockyvm.metalinux.online
INFO 2025-01-21 07:43:13,462 pid:97089 /usr/local/samba/lib64/python3.9/site-packages/samba/provision/__init__.py #501: DOMAIN SID:            S-1-5-21-3926415524-2617884273-3524401500
```
* I configured the `DNS` Resolver:
```
sudo tee -a  /etc/resolv.conf  <<EOF
search rockyvm.metalinux.online
nameserver 64.176.57.117
EOF
```
* Configured Kerberos by coping the generated config into `/etc/krb5.conf`:
```
sudo cp /usr/local/samba/private/krb5.conf /etc/krb5.conf
```
* Edited the configuration, so that it looked like the below without the example:
```
[libdefaults]
    dns_lookup_realm = false
    dns_lookup_kdc = true
    default_realm = SAMDOM.EXAMPLE.COM
```
* Started the `samba` service:
```
sudo systemctl enable samba-ad-dc
```
* The Kerberos ticket can then be requested with the following command:
```
kinit administrator
```
* Similarly to list Kerberos tickets:
```
klist
```
* Finally to join an Active Directory as a Domain Controller, the following example command can be ran:
```
samba-tool domain join samdom.example.com DC -U"SAMDOM\administrator"
```