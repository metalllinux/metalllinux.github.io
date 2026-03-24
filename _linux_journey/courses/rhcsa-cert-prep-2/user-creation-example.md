---
title: "User Creation Example"
category: "rhcsa-cert-prep-2"
tags: ["rhcsa-cert-prep-2", "user", "creation", "example"]
---

* `sudo useradd -u 1100 -s /bin/ksh -G wheel steve`
	* Creates the username `steve`, with user and group IDs of `1100`
	* Gives the `Korn Shell`
* `sudo useradd sue`
* `sudo useradd taylor`
* `sudo groupadd developers`
* `sudo gpasswd -M sue,taylor,steve developers`
	* Managing users from a group perspective is faster.
* `sudo passwd developers`
	* Give the `developers` group a password.
	* Others users not in the group will have to enter a password.
* `sudo chage -E 90 -W 5 steve`
	* Set the password to change every 90 days, with a 5 day warning.
	* If don't set the warning period, will default to 7 days.