---
title: "How to Setup KDE on Rocky Linux 10 Server"
category: "rocky-linux"
tags: ["rocky-linux", "setup", "kde", "rocky", "linux"]
---

# How to Setup KDE on Rocky Linux 10 Server

* Install `epel-release`:

```
sudo dnf install -y epel-release
```

* Enable the `crb` repo and install the KDE packages:

```
sudo dnf --enablerepo=epel,crb group -y install "KDE Plasma Workspaces"
```

* Set the `systemctl set-default` to `graphical`:

```
sudo systemctl set-default graphical
```

* Restart the machine.
