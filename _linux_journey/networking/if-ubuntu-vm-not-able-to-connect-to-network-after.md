---
title: "If Ubuntu Vm Not Able To Connect To Network After"
category: "networking"
tags: ["networking", "ubuntu", "able", "connect", "network"]
---

* Make sure Ethernet Adapter is the same as output from `ip a` in /etc/netplan/00-installer-config.yaml
* Try setting `dhcp4` to `yes` and comment out all static IP lines below that, aside from `version: 2`.
* Run `sudo netplan apply` after that to instantly apply the network config.