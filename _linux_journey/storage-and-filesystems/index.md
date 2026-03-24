---
title: "Storage & Filesystems"
layout: archive
permalink: /linux-journey/storage-and-filesystems/
sidebar:
  nav: "linux-journey"
render_with_liquid: true
---

Notes on ZFS, Btrfs, XFS, LVM, RAID, iSCSI, backups, and storage management.

{% assign pages = site.linux_journey | where_exp: "item", "item.path contains 'storage-and-filesystems/'" | sort: "title" %}
{% for page in pages %}
{% unless page.url contains 'index' %}
- [{{ page.title }}]({{ page.url | relative_url }})
{% endunless %}
{% endfor %}
