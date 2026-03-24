---
title: "Discover And Control Hardware"
category: "advanced-linux-kernel"
tags: ["advanced-linux-kernel", "discover", "control", "hardware"]
---

* Software Layers to and from Hardware.
* Applications call functions in libraries.
* Some functions invoke Kernel System Calls.
![Screenshot_20240317_093409.png](../../_resources/Screenshot_20240317_093409.png)
* Some system calls interact with hardware.
* Can find out information about HW on the system with `lshw` and `lspci`.
* `lsub` and `lsbk`
* `lscpu` and `lsdev`
* Can do disk benchmarking with `hdparm`.
* Can configure the hardware in software with Write (`echo`) to `proc`, `dev`or `sys` files.
* Legacy devices such as keyboards are on a different bus. I/O bus.
	* Can read and write bytes to the buses. Those are `inb` and `outb`
	* Disable the keyboard by writing a value with the `outb` command for example.
	* Can read in items with the `inb` command (serial devices)
* Can configure and change information with the `setpci` command.
* Interestingly if you run `lsusb`, all Intel device start with `8087` in their ID.
```
Bus 002 Device 002: ID 8087:8000 Intel Corp. Integrated Rate Matching Hub
```
* PCI devices, they have `8086` for Intel devices.
* A lot of companies will use the same underlying chip in their mouse and keyboards for example.
* `lscpu`, you a field called `BogoMIPS`. This isn't real MIPS and is for Bogus MIPS.
	* When the Kernel boot, it has a loop and measures performance. Use the `BogoMIPS` to calculate how long it takes to run certain tasks.