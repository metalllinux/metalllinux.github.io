---
title: "How to Set Up Video Playback Support (H.264) and More on Rocky Linux 9"
category: "rocky-linux"
tags: ["rocky-linux", "setup", "h264", "more", "video"]
---

# How to Set Up Video Playback Support (H.264) and More on Rocky Linux 9

```
sudo dnf config-manager --set-enabled crb
sudo dnf install https://download1.rpmfusion.org/free/el/rpmfusion-free-release-9.noarch.rpm                  https://download1.rpmfusion.org/nonfree/el/rpmfusion-nonfree-release-9.noarch.rpm
sudo dnf install gstreamer1-libav gstreamer1-plugins-bad-free gstreamer1-plugins-good ffmpeg
```
