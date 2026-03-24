---
title: "Understand System Maintenance Mechanics"
category: "advanced-linux-kernel"
tags: ["advanced-linux-kernel", "understand", "system", "maintenance", "mechanics"]
---

* System calls are functions implemented by the Kernel, but are meant to be called in user space.
* Kernel 5.3 for example has 340 system calls.
* When have the Linux Kernel source code, can look at the `include/uapi/asm-generic/unistd.h` file to see all of the system calls.
* `asm` is Assembly Langauge.
* System calls vary between architecture, x86-64 and ARM changes.
* Functions users can call are in the `man` pages.
* For example, if you look up `read` in the manual, it is called through the standard library (libc)
* Standard library uses architecture-dependent means to invoke the system call mechanism.
* Protocol and Library which tells the Kernel which system call to make.
* Suitable sised parameters are placed into registers.
* Kernel is invoked via the library, determines the system call and then calls it.
* If there is an error, the system call returns a negative value (function in the Kernel) to the library.
* If that value is negative, the library is going to set a global variable in the process address space. This error is called `errorno` to `abs` (absolute value or return value) and returns -1 back to the program. The error number provided has information on what the error is.
* The library is what sets `errorno`.
	* When there is `no` error, the library does not set `errorno` and returns the value it obtained from the Kernel.
* Useful shell shortcut -->
	* `grep -i read !$`
		* The `!$` means it will read the last thing on the previous line.
* If you download the Kernel source code, go to `/usr/src/line-(number)/include/uapi/asm-generic`. An example link is:
```
howard@skwigelf:/usr/src/linux-headers-5.15.0-100-generic/include/uapi/asm-generic
```
* To get an estimate of the number of system calls, we can do the following in the above directory: 
	* `grep "define __NR" unistd.d`
* Don't confuse user-space header file adnd Kernel space header files.
* Can check the `man` page for `read` for further information.
* System Call `man` pages have sections in the top-right hand corner, for example `KILL(1)` says we are in the first section of the `kill` command's `man` page.
* `kill -9` will `kill` a process.
* To go to another section in a `man` page, we perform `man 2 kill` for example.
* RETURN VALUE is always listed in each library.