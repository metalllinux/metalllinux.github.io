---
title: "If See Unknown Display In Pop! Os"
category: "general-linux"
tags: ["see", "unknown", "display", "pop"]
---

sudo nano /usr/share/X11/xorg.conf.d//20-ignore.conf
Add the following:
```
Section "Monitor"
    Identifier "None-2-1"
    Option "Ignore" "true"
EndSection
```
Then 
