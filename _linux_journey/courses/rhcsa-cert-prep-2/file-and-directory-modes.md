---
title: "File And Directory Modes"
category: "rhcsa-cert-prep-2"
tags: ["rhcsa-cert-prep-2", "file", "directory", "modes"]
---

* Standard Linux Permissions support three different modes.
	* Read
	* Write
	* Execute
		* Load file into memory and run on the CPU.
		* Sets `execute` bits.
* For directories:
	* Read Permissions - read the metadata of files in the directory.
		* If a user has read access to the directory.
			* Can list the contents of the directory.
				* Files and Directories inside it.
					* If user does not have `read` access and type `ls`, they will see a load of `?` within the directory.
					* Where the metadata should be.
	* Write Permissions - Write to the directory.
		* Creating new files.
	* Execute Permissions on a directory
		* Allowed to enter and traverse the directory.