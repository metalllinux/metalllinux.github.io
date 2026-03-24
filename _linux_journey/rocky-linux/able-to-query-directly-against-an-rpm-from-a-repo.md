---
title: "Able To Query Directly Against An Rpm From A Repo"
category: "rocky-linux"
tags: ["rocky-linux", "able", "query", "directly", "against"]
---

* `rpm -q --changelog <link> | grep <package_name>`
* Example is provided below:
```
rpm -q --changelog https://dl.rockylinux.org/pub/rocky/9.3/BaseOS/source/tree/Packages/k/kernel-5.14.0-362.24.1.el9_3.0.1.src.rpm | grep openvswitch
```
* Example output:
```
[howard@rocky-linux-9-1 Downloads]$ rpm -q --changelog kernel-5.14.0-362.8.1.el9_3.x86_64.rpm | grep openvswitch | grep ct_state
- net: openvswitch: Fix ct_state nat flags for conns arriving from tc (Antoine Tenart) [2045048]
```