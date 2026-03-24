---
title: "Setup Kde"
category: "project-tv"
tags: ["project-tv", "setup", "kde"]
---

* Enable the EPEL and CRB repositories:
```
sudo dnf install -y epel-release
sudo dnf config-manager --set-enabled crb
```
* Install the `KDE` package group:
```
sudo dnf groupinstall -y "KDE Plasma Workspaces"
```
* Install these packages:
```
sudo dnf install -y kscreen sddm kde-gtk-config dolphin konsole kate plasma-discover firefox rocky-backgrounds sddm-breeze
```
* Enable the graphical environment:
```
sudo systemctl set-default graphical
```
* Reboot:
```
sudo reboot
```