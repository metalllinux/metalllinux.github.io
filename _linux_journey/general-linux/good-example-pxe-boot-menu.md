---
title: "Good Example Pxe Boot Menu"
category: "general-linux"
tags: ["good", "example", "pxe", "boot", "menu"]
---

```
cat << "EOF" | sudo tee /var/lib/tftpboot/pxelinux.cfg/default
default menu.c32
prompt 0
timeout 300
ONTIMEOUT local

menu title ########## PXE Boot Menu ##########

label 1
menu label ^1) Install Rocky Linux 9.5 x64 with a Local Repo
  kernel rocky95/vmlinuz
  append initrd=rocky95/initrd.img inst.zram=1 inst.repo=ftp://10.25.96.3/pub devfs=nomount

label 2
menu label ^2) Install Rocky Linux 9.5 x64 using HTTP
  kernel rocky95/vmlinuz
  append initrd=rocky95/initrd.img inst.zram=1 inst.repo=https://dl.rockylinux.org/pub/rocky/9.5/BaseOS/x86_64/os/

label 3
menu label ^3) Install Rocky Linux 9.5 with a Kickstart File
  kernel rocky95/vmlinuz
  append initrd=rocky95/initrd.img inst.zram=1 inst.ks=nfs:10.25.96.3:/ks/rocky95.cfg ip=dhcp net.ifnames=0 biosdevname=0

label 4
menu label ^4) Boot from local drive
EOF
```