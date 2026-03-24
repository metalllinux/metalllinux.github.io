---
title: "/etc/apt/sources.list.d/pve-enterprise.list"
category: "general-linux"
tags: ["change", "proxmox", "enterprise", "subscription", "subsc"]
---

#/etc/apt/sources.list.d/pve-enterprise.list

From: deb https://enterprise.proxmox.com/debian/pve bookworm enterprise
To: deb http://download.proxmox.com/debian/pve bookworm pve-no-subscription

#/etc/apt/sources.list.d/ceph.list
From: deb https://enterprise.proxmox.com/debian/ceph-quincy bookworm enterprise
To: deb http://download.proxmox.com/debian/ceph-quincy bookworm no-subscription

sudo apt update

sudo apt dist-upgrade