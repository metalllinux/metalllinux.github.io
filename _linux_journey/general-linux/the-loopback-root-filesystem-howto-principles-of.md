---
title: "2. Principles of Loopback Devices and Ramdisks"
category: "general-linux"
tags: ["loopback", "root", "filesystem", "howto", "principles"]
---

[Next](https://tldp.org/HOWTO/archived/Loopback-Root-FS/Loopback-Root-FS-3.html) [Previous](https://tldp.org/HOWTO/archived/Loopback-Root-FS/Loopback-Root-FS-1.html) [Contents](https://tldp.org/HOWTO/archived/Loopback-Root-FS/Loopback-Root-FS.html#toc2)

* * *

## <a id="s2"></a>2\. Principles of Loopback Devices and Ramdisks

First I will describe some of the general principles that are used in the setting up of a loopback filesystem as the root device.

## <a id="ss2.1"></a>2.1 Loopback Devices

A **loopback device** in Linux is a virtual device that can be used like any other media device.

Examples of normal media devices are hard disk partitions like `/dev/hda1`, `/dev/hda2`, `/dev/sda1`, or entire disks like the floppy disk `/dev/fd0` etc. They are all devices that can be used to hold a files and directory structures. They can be formatted with the filesystem that is required (ext2fs, msdos, ntfs etc.) and then mounted.

The loopback filesystem associates a file on another filesystem as a complete device. This can then be formatted and mounted just like any of the other devices listed above. To do this the device called `/dev/loop0` or `/dev/loop1` etc is associated with the file and then this new virtual device is mounted.

## <a id="ss2.2"></a>2.2 Ramdisk Devices

In Linux it is also possible to have another type of virtual device mounted as a filesystem, this is the **ramdisk device**.

In this case the device does not refer to any physical hardware, but to a portion of memory that is set aside for the purpose. The memory that is allocated is never swapped out to disk, but remains in the disk cache.

A ramdisk can be created at any time by writing to the ramdisk device `/dev/ram0` or `/dev/ram1` etc. This can then be formatted and mounted in the same way that the loopback device is.

When a ramdisk is used to boot from (as is often done on Linux installation disks or rescue disks) then the disk image (the entire contents of the disk as a single file) can be stored on the boot floppy in a compressed form. This is automatically recognised by the kernel when it boots and is uncompressed into the ramdisk before it is mounted.

## <a id="ss2.3"></a>2.3 The Initial Ramdisk Device

The **initial ramdisk** device in Linux is another important mechanism that we need to be able to use a loopback device as a the root filesystem.

When the initial ramdisk is used the filesystem image is copied into memory and mounted so that the files on it can be accessed. A program on this ramdisk (called `/linuxrc`) is run and when it is finished a different device is mounted as the root filesystem. The old ramdisk is still present though and is mounted on the directory `/initrd` if present or available through the device `/dev/initrd`.

This is unusual behaviour since the normal boot sequence boots from the designated root partition and keeps on running. With the initial ramdisk option the root partition is allowed to change before the main boot sequence is started.

## <a id="ss2.4"></a>2.4 The Root Filesystem

The root filesystem is the device that is mounted first so that it appears as the directory called `/` after booting.

There are a number of complications about the root filesystem that are due to the fact that it contains all files. When booting the `rc` scripts are run, these are either the files in `/etc/rc.d` or `/etc/rc?.d` depending on the version of the `/etc/init` program.

When the system has booted it is not possible to unmount the root partition or change it since all programs will be using it to some extent. This is why the initial ramdisk is so useful because it can be used so that the final root partition is not the same as the one that is loaded at boot time.

## <a id="ss2.5"></a>2.5 The Linux Boot Sequence

To show how the initial ramdisk operates in the boot sequence, the order of events is listed below.

1.  The kernel is loaded into memory, this is performed by `LILO` or `LOADLIN`. You can see the `Loading...` message as this happens.
2.  The ramdisk image is loaded into memory, again this is performed by `LILO` or `LOADLIN.` You can see the `Loading...` message again as this happens.
3.  The kernel is initialised, including parsing the command line options and setting of the ramdisk as the root device.
4.  The program `/linuxrc` is run on the initial ramdisk.
5.  The root device is changed to that specified in the kernel parameter.
6.  The init program `/etc/init` is run which will perform the user configurable boot sequence.

This is just a simplified version of what happens, but is sufficient to explain how the kernel starts up and where the initial ramdisk is used.

* * *

[Next](https://tldp.org/HOWTO/archived/Loopback-Root-FS/Loopback-Root-FS-3.html) [Previous](https://tldp.org/HOWTO/archived/Loopback-Root-FS/Loopback-Root-FS-1.html) [Contents](https://tldp.org/HOWTO/archived/Loopback-Root-FS/Loopback-Root-FS.html#toc2)