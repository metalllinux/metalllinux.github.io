---
title: "How Set Static Ip With Nmcli (Networkmanager)"
category: "networking"
tags: ["networking", "static", "nmcli", "networkmanager"]
---

`nmcli con` to see all of the adapters.

Then to set the static IP permanently, do something like:

nmcli con mod "Linux" \
  ipv4.addresses "192.168.3.52/24" \
  ipv4.gateway "192.168.3.1" \
  ipv4.dns "192.168.3.1" \
  ipv4.method "manual"