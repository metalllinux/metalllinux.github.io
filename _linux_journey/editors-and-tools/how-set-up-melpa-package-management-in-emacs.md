---
title: "How Set Up Melpa Package Management In Emacs"
category: "editors-and-tools"
tags: ["editors-and-tools", "melpa", "package", "management", "emacs"]
---

* Add the following to the .emacs file:
```
(require 'package)
(add-to-list 'package-archives '("melpa" . "https://melpa.org/packages/"))
  (package-initialize)
```
* This example is for `evil` mode:
```
M-x package-refresh-contents
M-x package-install RET evil
```
* Add the following to the `.emacs` file:
```
(require 'evil)
(evil-mode 1)
```