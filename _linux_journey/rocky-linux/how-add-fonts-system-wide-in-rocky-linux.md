---
title: "How Add Fonts System Wide In Rocky Linux"
category: "rocky-linux"
tags: ["rocky-linux", "add", "fonts", "system", "wide"]
---

* Create a directory for the fonts in `/usr/share/fonts` and place the font files in there.
* Scan the font directories and rebuild the font information cache with `sudo fc-cache -f -v`