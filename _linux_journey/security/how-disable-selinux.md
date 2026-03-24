---
title: "How Disable Selinux"
category: "security"
tags: ["security", "disable", "selinux"]
---

```
sudo setenforce 0
sudo sed -i 's/^SELINUX=.*/SELINUX=permissive/g' /etc/selinux/config
```