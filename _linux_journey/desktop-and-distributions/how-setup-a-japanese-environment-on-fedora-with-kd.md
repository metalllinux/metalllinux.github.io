---
title: "How Setup A Japanese Environment On Fedora With Kd"
category: "desktop-and-distributions"
tags: ["desktop-and-distributions", "setup", "japanese", "environment", "fedora"]
---

```
sudo dnf install -y fcitx5
sudo dnf install -y fcitx5-mozc
```
* Go to `Virtual Keyboard` --> `Fcitx Wayland Launcher`
* Add this to your `~/.bashrc` file:
```
export XMODIFIERS=@im=fcitx
```
* Log out and then back in again.
* Select the `mozc` and `Japanese keyboard` options from the Mozc menu.
