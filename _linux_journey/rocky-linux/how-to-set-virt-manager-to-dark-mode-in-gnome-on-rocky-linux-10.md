---
title: "How to Set virt-manager to Dark Mode on Rocky Linux 10"
category: "rocky-linux"
tags: ["rocky-linux", "virt", "manager", "dark", "mode"]
---

# How to Set virt-manager to Dark Mode on Rocky Linux 10

```
mkdir -p ~/.config/gtk-3.0
echo '[Settings]
gtk-application-prefer-dark-theme=1' > ~/.config/gtk-3.0/settings.ini
```
