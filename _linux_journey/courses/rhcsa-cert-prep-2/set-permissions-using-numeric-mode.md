---
title: "Set Permissions Using Numeric Mode"
category: "rhcsa-cert-prep-2"
tags: ["rhcsa-cert-prep-2", "permissions", "numeric", "mode"]
---

* Permission Methods
	* Numeric Method
	* Symboolic Method
* `-rwxr-x---. 1 user1 accounting 0 Jan 5 13:26 file.txt`
	* If `-rwxr-x---` starts witth a `-`, this means it is a file.
	* If it was a directory, we would see the letter `D`.
	* If it is a symbolic link, it would be an `L`.
	* If it is a character device, it would be a `C`.
	* If it is a pipe, it would be `P`
	* If it is a block device, then it would be `B`
		* Next 9 characters, would be `rwxr-x---`
			* User
			* Group Owner
			* Permission
		* First Group `rwx` is the User Owner of the file.
		* Next Group (`r-x`) is for the Group Owner.
		* Last Group (`---`) is for Permissions for Others.
			* People whom don't belong to the group, everyone in the universe.
	* Must know the values of Read, Write and Execute
		* Read --> `4`
		* Write --> `2`
		* Execute --> `1`
	* To add Read, Write and Execute for the owner.
		* `4` + `2` + `1` = `7`
	* To set Read and Execute for the Group Owner:
		* `4` + `1` = `5`
	* Other has no permissions, so is set to `0`
	* Then to set the permissions for the above `file.txt`, we would use the values `750`
	* Syntax for `chmod` --> Change Mode
		* `chmod [options] <permissions> <filename>`
		* `chmod 750 file.txt`
	* Initial permissions are assigned to a file, based on the value of the `umask`.
	* Use case for Recursive in Symbolic Mode.