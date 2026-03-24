---
title: "Use The Proc And Sys Filesystems And Device File"
category: "advanced-linux-kernel"
tags: ["advanced-linux-kernel", "proc", "sys", "filesystems", "device"]
---

* Virtual Filesystems are filesystems where data is not stored on disk.
* `proc` and `sysfs` filesystems are virtual filesystems.
* Contents is dynamically generated when you check the files within the two above directories.
* Each file and directory entry has an associated function in the Kernel and that produces the contents on demand.
* Can check how much memory is being used by `cat`ing the appropriate file.
* `/proc` is mounted on the filesystem at boot time.
* The Docker engine mounts `/proc` into the container you are running.
	* Can create a container where `/proc` is not mounted and then commands such as `ps` do not work.
* `proc` gets its name from `process`.
* The `ps` command can then just check `proc` to get information about certain processes.
* `proc` contains other information about the Kernel aside from the processes.
* Good way to get snapshot up-to-date information about the Kernel.
* Some `proc` files can be written to. These are called `Kernel Tunable Variables`
* If you write to the file, it will be written to and the Kernel changeds the variable appropriately.
	* Does not save to disk and interacts with the Live Kernel.
	* The values are lost at reboot.
	* There is a config file in `/etc`, where you can place entries in there.
	* When the Kernel boots up, it will then have those files written to.
* For `proc`, each process has a directory named with its PID.
	* For example, the PID of the `ls` command. Once the command finishes, the directory will be gone.
* Directory for a PID has information about memory usage, the program itself, what files it has open and more.
* Threads have entries under the directory `task`.
	* Shows entries of all of the threads associated with a process.
	* On Linux, every process has at least 1 thread.
		* If a process calls `pthreadcreate` to get a Posix Thread and it will create an additional task.
		* If there is a Java program running Java threads, it will create additional tasks.
		* Inside the Kernel, `task` is used aside from `thread` or `process`
		* A process may have multiple `tasks` associated with it.
		* Can find information of all of them under the `proc` PID.
* `/sys`
	* This is mounted at boot.
	* `sysfs` is for "kernel object" info.
		* A Kernel object can be compiled code, that you load directly into the Kernel.
		* This is a data structure in the Kernel, that has information about hardware.
		* Kernel objects can be connected together, to show a relationship.
		* PCI device can be plugged into a PCI bus - including multiple other PCI devices. Therefore, there is a relationship between the bus and objects.
		* When you plug in new devices, new entries show up in the `/sys` filesystem.
		* The command `lspci`, can get information by looking inside the `/sys` filesystem.
* Device Files.
	* These are typcailly located under `/dev`. There are two kinds of Device Files:
		* Character and Block Device Drivers.
		* Device file is identified with a major number, minor number and also having a type of either `c or b`. We can see this with `ls -l`.
			* Type C is a character device file.
			* Type B is a block device file.
			* Traditionally, the major number is used to identify which device driver, is associated with a particular file.
				* When you open up that file, the Kernel then knew which device drivers to call.
				* The Kernel did not care about the number, only the device driver.
				* For example, if you have two serial ports, you can have two devices with the same major number and separate minor numbers.
					* If you open one device up, the serial port device driver is called for the device, the open function looks at which file you opened and then in particular the minor number and it could then work out which serial port it was talking to.
				* For block device files (where those files are used to mount filesystems)
					* Block files are used for mounting stuff.
						* The block device driver can then use the minor number, to understand which disk it is referring to and the partition as well.
						* The minor number can encode multiple kinds of information.
	* The Kernel maintains a relationship between the three characteristics and what driver to call.
		* As an example, a character driver can implement `open(), read(), write() and ioctl()`. These are `file operations`, as that is what the data structure is called.
			* These functions would be registered with the Kernel.
				* Then need a device file with the major number.
					* Nowadays, the drivers do not have a pre-assigned number and will request this from the Kernel. The driver will tell the Kernel how many major and minor numbers it needs and the Kernel will give them a block.
						* Two separate device drivers can get the same major number, but of course the minor numbers would be different. The combination of the major number and the minor number are what is needed to identify the driver.
	* A process opens a device file and then can read, write and so on with the file descriptor. The Kernel then arranges to have the driver's function called.
	* On Linux systems of today, device files are dynamically created. For example, the `/dev` might only be in RAM and not on the disk.
		* `/dev` is always populated.
		* One hardcoded place is `/dev/null`, as this always has the same major and minor numbers.
		* A daemon running will get that information and then create the device files.
	* An example of the process is `echo hi > /dev/null`
		* The process opens with the file `/dev/null`,  then we enter the Kernel and the Kernel checks what is being opened (see `/dev/null`) and sees that it is a character device file. The Kernel looks at the Major and Minor numbers. An object is then created, which records the number information. It then associates the driver's functions, with the major number for the device file. We then know what driver has been registered to which number and whom can use `/dev/null`.
