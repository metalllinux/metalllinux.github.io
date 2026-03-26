---
title: "Setup Zfs Ubuntu 24.04"
category: "project-tv-v2"
tags: ["project-tv-v2", "setup", "zfs", "ubuntu"]
---

* Check for the disks you want to setup with `zfs` using `by-id`:
```
ls -lh /dev/disk/by-id/
```
* Create the mount point for your pool:
```
sudo mkdir /mnt/mediapool
```
* Create the ZFS pool with your drives:
```
sudo zpool create -m /mnt/mediapool -o ashift=12 mediapool mirror ata-ST12000NM0127_ZJV62WXW ata-ST12000NM0127_ZJV68GKP
```
* Check the status of the pool:
```
zpool status -v
```
* Create the datasets:
```
sudo zfs create mediapool/anime
sudo zfs create mediapool/media-d
sudo zfs create mediapool/media-b
sudo zfs create mediapool/films
sudo zfs create mediapool/gaming_videos
sudo zfs create mediapool/media-c
sudo zfs create mediapool/music
sudo zfs create mediapool/media-a
sudo zfs create mediapool/shows
sudo zfs create mediapool/skateboarding
sudo zfs create mediapool/tv
sudo zfs create mediapool/youtube
```
* Change permissions on all datasets:
```
sudo chown -R myuser:myuser /mnt/mediapool
```
