---
title: "Add the following to /etc/fstab"
category: "storage-and-filesystems"
tags: ["storage-and-filesystems", "setup", "webdav", "arch", "linux"]
---

```
sudo pacman -S spice-vdagent
sudo pacman -S qemu-guest-agent
sudo pacman -S phodav
sudo vim /etc/conf.d/spice-webdavd
yay -S davfs2
# Add the following to /etc/fstab
http://127.0.0.1:9843 /mnt/webdav davfs rw,user,uid=user,noauto 0 0 
usermod -aG network user
sudo mkdir /mnt/webdav 
# Edit ~/.davfs2/davfs2.conf
# Add the following:
use_locks 0
add_header Cookie "key1=value1; key2=value2"

# Edit ~/.davfs2/secrets
# Add the following:
http://127.0.0.1:9843

sudo systemctl daemon-reload

# Mount with the following command and the password is blank
mount -t davfs http://127.0.0.1:9843
```