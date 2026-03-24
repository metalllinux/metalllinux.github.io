---
title: "Log In And Switch Users In Multi User Targets"
category: "rhcsa-cert-prep-2"
tags: ["rhcsa-cert-prep-2", "log", "switch", "users", "multi"]
---

* Times we need to switch temporarily, to access `root` or another resource.
* `whoami`
	* Prints out the user you are logged in as.
* `logname`
	* Does a similar thing to `whoami`
* The differences between the two are:
	* `su root`
		* Then if type in `whoami`
			* Says we are `root`
		* If type in `logname`
			* Shows the user you originally logged in as.
	* The environment (system configuration etc) is what occurs when you log in.
		* Can check with `echo $PATH`
			* Shows a list of directories that Linux will look through to find commands.
				* The directories also show your username in them.
					* When switching to `root`, you still keep the original user's environment.
* For `su - root`, emphasis on the `-`
	* Do the same Path Variable command as above.
		* In this case, we also inherit the `root` user's environment.
			* Can also switch users by using the `sudo` command.