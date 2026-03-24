---
title: "How to Remove a Repository from Rocky Linux"
category: "rocky-linux"
tags: ["rocky-linux", "remove", "repository", "rocky", "linux"]
---

# How to Remove a Repository from Rocky Linux

* Delete the repository:

```
sudo rm /etc/yum.repos.d/<name>
```

* Check it was deleted:

```
dnf repolist
```
