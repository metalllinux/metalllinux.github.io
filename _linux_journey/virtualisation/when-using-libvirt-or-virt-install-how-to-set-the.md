---
title: "vnc_listen = '0.0.0.0'"
category: "virtualisation"
tags: ["virtualisation", "when", "libvirt", "virt", "install"]
---

* Edit this file:
```
/etc/libvirt/qemu.conf
```
* Uncomment this line:
```
#vnc_listen = "0.0.0.0"
```
* Restart `libvirt` with:
```
sudo systemctl restart libvirtd
```