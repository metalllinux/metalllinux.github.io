---
title: "How Find Ip Address Of Vm In Kvm 1"
category: "virtualisation"
tags: ["virtualisation", "find", "address", "kvm"]
---

`export vm_ip_address=$(virsh domifaddr <vm_name> | awk '/ipv4/ {print $4}' | awk -F'/' '{print $1}')`