---
title: "Extend Existing Logical Volumes"
category: "rhcsa-cert-prep-2"
tags: ["rhcsa-cert-prep-2", "extend", "existing", "logical", "volumes"]
---

* One advantage of LVM is you can resizean LV with non-contiguous drive space.
* In this example, another drive is being added to the LVM.
	* Get a list of the partitions with `cat /proc/partitions`
		* In this case, the new drive is `/dev/vdc`
		* Need to put a partition on that, for that we need to use `gdisk` --> `sudo gdisk /dev/vdc`
			* `n` for new partition.
			* Select the defaults.
			* `p` for printing the partition table.
				* Check again with `cat /proc/partitions` and the logical `vdc1`.
					* Run `partprobe` if you don't see the new partition in the list.
			* To create a physical volume, `sudo pvcreate /dev/vdc1`
				* Then verify with `sudo pvs`. You can see it is not part of a Volume Group.
		* Now we can check all of the available Volume Groups:
			* `sudo vgs`
				* We can extend `vgdata` by adding a new physical volume to it.
					* `sudo vgextend vgdata /dev/vdc1`
			* Then again run `sudo vgs` and you'll see the `vgdata` group is a lot larger.
				* Then we need to resize the logical volume.
					* Use `lvresize` then we verify the logical volume size first type.
						* Then do `sudo lvs` you'll still see the volume group is 500MB, something like:
![Screenshot_20230926_104455.png](../../_resources/Screenshot_20230926_104455.png)
						* `sudo lvresize -l 100%FREE /dev/vgdata/lvdata`
![Screenshot_20230926_110039.png](../../_resources/Screenshot_20230926_110039.png)
* When specifying a logical volume, we provide it the full path.
	* If you do `sudo lvs` again, the logical volume will be much larger.
		* To see the file size, just run `df -h`
			* In the above example, the file system is `XFS`, so it will still be the same size.
				* For that, we use `xfs_growfs` to resize it. 
					* `sudo xfs_growfs /dev/vgdata/lvdata`
						* Then verify with `df -h`
							* It will then be expanded to the new file system size.
				* If it were `EXT3` or `EXT4`, we use `resize2fs`. 
					* The `lvsize` command can also resize partitions as well. Older versions cannot.

