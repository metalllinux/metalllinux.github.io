---
title: "To Get SSH Access to a Rocky Linux 8.10 with XFCE Box:"
category: "rocky-linux"
tags: ["rocky-linux", "ssh", "access", "rocky", "linux"]
---

# To Get SSH Access to a Rocky Linux 8.10 with XFCE Box:

* Install `ssh` server:

```
dnf install -y openssh-server
```

* Enable the `sshd` service:

```
systemctl enable --now sshd
```
