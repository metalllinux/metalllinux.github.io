---
title: "Setup Zfs Ubuntu 24.04"
category: "project-tv"
tags: ["project-tv", "setup", "zfs", "ubuntu"]
---

```
sudo zfs create mediapool/tv
sudo zfs create mediapool/youtube
```
* The other datasets are automatically created by the Sanoid / Syncoid replication process.