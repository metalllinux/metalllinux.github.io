---
title: "Mount And Unmount Cifs And Nfs Network File System"
category: "rhcsa-cert-prep-2"
tags: ["rhcsa-cert-prep-2", "mount", "unmount", "cifs", "nfs"]
---

* Two main types of Network Filesystems are NFS and CIFS
* NFS --> Network File System
	* Linux and Unix default.
* CIFS --> Network File System for Windows
		* To mount a remote NFS File System, we do `sudo yum -y install nfs-utils`
		* Then create a mountpoint, for example `sudo mkdir /mnt/nfsshare`
			* `/mnt` is usually set aside for Network Mounts.
			* Then we mount the remote share with `mount -t nfs 192.168.1.218:/share /mnt/nfsshare`
			* We need to also mount these in `fstab`.
		* For an `NFS remote share`, the syntax would look like the following `192.168.1.218:/share /mnt/nfsshare nfs _netdev 0 0`
			* `/mnt/nfsshare` is the local mountpoint.
				* `_netdev` ensures networking is running before mounting.
					* The system waits for the network to come up, before mounting the share.
						* `0 0` turns of `dump/restore and filesystem check` at boot.
		* Unmounting an NFS share is as simple as `sudo umount /mnt/nfsshare`
* The other network file system is CIFS
	* `sudo yum -y install samba-client cifs-utils`
		* Need to make sure the above are installed.
	* CIFS --> Common Internet File System
		* Used to mount remote Windows shares.
			* Test with smbclient --> `smbclient //192.168.1.218/smbshare -U user1`
				* Useful for troubleshooting CIFS network drives
				* Can use `smbclient to connect to a Windows share`
					* With an FTP-like interface
						* You can either set a hostname or IP address.
							* In Windows, the same path uses backslashes.
								* `-U user1` specifies the user whom you want to login as.
			* Then make the `smb` share with `sudo mkdir /mnt/smbshare`
				* Then mount it with `mount //192.168.1.218/smbshare /mnt/smbshre -o username=user1` have to specify whom to authenticate as.
				* With NFS, you authenticate as yourself.
					* Device is the CIFS URL, which is `//192.168.1.218/smbshare`
						* Don't want to place a password in `/etc/fstab`, because it is world readable.
							* Therefore, a credentials file is created.
								* `sudo vim /etc/samba/credentials`
									* Nobody but `root` can read this file.
										* It has `username=user1
password=testpass`
* The credentials would then be referenced like this in `/etc/fstab`:
![Screenshot_20230926_160638.png](../../_resources/Screenshot_20230926_160638.png)