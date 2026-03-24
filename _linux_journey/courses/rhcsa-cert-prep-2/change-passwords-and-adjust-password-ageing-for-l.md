---
title: "Change Passwords And Adjust Password Ageing For L"
category: "rhcsa-cert-prep-2"
tags: ["rhcsa-cert-prep-2", "change", "passwords", "adjust", "password"]
---

* Main tool for managing passwords on Linux, is the `passwd` command.
	* If type in the command `passwd` without any additional flags, it will encode the password and save it in the `/etc/shadow` file.
	* An admin can use the same tool to lock/unlock passwords and set account ageing information.
	* Common `passwd` Options:
	* Delete password
		* `-d`
			* Essentially a newly created user, without a password.
		* `-e`
			* Expires a password.
				* User with expired password, needs to reset the password on next login.
		* `-l`
			* Locks a password.
				* Only locks the password and if the user has valid SSH keys, they would still be able to login.
					* Use account ageing to lock the actual account.
						* The `usermod` command can do the same action, with an uppercase `-L` instead.
		* `-u`
			* Unlocks an account password.
		* `-S`
			* Outputs the password's status.
		* Example `passwd` usage.
			* `sudo useradd test`
				* Can verify by looking at the `/etc/shadow` file:
					* `sudo cat /etc/shadow`
					* The last line will show the newly added user.
						* Checking the second column, you will see two `!!`.
							* It means that the `test` account will not have a password.
			* `sudo passwd test`
				* Provides a password.
					* Insecure passwords will be informed.
						* If elevate to `root` privileges, can override this warning.
					* If user setting our own password, we would not be able to override the warning.
					* Check the`/etc/shadow` file again and the second column will now contain a SHA512 password in it.
			* To lock the account, we use `sudo passwd -l brian`
				* If you check the `/etc/shadow` file again, you will see in the second column the SHA512 Hash, but it is prefixed by two `!!` marks.
					* The `test` account can still login if have SSH keys.
						* Check the `change` command if you need more power for locking accounts.
			* To unlock the password:
				* `sudo passwd -u test`
					* If you check the `/etc/shadow` again, the same has will be present.
			* To have further control on which passwords are acceptable:
				* You can find that setting in the `/etc/security/pwquality.conf` file
			* `less -N`
				* Turns line numbers on.
			* The `pwquality.conf` file defines which character combinations are allowed in an acceptable password.
				* For example, if `difok` is equal to 1, at least 1 character in the new password, cannot be in the old one.
				* Another example is `minlen`, if this is set to `8`, then the password has to be a minimum length of 8 characters.
				* A third example is `LETTER_HEREcredit`
					* If you have a strong character in your password.
						* Receive "credit", that can be applied toward a minimum password length.
					* Credit can be given for uppercase, lowercase and other characters.
						* Including ones that are not digits as well.
				* A fourth example is `minclass = 0`
					* Sets the minimum number of character classes.
						* digits, lowercase, uppercase and more.
							* If the value is set to `1` , can then have a password that is all digits, all uppercase, all lowercase or all other characters.
				* A fifth example is `maxrepeat = 0`
					* Sets the number of duplicate, adjacent characters.
				* A sixth example is `maxclassrepeat = 0`
					* Sets the number of duplicate, adjacent characters of the same class.
				* A seventh example is `gecoscheck = 0`
					* Checks for characters in the gecos field, that are also in the password.
				* An eight example is `dictcheck = 1`
					* Enables checking against a cracklib dictionary. For dictionary-based passwords.
				* A ninth example is `usercheck = 1`
					* Doesn't allow the user's name to be in their password.
				* The tenth and last example is `enforcing = 1`
					* Allows enforcing by pluggable authentication modules.