---
title: "Special File Bits Suid And Sgid"
category: "rhcsa-cert-prep-2"
tags: ["rhcsa-cert-prep-2", "special", "file", "bits", "suid"]
---

* There are additional special bits for privilege escalation on executable files.
	* First is called `Set user ID (SUID)`
		* Run as user owner of the file.
		* Instructs Linux to run the executable file.
	* Second is called `Set group ID (SGID)`
		* Run as group owner of the file.
		* Instructs Linux to run the executable file.
	* Lastly, `Sticky`
		* Historically in Unix, if you set the `Sticky` bit on a program, it would remain in `swap`.
			* Makes it execute faster, the next time it is run.
				* Some versions of UNIX and BSD still maintain this functionality.
		* Not available in Linux.
			* Linux caches all executables for faster execution.
* If you check the `/usr/bin/su` command, you will see the file in `red`.
	* For example, `SUID Bit with Execute Permissions`
	* `.rwsr-xr-x 51k root 27  6月 22:15 /usr/bin/su`
		* The permissions for the `User Owner` are `rws`
		* The `s` in the User Owner's execute position, means we have `SUID bits set`. If the `s` is lowercase, then the underlying execute bit is also set.
		* If the `s` is uppercase `S`, then the execute permissions are not set.
			* Case of the letter `s`, is the easiest way to tell if the execute bit is set or not.
	* When the `s` exists in the Group Owner Permissions, such as `-rwxr-sr-x`, then the SGID bit is set.
		* Similarly, if the `S` is uppercase, then the underlying execute permissions are not set.
		* When the SUID bit is set and a regular user executes a command, their privileges get elevated to that of a user owner.
		* In this example: `.rwsr-xr-x 51k root 27  6月 22:15 /usr/bin/su`
			* User1 would be executing the `su` command as `root`.
				* This is due to the SUID bit.
* How to set the `SUID` bit:
	* Remember, permissions are:
		* Read = `4`
		* Write = `2`
		* Execute = `1`
			* User Owner --> Read permissions are set to `4`.
				* Write permissions are set to `2`.
				* Execute permissions are set to `1`.
					* We know this, because execute is equal to `1`.
						* Combined, this is equal to `7`.
	* For the Group Owner, we have read --> `4` and execute, which is equal to `1` for a total of `5`.
	* Permissions for `Other`.
		* Total permission are `755` --> `4+2+1=7`, `4+0+1=5`, `4+0+1=5`
* SUID, SGID and Sticky have values.
	* SUID is worth `4`.
	* SGID is worth `2`.
	* Sticky is worth `1`.
		* Of course, Sticky has no effect on files in Linux.
* To set the SUID bit:
	* Prefix the permissions with an extra digit.
	* Standard permissions are `755`.
		* We have an `s` in the user owner permissions.
			* We add a `4` for SUID.
			* `4+2+1 = 7`, `4+0+1 = 5`, `4+0+1 = 5`
				* There are no special bits in the group owner.
				* Add it all up and the result is `4`.
					* Total permissions with SUID set is:
					* `4 7 5 5`
						* To set these permissions with numeric mode, would type `sudo chmod 4755 /usr/bin/su`
						* Can use symbolic mode with `sudo chmod u+s /usr/bin/su`
							* `u` for `user`
		* SGID Execution:
* `SGID` Execution is very similar to `SUID`.
	* When SGID is set, the `s` resides in the Execute Position: `-rwxr-`s`r-x`
		* Of the Group Owner's permission.
			* When a regular user such as `user1` executes a command with `SGID` set, 
				* It runs with the privileges of the group owner of the file.
					* `-rwsr-sr-x. 1 root screen 0 Jan 5 13:26 /usr/bin/screen`
						* In the above case, this would be the `screen` group, such as `r-s` --> `screen` group
* To add the `SGID` bit to a file:
	* Prefix the permissions with a `2`
		* So for example: `-rwsr-sr-x. 1 root screen 0 Jan 5 13:26 /usr/bin/screen`
			* This would be `2 7 5 5`
				* Remember SUID = `4`, SGID = `2` and Sticky = `1`
					* That would make the `screen` command in the above example, with the permissions `2755`.
						* Then set with `sudo chmod 2755 /usr/bin/screen`.
						* Symbolic mode would be `sudo chmod g+s /usr/bin/screen`
							* `g` for `group`.
* All of the above commands allow privilege escalation, without requiring a password.
	* Can use the `find` command to look for these.
		* `sudo find / -perm -4000`
			* Finds all files with the SUID bit set.
	* To find files with the SGID bit set.
		* `sudo find / -perm -2000`