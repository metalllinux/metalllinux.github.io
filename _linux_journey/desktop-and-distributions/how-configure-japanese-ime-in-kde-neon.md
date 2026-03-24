---
title: "How Configure Japanese Ime In Kde Neon"
category: "desktop-and-distributions"
tags: ["desktop-and-distributions", "configure", "japanese", "ime", "kde"]
---

sudo apt install fonts-noto-cjk-extra
sudo apt install language-pack-ja
sudo apt install ibus-mozc
Add the following in `~/.bashrc`:
```
XMODIFIERS DEFAULT=@im=ibus
GTK_IM_MODULE=ibus
QT_IM_MODULE=ibus
```