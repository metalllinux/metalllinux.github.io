---
title: "How Add Group To A Samba Share"
category: "security"
tags: ["security", "add", "group", "samba", "share"]
---

sudo groupadd samba
sudo usermod -g samba howard
sudo usermod -g samba guest
sudo chmod 770 /mnt/watanabe_memories/
In smb.conf, we need:
valid users = @samba
Like so:
```
[tribunal_watanabe_memories]
path = /mnt/watanabe_memories
valid users = @samba
browsable = yes
writable = yes
read only = no
guest ok = yes
```
sudo systemctl restart smb; sudo systemctl restart nmb