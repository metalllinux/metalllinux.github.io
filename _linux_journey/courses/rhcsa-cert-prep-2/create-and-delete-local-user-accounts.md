---
title: "Create And Delete Local User Accounts"
category: "rhcsa-cert-prep-2"
tags: ["rhcsa-cert-prep-2", "create", "delete", "local", "user"]
---

* In Linux, every user has the following:
	* Username
	* User ID
	* Primary Group
		* For use with discretionary access control.
			* Meaning access is granted based on whom the user is and what groups they belong to.
* Users and Passwords
	* User Account Information
		* Stored in `/etc/passwd`
	* Passwords and Account Aging
		* Stored in `/etc/shadow`
	* User account commands and defaults for the shadow utilities, are stored in:
		* `/etc/login.defs`
* Account Defaults
	* Commands that use the `login.defs` file include:
	* `/etc/login.defs`
		* `useradd`
		* `userdel`
		* `usermod`
		* `groupadd`
		* `groupdel`
		* `groupmod`
		* `change`
	* `/etc/login.defs` contains:
		* Password ageing settings.
		* Minimum and Maximum numbers for user ids.
		* Minimum and Maxium numbers for system account ids.
		* Minimum and Maximum numbers for user group ids.
		* Minimum and Maximum numbers for system group ids.
![Screenshot_20230712_205604.png](../../_resources/Screenshot_20230712_205604.png)
	* Notice in most cases that system id numbers are less than 1000.
	* Also configured are whether to create initial home directories.
		* and the hash encoding type, such as MD5 or SHA512.
	* `/etc/default/useradd`
		* `HOME=/home`
			* Details where home directories are created.
		* `INACTIVE=-1`
		* `EXPIRE=`
			* Whether the account should expire.
		* `SHELL=/etc/skel`
			* Which shell to use - if not specified in the command line.
		* `SKEL=/etc/skel`
			* Where the skeleton directory resides.
			* Contains the files that are copied to each new users' home directory.
			* An example of this is here:
`howard@explosion:~$ ls -la /etc/skel
total 28
drwxr-xr-x 1 root root   84 Jun 20 11:07 .
drwxr-xr-x 1 root root 4040 Jul 13 21:46 ..
-rw-r--r-- 1 root root  220 Apr 24 06:23 .bash_logout
-rw-r--r-- 1 root root 3526 Apr 24 06:23 .bashrc
-rw-r--r-- 1 root root 5290 Apr 14 04:58 .face
lrwxrwxrwx 1 root root    5 Apr 14 04:58 .face.icon -> .face
-rw-r--r-- 1 root root  807 Apr 24 06:23 .profile
`
		* Includes shell initialisation files such as:
			* `.bash_logout`
			* `.bash_profile`
			* `.bashrc`
		* Can add any other files you want here to add to a new user's home directory.
			* Mozilla configuration files and so on.
		* `CREATE_MAIL_SPOOL=yes`
			* Whether to create a mail spool or not.
	* Pluggable Authentication Modules
		* Inside the `/etc/pam.d/` directory.
			* Configuration files for the pluggable authentication modules are stored.
				* `atd`
				* `crond`
				* `cups`
				* `login`
				* `passwd`
				*  `polkit-1`
				* `remote`
				* `runuser`
				* `sshd`
		* `useradd` command
			* Any options left out are taken from the system defaults.
			* `sudo useradd test`
				* Can check for passwords by going to viewing `/etc/passwd`
* Breaking down the `passwd` file.
`test:x:1001:1001::/home/test:/bin/bash
`
		* `test` = username
		* `x` = placeholder for the password.
			* In previous versions of RHEL, the password was stored here.
				* `x` means we are using the shadow suite and the password is stored in the `/etc/shadow` file.
		* `1001`
			* User's numeric ID number.
		* `1001`
			* Primary group ID number.
			* Every user has to belong to one group, which is their primary group.
				* When a user creates any files, they will be owned by this particular group.
			* Can cross-reference the group ID in the `\etc\group` file.
			* Can see the group listed here.
			* In Red Hat-based distributions, primary group is the group with the same name as the user. Created automatically.
			* Not all distributions act this way.
		* Fifth column `bob` is the `GECOS` field.
			* Used to store general records.
				* Essentially a comment field to store information about the user account.
			* This field is world-readable.
		* `/home/test` user's home directory.
			* Also configured in the `/etc/login.defs` file.
		* `/bin/bash`
			* The shell to execute upon login.
           * Need to view the password and ageing information in the `/etc/shadow` file.
               * If there is a second column with 2 exclamation points, it means a password has not been set yet.
                   * The user would not be able to login.
                       * After entering in `passwd USER` and adding their user, you will see an encoded password for them in the `/etc/shadow` file.
               * Not all Linux distros create the home directory for a new user automatically (based on a setting by `login.defs`.
               * `ls -a`
                   * Show all files.
               * If you do the above command in the home directory, you see all of the hidden files
                   * `.bash_logout`
                   * `.bash_profile`
                   * `.bashrc`
                   * `.mozilla`
               * The above are copied over from the `/etc/skel` directory.
                   * Also listed in the `login.defs` configuration file.
If you want to delete a user, but keep their home directory and files:
       * `sudo userdel USER`
If want to delete a user and their home directory:
       * `sudo userdel -r USER`
          * View the `/etc/passwd` to verify deletion.
              * To verify the home directory is gone `ls /home` and then check the user is gone.
			