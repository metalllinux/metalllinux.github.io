---
title: "Why Dates Do Not Match up in a Kernel Source Tree"
category: "kernel-and-system-internals"
tags: ["kernel-and-system-internals", "dates", "match", "kernel", "source"]
---

# Why Dates Do Not Match up in a Kernel Source Tree

for context on everyone in the thread, if you have a specific kernel VNR you should be able to search it in the kernel-src-tree.
 {vendor}_kernel-NVR
SHOULD pretty closly match the src.rpm from that vendor it was generated from to do the reconstructions I pull ALL available CENTOS / RESF vaulted src.rpms, and because they were built in the past the dates will never matchup since I created this version of kernel-src-tree less than a year ago

If its ciq its tagged and that date will always be ahead of the src/binary rpm because of the manual build/sign/test process we go through
In the early days it was very sloppy but its now generated with automation at content release time (ie PR to dist-git)

