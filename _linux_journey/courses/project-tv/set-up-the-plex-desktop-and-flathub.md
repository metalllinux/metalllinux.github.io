---
title: "Set Up The Plex Desktop And Flathub"
category: "project-tv"
tags: ["project-tv", "plex", "desktop", "flathub"]
---

* Install Flatpak:
```
sudo dnf install flatpak
```
* Add the Flathub repository:
```
flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
```
* Reboot:
```
sudo reboot
```
* Install the Plex desktop:
```
flatpak install flathub tv.plex.PlexDesktop
```