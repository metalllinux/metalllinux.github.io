---
title: "Why Rocky 8 Does Not Work On A Vm"
category: "rocky-linux"
tags: ["rocky-linux", "rocky", "work"]
---

From Skip:
```
Rocky 8 will not work (even in a VM), unless you make an image using a newer upstream kernel.
The 4.18.0 one from rhel/rocky 8 has a built-in pagesize (iirc) setting which is incompatible w/ the Mac processor
```