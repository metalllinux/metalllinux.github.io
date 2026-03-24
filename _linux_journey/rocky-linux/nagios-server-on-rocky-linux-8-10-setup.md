---
title: "Nagios Server On Rocky Linux 8.10 Setup"
category: "rocky-linux"
tags: ["rocky-linux", "nagios", "server", "rocky", "linux"]
---

* Upgraded all packages:
```
dnf upgrade -y
```
* I enabled FIPS:
```
fips-mode-setup --enable
```
* Rebooted the server:
```
reboot
```
* Ensured that `FIPS` mode was enabled:
```
[root@rocky-linux-810-fips-nagios-server ~]# fips-mode-setup --check

FIPS mode is enabled.
```
* I then followed the [Nagios Installation Guide](https://support.nagios.com/kb/article/nagios-core-installing-nagios-core-from-source-96.html#RHEL) and ran the following commands:
* Installed the required packages:
```
dnf install -y gcc glibc glibc-common perl httpd php wget gd gd-devel
dnf install -y openssl-devel
```
* Switched to the `tmp` directory:
```
cd /tmp
```
* Pulled the latest source code:
```
wget --output-document="nagioscore.tar.gz" $(wget -q -O - https://api.github.com/repos/NagiosEnterprises/nagioscore/releases/latest  | grep '"browser_download_url":' | grep -o 'https://[^"]*')
```
* Ran `tar -xzf` on the file:
```
tar xzf nagioscore.tar.gz
```
* Changed into the `cd /tmp/nagios-*` directory:
```
cd /tmp/nagios-*
```
* Compiled it successfully:
```
./configure
make all
```
* Created the `nagios` user and group:
```
[root@rocky-linux-810-fips-nagios-server nagios-4.5.9]# make install-groups-users
groupadd -r nagios
useradd -g nagios nagios
```
* Added the `apache` user to the `nagios` group:
```
usermod -a -G nagios apache
```
* Installed all binaries:
```
make install
```
* Installed the `nagios` Daemon and enabled the `httpd.service`:
```
make install-daemoninit
systemctl enable httpd.service
```
* Installed Command Mode:
```
make install-commandmode
```
* Installed Configuration files:
```
make install-config
```
* Installed the Apache Web Server files:
```
make install-webconf
```
* I disabled `firewalld`, similarly to what you had performed on your system:
```
systemctl disable --now firewalld
```
* I disabled `SELinux`:
```
setenforce 0
sed -i 's/SELINUX=enforcing/SELINUX=permissive/' /etc/selinux/config
```
* Created the `nagiosadmin` account:
```
htpasswd -c /usr/local/nagios/etc/htpasswd.users nagiosadmin
```

* For the `Nagios` `nagios.cfg` file configuration, I went through the [Nagios Core configuration documentation in full](https://assets.nagios.com/downloads/nagioscore/docs/nagioscore/3/en/configmain.html) and
* My log file was stored under `/usr/local/nagios/var/nagios.log`
* I did not observe any changes of note aside from added object configuration commands in your `nagios.cfg` file, so I have not modified this file.
* I verified my configuration using `/usr/local/nagios/bin/nagios -v /usr/local/nagios/etc/nagios.cfg` and observed no Warnings or Errors:
```
Total Warnings: 0
Total Errors:   0

Things look okay - No serious problems were detected during the pre-flight check
```
* Similarly under `/etc/httpd/conf.d/nagios.conf`, I did not see any major changes required with your config file and have not changed it.

* Started the `httpd` service:
```
systemctl enable --now httpd.service
```
* Started the `Nagios` service:
```
systemctl enable --now nagios.service
```
* I set up a GUI on the `Nagios` server so I could easily access the `Nagios Web Interface`:
```
dnf group install -y "Server with GUI"
systemctl set-default graphical
reboot
```
* After opening `Firefox`, I was able to navigate to `localhost/nagios` and successfully log in using my `nagiosadmin` credentials.

* For the `Nagios` plugin installation, I followed these steps:
* Installed the required packages:
```
dnf install -y gcc glibc glibc-common make gettext automake autoconf wget openssl-devel net-snmp net-snmp-utils
```
* Changed into the `/tmp` directory:
```
cd /tmp
```
* Downloaded the plugins tarball:
```
wget --output-document="nagios-plugins.tar.gz" $(wget -q -O - https://api.github.com/repos/nagios-plugins/nagios-plugins/releases/latest  | grep '"browser_download_url":' | grep -o 'https://[^"]*')
```
* Ran `tar -zxf` on the tarball:
```
tar zxf nagios-plugins.tar.gz
```
* I changed into the directory:
```
cd /tmp/nagios-plugins-*
```
* Successfully installed the packages with:
```
./configure
make
make install
```
* Confirmed the plugins were available at `/usr/local/nagios/libexec/`:
```
[root@rocky-linux-810-fips-nagios-server nagios-plugins-2.4.12]# ls -l /usr/local/nagios/libexec/ | wc -l
65
```
* Pulled down the latest version of the `nrpe` plugin:
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
make install-init
```
* Checked that the `Nagios` Server could connect to the Client:
```
/usr/local/nagios/libexec/check_nrpe -H 10.25.96.4 
```
* This was successful and I could connect to the non-FIPS node from the FIPS node:
```
[root@rocky-linux-810-fips-nagios-server nrpe-4.1.3]# /usr/local/nagios/libexec/check_nrpe -H 10.25.96.4 
NRPE v4.1.3

[root@rocky-linux-810-fips-nagios-server nrpe-4.1.3]# /usr/local/nagios/libexec/check_nrpe -H 10.25.96.4 -c check_users
USERS OK - 1 users currently logged in |users=1;5;10;0

[root@rocky-linux-810-fips-nagios-server nrpe-4.1.3]# /usr/local/nagios/libexec/check_nrpe -H 10.25.96.4 -c check_load
OK - load average per CPU: 0.00, 0.00, 0.00|load1=0.000;0.150;0.300;0; load5=0.000;0.100;0.250;0; load15=0.000;0.050;0.200;0; 
[root@rocky-linux-810-fips-nagios-server nrpe-4.1.3]# 
```