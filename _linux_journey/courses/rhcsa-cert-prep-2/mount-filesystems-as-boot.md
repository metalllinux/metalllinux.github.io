---
title: "Mount Filesystems As Boot"
category: "rhcsa-cert-prep-2"
tags: ["rhcsa-cert-prep-2", "mount", "filesystems", "boot"]
---

* Example will be using the LV data logical volume.
	* Firstly, we create the mount point with `sudo mkdir /media/lvdata` 
	* Can name the directory whatever, but good to name it something obvious.
* Now we mount it with `sudo mount /dev/vgdata/lvdata /media/lvdata`
* Can then check the mount with `df -T`.
* Can also just type in `mount` and it shows all of the mounts with all information. The latest mount points will be at the bottom of the list.
* To survive a reboot, the mount has to be added to `fstab` (File System Table).
	* `sudo vim /etc/fstab`
	* At the bottom of the file, add the following line: `/dev/vgdata/lvdata /media/lvdata xfs defaults 1 2`
		* `2` is for the backup.
* To then test fstab, we can do the following:
	* `sudo umount /media/lvdata`
	* Then test fstab with:
		* `sudo mount -a`
			* This then reads the `fstab` attempts to mount anything that isn't already mounted (much more useful than rebooting)
* Mounting a logical volume based on its path is always a good idea.