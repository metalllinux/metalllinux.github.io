---
title: "How Set Terminator To Dark Theme"
category: "general-linux"
tags: ["terminator", "dark", "theme"]
---

Install this plugin: https://github.com/yurenchen000/terminator-autotheme-plugin
* Download the Python file.
* Create the plugins directory:
```
mkdir ~/.config/terminator/plugins
```
* Copy the Python file into the `plugins` directory:
```
mv ~/.config/terminator/auto_theme.py ~/.config/terminator/plugins/
```
* Restart Terminator if it is open.
* Go to `Settings` --> `Plug-ins` and then select `Auto Theme`.
* Restart Terminator again and it will go into dark mode.