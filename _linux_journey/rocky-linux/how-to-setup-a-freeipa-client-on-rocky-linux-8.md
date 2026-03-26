---
title: "FreeIPA Server Setup"
category: "rocky-linux"
tags: ["rocky-linux", "setup", "freeipa", "client", "rocky"]
---

### FreeIPA Server Setup
* I set up a FreeIPA instance on Rocky Linux 9.5
* Authenticated against the Kerberos server:
```
kinit admin
```
* I added two users:
```
ipa user-add test-no-1 --first=test --last=no1 --password
ipa user-add test-no-2 --first=test --last=no2 --password
```
* I added the external IP of the FreeIPA Client as a DNS entry:
```
ipa dnsrecord-add metalinux.site rocky-linux-810-freeipa-client --a-rec 45.76.216.137
```

### Client Setup
* Configured the hostname of the client:
```
sudo hostnamectl set-hostname client.metalinux.site
```
* I addeed the following entries into `/etc/hosts`:
```
cat << "EOF" | sudo tee /etc/hosts
45.76.194.188 ipa.metalinux.site
45.76.216.137 client.metalinux.site
EOF
```
* I installed the client package:
```
sudo dnf install -y freeipa-client
```
* I then configured the FreeIPA client:
```
sudo ipa-client-install --hostname=`hostname -f` --mkhomedir --server=ipa.metalinux.site --domain metalinux.site  --realm METALINUX.SITE
```
* This completed successfully:
```
Autodiscovery of servers for failover cannot work with this configuration.
If you proceed with the installation, services will be configured to always access the discovered server for all operations and will not fail over to other servers in case of failure.
Proceed with fixed values and no DNS discovery? [no]: yes
Do you want to configure chrony with NTP server or pool address? [no]: yes
Enter NTP source server addresses separated by comma, or press Enter to skip: uk.pool.ntp.org             
Enter a NTP source pool address, or press Enter to skip:                   
Client hostname: client.metalinux.site
Realm: METALINUX.SITE
DNS Domain: metalinux.site
IPA Server: ipa.metalinux.site
BaseDN: dc=metalinux,dc=site
NTP server: uk.pool.ntp.org

Continue to configure the system with these values? [no]: yes
Synchronizing time
Configuration of chrony was changed by installer.
Attempting to sync time with chronyc.
Time synchronization was successful.
User authorized to enroll computers: admin
Password for admin@METALINUX.SITE: 
Successfully retrieved CA cert
    Subject:     CN=Certificate Authority,O=METALINUX.SITE
    Issuer:      CN=Certificate Authority,O=METALINUX.SITE
    Valid From:  2025-02-07 07:07:55
    Valid Until: 2045-02-07 07:07:55

Enrolled in IPA realm METALINUX.SITE
Created /etc/ipa/default.conf
Configured /etc/sssd/sssd.conf
Systemwide CA database updated.
Hostname (client.metalinux.site) does not have A/AAAA record.
Failed to update DNS records.
Missing A/AAAA record(s) for host client.metalinux.site: 45.76.216.137.
Incorrect reverse record(s):
45.76.216.137 is pointing to 45.76.216.137.vultrusercontent.com. instead of client.metalinux.site.
Adding SSH public key from /etc/ssh/ssh_host_dsa_key.pub
Adding SSH public key from /etc/ssh/ssh_host_ecdsa_key.pub
Adding SSH public key from /etc/ssh/ssh_host_ed25519_key.pub
Adding SSH public key from /etc/ssh/ssh_host_rsa_key.pub
Could not update DNS SSHFP records.
SSSD enabled
Configured /etc/openldap/ldap.conf
Configured /etc/ssh/ssh_config
Configured /etc/ssh/sshd_config
Configuring metalinux.site as NIS domain.
Configured /etc/krb5.conf for IPA realm METALINUX.SITE
Client configuration complete.
The ipa-client-install command was successful
```
* I could successfully log in with my `test-no-1` user generated on the FreeIPA server, using the client machine:
```
myuser@myuser-MacBook-Pro 1822 % ssh test-no-1@45.76.216.137
(test-no-1@45.76.216.137) Password: 
(test-no-1@45.76.216.137) Password expired. Change your password now.
Current Password: 
(test-no-1@45.76.216.137) New password: 
(test-no-1@45.76.216.137) Retype new password: 
Activate the web console with: systemctl enable --now cockpit.socket
```

### TigetVNC Setup - FreeIPA Client 
* I set up the FreeUPA Client to have a graphical environment (GNOME in this case):
```
sudo dnf group install -y "Server with GUI"
```
* I set the default target into `graphical` mode:
```
systemctl set-default graphical
```
* I installed the `tigervnc` package:
```
sudo dnf install -y tigervnc-server
```
* For the `service`, I set the display number as `3`:
```
sudo cp /usr/lib/systemd/system/vncserver@.service /etc/systemd/system/vncserver@:3.service
```
* Under `vncserver.users` I added my two FreeIPA Server users and assigned each of them to display `3`:
```
cat << "EOF" | sudo tee -a /etc/tigervnc/vncserver.users
:3=test-no-1
:3=test-no-2
EOF
```
* I set the `vncpasswd`:
```
vncpasswd
```
* Selected `n` at the prompt for `view-only` password.
* Taking user `test-no-1` as an example, I ran the following configuration:
* I set the `gnome-session` to be the current session:
```
echo gnome-session > /home/test-no-1/.session
```
* I generated the `vnc` directory:
```
mkdir /home/test-no-1/.vnc
```
* I created the `vnc` configuration file:
```
cat << "EOF" | tee -a /home/test-no-1/.vnc/config
session=gnome
securitytypes=vncauth,tlsvnc
geometry=1920x1080
EOF
```
* Then as `root` I started the `vncserver`:
```
sudo systemctl enable --now vncserver@:3.service
```
* I added the appropriate firewall rules:
```
sudo firewall-cmd --permanent --add-service=vnc-server
sudo firewall-cmd --permanent --add-port=5902/tcp
sudo firewall-cmd --reload
```
* I installed `remmina`:
```
sudo dnf install -y epel-release
sudo dnf install -y remmina
```

### Other Testing
* I also performed extensive testing with `OpenLDAP`, building it both from `source` and installing it via RPMs. Unfortunately whilst I could bring up both an `OpenLDAP` Server and `OpenLDAP` Client, regardless of the configuration changes and logs checked, I could not log in with a user on the `OpenLDAP` Client that was generated on the `OpenLDAP` Server.

### Current Point in Testing
* I am now trying to have the two FreeIPA Server users use Remmina to start a VNC session.

### Next Steps
* I will continue to test the above until a working solution is found for the FreeIPA users to use a VNC client.
* Regarding the above research and testing so far, is this what you were looking for Tim or shall I re-direct my efforts in another direction?

Many thanks always for going through all of my testing and findings. I hope you have a lovely weekend on your side and look forward to working on this more next week.

Kind Regards,
myuser