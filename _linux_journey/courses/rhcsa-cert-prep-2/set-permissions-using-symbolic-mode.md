---
title: "Set Permissions Using Symbolic Mode"
category: "rhcsa-cert-prep-2"
tags: ["rhcsa-cert-prep-2", "permissions", "symbolic", "mode"]
---

* `-rwxr-x---`
* In symbolic mode, a value is assigned to each position and presents a symbolic representation of the desired permissions.
	* For example `u=rwx`
	* No math involved unlinke numeric mode.
* For example, to specify `rwx` for the User Owner.
	* This would be `u=rwx`
* For `r-x` for the Group Owner:
	* `g=rx`
* To set `---` for Other:
	* `o=`
		* There is intentionally nothing after the `=`
* To set multple permissions at once, separate them with a comma --> `chmod u=rwx,g=rx,o= file.txt`
* Can also add permissions by changing the `=` into a `+`
	* `chmod u+rwx file.txt`
		* Adds `rwx` to a user.
* To subtract permissions, replace with a `-` sign.
	* `chmod u-x file.txt`
	* To take execute permissions away from Other, this would be `chmod o-x file.txt`
* How to add multiplep permissions at once:
	* `chmod u=rwx,g=rx,o= file.txt`
		* More typing, but easier to understand.
			* To add or take away permission, in numeric mode we would have to know the initial permissions and then re-calculate accordingly.
* Can add and subtract permissions in symbolic mode.
* Remove execute permissions from the group `chmod g-x file.txt`
* Can also remove individual permissions per Owner:
	* `chmod ugo-x file.txt`
* Can specify `a` for all positions, includes User Owner, Group Owner and Other.
	* `chmod a-x file.tx`
* To remove execute permissions for every file in a user's home directory:
	* `sudo chmod -R a-x /home/bob`
		* Changing another user's permissions, so have to do it with `sudo`
* `man chmod` for more information.