---
title: "Configure Secure Shell"
category: "rhcsa-cert-prep-2"
tags: ["rhcsa-cert-prep-2", "configure", "secure", "shell"]
---

* SSH (Secure Shell)
* Provides an Interactive Login Shell 
* Provide Non-interactive Remote Command Execution.
* Secure Network File Copy.
* Simple network tunnelling of traffic.
* Linux, MacOS and Unix all come with SSH Servers built-in.
	* Windows does not come with SSH.
* In Linux, the main configuration files are stored in `/etc/ssh`
	* The client has these stored in `/etc/ssh/ssh_config` 
	* The server has these stored in `/etc/ssh/sshd_config` (this is the main one, only really need to edit this one) and `/etc/sysconfig/sshd`
* SSH answers on port 22 by default, but can change this in the file.
	* Many other items in the file, such as ciphers, compression, access control and forwarding.
* Per user client configuration file.
	* `~/.ssh/config`
		* Helps for overwriting certain configuration items.
			* The `.ssh` directory does not exist, until you attempt to connect to a server for the first time.
		* Helps stores information about the remote service.
			* Example of a user's personal configuration:
![Screenshot_20230916_220232.png](../../_resources/Screenshot_20230916_220232.png)
* If a remote server uses port `1022` and a private-public key is generated for it, the above image configuration file would look like that.
	* If there was no configuration file, we would hae to type in the command like so: `ssh -p 1022 myuser@server1.vmguests.com -i ~/.ssh/server1.key`
		* `-i` is used for the identity of the file.
* WIth the above config file in place, all we need to do is type in `ssh server_name`
	* Makes management and access to multiple servers easier.
*  
