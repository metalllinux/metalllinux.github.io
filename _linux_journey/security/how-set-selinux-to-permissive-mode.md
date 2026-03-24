---
title: "How Set Selinux To Permissive Mode"
category: "security"
tags: ["security", "selinux", "permissive", "mode"]
---

```
sed -i 's/SELINUX=enforcing/SELINUX=permissive/' /etc/selinux/config
```
