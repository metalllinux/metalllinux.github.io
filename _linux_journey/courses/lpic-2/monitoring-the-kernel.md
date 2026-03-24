---
title: "Monitoring The Kernel"
category: "lpic-2"
tags: ["lpic-2", "monitoring", "kernel"]
---

* What modules is the Kernel using (this we can monitor and look at).
* Whether hardware has been detected.
	* The Kernel cannot read the hardware properly.
* Performance is under control of the Kernel as well.
* Another Operating System called `Plan 9`, originally from AT&T's Bell Labs
	* Wanted to represent everything as a `file`. memory, network communications etc as files.
* Checking `/dev`, all of the files there are representations of the hardware.
* The Kernel represents a lot of what it is doing as files as well.
	* We can check this in `/proc`
	* If we back up to `root`, we can see that some are symlinks (points to other directories).
	* If you check the permissions for `proc`, these look a little strange:
```
dr-xr-xr-x 337 root root     0 Jan 24 08:52 proc
```
* The `337` above represents the amount of links to that directory.
	* Only `root` has read and execute and no one has write permissions.
	* `proc` is a pseudo directory and not a main directory.
		* Representing the activity of the Kernel.
	* All of the files inside `/proc` contain data on what the Kernel is currently doing.
	* To find out the version of the Kernel we are running, we go into `/proc` --> `/proc/sys/kernel`
		* In that directory, you will find a file called `version`
		* If you then `cat version`, you then receive an output like this:
```
howard@explosion:~$ cat /proc/sys/kernel/version
#101-Ubuntu SMP Tue Nov 14 13:30:08 UTC 2023
```
* When running `cat` and receiving the output of the above, we interacted with the Linux API.
* When you run a program, you are not actually running it - you are asking the Kernel to run it for you.
	* For example editing a file with `vim`
	* While `vim` is open, we find the `vim` process with `ps aux | grep vim` You wil see the process ID outputted.
		* Back in the `/proc` directory, you can see all of the running processes, we can `cd` into the process ID directory and see exactly what `vim` is doing.
			* If you then run `ls -l` inside the process directory and then `grep` for `cwd` (current working directory), it symlinks back to the `user's` home directory (where hte command is being ran from).
			* The symlink `exe` also shows the binary that was ran, for example `exe -> /usr/bin/vim.basic`
			* We can also check the file `cmdline`, which shows the exact file that was ran: `vim file1.txt`
			* We can view all of the environmental variables that the application is relying on as well.
				* We do this with `cat environ` and it shows all of the variables that are in use.
* We can also shorten the commands we are running, for example `cat /proc/sys/kernel/version` can output the same as if we had done `uname -v`
	* `uname -v` says "give me the Unix Kernel Name and Version". As an example:
```
#101-Ubuntu SMP Tue Nov 14 13:30:08 UTC 2023
```
* The #101 is a tile.
	* Again, using `cat` doesn't access the file directly and it goes via the Linux API to talk to the Kernel.
* We can also do `uname -a` and it will collect information from multiple places and represent it back to us.
* We can then do `cat /proc/uptime`
	* Shows the time in minutes and seconds.
	* `uptime` command presents the exact same information, but in a human readable format.
* To the see the modules that have been loaded, we can do `cat /proc/modules`
	* Of course `lsmod` does the exact same thing and is formatted much more nicely.
* However, the `/proc` directory is useful, if you do not have commands avialable such as `lsmod` on a particular system.
* It is possible to write to several locations within `/proc`, it is not all `read-only`. It is possible to change the Kernel's behaviour.
	* Can implement changes from `/proc/sys/kernel`
	* Some scenarios where this has to happen. 
		* Google has an outage in their GCP. Took 3.5 hours to come back online. Google was re-provisioning some servers. During the re-provisioning, they had a shared caching database. When the servers tried to connect to each other, they exceeded the maximum amount of open connections that the Linux Kernel allows by default. The Kernel has limits that are put in place. The engineers needed to increase the limit within the Linux Kernel.
			* An example is the maximum amount of open files. This would be `/proc/sys/fs` for file system.
				* Inside, you will see `file-max`, which is the maximum amount of files you can have open.
				* `file-nr` is the amount of files that I currently have open. For example we have `howard@explosion:~$ cat /proc/sys/fs/file-nr
12448	0	9223372036854775807` and so `12448` are currently open.
				* If we want to change `file-max`, we can just open that as a text file and then save it. If you make a typo, that can cause a lot of issues.
					* The utility used instead is `sysctl` or System Control.
					`sysctl` is designed to interact with the Kernel and set values accordingly.
						* We then do `sudo sysctl fs.file-max` We want to set the filesystem's maximum files. This will return a value in the style of `fs.file-max = 1000000`
						* We can then write with `sudo sysctl -w fs.file-max=2000000`
							* If you reboot however, this doesn't persist and it goes away.
								* If you want the changes to persist, you have to store them in the filesystem.
									* In older Linux distros, you can change `/etc/sysctl.conf`, make the changes to the Kernel there and they then persist. There is a file afterwards called `sysctl.d`. Example of `sysctl.d` for Linux Mint:
```
howard@explosion:/etc/sysctl.d$ ls
10-console-messages.conf  10-ipv6-privacy.conf  10-kernel-hardening.conf  10-magic-sysrq.conf  10-network-security.conf  10-ptrace.conf  10-zeropage.conf  99-sysctl.conf  README.sysctl
```
* Each of the above changes are numbered at the start and are applied in order from lowest to highest.
* To add your own, you do `sudoedit 00-custom-settings.conf`. Example contents would be:
```
fs.file-max=2000000
```
* Would need to reboot the machine to take effect.
	* To process any changes WITHOUT a reboot, we do `sudo sysctl -p` to process any changes.