---
title: "How Set Static Ip On Ubuntu 20.04"
category: "desktop-and-distributions"
tags: ["desktop-and-distributions", "static", "ubuntu"]
---

Go into first available netplan file: `sudo nano /etc/netplan/`

Configure the file similarly to this:

network:
  version: 2
  renderer: networkd
  ethernets:
    ens3:
      dhcp4: no
      addresses:
        - 192.168.121.221/24
      gateway4: 192.168.121.1
      nameservers:
          addresses: [8.8.8.8, 1.1.1.1]

Apply the configuration with `sudo netplan apply`