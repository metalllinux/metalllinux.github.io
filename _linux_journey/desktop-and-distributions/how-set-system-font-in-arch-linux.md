---
title: "How Set System Font In Arch Linux"
category: "desktop-and-distributions"
tags: ["desktop-and-distributions", "system", "font", "arch", "linux"]
---

Create the file and directory:
```
~/.config/fontconfig/fonts.conf
```
* Add the following:
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE fontconfig SYSTEM "fonts.dtd">
<fontconfig>
	<alias>
		<family>monospace</family>
		<prefer><family>Cousine</family></prefer>
	</alias>
</fontconfig>
```
* Refresh the font cache.
```
fc-cache -fv
```