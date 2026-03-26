---
title: "How To Setup A Freeipa Server On Rocky Linux 9"
category: "rocky-linux"
tags: ["rocky-linux", "setup", "freeipa", "server", "rocky"]
---

* Bought a cheap domain `metalinux.site` and then created a subdomain called `ipa.metalinux.site`
* Set up a Rocky Linux 9.5 FreeIPA Server:
* Fully updated the node:
```
sudo dnf upgrade -y
```
* Set the hostname:
```
sudo hostnamectl set-hostname ipa.metalinux.site
```
* Mapped the server IP and hostnames in the `/etc/hosts` file:
```
sudo tee -a  /etc/hosts <<EOF
64.176.37.44    ipa.metalinux.site  ipa
EOF
```
* Configured the timezone:
```
sudo timedatectl set-timezone Asia/Tokyo
```
* Setup the firewall services:
```
sudo firewall-cmd --add-service={freeipa-ldap,freeipa-ldaps,dns,ntp,http,https,kerberos} --permanent
sudo firewall-cmd --reload
```
* Installed `FreeIPA` packages:
```
sudo dnf install -y freeipa-server freeipa-server-dns freeipa-client 
```
* Started the interactive part of the installation:
```
sudo ipa-server-install --setup-dns --allow-zone-overlap
```
* Set the following options during the installation:
```
Example: master.example.com

Server host name [ipa.metalinux.site]: 

Warning: skipping DNS resolution of host ipa.metalinux.site
The domain name has been determined based on the host name.

Please confirm the domain name [metalinux.site]: 

The kerberos protocol requires a Realm name to be defined.
This is typically the domain name converted to uppercase.

Please provide a realm name [METALINUX.SITE]: 
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

Checking DNS domain metalinux.site., please wait ...
DNS zone metalinux.site. already exists in DNS and is handled by server(s): ['dns1.registrar-servers.com.', 'dns2.registrar-servers.com.'] Please make sure that the domain is properly delegated to this IPA server.

Do you want to configure DNS forwarders? [yes]: 
Following DNS servers are configured in /etc/resolv.conf: 108.61.10.10, 2001:19f0:300:1704::6

Do you want to configure these servers as DNS forwarders? [yes]: 
All detected DNS servers were added. You can enter additional addresses now:

Enter an IP address for a DNS forwarder, or press Enter to skip: 
DNS forwarders: 108.61.10.10, 2001:19f0:300:1704::6
Checking DNS forwarders, please wait ...

Do you want to search for missing reverse zones? [yes]: 
Reverse record for IP address 64.176.37.44 already exists
Trust is configured but no NetBIOS domain name found, setting it now.

Enter the NetBIOS name for the IPA domain.
Only up to 15 uppercase ASCII letters, digits and dashes are allowed.
Example: EXAMPLE.

NetBIOS domain name [METALINUX]: 

Do you want to configure chrony with NTP server or pool address? [no]: no

The IPA Master Server will be configured with:
Hostname:       ipa.metalinux.site
IP address(es): 64.176.37.44
Domain name:    metalinux.site
Realm name:     METALINUX.SITE

The CA will be configured with:
Subject DN:   CN=Certificate Authority,O=METALINUX.SITE
Subject base: O=METALINUX.SITE
Chaining:     self-signed

BIND DNS server will be configured to serve IPA domain with:
Forwarders:       108.61.10.10, 2001:19f0:300:1704::6
Forward policy:   first
Reverse zone(s):  No reverse zone

Continue to configure the system with these values? [no]: yes
```
* Issued the following command to authenticate against the `Kerberos` server:
```
kinit admin
```
* Was able to navigate to and use the `admin` credentials to log into the  `https://ipa.metalinux.site/ipa/ui/` FreeIPA Dashboard.
* Successfully added a new user as well:
```
[root@Rocky-Linux-9-FreeIPA-Server ~]# ipa user-add myuser --first=Admin --last=Smith --password
Password: 
Enter Password again to verify: 
-------------------
Added user "myuser"
-------------------
  User login: myuser
  First name: Admin
  Last name: Smith
  Full name: Admin Smith
  Display name: Admin Smith
  Initials: AS
  Home directory: /home/myuser
  GECOS: Admin Smith
  Login shell: /bin/sh
  Principal name: myuser@METALINUX.SITE
  Principal alias: myuser@METALINUX.SITE
  User password expiration: 20241210064445Z
  Email address: myuser@metalinux.site
  UID: 1443200003
  GID: 1443200003
  Password: True
  Member of groups: ipausers
  Kerberos keys available: True
```