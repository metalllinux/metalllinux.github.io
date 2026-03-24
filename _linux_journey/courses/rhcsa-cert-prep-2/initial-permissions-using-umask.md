---
title: "Initial Permissions Using Umask"
category: "rhcsa-cert-prep-2"
tags: ["rhcsa-cert-prep-2", "initial", "permissions", "umask"]
---

* When files created, initial permissions are applied automatically.
	* Calculated based on a bit mask called `umask`.
* To see a `umask`, type in `umask` into a terminal.
* Can also view `umask` in symbolic notation, using the `-S` option.
* For example:
	* `umask`
	* `0022`
	* `umask -S`
	* `u=rwx,g=rx,o=rx`
* `umask` can either have 3 or 4 characters.
* Can add the leading `0`, or leave it off for standard permissions.
	* Isn't the same format as numeric permissions such as `754`
	* This is because the values are upside down, because it is a mask.
* Intial Directory Permissions.
	* `777` Max Initial Directory Mode
* To calculate the `umask`, have to subtract this from maximum allowed initial permissions.
	* Based on whether the item is a file or directory.
		* For directories, maximum initial permissions are `777`.
			* This is because having `execute` on a directory, does not cause a security risk.
		* Then for example we have a `umask` of `022`.
			* We minus that from the `maximum initial permissions` , `777` - `022` = `755`
				* Or in symbolic mode, this would be `rwxr-xr-x`
	* `666` Max Initial File Mode
		* Do not allow execute permissions on files by default, for security purposes.
			* In symbolic mode, this would be `rw--rw-rw-`
* To calculate the `umask` for Initial File Permissions:
	* `666` - `022`= `644`
		* In symbolic mode, this would be `rw-r--r--`
* Temporarily changing the `umask` command:
	* `umask 0002`
		* Then verify it has been set my typing `umask`.
			* A `umask` of `0002`, would give default directory permissions of `rwxrwxr-x` .
			* For files, this would give `rw-rw-r--`
* All of this works only for our current login session.
* If a user wants to permanently change their `umask`, they can add it to their `bash` startup file.
	* In `.bashrc`
* An example of `.bashrc`:
`File: /home/howard/.bashrc
# .bashrc
umask 0002
# If not running interactively, don't do anything
[[ $- != *i* ]] && return`
* If an administrator wants to change the systemwide `umask`
	* Can add the above configuration to `/etc/profile.d/umask.sh`
		* Should have a different `umask` for `root` and then other Users.
	* The file would look like this:
`if [ "$UID" -ge 1000 ] ;then`
`	       umask 0002`
`fi`
		* `-ge` means greater or equal to.
		* Only overrides the `umask` if the user's ID number is `1000` or greater.
		* Save and Exit and then it takes effect the next time you log in.
		