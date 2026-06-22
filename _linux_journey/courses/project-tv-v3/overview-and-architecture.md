---
title: "Overview and Architecture"
category: "project-tv-v3"
tags: ["project-tv-v3", "overview", "architecture", "kubernetes"]
---

## Project TV v3 (Rocky Edition)

Project TV v3 is a complete rewrite of the media server setup, migrating from Ubuntu 24.04 with Docker Compose to Rocky Linux 10 with Kubernetes (kubeadm).

### Key changes from v2

| Feature | v2 (Ubuntu) | v3 (Rocky) |
|---------|-------------|------------|
| OS | Ubuntu 24.04 | Rocky Linux 10 |
| Container orchestration | Docker Compose | Kubernetes (kubeadm) |
| Music server | None | Navidrome |
| Library refresh | VM + xdotool | Jellyfin API CronJob |
| TV tuner driver | DEB package | RPM (DKMS) |
| ZFS datasets | Fixed list | Dynamic (installer prompts) |
| Installation | Manual steps | Interactive installer |

### Architecture

```
Rocky Linux 10 (Host)
├── ZFS Pool (user-configured datasets)
├── Kubernetes (kubeadm + containerd + Flannel)
│   ├── Mirakurun (TV tuner management, port 40772)
│   ├── EPGStation + MariaDB (TV recording, port 8888)
│   ├── Jellyfin (media server, port 8096)
│   ├── Tube Archivist + Redis + ES (YouTube archive, port 8000)
│   ├── Navidrome (music server, port 4533)
│   └── CronJob: Jellyfin library refresh (hourly)
├── Sanoid (ZFS snapshot management)
├── KDE Plasma 6 (desktop)
└── px4_drv (TV tuner kernel driver, DKMS RPM)
```

### Hardware used

* Intel 12th Gen Alder Lake-S with UHD Graphics 730
* PLEX PX-W3PE5 TV tuner (USB, via MosChip MCS9990 PCIe USB card)
* SCM SCR331-LC1 SmartCard reader (for B-CAS)
* Realtek RTL8111 Gigabit Ethernet
* NVMe boot drive + SATA drives for ZFS

### Repository

All scripts, manifests, and documentation are at:
[github.com/metalllinux/project-tv-rocky-edition](https://github.com/metalllinux/project-tv-rocky-edition)
