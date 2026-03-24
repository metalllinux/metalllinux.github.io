---
title: "How to Permanently Set SELinux into Permissive Mode"
category: "security"
tags: ["security", "permanently", "selinux", "into", "permissive"]
---

# How to Permanently Set SELinux into Permissive Mode

```
sudo sed -i 's/^SELINUX=.*/SELINUX=permissive/' /etc/selinux/config
```

