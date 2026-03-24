---
title: "How to Add a User to the sudoers File in Debian 13"
category: "desktop-and-distributions"
tags: ["desktop-and-distributions", "add", "user", "sudoers", "file"]
---

# How to Add a User to the sudoers File in Debian 13

* At the GRUB menu, select the recovery menu for the latest kernel.

* Log in with the `root` account.

* Mount the root directory:

```
mount -o remount,rw /
```

* Give the user `sudo` privileges:

```
sudo usermod -aG sudo username
```

* Then type `exit`
