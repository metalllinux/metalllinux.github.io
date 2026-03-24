---
title: "How To Enable Fips On Any Enterprise Distro At Boo"
category: "security"
tags: ["security", "enable", "fips", "any", "enterprise"]
---

* Boot into the ISO from Ventoy or the source of choice.
* Hit `e` to go into the GRUB settings.
* Add `fips=1` to the end of the middle cmdline parameter line.
* Then continue the boot, install the OS and check that FIPS is enabled with:
```
fips-mode-setup --check
```