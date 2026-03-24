---
title: "List And Identify Selinux File And Process Context"
category: "rhcsa-cert-prep-2"
tags: ["rhcsa-cert-prep-2", "list", "identify", "selinux", "file"]
---

* All Subjects and Objects in SELinux have a security label.
	* To get the security context of a user, use the `id` command.
		* `id -Z`
			* Then shows the Security Context of a user.
				* For example in this case, we see the output of `unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023`
					* SELinux User Context --> `unconfined_u`
					* Role for role-based access control is `unconfined_r`
					* Type for Type Enforcement is `unconfined_t`
						* This part is for Mandatory Access Control
					* `s0-s0:c0.c1023` is the security level for multi-level and multi-category security.
* How check the security context of running processes using the `ps` command:
	* `ps -eZ`
		* Shows all processes and their security context.
			* Files have a Security Context as well, since they are also Objects.
				* For files, we can use `ls -lZ`
* Domain Transitions
	* Subjects can move from one type to another.
		* If the Security Policy allows it.
		* An example is the `passwd` command, we can check this with `ls -lZ /usr/bin/passwd`
			* This outputs `root root system_u:object_r:passwd_exec_t
				* The password command's type is `passwd_exec_t` in this case.
					* When passwords are set, they are written to the `/etc` shadow file.
						* To get the Context, have to use `sudo`. `sudo ls -lZ /etc/shadow
							* The output will show `shadow_t`
								* If change the password and just leave it running without entering a password and then check the running process with `ps -eZ`, you'll see the Context as `passwd_t`
									* When the `passwd` command is run, it can transition to the `passwd_t` type.
										* There is a rule that allows a Subject of type `passwd_t`, to write to an Object with type `shadow_t`.
											* If it does not transfer to the `passwd_t` type, the command cannot write to the shadow file.
* All Users, Processes and Files have a Security Context.
	* Processes can transfer from one `Type` to another to execute code in that `Type`.
		* If the security policy allows it.