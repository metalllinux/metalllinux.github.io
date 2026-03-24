---
title: "Challenge Solution Local Storage"
category: "rhcsa-cert-prep-2"
tags: ["rhcsa-cert-prep-2", "challenge", "solution", "local", "storage"]
---

* Needed to add two virtual drives to the VM.
* Partition both of the drives. --> Making them physical drives.
* Create a new volume group, including both drives and create a logical volume.
* Format the logical volume and mount the logical volume.
* Make sure that it boots on startup.
	* For adding the virtual drives, we can open Virt Manager, press the bulb icon, click `Add Hardware` , select `Storage` and then create the drives there.
		* Do the same process twice.
* Need to make partitions on each drive.
	* In this case, the drives are `vdd` and `vde`.
		* `sudo gdisk /dev/vdd`
		* `n` for new partition and then all as defaults. `w` to write.
		* Do the same thing for `vde`
			* Then see the new partitions `vdd1` and `vde1`
* Then need to make the partitions available as physical volumes for `lvm` --> `sudo pvcreate /dev/vdd1` and the same thing for `sudo pvcreate /dev/vde1`
	* Verify then with `sudo pvs`
* Then need to create a volume group containing both physical volumes.
	* `sudo vgcreate vgchallenge /dev/vdd1 /dev/vde1`
		* Creates a volume group called `vgchallenege`.
			* Includes both physical volumes in the group.
				* Then verify with `sudo vgs`
* Then we need to carve out a logical volume from the volume group.
	* `sudo lvcreate --name lvchallenge -l 100%FREE vgchallenge`
		* Creates a logical volume called `lvchallenge` and it takes up 100% of the available space.
			* Then check with `sudo lvs`
* Then we need to format the logical volume.
	* Format it as `xfs` with `sudo mkfs -t xfs /dev/vgchallenge/lvchallenge`
		* Then check with `sudo blkid`
* Then need to ensure it mounts automatically.
	* Create a mountpoint with `sudo mkdir /media/lvchallenge`
		* Then mount it with `sudo mount /dev/vgchallenge/lvchallenge /media/lvchallenge`
			* Verify with `df -T`
				* Shows the mounted volumes and filesystems.
* Edit `/etc/fstab` 
	* Then add the following line at the bottom of the file:
		* ``/dev/vgchallenge/lvchallenge /media/lvchallenge xfs defaults 1 2`
			* `1` so it is included in the file system backup
			* `2` if there is a file system backup, it will do this volume as a higher priority.
* Now test the configuration with `sudo umount -a` and it will go through the fs tab and attempt to unmount each drive.
* Check that it is unmounted with `df`
* Then run `sudo mount -a`
* Then verify again with `df`
* Sometimes with KVM virtual machines, you need to remove the previous storage devices, that were not in the previous snapshots, before restoring the snapshot.