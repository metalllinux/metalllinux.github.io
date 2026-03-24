---
title: "Skip 1S Setup Ubuntu 24.04"
category: "project-tv-v2"
tags: ["project-tv-v2", "skip", "setup", "ubuntu"]
---

* Download the `Skip` `appimage` from:
```
https://flirc.tv/products/skip1s-remote-universal-remote-control?variant=43489094729960
```
* `rsync` the image from your host to the media server:
```
rsync /home/howard/Downloads/SkipApp-0.9.993.9235-Beta-x64.AppImage.tar.gz howard@192.168.1.107:~/****
```
* Extract the `appimage`;
```
tar -xf ./SkipApp-0.9.993.9235-Beta-x64.AppImage.tar.gz
```
* Move the `appimage` to the `appimages` directory:
```
mv skip-app_0.9.993+9235_amd64.AppImage ~/appimages/
```
* Run the `appimage`:
```
~/appimages/skip-app_0.9.993+9235_amd64.AppImage
```
* For the appimage, you need a mouse with a scroll wheel, as there is no bar available to move down the list of actions in the `Activity` pane.
* Only set up the Flirc --> Windows Media centre profile, no need for the Flirc --> Kodi profile.