---
title: "How Set Emacs Into Dark Mode"
category: "editors-and-tools"
tags: ["editors-and-tools", "emacs", "into", "dark", "mode"]
---

Create ~/.emacs file.
Copy the following into the file:
```
(add-to-list 'load-path "~/.emacs.d/auto-dark/")
(require 'auto-dark)
(auto-dark-mode t)
```
* Place the `auto-dark.el` file from https://github.com/LionyxML/auto-dark-emacs into `~/.emacs.d/auto-dark/auto-dark.el`