---
title: "FreeIPA Server Setup"
category: "security"
tags: ["security", "setup", "local", "freeipa", "server"]
---

### FreeIPA Server Setup
* Run `nmcli` to see networking statistics.
* Change to `root`:
```
su - root
```
* Change the hostname of the FreeIPA server to a FQDN:
```
<hostname>.example.local
```
* Check the hostname was set with `hostnamectl`
* Then open the `/etc/hosts` file and add the following information:
```
<IP_ADDRESS>	<FQDN>	<HOSTNAME>
```
* An example would be:
```
10.0.2.63	centos-9-server.example.local	centos-9-server.example.local
```
* Install the required packages:
```
dnf install -y freeipa-server-dns
```
* Check it installed with `ipa --version`
* Then start the configuration:
```
ipa-server-install --setup-dns --auto-reverse
```
* `--auto-reverse` automatically sets up a DNS lookup.
* Follow these steps next:
```
[root@freeipa-server ~]# ipa-server-install --setup-dns --auto-reverse

The log file for this installation can be found in /var/log/ipaserver-install.log
==============================================================================
This program will set up the IPA Server.
Version 4.12.2

This includes:
  * Configure a stand-alone CA (dogtag) for certificate management
  * Configure the NTP client (chronyd)
  * Create and configure an instance of Directory Server
  * Create and configure a Kerberos Key Distribution Center (KDC)
  * Configure Apache (httpd)
  * Configure DNS (bind)
  * Configure SID generation
  * Configure the KDC to enable PKINIT

To accept the default shown in brackets, press the Enter key.

Enter the fully qualified domain name of the computer
on which you're setting up server software. Using the form
<hostname>.<domainname>
Example: master.example.com


Server host name [freeipa-server.example.local]: 

Warning: skipping DNS resolution of host freeipa-server.example.local
The domain name has been determined based on the host name.

Please confirm the domain name [example.local]: 

The kerberos protocol requires a Realm name to be defined.
This is typically the domain name converted to uppercase.

Please provide a realm name [EXAMPLE.LOCAL]: 
Certain directory server operations require an administrative user.
This user is referred to as the Directory Manager and has full access
to the Directory for system management tasks and will be added to the
instance of directory server created for IPA.
The password must be at least 8 characters long.

Directory Manager password: 
Password (confirm): 

The IPA server requires an administrative user, named 'admin'.
This user is a regular system account used for IPA server administration.

IPA admin password: 
Password (confirm): 

Checking DNS domain example.local., please wait ...
Do you want to configure DNS forwarders? [yes]: 
Following DNS servers are configured in /etc/resolv.conf: 192.168.1.1
Do you want to configure these servers as DNS forwarders? [yes]: 
All detected DNS servers were added. You can enter additional addresses now:
Enter an IP address for a DNS forwarder, or press Enter to skip: 
DNS forwarders: 192.168.1.1
Checking DNS forwarders, please wait ...
Checking DNS domain 1.168.192.in-addr.arpa., please wait ...
Reverse zone 1.168.192.in-addr.arpa. will be created
Using reverse zone(s) 1.168.192.in-addr.arpa.
Trust is configured but no NetBIOS domain name found, setting it now.
Enter the NetBIOS name for the IPA domain.
Only up to 15 uppercase ASCII letters, digits and dashes are allowed.
Example: EXAMPLE.


NetBIOS domain name [EXAMPLE]: 

Do you want to configure chrony with NTP server or pool address? [no]: 

The IPA Master Server will be configured with:
Hostname:       freeipa-server.example.local
IP address(es): 192.168.1.11
Domain name:    example.local
Realm name:     EXAMPLE.LOCAL

The CA will be configured with:
Subject DN:   CN=Certificate Authority,O=EXAMPLE.LOCAL
Subject base: O=EXAMPLE.LOCAL
Chaining:     self-signed

BIND DNS server will be configured to serve IPA domain with:
Forwarders:       192.168.1.1
Forward policy:   only
Reverse zone(s):  1.168.192.in-addr.arpa.

Continue to configure the system with these values? [no]: yes
```
* Backup the certificates:
```
mkdir backup
```
* Copy over the root certificates:
```
cp /root/cacert.p12 backup/
```
* Check open ports in `firewalld`:
```
firewall-cmd --list-ports
```
* Check the open ports:
```
firewall-cmd --list-services
```
* Add the following TCP ports:
```
firewall-cmd --add-port={80,443,389,636,88,464,53}/tcp --permanent
```
* Add these UDP ports:
```
firewall-cmd --add-port={88,464,53,123}/udp --permanent
```
* Reload the firewall:
```
firewall-cmd --reload
```
* Run `kinit` for the `admin` account:
```
kinit admin
```
* Create a user account:
```
ipa user-add test --password --homedir=/home/test --shell=/bin/bash
```
* Add the user's First Name and Last Name.
* Enter the new user's password.
### FreeIPA Client Setup
* On the client machine, make sure the created user has `sudo` permissions.
* Need to have a fully qualified domain name.
* Modify it using the following:
```
sudo hostnamectl hostname freeipa-client.example.local
```
* Now we have set the domain of the client to be the same as the FreeIPA server.
* Check the client has a connection to the FreeIPA server.
* Install the FreeIPA client package:
```
sudo dnf install -y freeipa-client
```
* Now need to point the FreeIPA client to the server via DNS.
* Change the DNS on the client system using the `nmcli` command:
```
sudo nmcli c m "enp1s0" ipv4.dns <FreeIPA_Server_Address>
```
* Bring the connection up:
```
sudo nmcli c u "enp1s0" 
```
* Afterwards, the FreeIPA Client should be able to reach the Internet.
* Now configure the client using the `ipa-client-install` command:
```
sudo ipa-client-install --enable-dns-updates --mkhomedir
```
* Example `ipa-client-install` configuration options:
```
[howard@rocky-linux-9 ~]$ sudo ipa-client-install --enable-dns-updates --mkhomedir
This program will set up IPA client.
Version 4.12.2

Discovery was successful!
Do you want to configure chrony with NTP server or pool address? [no]: 
Client hostname: freeipa-client.example.local
Realm: EXAMPLE.LOCAL
DNS Domain: example.local
IPA Server: freeipa-server.example.local
BaseDN: dc=example,dc=local

Continue to configure the system with these values? [no]: yes
```
* Under `User authorized to enroll computers:` you can choose either `admin` or `root`
* Once the configuration is done, for a visual representation, install a GUI (in this case the FreeIPA client is being set up as a Workstation):
```
sudo dnf group install -y "Workstation"
sudo systemctl set-default graphical
```
* `reboot` the client.
* Log back in with an existing user (not one from your newly created FreeIPA server).
	* This is due to having no account to connect to on the domain as of yet (it does exist on the domain, just not on the client).
* Create the user.