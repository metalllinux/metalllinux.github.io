---
title: "When Using Virt Install And A Kickstart File Run"
category: "virtualisation"
tags: ["virtualisation", "when", "virt", "install", "kickstart"]
---

```
virt-install --name test --ram 16384 --vcpus 8 --disk path=/home/myuser/images/test.qcow2,format=qcow2,size=20 --os-variant rocky9 --network bridge=virbr0,model=virtio --graphics none --location /home/myuser/isos/Rocky-9.5-x86_64-dvd.iso --initrd-inject=/home/myuser/test.cfg --extra-args="inst.ks=file:/test.cfg console=ttyS0,115200n8" > /tmp/install.log 2>&1
```
* Then `tail` the logs using the following command:
```
tail -f /tmp/install.log
```