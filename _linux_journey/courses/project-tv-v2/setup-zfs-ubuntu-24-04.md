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
sudo mkdir /mnt/vector
```
* Create the ZFS pool with your drives:
```
sudo zpool create -m /mnt/vector -o ashift=12 vector mirror ata-ST12000NM0127_ZJV62WXW ata-ST12000NM0127_ZJV68GKP
```
* Check the status of the pool:
```
zpool status -v
```
* Create the datasets:
```
sudo zfs create vector/anime
sudo zfs create vector/children_shows
sudo zfs create vector/dance_videos
sudo zfs create vector/films
sudo zfs create vector/gaming_videos
sudo zfs create vector/live_shows
sudo zfs create vector/music
sudo zfs create vector/photos
sudo zfs create vector/shows
sudo zfs create vector/skateboarding
sudo zfs create vector/tv
sudo zfs create vector/youtube
```
* Change permissions on all datasets:
```
sudo chown -R howard:howard /mnt/vector
```
