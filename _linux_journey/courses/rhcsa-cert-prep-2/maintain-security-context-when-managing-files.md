---
title: "Maintain Security Context When Managing Files"
category: "rhcsa-cert-prep-2"
tags: ["rhcsa-cert-prep-2", "maintain", "security", "context", "when"]
---

* When you copy a file to a new location, it inherits the security context of the directory.
* If you copy a file to /home, the type will be `user_home_der_T`
* If you want to keep the original security context of a file.
	* Need to apply additional options to the commands.
		* `cp -a`
			* `-a` is for archive and preserves permissions, access controls lists, extended attributes and SELinux security context.
			* `mv` command preserves attributes by default.
			* When you want to backup a file using `tar`, you need to pass the `--selinux` option, which preserves the security context.
			* To copy files from one host to another, whilst preserving the security context:
				* `rsync -a X`
		* The safer option though is to `cp` or `mv` the commands normally and then restore their context with `restorecon`