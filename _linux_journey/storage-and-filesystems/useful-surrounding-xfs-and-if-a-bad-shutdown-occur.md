---
title: "Useful Surrounding Xfs And If A Bad Shutdown Occur"
category: "storage-and-filesystems"
tags: ["storage-and-filesystems", "useful", "surrounding", "xfs", "bad"]
---

Use EXT4 instead.
* XFS stores stuff in memory.  Look at the stack trace, if the system goes away, then the memory disappears, latest recorded transactions.
* Can be an ECC error on the hardware side.
* If the system 