---
title: "Mount File Systems Ats Boot By Id Or Label"
category: "rhcsa-cert-prep-2"
tags: ["rhcsa-cert-prep-2", "mount", "file", "systems", "ats"]
---

* Works well to mount logical volumes by path, since the mount always stays the same.
	* For regular partitions however, this may not always be the case.
		* The path of the disk depends on when and where the OS sees the drive.
			* For example, 4 USB drives are plugged in, they are assigned a certain order when the host boots up.
				* In this case the first one is `Drive 1 /dev/sda`, `Drive 2 /dev/sdb`, `Drive 3 /dev/sdc`, `Drive 4 /dev/sdd` and so on.
					* However, if you unplug Drive 2, the old `/dev/sdc` becomes `/sdb` and the old `/sdd` becomes `/sdc`.
						* If the drive path changes and `/etc/fstab` has a line to mount the drive, it freezes the boot process.
							* It is better to mount the drives based on a label, for example `LABEL=backup` OR `UUID=<insert UUID>` and then the mount point on the machine.
* Example of mounting a drive based on UUID or Labels:
	* Create two additional partitions on the logical drive `/dev/vdb`
		* `sudo gdisk /dev/vdb`
			* `n` for new partition, default settings. `First sector` is default and `Last sector` is `+250M`. Select the default partition type.
				* Do the same as the above for the other partition.
* `p` to print the partition table.
	* The Kernel will still use the old partition table, can verify with `cat /proc/partitions`
		* If the new partitions are not listed, can run `sudo partprobe` to make the Kernel aware of the new partitions.
			* If that still doesn't fix it, then reboot.
				* Sometimes the drive can become locked and the Kernel cannot update the live partition table.
					* Usually, this is due to a drive being mounted.
						* In that case, unmount the drive and run `partprobe` again.
* Next, format the partitions as `ext4` with `sudo mkfs -t ext4 /dev/vdb2` , same for `sudo mkfs -t ext4 /dev/vdb3` as well.
	* Then check with `sudo blkid`, see both partitions are formatted as `ext4`.
		* Then create the mount point with `sudo mkdir /media/vdb2` and do the same for `vdb3`. 
		* One partition will be mounted by UUID. The other partition will be mounted by a label. 
			* Can find the UUID for the drive via `sudo blkid`.
				* Then edit `/etc/fstab` and add `UUID=ID_HERE /media/vdb2 ext4 defaults 0 0`
					* `0 0` is dump and restore.
					* The other partition we can set a label on the file system and mount it by label.
						* File System label are file system specific.
							* These are file system specific as well.
								* Since we are using ext4, we can set the file system label with the `e2label` command.
									* If it was formatted with `xfs`, we would use the `xfs_admin` command.
								* `sudo e2label /dev/vdb3 backups`
									* Can then verify the label it is given afterwards with `sudo e2label /dev/vdb3`
										* It will then say `backups`
* If you want more information about the filesystem, use `sudo tune2fs -l /dev/vdb3` , the scroll up and you will see the `Filesystem volume name` as `backups`
	* Once the label is set, edit `fstab` again.
		* Then add `LABEL=backups /media/vdb3 ext4 defaults 0 0`
		* To verify the lines in `fstab` work do `sudo mount -a` and any errors, then change the `fstab` entries.
* Mount Cheat Sheet:
[cheatsheet-mount.pdf](../../_resources/cheatsheet-mount-1.pdf)