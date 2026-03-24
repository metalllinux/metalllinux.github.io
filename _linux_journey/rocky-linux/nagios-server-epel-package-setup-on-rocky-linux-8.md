---
title: "Nagios Server on Rocky Linux 9.5 FIPS with EPEL Packages Setup"
category: "rocky-linux"
tags: ["rocky-linux", "nagios", "server", "epel", "package"]
---

## Nagios Server on Rocky Linux 9.5 FIPS with EPEL Packages Setup
* I went through the exact same setup steps as I listed before.
* Enabled the EPEL repo:
```
dnf config-manager --set-enabled powertools
dnf install epel-release
```
* Installed the `nagios` package:
```
dnf install -y nagios
```
* Continued on from the "* Added the `apache` user to the `nagios` group:" step:
```
usermod -a -G nagios apache
```
* Enabled the `httpd.service` file:
```
systemctl enable httpd.service
```
* Disabled the firewall:
```
systemctl disable --now firewalld
```
* Disabled `SELinux`:
```
setenforce 0
sed -i 's/SELINUX=enforcing/SELINUX=permissive/' /etc/selinux/config
```
* Installed the `nagios-plugins-all` package:
```
dnf install -y nagios-plugins-all
```
* Installed the `nrpe` plugin:
```
dnf install -y nrpe
```
* No problems with the `nagios` configuration:
```
nagios -v /etc/nagios/nagios.cfg
Total Warnings: 0
Total Errors:   0
```
* Started the `httpd` service:
```
systemctl enable --now httpd.service
```
* Output from `systemctl status httpd`:
```
● httpd.service - The Apache HTTP Server
   Loaded: loaded (/usr/lib/systemd/system/httpd.service; enabled; vendor preset: disabled)
  Drop-In: /usr/lib/systemd/system/httpd.service.d
           └─php-fpm.conf
   Active: active (running) since Wed 2025-01-22 06:08:36 UTC; 4s ago
     Docs: man:httpd.service(8)
 Main PID: 5779 (httpd)
   Status: "Started, listening on: port 80"
    Tasks: 213 (limit: 48980)
   Memory: 44.6M
   CGroup: /system.slice/httpd.service
           ├─5779 /usr/sbin/httpd -DFOREGROUND
           ├─5785 /usr/sbin/httpd -DFOREGROUND
           ├─5786 /usr/sbin/httpd -DFOREGROUND
           ├─5787 /usr/sbin/httpd -DFOREGROUND
           └─5788 /usr/sbin/httpd -DFOREGROUND

Jan 22 06:08:36 rocky-linux-810-fips-nagios-server systemd[1]: Starting The Apache HTTP Server...
Jan 22 06:08:36 rocky-linux-810-fips-nagios-server httpd[5779]: AH00558: httpd: Could not reliably determine the server's fully qualified domain name, using ::1. Set the 'Serv>
Jan 22 06:08:36 rocky-linux-810-fips-nagios-server systemd[1]: Started The Apache HTTP Server.
```
* Started the `nagios` service:
```
systemctl enable --now nagios.service
```
* From `systemctl status nagios`, this also started without issue:
```
● nagios.service - Nagios Core 4.4.9
   Loaded: loaded (/usr/lib/systemd/system/nagios.service; enabled; vendor preset: disabled)
   Active: active (running) since Wed 2025-01-22 06:09:26 UTC; 13s ago
     Docs: https://www.nagios.org/documentation
  Process: 6040 ExecStart=/usr/sbin/nagios -d /etc/nagios/nagios.cfg (code=exited, status=0/SUCCESS)
  Process: 6038 ExecStartPre=/usr/sbin/nagios -v /etc/nagios/nagios.cfg (code=exited, status=0/SUCCESS)
 Main PID: 6041 (nagios)
    Tasks: 8 (limit: 48980)
   Memory: 7.1M
   CGroup: /system.slice/nagios.service
           ├─6041 /usr/sbin/nagios -d /etc/nagios/nagios.cfg
           ├─6042 /usr/sbin/nagios --worker /var/spool/nagios/cmd/nagios.qh
           ├─6043 /usr/sbin/nagios --worker /var/spool/nagios/cmd/nagios.qh
           ├─6044 /usr/sbin/nagios --worker /var/spool/nagios/cmd/nagios.qh
           ├─6045 /usr/sbin/nagios --worker /var/spool/nagios/cmd/nagios.qh
           ├─6046 /usr/sbin/nagios --worker /var/spool/nagios/cmd/nagios.qh
           ├─6047 /usr/sbin/nagios --worker /var/spool/nagios/cmd/nagios.qh
           └─6048 /usr/sbin/nagios -d /etc/nagios/nagios.cfg

Jan 22 06:09:26 rocky-linux-810-fips-nagios-server nagios[6041]: qh: echo service query handler registered
Jan 22 06:09:26 rocky-linux-810-fips-nagios-server nagios[6041]: qh: help for the query handler registered
Jan 22 06:09:26 rocky-linux-810-fips-nagios-server nagios[6041]: wproc: Successfully registered manager as @wproc with query handler
Jan 22 06:09:26 rocky-linux-810-fips-nagios-server nagios[6041]: wproc: Registry request: name=Core Worker 6045;pid=6045
Jan 22 06:09:26 rocky-linux-810-fips-nagios-server nagios[6041]: wproc: Registry request: name=Core Worker 6046;pid=6046
Jan 22 06:09:26 rocky-linux-810-fips-nagios-server nagios[6041]: wproc: Registry request: name=Core Worker 6042;pid=6042
Jan 22 06:09:26 rocky-linux-810-fips-nagios-server nagios[6041]: wproc: Registry request: name=Core Worker 6043;pid=6043
Jan 22 06:09:26 rocky-linux-810-fips-nagios-server nagios[6041]: wproc: Registry request: name=Core Worker 6044;pid=6044
Jan 22 06:09:26 rocky-linux-810-fips-nagios-server nagios[6041]: wproc: Registry request: name=Core Worker 6047;pid=6047
Jan 22 06:09:27 rocky-linux-810-fips-nagios-server nagios[6041]: Successfully launched command file worker with pid 6048
```
* Started the `nrpe` service:
```
systemctl start nrpe
```
* When running the `/usr/lib64/nagios/plugins/check_nrpe -H 127.0.0.1` command, there is no issue there:
```
/usr/lib64/nagios/plugins/check_nrpe -H 127.0.0.1
NRPE v4.1.2
```
* Users can be seen on the `Nagios` Client machine:
```
/usr/lib64/nagios/plugins/check_nrpe -H 10.55.96.4 -c check_users
USERS OK - 1 users currently logged in |users=1;5;10;0
```
* Similarly the load can be seen as well:
```
/usr/lib64/nagios/plugins/check_nrpe -H 10.55.96.4 -c check_load
OK - load average per CPU: 0.01, 0.01, 0.00|load1=0.007;0.150;0.300;0; load5=0.007;0.100;0.250;0; load15=0.000;0.050;0.200;0; 
```