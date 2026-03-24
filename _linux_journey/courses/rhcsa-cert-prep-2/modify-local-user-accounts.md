---
title: "Modify Local User Accounts"
category: "rhcsa-cert-prep-2"
tags: ["rhcsa-cert-prep-2", "modify", "local", "user", "accounts"]
---

* In order to change a user's account settings, after a user has been created, need to use `usermod`:
	* `usermod [option] <username>`
	* `usermod` options:
	* Specify home dir:
		* `-d <homedir>`
	* Change user ID:
		* `-u <userid>`
			* For example having NFS for network file sharing and need to use the same USER ID on different hosts.
	* Change primary group ID:
		* `-g <groupid>`
			* All users belong to the primary group.
			* In RHEL-based Linux:
				* The primary group is unique to the user.
				* Created automatically.
					* All files created by the user.
					* Will belong to the primary group initially.
	* Supplemental groups:
		* If you want the user to belong to an additional or supplemental group
		* `-G <groups>`
			* May want a user to belong to the `wheel` group, so they have admin privileges.
			*  Or a group that manages a specific service, such as Apache.
				*  It is a complete list and will override the list, unless the next option is selected.
	*  Append to existing settings:
		*  `-a`
			*  If you do that in combination with `-G`, such as `-Ga`, it allows you to append information to Supplemental groups.
	*  Change a user's name.
		*  `-l <name>`
	*  Lock/unlock a user's password.
		*  `-L` / `-U`
	*  It does not stop a user from authenticating using other methods, such as private-public key pairs.
	*  Move home directory
		*  `-m`
	*  If user wants a specific shell, that is not default such as `zsh`:
		*  `-s <shell>`