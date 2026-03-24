---
title: "Use Booleans To Modify Selinux Behaviour"
category: "rhcsa-cert-prep-2"
tags: ["rhcsa-cert-prep-2", "booleans", "modify", "selinux", "behaviour"]
---

* in multiple cases, Admins do not have to rewrite SELinux policies.
	* To permit certain actions.
		* SELinux has booleans - these activate/deactivate certain functionality.
			* To get a list of booleans, we do `getsebool -a`
			* To find an individual value, we do `getsebool mozilla_plugin_use_gps`
				* In the above case, it shows the boolean is `off`
			* Can also get the list of booleans, with `sestatus -b`
			* A third tool to grab the list of booleans, is `semanage`
				* Elevated privileges are required for this one.
					* `sudo semanage boolean -l`
						* This command also provides a short description of each boolean.
			* To temporarily change a boolean, use the `set setsebool mozilla_plugin_use_gps on`
				* This will not survive a reboot.
					* To make a boolean consistent, we have to add it to the policy.
						* `sudo set setsebool -P mozilla_plugin_use_gps on`
							* Then verify this with `semanage`, using `sudo semanage boolean -l | egrep 'SELinux|mozilla_plugin_use_gps'`
								* egrep and alternation were used, to show the header and the boolean.