---
title: "List, Create And Delete Partitions On Mbr And Gpt"
category: "rhcsa-cert-prep-2"
tags: ["rhcsa-cert-prep-2", "list", "create", "delete", "partitions"]
---

* If adding a drive via the VM Manager GUI -->
	* Add Hardware
		* Storage
			* Can then change the disk settings there.
* Via the Terminal, can get a list of drives with:
	* `cat /proc/partitions`
		* Has an output similar to
howard@skwigelf:~$ cat /proc/partitions
major minor  #blocks  name

 259        0  500107608 nvme0n1
 259        1     524288 nvme0n1p1
 259        2     499712 nvme0n1p2
 259        3  499082240 nvme0n1p3
 254        0  499065856 dm-0
 254        1   24412160 dm-1
 254        2    9764864 dm-2
 254        3     999424 dm-3
 254        4    1949696 dm-4
 254        5  461889536 dm-5

* The information comes directly from the Kernel. This is what the Kernel currently recognises.
	* Another way to check is with `lsblk`.
* If you want to read the partition table directly:
	* Use `fdisk -l /dev/DRIVE`	
		* Shows the partition table from the drive itself.
* Legacy Systems store their boot information in the MBR or Master Boot Record.
	* Numerous systems use GUI.
* UEFI systems use the GPT partition table.
* fdisk is the legacy tol for BIOS-based systems.
	* `fdisk` has a limitation of 4 real partitions (primary partitions).
		* If you want more partitions, one of the partitions needs to be an extended partition.
			* Inside the extended partition, can then create logical partitions.
				* All Primary and Extended Partitions will be numbered 1 ~ 4. All Logical Partitions are numbered 5 and up.
		* GPT Support with `fdisk` is available, but experimental as of now.
* `gdisk` is designed for GPT partitions.
	* Can have an unlimited number of partitions.
	* It also stores a BIOS partition table as well.
	* Even non-UEFI systems can use the GPT table.
* `parted`
	* Allows the creation of partitions and even formatting. 
![Screenshot_20230920_213423.png](../../_resources/Screenshot_20230920_213423.png)
`sudo gdisk /dev/DRIVE`
![Screenshot_20230920_213618.png](../../_resources/Screenshot_20230920_213618.png)
* `n` for a new partition.
* `First sector` --> Press `enter`
* `Last sector` --> `+500M`
* Select enter for the default partition of `8300` Linux Partition.
* `p` to print the partition table.
* `w` to write to this.
	* To verify the Kernel sees the above changes, we use `cat /proc/partitions`
		* You will see the new partition in the list.
* To delete the partition, use `d`
* Always check with `cat /proc/partitions` to verify the partition has been added.
	* If the partition hasn't been detected, running the `partprobe` command or rebooting to force the Kernel to recognise the new partition, 

