---
title: "Read Access Control Lists"
category: "rhcsa-cert-prep-2"
tags: ["rhcsa-cert-prep-2", "read", "access", "control", "lists"]
---

* ACLs are layered on top of Linux permissions.
	* Can't use standard tools such as `ls` to list those.
* An example:
	* `mkdir aclexercise`
	* `touch aclfile`
	* To read the ACLs on the file, we would use the `getfacl` command.
		* Installed by default on CentOS.
			* `getfacl aclfile`
		* For example, you would see a similar output to this:
`getfacl temp
# file: temp
# owner: myuser
# group: myuser
user::rw-
group::r--
other::r--
* Lists the standard Linux permissons.
* Can list the same permissions in tabular format.
	* Easier to see which permissions belong to each user.
	* `getfacl -t aclfile`
`getfacl -t temp
# file: temp
USER   myuser    rw-
GROUP  myuser    r--
other            r--`
* Can set ACLs using `setfacl`.
	* `setfacl -m user:root:rwx aclfile`
		* The `-m` is for modify.
		* The `username` here would be `root`.
		* Then the permissions come after that, which in this case is `rwx`.
			* Sets an ACL for a `root` user.
* Then the file would look something like this:
`getfacl -t temp
# file: temp
USER   myuser    rw-
user   root      rwx
GROUP  myuser    r--
mask             rwx
other            r--`
* Will see on CentOs that the permissions of the file will now look like `-rw-rwxr--+`, notice the `+` at the end.
	* On Garuda Linux anyway, it looks like an `@` --> `.rw-rwxr--@`
		* Shows we have an ACL on  the file.
		* Also notice from the previous example, there is a `mask` line: 
		* `mask             rwx`
			* Shows the maximum allowed permissions.
* Can also list permissions recursively.
	* `getfacl -R /home > home-perms.txt`
* Can see more information by using `man getfacl`
