---
title: "Working Virt Install Command That References And I"
category: "virtualisation"
tags: ["virtualisation", "working", "virt", "install", "command"]
---

```
virt-install --import --name rocky-linux-95-minimal --ram 16384 --vcpus 8 --disk path=/var/lib/libvirt/qcow2/rocky-linux-95-minimal.qcow2,format=qcow2,size=20 --os-variant rocky9 --network bridge=virbr0,model=virtio --graphics none --location /var/lib/libvirt/images/rocky-linux-95-x86_64-minimal.iso --initrd-inject /var/lib/libvirt/kickstart_files/rocky-linux-95-kickstart.cfg --extra-args "inst.ks=file:rocky-linux-95-kickstart.cfg console=ttyS0,115200n8"
```