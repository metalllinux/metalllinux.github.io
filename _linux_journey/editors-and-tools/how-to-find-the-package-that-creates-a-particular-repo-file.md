---
title: "How to Find the Package that Creates a Particular Repo File"
category: "editors-and-tools"
tags: ["editors-and-tools", "find", "package", "creates", "particular"]
---

# How to Find the Package that Creates a Particular Repo File

```
rpm -qf /etc/yum.repos.d/rocky.repo
dnf provides /etc/yum.repos.d/rocky.repo
```

