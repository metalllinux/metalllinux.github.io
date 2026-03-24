---
title: "Configure Inheritance With Default Access Control"
category: "rhcsa-cert-prep-2"
tags: ["rhcsa-cert-prep-2", "configure", "inheritance", "default", "access"]
---

* Standard Linux Permissions only have one type of inheritance --> `SGID` bit on directories.
	* The files and directories inside of this, inherit the `group owner` of the parent directory.
		* There can only be one of.
* Default ACLs allow files and directories to inherit any number of permissions.
			* If you want a user to access a directory, you set a regular ACL on it first.
				* If you want that user to access everything inside a directory, then set a Default ACL.
					* Default ACLs provide inheritance.
						* Usually both operations are required.
* Example
	* `sudo mkdir ~/acldir`
		* `cd ~/acldir`
			* `sudo mkdir dir1`
				* `cat /etc/passwd` to check if we have a `Bob` user.
					* If the user is not present, then have to do `sudo useradd bob`
* `sudo setfacl -m user:bob:rwx dir1`
	* Verify with `getfacl dir1`
		* Check that `bob` can access anything in the directory with recursive mode.
			* `sudo setfacl -R -m user:bob:rwx dir1`
				* This sets an ACL on every file inside of `dir1`, granting `bob` access.
					* Create ACL for any future files that are created in `dir1`:
						* `sudo setfacl -d -m user:bob:rwx dir1`
							* Verify with `getfacl dir1`
* Previous two steps ensures that `bob` has `rwx` on the directory.
	* Makes sure that all files that exist in the directory are accessible to `bob` as well.
		* To provide permissions for another user.
			* `cd ~/acldir/dir1`
				* `sudo touch aclfile2.txt`
				* `getfacl aclfile2.txt`
					* Can see an ACL on the file already, even though it was not set.
						* This is what is inherited from the default ACL.
							* Remember the `mask` row are the maximum permissions that can be given.