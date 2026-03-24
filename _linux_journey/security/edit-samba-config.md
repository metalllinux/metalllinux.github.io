---
title: "Edit Samba Config"
category: "security"
tags: ["security", "edit", "samba", "config"]
---

sudo vim /etc/samba/smb.conf
* Restart Samba services after editing the config.
sudo systemctl restart smbd.service nmbd.service

Also create shares in `/mnt/` instead and change owner to samba user and `chmod 777`