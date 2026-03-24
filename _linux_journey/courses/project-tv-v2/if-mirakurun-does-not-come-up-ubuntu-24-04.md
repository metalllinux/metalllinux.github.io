---
title: "If Mirakurun Does Not Come Up Ubuntu 24.04"
category: "project-tv-v2"
tags: ["project-tv-v2", "mirakurun", "come", "ubuntu"]
---

If you observe the following when bringing up the Mirakurun container:
```
Error response from daemon: error gathering device information while adding custom device "/dev/px4video0": no such file or directory
```

* Pull the latest `.deb` package for the Plex TV Card Unofficial Driver:
```
wget https://github.com/tsukumijima/px4_drv/releases/download/v0.5.2/px4-drv-dkms_0.5.2_all.deb
```
* Install the Plex driver:
```
sudo gdebi -n px4-drv-dkms_0.5.2_all.deb
```
* Reboot your machine:
```
sudo reboot
```