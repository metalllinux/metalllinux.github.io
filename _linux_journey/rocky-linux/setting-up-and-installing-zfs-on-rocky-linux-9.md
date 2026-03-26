---
title: "Setting Up And Installing Zfs On Rocky Linux 9"
category: "rocky-linux"
tags: ["rocky-linux", "setting", "installing", "zfs", "rocky"]
---

* Upgrade all packages:
```
sudo dnf upgrade -y
```
* Add the OpenZFS repository:
```
sudo dnf install -y https://zfsonlinux.org/epel/zfs-release-3-0$(rpm --eval "%{dist}").noarch.rpm
```
* Add the `epel-repository`:
```
sudo dnf install -y epel-release
```
* Install the latest `kernel-devel` package:
```
sudo dnf install -y kernel-devel
```
* Clean out `dnf`:
```
sudo dnf clean all
```
* Re-create repository caches:
```
sudo dnf makecache
```
* Install `zfs`:
```
sudo dnf install -y zfs
```
* Load the `zfs` module:
```
sudo /sbin/modprobe zfs
```
* In the event that you see a message of `modprobe: FATAL: Module zfs not found in directory /lib/modules/`
* Uninstall the `zfs` package and its required packages:
```
sudo dnf remove -y zfs
```
* Clean out `dnf`:
```
sudo dnf clean all
```
* Re-create repository caches:
```
sudo dnf makecache
```
* Reinstall `zfs` and it should perform the `dkms` build process:
```
sudo dnf install -y zfs
```
* If you updated the kernel with `sudo dnf upgrade -y`, REBOOT now.
* Load the `zfs` module:
```
sudo /sbin/modprobe zfs
```
* Check for the disks you want to setup with `zfs` using `by-id`:
```
ls -lh /dev/disk/by-id/
```
* Create the mount point for your pool:
```
sudo mkdir /mnt/<mount_point_name>
```
* Create the ZFS pool with your drives:
```
sudo zpool create -m /mnt/<mount_point_name> -o ashift=12 <pool_name> mirror ata-<drive_1> <drive_2>
```
* Check the status of the pool:
```
zpool status -v
```
* Create the datasets:
```
sudo zfs create server-a/anime
sudo zfs create server-a/bitcoin
sudo zfs create server-a/media-d
sudo zfs create server-a/media-b
sudo zfs create server-a/documents
sudo zfs create server-a/ebooks
sudo zfs create server-a/films
sudo zfs create server-a/games
sudo zfs create server-a/gaming_videos
sudo zfs create server-a/isos
sudo zfs create server-a/linux
sudo zfs create server-a/media-c
sudo zfs create server-a/music
sudo zfs create server-a/media-a
sudo zfs create server-a/shows
sudo zfs create server-a/media-e
sudo zfs create server-a/software
```
* Set compression for each dataset:
```
sudo zfs set compression=zstd-19 server-a/anime
sudo zfs set compression=zstd-19 server-a/bitcoin
sudo zfs set compression=zstd-19 server-a/media-d
sudo zfs set compression=zstd-19 server-a/media-b
sudo zfs set compression=zstd-19 server-a/documents
sudo zfs set compression=zstd-19 server-a/ebooks
sudo zfs set compression=zstd-19 server-a/films
sudo zfs set compression=zstd-19 server-a/games
sudo zfs set compression=zstd-19 server-a/gaming_videos
sudo zfs set compression=zstd-19 server-a/isos
sudo zfs set compression=zstd-19 server-a/linux
sudo zfs set compression=zstd-19 server-a/media-c
sudo zfs set compression=zstd-19 server-a/music
sudo zfs set compression=zstd-19 server-a/media-a
sudo zfs set compression=zstd-19 server-a/shows
sudo zfs set compression=zstd-19 server-a/media-e
sudo zfs set compression=zstd-19 server-a/software
```
* Set the owner of the mount directory and all sub-directories to your user:
```
sudo chown -R myuser:myuser /mnt/server-a/<mount_point_name>
```
