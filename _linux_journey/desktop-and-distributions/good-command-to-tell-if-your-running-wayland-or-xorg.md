---
title: "Good Command to Tell if You're Running Wayland or Xorg"
category: "desktop-and-distributions"
tags: ["desktop-and-distributions", "good", "command", "tell", "your"]
---

# Good Command to Tell if You're Running Wayland or Xorg

loginctl show-session $(loginctl | grep $(whoami) | awk '{print $1}') -p Type

