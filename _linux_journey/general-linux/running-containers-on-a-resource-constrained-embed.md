---
title: "Running Containers On A Resource Constrained Embed"
category: "general-linux"
tags: ["running", "containers", "resource", "constrained", "embed"]
---

* Digi Accelerated Linux
* Why Use a Resource Constrained Device?
	* Read-only root filesystem.
		* User is unable ot modify the OS.
	* Inexpensive.
	* Optimised for the task at hand.
* What is a container?
	* Runs binaries in a protected space.
	* Run as unprivileged user to protect the host.
	* Give access to hardware, peripherals.
	* Runs under current host kernel.
		* Many years ago `chroot` and `cgroups` were used.
* Why run containers on a resource constrained device?
	* Extensibility
		* Add new functionality not included in the firmware image.
			* Python
			* Perl
			* Java
	* Ability to run your own applications.
		* Firmware updated for connected devices.
		* Communications
* Light processing on the network boundary possible.
* Removing the need for another device.
* What resources are required?
	* Storage
		* Utilities - starting / stopping the container.
		* Managing the container.
	* Libraries
		* Required by the utilities
	* Container filesystem
* RAM
* CPU
* Advantages for running Docker.
	* Use a layered filesystem
* Disadvantages
	* Sise 275MB usage.
	* Too many libraries.
* Advantages for LXC
	* Advantages 
		* Small 85MB on a PC.
		* High configurable
		* Performance
		* Fewer dependencies
	* Disadvantages
		* Most LXC containers are OS images.
* LXC
* There is a difference between `start` and `execute`. `start` will start the system and `execute` will run the applications.
* LXC traditionally runs OS images.
* Can use the host system.
* LXC can mount host directories.
* The container can appear just like the host.
* User processes are run inside the container.
* Persistent vs Volatile
	* Volatile containers run entirely in RAM.
	* Everytime container starts, it will be clean.
	* Limits writes to flash.
* Persistent containers run from flash.
* What about the linker?
	* Host vs. User Linker
* Can use the linker to show dependencies, just like ldd
* Set `LD_LIBRARY_PATH` to use different libraries to the host.