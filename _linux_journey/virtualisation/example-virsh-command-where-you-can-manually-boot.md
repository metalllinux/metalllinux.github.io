---
title: "Example Virsh Command Where You Can Manually Boot"
category: "virtualisation"
tags: ["virtualisation", "example", "virsh", "command", "where"]
---

```
virt-install   --name rocky-linux-8-pxe-boot   --memory 2048   --vcpus 2   --disk size=20   --network bridge=virbr0   --pxe   --os-type=linux   --os-variant=rocky8   --graphics none   --console pty,target_type=serial --boot network,menu=on
```