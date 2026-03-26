---
title: "How Add Group To A Samba Share"
category: "security"
tags: ["security", "add", "group", "samba", "share"]
---

sudo groupadd samba
sudo usermod -g samba myuser
sudo usermod -g samba guest
sudo chmod 770 /mnt/shared_files/
In smb.conf, we need:
valid users = @samba
Like so:
```
[backup_shared_files]
path = /mnt/shared_files
valid users = @samba
browsable = yes
writable = yes
read only = no
guest ok = yes
```
sudo systemctl restart smb; sudo systemctl restart nmb