* You can also have a device file, that does not have a number associated with it.
* Many years ago, the `/dev` directory had to be populated manually with the device drivers it required.
* Checking through `/proc`
	* Run `ps -l`  and you see na output similar to:
```
howard@explosion:~$ ps -l
F S   UID     PID    PPID  C PRI  NI ADDR SZ WCHAN  TTY          TIME CMD
0 S  1000    6395    6366  0  80   0 -  3083 do_wai pts/1    00:00:00 bash
4 R  1000    6403    6395  0  80   0 -  3430 -      pts/1    00:00:00 ps

```
* `PPID` means Parent Process ID. In this case, it is `6395`
	* Can go into that directory with `cd /proc/6395`. Then run `ls -l`
* Of note, you see a `cmdline` file to see how the command was invoked.
* `cwd` is a soft link and points to the directory that the process is in at the time.
* `exe` is a soft link and shows you what program that the process is running. For example:
```
lrwxrwxrwx  1 howard howard 0  3月 23 21:33 cwd -> /proc/10303
lrwxrwxrwx  1 howard howard 0  3月 23 21:33 exe -> /usr/bin/bash
```
* There is also the directory called `fd`.
	* In this directory, we see 4 file descriptors:
```
lrwx------ 1 howard howard 64  3月 23 21:37 0 -> /dev/pts/1
lrwx------ 1 howard howard 64  3月 23 21:37 1 -> /dev/pts/1
lrwx------ 1 howard howard 64  3月 23 21:37 2 -> /dev/pts/1
lrwx------ 1 howard howard 64  3月 23 21:37 255 -> /dev/pts/1
```
* By convention, filedescriptor 0 is called standardIn.
* Filedescriptor 1 is called standardout.
* Filedescriptor 3 is called standarderror.
* The `255` is what the Shell does.
* If you close everything that refers to a file, the file itself can also disappear.
* Regarding `/dev/pts/1`, this is the `tty`. We can verify this with the `tty` command and it is the direct path/device for your window.
* For any process, you can see what file descriptor it has open, by looking at its `fd` directory.
* Another useful file in `/proc` is `interrupts`.
	* It will show the output as `0` bytes in size:
```
-r--r--r-- 1 root root 0  3月 24 06:14 /proc/interrupts
```
* However this is not the case.
* The `interrupts` file has statistics about devices that have caused interrupts.
	* It is tracked by CPU core.
* Example interrupt is:
```
TRM:      90078      90077      90078      90077   Thermal event interrupts
```
* Shows the number of interrupts per processor.
* To look further into device files, we check `/dev`.
	* Example is:
```
howard@skwigelf:/dev$ ls -l | grep null
crw-rw-rw-  1 root   root      1,   3  3月 24 06:14 null
```
* The first character you see is `c` and this stands for `character device` file.
* Instead of a size, we see `1, 3`.
	* In this case, the major number is `1`. On this device, `1` is standard and this is a regular device driver.
		* The memory driver uses the `3` minor number, to act like `/dev/null`
		* If the minor number is a different number, then the driver can use that to act differently.
* For `/dev/null`, if you redirect any output to it, it is essentially gone.
* Another related device file is `/dev/zero`. It looks like:
```
howard@skwigelf:/dev$ ls -l /dev/zero
crw-rw-rw- 1 root root 1, 5  3月 24 06:14 /dev/zero
```
* Remember, if you had a device driver assigned with the same major and minor numbers, it would act like `/dev/null`. It can be ran anywhere and does not have to be in `/dev/null` - it could be in your home directory.
* It is a privilege operation to create a device file.
	* Device files are generally held onto by root.
* The behaviour with `/dev/zero`, is if you read from it, it never gives the end of the file.
* If you cat `/dev/zero`, it will never stop.