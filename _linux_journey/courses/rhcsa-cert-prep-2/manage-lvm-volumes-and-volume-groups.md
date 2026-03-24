---
title: "Manage Lvm Volumes And Volume Groups"
category: "rhcsa-cert-prep-2"
tags: ["rhcsa-cert-prep-2", "manage", "lvm", "volumes", "volume"]
---

* There are limitations to standard partitions.
	* They have to be contignous on the disk.
		* If you want to resize a partition on the middle of the disk, this is not possible.
			* Cannot just take space from the `/var` partition, to add to the home partition, like in the below example:
![Screenshot_20230921_090032.png](../../_resources/Screenshot_20230921_090032.png)
* Logical volumes with LVM allow resising of volumes.
	* Includes resising, combining volumes and moving them.
	* If there is room in a volume group, you can resize them, even if the empty space is on another disk.
	* In this example, 50GB has been taken from the end of the drive:
![Screenshot_20230921_213134.png](../../_resources/Screenshot_20230921_213134.png)
* LVM looks at data on a disk in a logical way, as opposed to a physical way.
	* The data in a logical volume, can be in multiple different areas of the disk.
		* The space can be added to a volume and it does not have to be contiguos.
			* The drive space appears contiguous, to applications that sit on the drives.
				* It is possible to add more drives on the fly.
					* The logical volume can then be expanded across the drives like so:
![Screenshot_20230921_213357.png](../../_resources/Screenshot_20230921_213357.png)
* To create an LVM system, we need to add a partition or drive to an LVM Volume group.
	* Then divide that up into logical volumes.
		* To use it for LVM, we need to make a physical volume.
	* To prepare a partition for LVM, we do `sudo pvcreate /dev/PARTITION`
		* PVS --> Physical, Volume, Summary
			* `sudo pvs`
		* If you want to know more about your PVs, can use `sudo pvdisplay`
			* To reference physical volumes, you use the absolute path to the physical drive.
				* Now that the above partition is a PV, we can create a volume group and include it.
					* We use `vgcreate` for this.
						* `sudo vgcreate vgdata /dev/PARTITION`
							* It will create a volume group called `vgdata` and include (for example) a `/dev/vdb1` physical volume.
								* Verify the volume group has been created successfully with `sudo vgs`
									* For more information, we can use `sudo vgdisplay`
										* Now we can create a logical volume within the Volume Group. For that we use `lvcreate`
											* `sudo lvcreate --name lvdata --size 495M vgdata`
												* Creates a new logical volume that is `495M` in size called `lvdata` in the `vgdata` Volume Group.
													* The logical volume has to be slightly smaller than the Volume Group, so we can make sure it fits.
													* Check again with `sudo lvs`
														* In addition, `sudo lvdisplay`. The LV Path will be something like `/dev/vgdata/lvdata`
* There are two different paths you can use to refers to logical volumes.
	* To refer to a loglcal volume path, the syntax for that would be `/dev/VolumeGroupName/LocalVolumeName`
			* Can also use `/dev/mapper/VolumeGroupName-LogicalVolumeName` as well. If there is a hyphen in the volumegroupname or the logicalgroupname, then it gets harder to read.
* Now we need to format the logical volume with a file system.
	* Two commands include `mkfs` and `mke2fs` (mke2fs is more powerful)
		* `mke2fs` allows you to choose journal types and optimisations.
			* Both commands call on other tools to do the actual formatting.
* Linux File Systems
	* The historic filesystem is `ext2`, this supports permissions and ownership, but is not journalised. If the system crashes, the os does not know what it was last doing, due to not writing it as a journal.
		* Therefore, when booting up, the system has to check for corrupt files.
	* `ext3` is `ext2`, but with a journal. 
	* `ext4` supports larger drives. It is more robust than `ext3` and supports SSDs as well.
		* `ext2` and `ext3` drives can be migrated to `ext4`.
	* The default file system with Enterprise Linux is `XFS`
		* Created by Silicon Graphics, for its version of Unix. Supports larger drives than `ext4` and larger max file sizes.
* Useful chart of the file systems:
![Screenshot_20230922_181709.png](../../_resources/Screenshot_20230922_181709.png)
* How to format a logical volume as XFS.
	* `sudo mkfs -t xfs /dev/vgdata/lvdata`
		* You can then verify this with `sudo blkid`
* Cheat Sheets for LVM:
[fstab.pdf](../../_resources/fstab.pdf)
[cheatsheet-mount.pdf](../../_resources/cheatsheet-mount.pdf)
[cheatsheet-lvm-advanced.pdf](../../_resources/cheatsheet-lvm-advanced.pdf)
[cheatsheet-lvm.pdf](../../_resources/cheatsheet-lvm.pdf)
[cheatsheet-disktools.pdf](../../_resources/cheatsheet-disktools.pdf)

