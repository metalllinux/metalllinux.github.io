---
title: "How To Install Pandoc And Enable Live Markdown Preview In Doom Emacs"
category: "editors-and-tools"
tags: ["editors-and-tools", "install", "pandoc", "enable", "live"]
---

Install `pandoc`:

```
sudo dnf install -y pandoc
```

Ensure that markdown is enabled in `init.el`:

```
(doom! :lang markdown)   ; <-- make sure this line is present
```

Add the following to the end of `config.el`:

```
(after! markdown
  (setq markdown-command
        '("pandoc" "--from=markdown" "--to=html5" "--standalone")))
```

Run `doom sync` and restart Emacs.

Bring up the markdown editor with the following key combination:

```
C-c C-c l (or <localleader> p) to preview
```
