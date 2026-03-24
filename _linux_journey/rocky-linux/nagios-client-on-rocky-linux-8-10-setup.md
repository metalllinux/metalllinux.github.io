---
title: "Nagios Client On Rocky Linux 8.10 Setup"
category: "rocky-linux"
tags: ["rocky-linux", "nagios", "client", "rocky", "linux"]
---

* I followed [this guide](https://www.tecmint.com/how-to-add-linux-host-to-nagios-monitoring-server/) for setting up the Nagios client.
* Upgraded all packages:
```
dnf upgrade -y
```
* Installed required packages:
```
dnf install -y gcc glibc glibc-common gd gd-devel make net-snmp openssl-devel tar wget
dnf install -y make gettext automake autoconf wget openssl-devel net-snmp net-snmp-utils
```
* Created my `nagios` user:
```
useradd nagios
passwd nagios
```
* Installed all available plugins:
* Changed into `/tmp`:
```
cd /tmp
```
* Pulled the latest plugins tarball:
```
wget --output-document="nagios-plugins.tar.gz" $(wget -q -O - https://api.github.com/repos/nagios-plugins/nagios-plugins/releases/latest  | grep '"browser_download_url":' | grep -o 'https://[^"]*')
```
* Ran `tar -zxf`:
```
tar zxf nagios-plugins.tar.gz
```
* Changed directories:
```
cd /tmp/nagios-plugins-*
```
* Compiled the packages:
```
./configure
make
make install
```
* Set directory permissions for the `nagios` user:
```
chown nagios.nagios /usr/local/nagios
chown -R nagios.nagios /usr/local/nagios/libexec
```
* Pulled down the latest version of the `nrpe` plugin, which at the time of writing is `4.1.3`:
```
wget https://github.com/NagiosEnterprises/nrpe/releases/download/nrpe-4.1.3/nrpe-4.1.3.tar.gz
```
* Ran `tar -zxf`:
```
tar -zxf ./nrpe-4.1.3.tar.gz
```
* Changed directories:
```
cd nrpe-4.1.3/
```
* Compiled and installed `nrpe`:
```
./configure
make all
```
* Installed the plugin daemon and the sample config files:
```
make install-plugin
make install-daemon
make install-config
```
* Install the NRPE daemon as a `systemd` service:
```
make install-init
```
* Configured the NRPE plugin's configuration file at `/usr/local/nagios/etc/nrpe.cfg` and added the address of my `Nagios` server:
```
sed -i 's/allowed_hosts=127.0.0.1,::1/allowed_hosts=127.0.0.1,10.25.96.5/' /usr/local/nagios/etc/nrpe.cfg
```
* Enabled and then started the `nrpe` service:
```
systemctl enable --now nrpe
```
* I observed this started correctly from `journalctl -exu nrpe` and `netstat -at | grep nrpe`:
```
Jan 20 05:51:26 rocky-linux-810-non-fips-nagios-client nrpe[74633]: Starting up daemon
Jan 20 05:51:26 rocky-linux-810-non-fips-nagios-client nrpe[74633]: Server listening on 0.0.0.0 port 5666.
Jan 20 05:51:26 rocky-linux-810-non-fips-nagios-client nrpe[74633]: Server listening on :: port 5666.
Jan 20 05:51:26 rocky-linux-810-non-fips-nagios-client nrpe[74633]: Listening for connections on port 5666
Jan 20 05:51:26 rocky-linux-810-non-fips-nagios-client nrpe[74633]: Allowing connections from: 127.0.0.1,10.25.96.5

netstat -at | grep nrpe
tcp        0      0 0.0.0.0:nrpe            0.0.0.0:*               LISTEN     
tcp6       0      0 [::]:nrpe               [::]:*                  LISTEN
```
* Opened up required ports in the Firewall:
```
firewall-cmd --zone=public --add-port=5666/tcp --permanent
firewall-cmd --reload
```
* I ran `/usr/local/nagios/libexec/check_nrpe -H 127.0.0.1` to also check that `check_nrpe` was working correctly:
```
[root@rocky-linux-810-non-fips-nagios-client nrpe-4.1.3]# /usr/local/nagios/libexec/check_nrpe -H 127.0.0.1
NRPE v4.1.3
```
* Confirmed from multiple commands that the client was working as expected:
```
[root@rocky-linux-810-non-fips-nagios-client nrpe-4.1.3]# /usr/local/nagios/libexec/check_nrpe -H 127.0.0.1 -c check_users
USERS OK - 1 users currently logged in |users=1;5;10;0

[root@rocky-linux-810-non-fips-nagios-client nrpe-4.1.3]# /usr/local/nagios/libexec/check_nrpe -H 127.0.0.1 -c check_load
OK - load average per CPU: 0.00, 0.00, 0.00|load1=0.000;0.150;0.300;0; load5=0.000;0.100;0.250;0; load15=0.003;0.050;0.200;0;

[root@rocky-linux-810-non-fips-nagios-client nrpe-4.1.3]# /usr/local/nagios/libexec/check_nrpe -H 127.0.0.1 -c check_total_procs
PROCS OK: 140 processes | procs=140;150;200;0;

[root@rocky-linux-810-non-fips-nagios-client nrpe-4.1.3]# /usr/local/nagios/libexec/check_nrpe -H 127.0.0.1 -c check_zombie_procs
PROCS OK: 0 processes with STATE = Z | procs=0;5;10;0;
```