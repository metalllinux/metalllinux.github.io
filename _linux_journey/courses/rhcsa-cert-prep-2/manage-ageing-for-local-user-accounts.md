---
title: "Manage Ageing For Local User Accounts"
category: "rhcsa-cert-prep-2"
tags: ["rhcsa-cert-prep-2", "manage", "ageing", "local", "user"]
---

* Ageing in `/etc/login.defs`
	* Can determine when passwords need to be changed or when accounts should be automatically locked.
		* Can change these settings, in the global user account settings under `/etc/login.defs`
			* Example settings are:
				* `PASS_MAX_DAYS 99999`
				* `PASS_MIN_DAYS 0`
				* `PASS_MIN_LEN 5`
				* `PASS_WARN_AGE 7`
			* Any changes made will only affect newly created users.
				* If need to change existing user accounts, have to use other commands.
			* Can manually edit the `/etc/shadow` file, but it is easy to make a mistake in the columns.
		* The main command for changing user account settings is `chage` --> `chage [option] <username>`
			* Used to change the password and account ageing information for users.
				* Last day account is active --> `-d <days since 1970 or date>`
					* Settings this to `0` means a password has not changed and forces a password change on next login.
				* Expire date --> `-E <date>`
				* Inactive days --> `-I <days>`
					* Sets the number of days of inactivity, after the password expiration, before the account is locked.
				* Minimum days until change --> `-m <days>`
					* Minimum number of days between password changes.
						* If you set this to `0`, users can change their password at any time.
				* Maximum days valid --> `-M <days>`
					* Max number of days a password is valid for.
						* If the maximum number of days PLUS the `Last day account is active` (as shown above) are less than the current day, then the user has to change their password.
							* If want to give the user a warning before the password change date comes up, then use the `-W` option.
				* Warn days --> `-W <days>`
						* Number of days of warning in advance, before a password change is required.
				* List account ageing information --> `-l`
		* Grab the user account name with `sudo cat /etc/passwd`
			* Find ageing for a user:
				* `sudo chage -l test`
					* Shows all of the ageing information for that account.
		* If want to force a user to change their password at next login:
			* Can use the `passwd` command to forcefully expire their password.
				* Another way to do this is to use the `chage` command.
					* Changes ageing information for the user.
				* `sudo change -d 0 test`
					* Changes the day that the password was set to zero.
						* This forces the user to change their password on next login.
				* To switch to an account, we use `su - ACCOUNT_NAME`
							* If you do that after running the above `chage` command, you'll be prompted to change your password.
								* Then login with the previous user again with `Password expires` , `Account expires` and `Last password change` and you'll see the field set to `never` (aside from `Last password change`, which would be the current date).
									* The user will still be able to login via SSH keys however.
										* If the account expires, then this also is not possible.
				* To change the account expiration:
					* `sudo chage -E 2025-01-01 test`
						* `sudo chage -l test`
							* Then sets the `Account expires`
								* Can set to `90` days using the `-M` option.
									* `sudo chage -M 90 test`
				* Can also configure the account to automatically lock, if the password expires.
					* `sudo chage -I 10 test`
						* Changes the `Password inactive` field.
							* `sudo chage -I -l -m 0 -M 99999 -E -1 test`
								* `-I -1` will set the `Password inactive` to `never`.
									* `-m 0` , sets the minimum number of days between password changes to `0`
										* Allows the user to change their password at any time.
											* `-M 99999`, sets the maximum number of days between password changes. This is 274 years.
												* `-E -1` sets the account to never expire.