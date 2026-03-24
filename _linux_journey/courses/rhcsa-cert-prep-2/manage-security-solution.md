---
title: "Manage Security Solution"
category: "rhcsa-cert-prep-2"
tags: ["rhcsa-cert-prep-2", "manage", "security", "solution"]
---

* Moved the web document root.
* Configured discretionary access control to `allow`.
* Configured Apache access control to `allow`.
* Accessed the website via Firefox.
* Access was denied by SELinux.
* Current boolean does not provide access to a file. The solution is:
	* `setsebool -P httpd_read_user_content 1`
		* Allows the `apache` service to read the contents of `/home`
			* It does not just restrict `apache` to reading the contents of `/home/webdoc`
* Another solution is to use the `ausearch` (auto search) command.
	* Looks through the `audit.log` for HTTP.
		* `ausearch -c 'httpd' -raw | audit2allow -M my-httpd`
![Screenshot_20230914_170205.png](../../_resources/Screenshot_20230914_170205.png)
		* The full output of the above command would be `semodule -i my-httpd.pp`
		* Sends it to the audit to allow the command to write to the disk..
			* Creates an SELinux policy module called `my-httpd`
				* Then answers the customer's `my-httpd.pp` policy package.
* Can see `my-httpd.pp` and `my-httpd.te`
	* `httpd.te` has the following rule inside it:
		* `allow httpd_t user_home_t:file read;`
			* Allow a subject of type `httpd_t` to read objects of type `user_home_t`
				* It allows the `apache` process to read any files with type `user_home_t`.
* Third solution that is not provided either.
	* Check the SELinux type of `/var/www/html` 
		* That is the old document route.
			* `ls -ldZ /var/www/html`
				* Provides the SELinux security context:
![Screenshot_20230914_182356.png](../../_resources/Screenshot_20230914_182356.png)
						* Shows the type as `httpd_sis_content_t`
* Also show the type of the `webdoc`, that being `ls -ldZ /home/webdoc` --> `user_home_dir_t` 
	* To change the type temporarily to the correct type, we can use:
		* `sudo chcon -R -t httpd_sys_content_t
 /home/webdoc`
 	* This won't surive a system relabel or `restorecon` operation.
 	* Changes the type of the `webdoc` directory and files inside to `httpd_sys_content_t` 
		* From this, able to see the tes html file without issue.
			* To help it survive a `restorecon` or `relabel` we do `sudo semanage fcontext -a -t httpd_sysc_content_t "/home/webdoc(/.*)?"`
			* The `-a` is used for files.
				* Then follow-up with a `restorecon` --> `sudo restorecon /home/webdoc` , then add a new default type for files in the `/home/webdoc` directory.
					* Then if a `restorecon` is ran, these files will be relabelled to their defaults.
						* This is a granular solution.