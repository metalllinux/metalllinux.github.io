---
title: "How Provide Steam Flatpak Access To A Network Driv"
category: "networking"
tags: ["networking", "provide", "steam", "flatpak", "access"]
---

sudo flatpak override --filesystem=/run/user/1000/gvfs/smb-share:server=192.168.1.101,share=sonic_games/steam com.valvesoftware.Steam 