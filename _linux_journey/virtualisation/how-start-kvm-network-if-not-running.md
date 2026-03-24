---
title: "How Start Kvm Network If Not Running"
category: "virtualisation"
tags: ["virtualisation", "start", "kvm", "network", "running"]
---

* Check the status of the virtual networks:
`sudo virsh net-list --all`

* Start the default network:
`sudo virsh net-start default `

* To automatically start the default network, run: `sudo virsh net-autostart default`