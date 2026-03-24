---
title: "Install I3 On Opensuse"
category: "desktop-and-distributions"
tags: ["desktop-and-distributions", "install", "opensuse"]
---

Install server version of openSUSE
Run zypper install i3 dmenu i3status
Create the .xinitrc file in your home directory and follow https://wiki.archlinux.org/index.php/Xinit#xinitrc
Add exec i3 at the end of the file
Then run sudo startx