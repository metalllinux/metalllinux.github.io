---
title: "If Unable To Connect To Samba Share On A Rhel Base"
category: "rocky-linux"
tags: ["rocky-linux", "unable", "connect", "samba", "share"]
---

For example you receive:

```
[howard@explosion ~]$ smbclient //192.168.3.50/tribunal_pictures_backup
Password for [SAMBA\howard]:
tree connect failed: NT_STATUS_BAD_NETWORK_NAME
```

* Check if selinux is running with: `setatus`
* Then set it to Permissive mode with `setenforce 0`.
	* No reboot required.