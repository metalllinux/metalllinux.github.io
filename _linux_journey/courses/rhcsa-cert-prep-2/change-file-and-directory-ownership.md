---
title: "Change File And Directory Ownership"
category: "rhcsa-cert-prep-2"
tags: ["rhcsa-cert-prep-2", "change", "file", "directory", "ownership"]
---

* `-rwr-r--. 1 user1 accounting 0 Jan 5 13:26 file.txt`
	* User Owner is `user1`
	* Group Owner is `accounting`
		* `chown` to change ownership.
		* `chownn [options] <user>:<group> <file>`
			* Setting the user owner:
				* `chown user1 file.txt`
					* Need to be `root` or eleveate priviliges with `sudo`
			* Setting the group owner:
				* `chown :accounting file.txt`
			* To set both user and group ownership:
				* `chown user1:accounting file.txt`
					* Users and groups have to exist, before ownership change can occur.
						* Can get a list of users via viewing the `/etc/passwd` file.
			* Recursive Ownership
				* `chown -R user1:user1 /home/user1
					* Sets the primary group for multiple files.
						* Check `man chown` for more information on the `chown` command.