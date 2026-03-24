---
title: "How Set Dark Mode With Gtk Applications In Sway"
category: "general-linux"
tags: ["dark", "mode", "gtk", "applications", "sway"]
---

Create
```
~/.config/gtk-3.0/settings.ini
```
Add the following.
```
[Settings]
gtk-application-prefer-dark-theme=1
```
Restart the application for the changes to take effect.