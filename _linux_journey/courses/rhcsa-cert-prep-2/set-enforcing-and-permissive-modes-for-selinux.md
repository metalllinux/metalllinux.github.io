---
title: "Set Enforcing And Permissive Modes For Selinux"
category: "rhcsa-cert-prep-2"
tags: ["rhcsa-cert-prep-2", "enforcing", "permissive", "modes", "selinux"]
---

* Terms required firstly:
	* Discretionary Access Control
		* Means of restricting access to objects, based on identity of subjects and of groups to which they belong.
		* The access control is discretionary - subject with certain permissions can pass them on to other subjects. 
		* File permissions, access control lists, SUID, SGID, su/sudo privileges are discretionary.
	* Mandatory Access Control
		* Additional security layer over discretionary access control, limiting what can be done.
		*  The operating system constrains the ability of a subject to access an object.
* SELinux Terms
	*  Subject
		*  A user or process that accesses an object.
	*  Object
		*  A resource such as a file, directory, IO devices or pipe.
	*  Access
		*  An action performed by a subject on an object: read, write, delete and create.
	*  An example of a Subject accessing an Object:
		*  `vim temp.txt`
			*  Accessing, saving etc would incur Read, Write operations.
	*  Rule
		*  Allows or denies a subject to access an object.
	*  Security Policy
		*  System-wide set of rules defining which Subjects can access which Objects.
	*  Security Context/Label
		*  File metadata used to store SELinux attributes for Subjects and Objects
			*  All subjects and objects have a security context.
				*  The context is stored in the `Extended Attributes` section of the file's metadata.
*  An Example of SELinux Access Decision
	*  `vim` requests accses to an Object -> `file.txt`
		*  `vim` --> `SELinux Security Server` --> Queries the `SELinux Policy Database` (contains all of the rules). 
![Snapshot_2023-09-02_21-55-03.png](../../_resources/Snapshot_2023-09-02_21-55-03.png)
		* If permission is not granted, then it is denied from accessing:
![Snapshot_2023-09-02_21-58-27.png](../../_resources/Snapshot_2023-09-02_21-58-27.png)
			* This message is added to the  Access Vector Cache.
				* You can see the messages in the Operating System's log files.
* SELinux Operating Modes
	*  Enforcing
		* Security Policy is being enforced.
	*  Permissive
		* Policy is consulted and messages of policy violation are printed. Policy is not enforced.
			* Good for troubleshootig SELinux policy issues.
	* Disabled
		* SELinux is turned off and no mandatory access control is used.
* SELinux Enforcement Policies
	* Type Enforcement
		* Access Control based on Subject and Object types stored in a security context (tagged with a type) - used in the default targeted policy.
			* The rules determine what types can act on other types.
			* 
	* RBAC (Role-based Access Control)
		* Access Control based on users in roles.
	* Multi-level Security (MLS)/Multi-category Security (MCS)
		* Assigns a security level to different subjects and objects.
			* Access control based on security levels or categories of objects.
	* MCS is useful for containerisation of processes.
		* Makes policy decisions, based on the category.
* To get the current SELinux Mode, type `sestatus`
	* Can check what mode SELinux is in with `getenforce`
* To change the mode, you can use `sudo setenforce permissive`
	* This is only temporary and does not survive a reboot.
		* If want to make it permanent: edit `/etc/selinux/config` file.
			* In the file, set the `SELINUX=enforcing` to `permissive`. Need to reboot the system afterwards.

