---
title: "How Check Graphics Driver In Linux"
category: "general-linux"
tags: ["check", "graphics", "driver", "linux"]
---

sudo lshw -c video

May have to install `lshw` as well.

Check additional information about your graphics card:

lspci -nn | grep -E 'VGA|Display'
