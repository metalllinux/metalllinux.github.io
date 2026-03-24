---
title: "Elevating Privileges Using Sudo"
category: "rhcsa-cert-prep-2"
tags: ["rhcsa-cert-prep-2", "elevating", "privileges", "sudo"]
---

* Privilege Escalation Comparison
* `sudo`
	* Enter user's password
	* Elevates privileges for one command.
	* All command execution is logged.
	* Granular permission system; only allows certain people particular privileges.
		* Admin decides what commands you are allowed to run, as well as what files you have access to.
* `su`
	* Enter root's password
		* If someone leaves the company, then the password has to be changed.
	* Elevates privileges for whole session.
		* Increase chance of human error.
	* No accountability; all users who switch are `root`
	* All-powerful for anyone who has password.
* Example, `sudo cat /etc/shadow`
	* `sudo` will cache the user's password for a short period of time.
		* For convenience reasons, this is the reason why.
		* `sudo` has a configuration file, so you can provide privileges.
			*  Can even set which commands a user can run.
		* Can edit with `visudo`
			* Locks the `sudoers` file and edits it using `vi`.
				* `sudo visudo`
					* Once done editing, it checks the configuration.
					* Allows us to group together `users`, `hosts` and `commands`
						* Then create access control rules to allow certain users to run certain commands on certain hosts.
					* Important one is `%wheel`
						* When `sudo` is using operating system groups, we need to prefix the name with a `%` symbol.
						* `%wheel ALL=(ALL) ALL` - gives us permissions to run all commands on all hosts, as all users.
	* Check the `wheel` group in `/etc/group`
		* Last column on the right is `wheel:x:10:USER_HERE` and all members of the `wheel` group are added here.
			* How we are allowed to elevate privileges.
				* Add users to the `wheel` group and that allows them to elevate privileges.