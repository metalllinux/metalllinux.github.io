---
title: "Diagnose Routing Selinux Policy Violations"
category: "rhcsa-cert-prep-2"
tags: ["rhcsa-cert-prep-2", "diagnose", "routing", "selinux", "policy"]
---

* For instance where a user modifies critical system files.
* If the `auditd` service is running, SELinux logs to `/var/log/audit/audit.log`
*  If the `auditd` service is not running, it logs to `/var/log/messages`
*  Need to elevate privileges to see these.
	*  To create messages, we can change the Security Context of the `/etc/shadow` file.
		*  To see the original context, type in `sudo ls -lZ /etc/shadow`
			*  It will show `shadow_t` as the security context.
			*  Change the context with the following command:
				*  `sudo chcon -t etc_t /etc/shadow`
					*  In this case, the `etc_t` would not be the correct security context of this file.
						*  If you tail the audit log with `/var/log/audit/audit.log`
							*  Then attempt to change your password with the `passwd` command.
								*  The command will output an `Authentication token manipulation error` message.
								*  You can also receive SELinux alert messages.
									*  There is also an SELInux Alert Browser as well.
									*  Can click `Troubleshoot` and see solutions to the alerts provided.
										*  The least intrusive solution is at the top.
											*  To search the audit logs, you can use the `ausearch` command like so:
												*  `ausearch -c 'passwd' --raw | audit2allow -M my-passwd`
													*  This command searches the audit logs for the word `passwd` and then sends it to the `audit2allow` command and this builds a new security policy module. This allows the action to succeed.
														*  `semodule -X 300 -i my-passwd.pp`
															*  The security module is then inserted into the security policy and the action no longer fails.
																*  Creating a new security policy is a last resort, as messing around with Security Policies can be complex.
*  AVC Denial Message:
![Snapshot_2023-09-10_20-36-45.png](../../_resources/Snapshot_2023-09-10_20-36-45.png)
* Going through the above errors, we find `AVC`, which is `Access Vector Cache`. This tells us its an SELinux error.
	* We can see what was `denied`, which in this case was `{ create } for pid=202425`. The command name is `passwd`. The context of the subject is `passwd_t` and the context of the object is `etc_t`
	* The second message has a security context of `USER_CHAUTHTOK` (Change, Auth, Token). The same process ID of `pid=202425` is shown. The subject type is `passwd_t` again and the error message starts from `msg=op'`.  
		* The operation was a `PAM` --> Pluggable Authentication Module that was trying to change the authentication token. It was ran by the `user1` account. The command executed was `/usr/bin/passwd`. The host was `rhhost1` and it was on a `pts/2` terminal. The result was `res=failed`.
* SELinux Solutions:
	* Change a boolean to allow an action to happen.
		* Booleans are easy to look for and you can use the `sudo semanage boolean -l` command to view them.
			* This then gives you a short description.
				* Service configuration files will often have comments in them.
		* To change the boolean, we use:
			* `sudo setsebool -P <boolean> on`
	* Can change a file's type or directory. 
		* Can use `chcon` or `semanage`
			* Context can be incorrect, if files are not copied correctly.
				* Using the `chcon` command, we can modify the context appropriately.
					* These changes only last until an admin performs a `restorecon` or a system-wide relabel occurs.
						* Use `semanage` to change the file's context in the security database. This makes the change persistent.
							* Then use `restorecon` to change the context of the file.
								* A real-world example is if you want to place a MySQL DB into a non-standard location.
									* You would need to update the Security Context for the MySQL DB's directory in the policy. Then run `restorecon` on the directory and files.
	* The last resort is to create a Security Policy Module.
		* We are modifying the policy, to allow something, when originally it was being denied.
			* It is better to find out why it was being denied first and then fix it.
* In Summary with how to Troubleshoot SELinux Issues
	* Put SELinux into Permissive Mode.
		* Allows the application to run all the way through, generating all errors.
		* Run the application that was denied.
		* Search through the audit logs.
		* Look for SELinux Desktop Notifications.
		* Follow instructions in the SELinux Alert Browser.
* Finally, to restore the context of the `etc/shadow` file, we can run `sudo restorecon /etc/shadow`
						* 