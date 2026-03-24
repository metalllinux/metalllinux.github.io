---
title: "Create, Delete And Modify Local Groups And Group M"
category: "rhcsa-cert-prep-2"
tags: ["rhcsa-cert-prep-2", "create", "delete", "modify", "local"]
---

* Each user belongs to a primary group.
* When a user creates files, they are owned by the user's primary group.
* Users can also belong to supplemental groups.
	* Allows users the ability to access resources, owned by those additional groups.
* Create a group using `groupadd`
	* The most common option is `-g`
		* Specifying the group ID.
			* For example, creating a group called `accounting` with a group ID of `1050`
				* `sudo groupadd -g 1050 accounting`
					* Can verify this in the `/etc/group` file
						* Will see a newly created group called `accounting:x:1050:`
							* If we want to modify the attributes, we can use the `groupmod` command.
								* For example, changing the `group id`
									* `sudo groupmod -g 1051 accounting`
										* Changes the `group ID` to `1051`.
											* If `accounting` was a primary group for any users, their accounts would be automatically update.
												* Reflects the updated group IDs.
													* View the `/etc/group` file to see the updated `group id`
													* To place users in the group, we can use the `G` password. 
													* To add the `test` user into the `accounting` group.
														* `sudo gpasswd -a test accounting`
															* The group by the way, is the first column in the `/etc/group` file.
* `sudo usermod -a -G accounting test`
	* Does the same thing as the `group passwd` command.
		* If you want to add the `accounting` group for example, to the user's current list of groups, have to add the `-a` append option.
			* Since the G password command is group centric.
				* Use it to modify the `/etc/group` and `/etc/gshadow` files.
					* Similar to how the password command manages the `/etc/password` and `/etc/shadow` files.
* Can set passwords for groups.
	* `sudo gpasswd accounting`
		* Can verify this with the `/etc/gshadow` files.
			* Shows the hashed password as well.
				* Can change to the group, as long as the user is not `root` or `test`
					* Verify group membership by typing in `groups`
					* Create a new group with `newgrp accounting` 
						* Temporarily places the user into the `accounting` group.
						* If create a file and then check its permissions:
							* `ls -l`
								* Will see `test` `accounting`
									* Shows that the `accounting` group, will be your primary group.
										* By using the above method, we can join these groups and by doing so, make them our primary group.
											* If a user already in a group wants to change some stuff, they don't have to input a password.
* To delete a user from a group `sudo gpasswd -d test accounting`
* If you want to allow groups to administer themselves, instead of `root`.
	* Can add an administrator to a group.
		* `sudo gpasswd -A test accounting`
			* Then checking `/etc/group`
				* You can see that `test` is not in the `accounting` group.
				* If you want test to administer the `accounting` group and be a part of it.
					* You have to add the same user again.
				* If you have a list of users you want to add to a group, can use the `-M` option.
* To delete a group:
	* `sudo groupdel accounting`
* Verify the group is gone, by checking the `/etc/group` file.
	* Another good command for managing groups is `groupmod`, we can change the group ID and name.
		* Not as powerful as `usermod`, but still useful.