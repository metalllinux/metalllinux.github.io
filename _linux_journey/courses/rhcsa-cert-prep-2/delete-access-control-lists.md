---
title: "Delete Access Control Lists"
category: "rhcsa-cert-prep-2"
tags: ["rhcsa-cert-prep-2", "delete", "access", "control", "lists"]
---

* 3 different ways of deleting ACLs on a file or directory.
* Example, creating a directory and assigning multiple ACLs to it.
	* `mkdir acldeldir`
		* Set a user ACL:
			* `setfacl -m 	user:root:rwx acldeldir/`
		* Set a group ACL:
			* `setfacl -m group:root:rwx acldeldir/`
		* Another group ACL:
			* `setfacl -m group:audio:rw acldeldir/`
		* Last is the default ACL:
			* `setfacl -d -m user:root:rwx acldeldir/`
				* Then verify the ACLs with `getfacl`
	* To delete ACLs, use the `setfacl` command again:
		* Three different options available for deleting ACLs:
			* `-x Remove Specific ACLs`
			* `-k Remove all Default ACLs`
			* `-b Remove all ACLs`
				* To delete a specific ACL, specify a name such as `setfacl -x user:root acldeldir`
				* Remove User ACL is with `setfacl -x root acldeldir`
				* To delete a specific Default ACL, we would use `setfacl -x defaul:user:root acldeldir`
				* To delete all Default ACLs, use the `-d` option `setfacl -d acldeldir`
				* Remove All ACLs, use the following option: `setfacl -b acldeldir`
* A good example of the above is `setfacl -x group:root acldeldir`
	* The ACL we are targeting is the `root` `group` ACL.
		* When run `getfacl acldeldir`, willl then see `root` removed from the `group` lising.
	* For removing an individual user, we then run `setfacl -x root acldeldir`
		* Then with `getfacl acldeldir`, can see the `root` user ACL is now gone.
	* For removing all Default ACLs, run `setfacl -k acldeldir`
		* `getfacl acldeldir`
			* All `default` ACLs will then be removed.
	* For deleting remaining ACLs, can use the `-b` option.
		* `setfacl -b acldeldir`
	* If we want to recursively remove all ACLs within a directory, can use `setfacl -R -b acldeldir`
		* Removes any ACLs inside  the `acldeldir` directory, as well as on the directory itself.
* Solution answer:
	* `sudo mkdir /home/developers`
	* `sudo chown :developers /home/developers`
		* Make sure that all users can enter the developers group and read/write files.
			* `sudo chmod 770 /home/developers`
			* Verify with `ls -ld /home/developers`
	* All files created by the developers, should automatically be owned by the `developers` group.
		* Have to use the `SGID` bit for inheriting ownership.
			* `sudo chmod g+s /home/developers`
				* Verify again with `ls -ld /home/developers`
					* All files created in the directory, will inherit the group owner, which is `developers`
* Want 3 developers to read, write and create new ones, but not to delete files from other developers.
	* Need a sticky bit for this.
		* `sudo chmod o+t /home/developers`
			* Create dev test environments to test it.
				* Need to be able to traverse the directory and read the files.
					* Need to use `ACLs`.
						* Create the `devtest` group, which is `sudo groupadd devtest`
						* Now we need ACLs:
							* `sudo setfacl -m group:devtest:rx /home/developers
							* Then `getfacl /home/developers`
								* Gives all users in the `devtest` group read and execute permissions in the directory.
								* The above then provides the ability to traverse them.
								* Need a Default ACL, so the developers can access files in the future.
									* `sudo setfacl -d -m group:devtest:rx /home/developers`
										* Provides inheritance of group ownership.
											* `sudo usermod -a -G devtest user1`
												* `-a` is for append and `-G` is for supplemental group
													* Verify with `cat /etc/group`
														* Even though the user is in `/etc/group`, it can't traverse the directory directly.
															* `user1` won't be in the `devtest` group at the moment, you are added to the group on successful login. Can also use `su - user1` to login quicker and add the user that way.
																* If another developer wants to delete another's file in the directory, they will be stopped due to the stickybit.
															* 