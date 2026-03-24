---
title: "Check Kernel Driver For Gpu Command"
category: "kernel-and-system-internals"
tags: ["kernel-and-system-internals", "check", "kernel", "driver", "gpu"]
---

lspci -k | grep -EA3 'VGA|3D|Display'