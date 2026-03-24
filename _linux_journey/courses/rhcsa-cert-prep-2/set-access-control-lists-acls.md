---
title: "Set Access Control Lists (Acls)"
category: "rhcsa-cert-prep-2"
tags: ["rhcsa-cert-prep-2", "access", "control", "lists", "acls"]
---

* ACLs are turned on in CentOS.
* ACLs are not turnd on by default for other drives, only the OS partition.
* Syntax for `setfacl` is:
	* `setefacl -m user:<username>:<permission> <file>`
* Special bits and umasks to solve problems.
* ACLs esay to implement.
	* Give certain people privileges.
* For example if want to set `setfacl -m user:bob:rwx /home/file.txt`
	* Set `rwx` permissions for the username `bob`.
	* `getfacl file.txt`
		* Will then show user, group, mask and other.
			* To set another ACL, `sudo setfacl -m group:accounting:rx file.txt`
				* Able to set more than one ACL at a time.
					* `sudo setfacl -m user:bob:rwrx,group:accounting:rx file.txt`
						* Sets the user ACL as well as the group ACL.
							* Can shorten it with `sudo setfacl -m u:bob,g:accounting:rx file.txt`
								* Can substitute user and group appropriately.
									* If set User ACL and don't specify a username, it sets the standard permissions for the user owner.
									* `sudo setfacl -m user:rwx file.txt`
* Then if you do `getfacl file.txt`, it will set the permissions for the user owner.
* Exactly the same as typing `sudo chmod u=rwx file.txt`
	* You can set `user owner`, `group owner` and `other` by using the same method.
		* Can also set ACLs recursively using the `-R` option.
			* `sudo setfacl -R -m user:bob:rwx /home/bob`
* Check out `man setfacl`