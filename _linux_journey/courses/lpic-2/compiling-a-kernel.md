---
title: "Compiling A Kernel"
category: "lpic-2"
tags: ["lpic-2", "compiling", "kernel"]
---

* Reasons to compile a Kernel:
1. Special Hardware - they want the Kernel module to be loaded before the Kernel is booted.
	1. They want this to be part of the InitRD (RAM Disk that is created during initialisation).
2. Might want to exclude modules, because you don't want them to be loaded. No need to compile a Kernel for this however, as you can blacklist udev rules and use `grub` extensions.
3. Security Review - may need to do code review.
	1. Can run automated scanners on the code and then compile from there.
4. Hardware Optimisation - special CPU for large corporation, want the Kernel to be optimised for that hardware.
* Reason not to compile a Kernel:
	* Every update that is released for the Kernel (which is at least monthly) will break it.
	* Need full-time employee to manage that Kernel.
* If we want to build our own, we have the following pre-requisites.
	* How to enable these in an Ubuntu-based system.
		* `sudoedit /etc/apt/sources.list`
			* Shows various `apt` sources where packages are taken from.
		* You will see the `main restricted` repository, which has protected binaries and packages.
		* There will be a commented line called `deb-src http://us.archive.ubuntu.com/ubuntu focal main restricted`, which we need to uncomment. We uncomment this line.
		* After that we run `sudo apt update`
			* Now we can find the source code, in additional to the binary files.
* There are crucial differences between `apt` / `apt-get`. Unfortunately the development packages are not interchangeable.
	* Many of the bundle names only work with `apt-get` and don't work in `apt`
		* The packages we need are:
			* `sudo apt-get build-dep linux linux-image-$(uname -r)`
				* `build-dep` are the build dependencies
					* When we build a binary, there will be dependencies that are attached to it.
				* `linux`
					* Allows for Linux development.
				* `linux-image-$(uname -r)`
					* This is the Linux image that we want.
					* `uname -r` provides the current version of Kernel.
					* Pulls down a binary image of the current kernel that is digitally signed.
					* Official Kernel and Linux package.
			* If you run the command, it will bring down a lot of libarries.
		* Will require the GNU C Compiler `gcc`
		* Will require `bc` - Maths computational program.
			* Required for Floating Point Calculations (required for compiling).
		* Will require `biso` and `flex` (text parsers).
			* Look through the source code and build he proper files, needed for the compiler to run.
		* Will require `grub` version 2 and its utilities.
			* To build the Init RAM Disk.
		* Will require `libssl-dev`
			* For anything that needs encryption (Kernel makes heavy use of this).
		* Will require `fakeroot`
			* Builds a fake root file system. It DOES NOT make a fake root user.
			* When building a Kernel for different file systems, therefore need to build a fakeroot file system to buld the Kernel correctly.
	* Also require the following `sudo apt-get install build-essential libncurses`
		* Group of utilities for doing builds.
* * `sudo apt-get install build-essential libncurses5-dev gcc libssl-dev grub2 bc bison flex libelf-dev fakeroot`
* `libncurses5-dev`
	* If you want to do text-based menus, load this module.
* `libelf-dev`
	* Linux binaries are stored in the `elf` format. Need `libelf` to be able to successfully execute and build the binaries.
* Ubuntu has to make the source code available as part of the GPL.
	* That's why there is the option in the `sources.list` file to enable sources.
* We can either get the source code from the distro or kernel.org
* To get it from the distro, we can do `sudo apt-get source linux-image-unsigned-$(uname -r)`
	* We want the unsigned pakage, because if we modify it, it cannot be signed.
* If you pull the source code from the distro, you receive the newest package supported by them.
* To download from `kernel.org`, we can do `wget http://cdn.kernel.org/pub/linux/kernel/v5.x/linux-5.9.16.tar.xz` (kernel.org has the file in multiple compression formats).
	* Then do `tar -xvf linux-5.9.16.tar.xz`
* Most of the Kernel is written in `c`. You can modify the `.c` and `.h` files.
* There is a configuration systems that allows us to make changes to the Kernel.
	* If we want to base the configuration of four current OS, we can do that.
	* This will be stored in `/boot`
	* Inside that directory, you'll find `config-5.15.0-91-generic` or a similar kernel.
	* That is the configuration file.
		* Looking inside the configuration file, show multiple options and modifies how the Kernel behaves.
	* The options are baked in at compile time and they can also be overwritten.
	* We can bring those over into the Linux Kernel code, so that those options become baked in.
	* We can copy the `config-5.15.0-91-generic` file directly into the source code directory.
		* We copy the above file into the source directory as `.config`
* To modify the Kernel, there is a GUI option available.
	* `cd` into the directory where your source file are.
	* Then run `make defconfig` (CLI version)
		* This makes a default configuration file and writes it to `.config`
	* We can also run `make xconfig` to run a GUI version and select what kernel changes you want to perform.
	* We can also do `make menuconfig`
		* Needs `libncurses` to run. This is the text-based menu option.
		* Once ran, it goes through and reads the source code. 
		* This provides a text-based menu. 
			* In `Security options`, we can load `CA`s
			* `Device Drivers` and have them baked in as the system boots.
			* `Networking support` for IPV6 can be turned off. 
		* If the menu option has a `*`, that means it is built-in.
		* `M` is for module. It will be loaded, but if you don't have the right hardware, it will be unloaded.
			* By turning it off and not have it modularised, we are disabling support of it.
		* Once done, click `Save` and it will build the configuration as `.config`.
* Once we have the `.config` file, how can we build the Kernel to use it.
	* In the source directory, we can just run `make -j2 deb-pkg`
		* `-j` informs the compiler how many cores of your processor it can use.
			* Takes around 1 ~ 2 hours of compile time.
	* If you just run `make -j2`, it will build your new `vm-linux` or `vm-linuz` file. THIS IS THE PRIMARY COMMAND TO BUILD A KERNEL.
	* However with `make -j2 deb-pkg` it will build `install packages`.
		* You can use these to update the InitRD
		* It also updates the `vm-linux` or `vm-linuz` file.
* Once compilation is complete, you can copy the `vm-linux`/`vm-linuz` file over to your `/boot` directory and `grub` will boot from it.
		* You can symlink it as well.
		* If you select the `deb-pkg` option, you can install the packages with `apt`.
* If you have multiple of the same machine, you can just compile the source code once and distribute evenly.
	* Variations in hardware would require separate Kernels for each.
* Other files that also need to be updated aside from the Kernel.
	* InitRD
		* This contains modules that also need to be updated.
		* Modules may need to be updated in general.
* `dkms` utility. 
	* You can build Kernel modules with this.
	* `dkms build -m ena -V 1.1`
		* `ena` --> Elastic Network Adapter.
		* `-V` is version number.
	* This would build the module and compile it.
* To install the module, we then run `dkms install -m ena -V 1.1`
* 28 million lines of code are included in the `Kernel`.