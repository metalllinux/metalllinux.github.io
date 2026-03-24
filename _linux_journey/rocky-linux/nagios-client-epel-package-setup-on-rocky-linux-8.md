---
title: "Nagios Client on Rocky Linux 9.5 Non-FIPS with EPEL Packages Setup"
category: "rocky-linux"
tags: ["rocky-linux", "nagios", "client", "epel", "package"]
---

## Nagios Client on Rocky Linux 9.5 Non-FIPS with EPEL Packages Setup
* Similarly I went through the same steps as before.
* I stopped at the "* Ensured that `FIPS` mode was enabled:" stage.
* Enabled the EPEL repo:
```
dnf config-manager --set-enabled powertools
dnf install epel-release
```
* Installed the `nagios-plugins-all` package:
```
dnf install -y nagios-plugins-all
```
* Installed `nagios-plugins-nrpe`:
```
dnf install -y nagios-plugins-nrpe
```
* Installed the `nrpe` plugin:
```
dnf install -y nrpe
```
* Version of `nrpe` installed:
```
nrpe -V
NRPE - Nagios Remote Plugin Executor
Version: 4.1.2
```
* I then continued on from the "Configured the NRPE plugin's configuration file at `/usr/local/nagios/etc/nrpe.cfg` and added the address of my `Nagios` server:" point. The only change was that now the `nrpe.cfg` file was located at `/etc/nagios/nrpe.cfg`:
```
sed -i 's/allowed_hosts=127.0.0.1,::1/allowed_hosts=127.0.0.1,10.25.96.5/' /etc/nagios/nrpe.cfg
```
* Started and enabled the `nrpe` service:
```
systemctl enable --now nrpe
```
* Observed from `systemctl status nrpe` that connections were being listened for:
```
systemctl status nrpe
● nrpe.service - Nagios Remote Plugin Executor
   Loaded: loaded (/usr/lib/systemd/system/nrpe.service; enabled; vendor preset: disabled)
   Active: active (running) since Wed 2025-01-22 05:50:25 UTC; 3s ago
     Docs: http://www.nagios.org/documentation
 Main PID: 12709 (nrpe)
    Tasks: 1 (limit: 48983)
   Memory: 708.0K
   CGroup: /system.slice/nrpe.service
           └─12709 /usr/sbin/nrpe -c /etc/nagios/nrpe.cfg -f

Jan 22 05:50:25 rocky-linux-810-non-fips-nagios-client systemd[1]: Started Nagios Remote Plugin Executor.
Jan 22 05:50:25 rocky-linux-810-non-fips-nagios-client nrpe[12709]: Starting up daemon
Jan 22 05:50:25 rocky-linux-810-non-fips-nagios-client nrpe[12709]: Server listening on 0.0.0.0 port 5666.
Jan 22 05:50:25 rocky-linux-810-non-fips-nagios-client nrpe[12709]: Server listening on :: port 5666.
Jan 22 05:50:25 rocky-linux-810-non-fips-nagios-client nrpe[12709]: Listening for connections on port 5666
Jan 22 05:50:25 rocky-linux-810-non-fips-nagios-client nrpe[12709]: Allowing connections from: 127.0.0.1,10.25.96.5
```
* The same from `netstat -at | grep nrpe`:
```
netstat -at | grep nrpe
tcp        0      0 0.0.0.0:nrpe            0.0.0.0:*               LISTEN     
tcp6       0      0 [::]:nrpe               [::]:*                  LISTEN
```
* I opened the appropriate port in my firewall:
```
firewall-cmd --zone=public --add-port=5666/tcp --permanent
firewall-cmd --reload
```
* Disabled `SELinux`:
```
setenforce 0
sed -i 's/SELINUX=enforcing/SELINUX=permissive/' /etc/selinux/config
```
* Allowed the `nagios` server to access the client:
```
sed -i 's/allowed_hosts=127.0.0.1,::1/allowed_hosts=127.0.0.1,10.55.96.5/' /etc/nagios/nrpe.cfg
```
* Restarted the `nrpe` service:
```
systemctl restart nrpe
```
* `check_nrpe` returns the expected result:
```
/usr/lib64/nagios/plugins/check_nrpe -H 127.0.0.1
NRPE v4.1.2
```