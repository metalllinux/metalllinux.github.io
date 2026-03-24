---
title: "How Check Graphics Driver"
category: "general-linux"
tags: ["check", "graphics", "driver"]
---

lspci -nnk | egrep -i --colour 'vga|3d|2d' -A3 | grep 'in use'