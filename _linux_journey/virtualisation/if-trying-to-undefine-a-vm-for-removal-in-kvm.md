---
title: "If Trying To Undefine A Vm For Removal In Kvm"
category: "virtualisation"
tags: ["virtualisation", "trying", "undefine", "removal", "kvm"]
---

error: Refusing to undefine while domain managed save image exists

Add `-managed-save`

`virsh undefine bullseye-amd64 --remove-all-storage --managed-save`