---
title: "Insight into the RT Kernel Changelog"
category: "kernel-and-system-internals"
tags: ["kernel-and-system-internals", "insight", "into", "kernel", "changelog"]
---

# Insight into the RT Kernel Changelog

The change log will also NOT capture the changes in the RT development tree that red hat pulls for rt during this time period.
.rt7.132
vs
rt7.166
These are GIANT blob rewrites of the core pieces of the RT ... there a HEAPS of BUG_ON() in the 8.5 kernel that are magically resolved in the 8.6 kernel.
They told us they will not upgrade to 8.6 rt when i asked them to back in 2023.
Looking at the RT kernel as well for 8.6 you'll see they keep updating from rt7.166 -> rt7.189 throught the whole 8.6 process.
[jmaple@devbox kernel-src-tree]$ git tag --list  --sort=creatordate | grep resf_kernel-rt-4.18.0-372
resf_kernel-rt-4.18.0-372.9.1.rt7.166.el8
resf_kernel-rt-4.18.0-372.13.1.rt7.170.el8_6
resf_kernel-rt-4.18.0-372.16.1.rt7.173.el8_6
resf_kernel-rt-4.18.0-372.19.1.rt7.176.el8_6
resf_kernel-rt-4.18.0-372.26.1.rt7.183.el8_6
resf_kernel-rt-4.18.0-372.32.1.rt7.189.el8_6
and those changes are mostly invisible to us.

