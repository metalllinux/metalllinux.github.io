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
sudo zfs create sonic/anime
sudo zfs create sonic/bitcoin
sudo zfs create sonic/children_shows
sudo zfs create sonic/dance_videos
sudo zfs create sonic/documents
sudo zfs create sonic/ebooks
sudo zfs create sonic/films
sudo zfs create sonic/games
sudo zfs create sonic/gaming_videos
sudo zfs create sonic/isos
sudo zfs create sonic/linux
sudo zfs create sonic/live_shows
sudo zfs create sonic/music
sudo zfs create sonic/photos
sudo zfs create sonic/shows
sudo zfs create sonic/skateboarding
sudo zfs create sonic/software
```
* Set compression for each dataset:
```
sudo zfs set compression=zstd-19 sonic/anime
sudo zfs set compression=zstd-19 sonic/bitcoin
sudo zfs set compression=zstd-19 sonic/children_shows
sudo zfs set compression=zstd-19 sonic/dance_videos
sudo zfs set compression=zstd-19 sonic/documents
sudo zfs set compression=zstd-19 sonic/ebooks
sudo zfs set compression=zstd-19 sonic/films
sudo zfs set compression=zstd-19 sonic/games
sudo zfs set compression=zstd-19 sonic/gaming_videos
sudo zfs set compression=zstd-19 sonic/isos
sudo zfs set compression=zstd-19 sonic/linux
sudo zfs set compression=zstd-19 sonic/live_shows
sudo zfs set compression=zstd-19 sonic/music
sudo zfs set compression=zstd-19 sonic/photos
sudo zfs set compression=zstd-19 sonic/shows
sudo zfs set compression=zstd-19 sonic/skateboarding
sudo zfs set compression=zstd-19 sonic/software
```
* Set the owner of the mount directory and all sub-directories to your user:
```
sudo chown -R howard:howard /mnt/sonic/<mount_point_name>
```
