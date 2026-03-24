---
title: "How To Set Up Japanese Language Support In Fedora"
category: "desktop-and-distributions"
tags: ["desktop-and-distributions", "japanese", "language", "support", "fedora"]
---

* Install the following packages:
```
sudo dnf -y install fcitx5-mozc fcitx5-kkc fcitx5-autostart
```
* Log out and then log back in.
* In the FCITX Configurator, select Mozc and the Japanese Keyboard options.