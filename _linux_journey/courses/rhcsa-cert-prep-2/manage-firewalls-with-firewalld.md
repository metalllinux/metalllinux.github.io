---
title: "Manage Firewalls With Firewalld"
category: "rhcsa-cert-prep-2"
tags: ["rhcsa-cert-prep-2", "manage", "firewalls", "firewalld"]
---

* In enterprise Linux, the firewall admin tool is usually `firewalld`
* `iptables` cannot run at the same time as `firewalld`
* To start `firewalld`, run `sudo systemctl start firewalld` and `sudo systemctl enable firewalld`
* `firewall-cmd` is the command we use to interact with `firewalld`.
* To verify the state of the `firewalld` settings, can use `sudo firewall-cmd --state`.
* If you're editing the firewall rules remotely, can use the `sudo firewall-cmd --timeout=60` rule.
	* Reverts the rules aback after a certain length of time.
		* Useful if the rules lock you out of the network for some reason.
* To make the rules persistent, use `sudo firewall-cmd --permanent`
	* Need to do this, incase the machine reboots.
* An example of adding a rule (a web service in this instance):
	* `sudo firewall-cmd --permanent --add-service=http`
		* Allows HTTP traffic from the outside to the default zone.
	* To remove a service, we use the same line and modify it slightly.
		*  `sudo firewall-cmd --permanent --remove-service=http`
*  To open a port and protocol:
	*  `sudo firewall-cmd --permanent --add-port=443/tcp`
*  Can also add a range of ports, for example allowing VNC connections in:
	*   `sudo firewall-cmd --permanent --add-port=5901-5910/tcp`
		*  After modifying the firewall, you need to reload the rules.
			*  `sudo firewall-cmd --reload`
*  To list the services we use by name, `sudo firewall-cmd --get-services` 
*  To list the services enabled in the current zone:
	*  `sudo firewall-cmd --list-services` 
*  To list the ports enabled in the current zone:
	*  `sudo firewall-cmd --list-ports` 