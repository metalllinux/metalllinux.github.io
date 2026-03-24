---
title: "Stop A Running Vm In Kvm And Remove All Contents"
category: "virtualisation"
tags: ["virtualisation", "stop", "running", "kvm", "remove"]
---

`virsh destroy debian-bullseye-amd64`

`virsh undefine bullseye-amd64 --remove-all-storage`