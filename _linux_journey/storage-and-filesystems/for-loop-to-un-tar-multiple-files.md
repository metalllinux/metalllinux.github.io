---
title: "For Loop To Un Tar Multiple Files"
category: "storage-and-filesystems"
tags: ["storage-and-filesystems", "loop", "tar", "multiple", "files"]
---

`for i in *.tar; do tar -xvf "$i"; done`
To then remove the remaining `tar` files:
`for i in *.tar; do rm "$i"; done`