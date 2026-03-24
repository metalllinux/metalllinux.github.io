---
title: "How Set Static Ip With Nmcli"
category: "networking"
tags: ["networking", "static", "nmcli"]
---

   26  sudo nmcli con modify 'enp5s0' ifname enp5s0 ipv4.method manual ipv4.addresses 192.168.3.51/24 gw4 192.168.3.1
   27  sudo nmcli con modify 'enp5s0' ipv4.dns 192.168.3.1
   28  sudo nmcli con down 'enp5s0'
   29  sudo nmcli con up 'enp5s0'
