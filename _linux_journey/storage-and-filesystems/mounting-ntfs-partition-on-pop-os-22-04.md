---
title: "Mounting Ntfs Partition On Pop! Os 22.04"
category: "storage-and-filesystems"
tags: ["storage-and-filesystems", "mounting", "ntfs", "partition", "pop"]
---

* The `ntfs-3g` package is already installed. 
* `fuse3` is already installed, so no need for `fuse`.
* Please open the terminal. You will also need your password handy as well.
* Run `sudo parted -l` in the terminal to see information about all the available drives.
```
sudo parted -l
```
* This is my example below:
```
test@pop-os:~$ sudo parted -l
[sudo] password for test: 
Model: I-O DATA USB Flash Disk (scsi)
Disk /dev/sda: 4081MB
Sector size (logical/physical): 512B/512B
Partition Table: msdos
Disk Flags: 

Number  Start   End     Size    Type     File system  Flags
 1      1049kB  4081MB  4080MB  primary  ntfs
``` 
* Observe the name of the drive you are trying to mount. It should be `/dev/sd<letter>`. In the above example, we want to mount `/dev/sda1`. Since yours is a secondary hard drive, it will likely be labelled `/dev/sdb`.
* Make a mount point with `sudo mkdir -p /mnt/<mount_name>`
	* For example, I create a mount called `/mnt/chocolate`.
```
sudo mkdir -p /mnt/chocolate
```
* We now mount the drive with `sudo mount -t ntfs /dev/sd<letter><number> /mnt/<mount_name>`. In my example, this would be:
```
sudo mount -t ntfs /dev/sda1 /mnt/chocolate
```
* If you receive no errors or warning messages (just an empty output), that is good. The drive is now mounted to the mount point.
* To make the mount permanent if you reboot or shutdown your machine, we have to edit a file. This is the `/etc/fstab` file. We edit this with a text editor.
```
sudo nano /etc/fstab
```
* At the bottom of the file, we add the following line (the spaces are also important):
```
/dev/sd<letter><number>        /mnt/<mount_name>       ntfs    defaults        0       0
```
* In my example, this would be:
```
/dev/sda1        /mnt/chocolate       ntfs    defaults        0       0
```
* To save the changes, we press ctrl + o and then press enter.
* To exit the editor, we press ctrl + x and then press enter.
* To add the drive to your file manager, open the file manager and click `Other Locations`
![Screenshot from 2024-05-15 23-00-09.png](../_resources/Screenshot%20from%202024-05-15%2023-00-09.png)
* Then double click `Computer`
* Once inside there, open the `mnt` directory:
![Screenshot from 2024-05-15 23-03-18.png](../_resources/Screenshot%20from%202024-05-15%2023-03-18.png)
* You will then see your mounted drive. In my case it was `chocolate`.
![Screenshot from 2024-05-15 23-03-57.png](../_resources/Screenshot%20from%202024-05-15%2023-03-57.png)
* From there, you can drag the directory into the side menu for ease of access:
![Screenshot from 2024-05-15 23-04-54.png](../_resources/Screenshot%20from%202024-05-15%2023-04-54.png)