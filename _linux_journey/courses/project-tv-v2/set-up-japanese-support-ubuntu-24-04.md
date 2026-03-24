---
title: "Set Up Japanese Support Ubuntu 24.04"
category: "project-tv-v2"
tags: ["project-tv-v2", "japanese", "support", "ubuntu"]
---

* Install the `fcitx` packages:
```
sudo apt install -y fcitx5 fcitx5-mozc
```
* Go to Regional Settings --> Input Method --> Add Input Method.
* Select `No` to both questions that come up surrounding the user configuration.
* Log out and then back in again.
* Then where the `ja` is in the bottom left-hand corner, right-click and select `configure`.
* Then under `Available Input Method`, type `mozc` and then press the left arrow button.
* Remove the existing `Japanese Keyboard`.