---
title: "Disable SELinux on the Library Refresh VM"
category: "project-tv-v2"
tags: ["project-tv-v2", "disable", "selinux", "library", "refreshing"]
---

# Disable SELinux on the Library Refresh VM
```
sudo setenforce 0
sudo sed -i 's/^SELINUX=.*/SELINUX=permissive/g' /etc/selinux/config
```

