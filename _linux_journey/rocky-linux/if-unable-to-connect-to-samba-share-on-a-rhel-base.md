---
title: "If Unable To Connect To Samba Share On A Rhel Base"
category: "rocky-linux"
tags: ["rocky-linux", "unable", "connect", "samba", "share"]
---

For example you receive:

```
[myuser@myhost ~]$ smbclient //192.168.3.50/backup_pictures
Password for [SAMBA\myuser]:
tree connect failed: NT_STATUS_BAD_NETWORK_NAME
```

* Check if selinux is running with: `setatus`
* Then set it to Permissive mode with `setenforce 0`.
	* No reboot required.