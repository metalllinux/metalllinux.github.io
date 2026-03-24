---
title: "How To Use Scanimage"
category: "general-linux"
tags: ["scanimage"]
---

* Detect the scanners on your network with `scanimage -L` (have to use `sudo` if you are not part of the `scanner` group).
* Example command for good images is:
* `scanimage --resolution 600 --format=png > my_image.png`