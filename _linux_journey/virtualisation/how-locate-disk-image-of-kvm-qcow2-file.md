---
title: "How Locate Disk Image Of Kvm Qcow2 File"
category: "virtualisation"
tags: ["virtualisation", "locate", "disk", "image", "kvm"]
---

virsh domblklist <vm_name>

That will output something like:

```
[myuser@myhost:~]$ sudo virsh domblklist mastodon-ubuntu22.04
 Target   Source
--------------------------------------------------------
 vda      /home/myuser/vms/ubuntu-22-04-mastodon.qcow2
```