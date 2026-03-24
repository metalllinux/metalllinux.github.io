---
title: "How To Add A User In Ubuntu"
category: "desktop-and-distributions"
tags: ["desktop-and-distributions", "add", "user", "ubuntu"]
---

```
sudo useradd -m <USER>
```
* Add them to the `sudo` group.
```
sudo usermod -aG wheel <USER>
```
* Assign a password:
```
passwd <USER>
```
