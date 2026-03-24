---
title: "How Remove Particular Filesystem Access To A Flatp"
category: "general-linux"
tags: ["remove", "particular", "filesystem", "access", "flatp"]
---

sudo flatpak override com.valvesoftware.Steam --nofilesystem=/run/user/1000/gvfs/smb-share:server=192.168.1.101,share=sonic_games/steam