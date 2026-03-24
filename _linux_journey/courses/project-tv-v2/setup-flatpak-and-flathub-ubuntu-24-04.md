---
title: "Setup Flatpak And Flathub Ubuntu 24.04"
category: "project-tv-v2"
tags: ["project-tv-v2", "setup", "flatpak", "flathub", "ubuntu"]
---

* Install `flatpak` packages:
```
sudo apt install -y flatpak
```
* Enable `flathub`:
```
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
```
* Reboot the machine:
```
sudo reboot
```