---
title: "Warewulf Installation On Rocky Linux 8 And 9"
category: "rocky-linux"
tags: ["rocky-linux", "warewulf", "installation", "rocky", "linux"]
---

* Upgrade the node:
```
dnf upgrade -y
```
* If using a Vultr instance, make sure the normal VPC network is created for both the Controller Node and Compute Nodes to live in.
* The Compute Node should not be a bare metal instance, as the iPXE does not easily boot there.
```
dnf install -y https://github.com/warewulf/warewulf/releases/download/v4.5.8/warewulf-4.5.8-1.el8.x86_64.rpm
```

* Warewulf for Rocky Linux 9:

```
dnf install -y https://github.com/warewulf/warewulf/releases/download/v4.6.4/warewulf-4.6.4-1.el9.x86_64.rpm
```

```
sudo systemctl restart firewalld
sudo firewall-cmd --permanent --add-service=warewulf
sudo firewall-cmd --permanent --add-service=dhcp
sudo firewall-cmd --permanent --add-service=nfs
sudo firewall-cmd --permanent --add-service=tftp
sudo firewall-cmd --reload
```
```
sudo tee /etc/warewulf/warewulf.conf <<EOF
WW_INTERNAL: 45
ipaddr: 192.168.1.161
netmask: 255.255.255.0
network: 192.168.1.0
warewulf:
  port: 9873
  secure: false
  update interval: 60
  autobuild overlays: true
  host overlay: true
  syslog: false
  datastore: /usr/share
  grubboot: false
dhcp:
  enabled: true
  template: default
  range start: 192.168.1.253
  range end: 192.168.1.254
  systemd name: dhcpd
tftp:
  enabled: true
  tftproot: /var/lib/tftpboot
  systemd name: tftp
  ipxe:
    "00:00": undionly.kpxe
    "00:07": ipxe-snponly-x86_64.efi
    "00:09": ipxe-snponly-x86_64.efi
    00:0B: arm64-efi/snponly.efi
nfs:
  enabled: true
  export paths:
  - path: /home
    export options: rw,sync
    mount options: defaults
    mount: true
  - path: /opt
    export options: ro,sync,no_root_squash
    mount options: defaults
    mount: false
  systemd name: nfs-server
container mounts:
- source: /etc/resolv.conf
  dest: /etc/resolv.conf
  readonly: true
paths:
  bindir: /usr/bin
  sysconfdir: /etc
  localstatedir: /var/lib
  ipxesource: /usr/share/ipxe
  srvdir: /var/lib
  firewallddir: /usr/lib/firewalld/services
  systemddir: /usr/lib/systemd/system
  wwoverlaydir: /var/lib/warewulf/overlays
  wwchrootdir: /var/lib/warewulf/chroots
  wwprovisiondir: /var/lib/warewulf/provision
  wwclientdir: /warewulf
EOF
```
```
sudo systemctl enable --now warewulfd
```
```
sudo wwctl configure --all
```
```
sudo restorecon -Rv /var/lib/tftpboot/
```
```
sudo wwctl image import docker://ghcr.io/warewulf/warewulf-rockylinux:9 rockylinux-9 --build
sudo wwctl profile set default --container rockylinux-9
```
```
sudo wwctl profile set -y default --netmask=255.255.255.0 --gateway=192.168.1.150
sudo wwctl profile list
```
```
sudo wwctl node add node01 --ipaddr=192.168.1.253 --discoverable=true
sudo wwctl node list -a node01
```
```
sudo wwctl overlay build
```
* Turn on the Compute Node and it will then boot.
