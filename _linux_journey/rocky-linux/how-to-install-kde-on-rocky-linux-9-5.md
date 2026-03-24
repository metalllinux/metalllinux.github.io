---
title: "How To Install Kde On Rocky Linux 9.5"
category: "rocky-linux"
tags: ["rocky-linux", "install", "kde", "rocky", "linux"]
---

* Enable the EPEL and CRB repositories:
```
sudo dnf config-manager --set-enabled crb
sudo dnf -y install epel-release
```
* Install the `KDE` package group:
```
sudo dnf groupinstall "KDE Plasma Workspaces" -y
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