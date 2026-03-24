---
title: "Special Directory Bits Sgid And Sticky"
category: "rhcsa-cert-prep-2"
tags: ["rhcsa-cert-prep-2", "special", "directory", "bits", "sgid"]
---

* The behaviour is different that with files.
* Setting the SUID `Set user ID`
	* No affect on directories.
* Set group ID (SGID)
	* Provides group inheritance for files.
		* and directories created inside the directory we configure.
* The `Sticky` bit works for directories in Linux.
	* When the `Sticky` bit is set, only the owners can delete their files.
* To test this, you can run `sudo mkdir accounting`
	* The directory will be owned by `root` and the group as `root`.
	* The permissions for the User Owner are `rwx`.
	* The Group Owner is `r-x`
	* Other is `r-x`
	* Create the `accounting` group with `sudo groupadd acconting`
	* Change the `accounting` group directory's group name.
		* `sudo chown :accounting accounting`
			* Now need to add  the `SGID` bit and write permissions for the Group Owner.
				* `sudo chmod 2770 accounting`
					* The `2` is for `SGID`
						* Should then give us `rwx` for the root user.
						* `rws` for the `accounting` group.
						* `---` for Other.
							* Plus SGID, which has the letter `s` (shown above) in the group position.
* How do these SGID Bits affect directories?
	* The SGI Bits represent the only inheritance in standard Linux permissions and ownership.
		* For example, all files and directories created inside the `accounting` directory, will inherit the Group Owner, which in this case is the `accounting` group.
		* If `user1` creates a file in the `accounting` directory, it will be owned by `user1` and the `accounting` group.
		* Allows us to create a di rectory for group collaboration.
		* All users would need to belong to the `accounting` group to have write access.
			* To demonstrate in a terminal, we do `sudo useradd -G accounting ted`
				* `-G` is supplemental group
			* Provide `ted` a password with `sudo passwd ted`
			* Creates username called `ted`, which belongs to the `accounting` group.
			* Should see the accounting group at the bottom if run `cat /etc/group`
				* Will see `ted` added to the end of the line here as well.
			* Login as `ted` with `su - ted`
			* cd into the accounting directory.
			* Create a file with `touch` and you will see it owned by `ted` and the `accounting` group.
* We add a Sticky bit, by adding a `1` to the left of the permissions.
	* For example `sudo mkdir stickydir`
		* Give all permissions to all people, including the Sticky bit as well.
			* `sudo chmod 1777 stickydir`
				* You will see the directory has a `t` in the execute position of Other.
					* This will be a lowercase `t`, if execute for Other is set.
						* Otherwise it will be an uppercase `T`.
							* The purpose of a Sticky Bit on a directory, is to keep users from deleting or moving each other's files.
							* `cd` into the directory with `cd /home/stickydir/`
							* Then `touch file.txt`
								* Now give `rwx` permissions to everyone, with `chmod 777 file.txt`
									* Then change into another user, for example `su - ted`
										* The file `file.txt` has `rwx` for all users, so we have full accses, including delete.
											* If you then do `rm file.txt`, you will not be allowed to remove it.
											* The Sticky BIt is usually used for world-writable sticky directories, such as `/tmp`
												* You can verify this by typeing in `ls -ld /tmp` (the `-ld` is for directory). You should then see the `t` in the `Other` permissions section.