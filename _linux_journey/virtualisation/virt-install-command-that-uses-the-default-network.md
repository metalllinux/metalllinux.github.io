---
title: "Virt Install Command That Uses The Default Network"
category: "virtualisation"
tags: ["virtualisation", "virt", "install", "command", "uses"]
---

```
virt-install --name rocky-linux-95-vm --ram 8096 --vcpus 8 --disk path=/var/lib/libvirt/images/rocky-linux-95-vm.img,size=20 --
os-variant rocky9 --network default --graphics none --console pty,target_type=serial --extra-args 'console=ttyS0,115200n8' --location ~/isos/Rocky-9.5-x86_64-dvd.iso
```