---
title: "See smb.conf.example for a more detailed config file or"
category: "general-linux"
tags: ["current", "smbconf", "file"]
---

```
# See smb.conf.example for a more detailed config file or
# read the smb.conf manpage.
# Run 'testparm' to verify the config is correct after
# you modified it.
#
# Note:
# SMB1 is disabled by default. This means clients without support for SMB2 or
# SMB3 are no longer able to connect to smbd (by default).

[global]
	workgroup = METALOCALYPSE
	security = user

	passdb backend = tdbsam

	printing = cups
	printcap name = cups
	load printers = yes
	cups options = raw

[homes]
	comment = Home Directories
	valid users = %S, %D%w%S
	browseable = No
	read only = No
	inherit acls = Yes

[printers]
	comment = All Printers
	path = /var/tmp
	printable = Yes
	create mask = 0600
	browseable = No

[print$]
	comment = Printer Drivers
	path = /var/lib/samba/drivers
	write list = @printadmin root
	force group = @printadmin
	create mask = 0664
	directory mask = 0775

[tribunal_documents_backup]
path = /mnt/dethklok/documents
valid users = howard
browsable = yes
writable = yes
read only = no

[tribunal_movies_backup]
path = /mnt/dethklok/movies
valid users = howard
browsable = yes
writable = yes
read only = no

[tribunal_pictures_backup]
path = /mnt/dethklok/pictures
valid users = howard
browsable = yes
writable = yes
read only = no

[tribunal_watanabe_memories]
path = /home/howard/watanabe_memories
browsable = yes
writable = yes
read only = no
guest ok = yes
```