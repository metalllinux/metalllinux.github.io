---
title: "Command to Show the Current Graphics Driver in Use"
category: "general-linux"
tags: ["command", "display", "current", "graphics", "driver"]
---

# Command to Show the Current Graphics Driver in Use

```
lspci -nnk | grep -A3 -i 'vga\|3d\|display'
```

