---
title: "Force Flatpak To Use The Correct Gtk Theme Across"
category: "desktop-and-distributions"
tags: ["desktop-and-distributions", "force", "flatpak", "correct", "gtk"]
---

sudo flatpak override --filesystem=$HOME/.themes
sudo flatpak override --env=GTK_THEME=<theme_name>
Restart all flatpak apps to see the change.