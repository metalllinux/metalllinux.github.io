---
title: "Kernel Modules"
category: "lpic-2"
tags: ["lpic-2", "kernel", "modules"]
---

* If you're not seeing hardware show up, then implement the modules.
* Linux Kernel is Monolithic - in RAM it has everything there.
* `Dynamic Kernel Modules` can load in modules as required. This is powered by DKMS (Dynamic Kernel Module System).
	* If it hits hardware, then great and it keeps the module. If it does not hit hardware, it then unloads the unnused module.
		* Allows the system to have as much free RAM as possible to play with.
* Distros take the Kernel, GNU Utils, X/Wayland and to add various modules and hardware support.
	* Some distros only include Open Source drivers.
	* Proprietary wireless drivers such as Intel can be taken by some distros and still loaded.
* Useful command is `lsmod`
	* List modules that are loaded on the system.
		* IT WILL NOT LIST THE ONES THAT ARE NOT LOADED.
	* It will output the `name` of the module, the `Size` of the module and what other modules are depending on it (specified by the `Used by` column).
	* For example `rfcomm` stands for Radio Frequency Communications and is likely the WiFi driver, bluetooth etc. 
* Next command is `modinfo`and we can get more information by runnng `modinfo <module name>`
* All of the modules are running in Kernel Space.
* For example with `modinfo zstd_compress`, you can see exactly where the file is stored:
```
filename:       /lib/modules/5.15.0-91-generic/kernel/lib/zstd/zstd_compress.ko
```
* Kernel modules have an extension of `.ko`
* We can check further in `/lib/modules` if we want to change the files or replace them. These would go into `/lib/modules`
* During boot and hardware discovery, if the hardware is there it loads it and if it is not there, it unloads it.
* When you compile a Kernel, you can place modules into the Kernel and say `There are going to run`.
	* You can speed up your boot time and hardware detection by doing that.
* Whenever hardware changes on your system, we can see this in `dmesg`. For example if you have bluetooth, in `dmesg` you see `Registered procol family <number>` and `HCI device and connection manager initiallized`. That would also load `usbcore`, for if it is a USB bluetooth adapter. `btusb`is the interface driver.
	* When hardware is added, it looks for the appropriate module at the time.
* We can temporarily load a module.
	* Ideally should check vendor documentation on which module is required.
* To install a module, we run the command `sudo insmod <module_file>`
	* An example is deploying a system to AWS, where they have ENA (Elastic Network Adapters). 
	* Example: `sudo insmod /lib/modules/5.15.0-91-generic/kernel/drivers/net/ethernet/amazon/ena/ena.ko`
		* Then check with `lsmond | grep <name>` 
			* Was it assigned a device name by `udev` (this runs in the background).
* Can then remove the `mod` with `sudo rmmod <module_name>`
* For `lsmod`, `insmod` and `rmmod`, there is a command that replaces all of those called `modprobe`.
	* `sudo modprobe -a <module_name>` (the `-a` is to add a module).
	* To remove the module, we do `sudo modprobe -r <module_name>`
* The module name rarely matches the device name.
* Worth checking if the module has loaded in `dmesg` and grepping the output.
* If you know what type of hardware you are looking for, you can check the bus it is on.
	* `lsusb` for the USB bus.
	* `lspci` for the PCI card.
		* If you see an `unknown` device, the device is missing a module.
			* Virtual devices are also tricky to spot.
* We also have `lsdev`, which lists all of the devices. Good way to check that the module did its job and the device is online.
	* Need to install `procinfo` if there is no output from the above.
* Ethernet adapter used to be called `eth0`, but then they renamed it based on the bus. --> `ens`. So you see an adapter called `enp0s10`, which is Ethernet, Bus Number and Slot Number.
* MAC --> Media Access Control
* Can overwrite the names provided to devices.
	* Using the device's identifier, you can create a `udev rule` based on that and specify what the name is. 
	* An example of a `udev rule` is in `/etc/udev`, you will see a `udev.conf` file. However, we want the directory called `rules.d`, where we can create our own rules. `hwdb.d` is the hardware database directory.
	* Recommended to not modify in `hwbd.d`. If there are any updates, that is then overwritten.
	* We can create a new rule in `rules.d`, we can use `sudoedit`
		* With network adapters, the vendor may have a preferred name. The files are run in order, based on their filename.
			* For example `sudoedit 70-persistent-ipoib.rules`. The prior is the Ubuntu naming scheme.
				* Inside the above file, we can specify the rules to overwrite the behaviour:
```
# This is the network subsystem that is being overwritten
# ACTION is when new hardware is being added to the system
# DRIVERS is where we specify the particular driver if we were keying off that. ?* allows us to not care what the driver is and so any network driver is loaded
# ATTR is the attribute used to identify the card. type is 1, because we only have 1 MAC Address on the adapter
# Kernel is the name it is assigned by default
SUBSYSTEM=="net", ACTION=="add", DRIVERS=="?*", ATTR{address}=="MAC_ADDRESS", ATTR{type}=="1", KERNEL=="ens666", NAME=="eth0"
```
* Now when the Kernel sees the above adapter, it will be called `ens666`by the Kernel itself, but known as `eth0` to the users.
* The above change will not take effect until a reboot is called.
	* To force it to be loaded with a reboot, we can do `sudo udevadm control --reload-rules && udevadm trigger`
	* `udevadm` is `udev admin`