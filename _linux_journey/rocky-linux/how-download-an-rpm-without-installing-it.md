---
title: "How Download An Rpm Without Installing It"
category: "rocky-linux"
tags: ["rocky-linux", "download", "rpm", "without", "installing"]
---

Example:
`sudo dnf install --downloadonly --downloaddir ./ htop`
* If you don't specify `--downloaddir`, the package will be stored in `/var/cache/yum/ in rhel-{arch}-channel/packages`.