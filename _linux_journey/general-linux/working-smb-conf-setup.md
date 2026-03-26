---
title: "Working Smb.Conf Setup"
category: "general-linux"
tags: ["working", "smbconf", "setup"]
---

[backup_pictures]
path = /mnt/mypool/pictures
valid users = myuser
browsable = yes
writable = yes
read only = no

```
 135  sudo dnf install samba samba-common samba-client
  136  sudo cp /etc/samba/smb.conf /etc/samba/smb.conf.bkp
  137  sudo vim /etc/samba/smb.conf
  138  sudo systemctl start smb
  139  sudo systemctl enable smb
  140  sudo systemctl start nmb
  141  sudo systemctl enable nmb
  142  sudo firewall-cmd --permanent --add-service=samba
  143  sudo firewall-cmd --reload
  144  sudo firewall-cmd --list-services
  145  sudo smbpasswd -a myuser
  146  sudo chmod 755 /mnt/mypool/pictures/
  147  ls -l /mnt/mypool/
  148  sudo chcon -t samba_share_t /mnt/mypool/pictures/
  149  sudo vim /etc/samba/smb.conf
  150  sudo systemctl restart smb
  151  sudo systemctl restart nmb
```