---
title: "Kde And Tigerserver Cannot Be Ran At The Same Time"
category: "desktop-and-distributions"
tags: ["desktop-and-distributions", "kde", "tigerserver", "cannot", "ran"]
---

* Must disable the `tigervncserver` first with:
```
sudo systemctl enable --now vncserver@:3.service
```