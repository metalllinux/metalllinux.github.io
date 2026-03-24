---
title: "Samba Setup With Yast2"
category: "security"
tags: ["security", "samba", "setup", "yast2"]
---

* Set up samba server via YAST software.
* Make sure `chmod` permissions are set to `777`.
* Allow guest access as well!
* Restart `samba` with `sudo systemctl restart smb nmb`
* Configuration file is located under `/etc/samba/smb.conf`