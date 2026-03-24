---
title: "Good Way To Add Text Via The Tee Command"
category: "general-linux"
tags: ["good", "way", "add", "text", "tee"]
---

```
$ sudo tee /etc/modules-load.d/containerd.conf <<EOF
overlay
br_netfilter
EOF
```