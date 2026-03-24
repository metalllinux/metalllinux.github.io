---
title: "The Command to Backup All Directories Excluding the Tickets Directory"
category: "storage-and-filesystems"
tags: ["storage-and-filesystems", "command", "backup", "all", "directories"]
---

# The Command to Backup All Directories Excluding the Tickets Directory

```
tar -cvf documents.tar.gz --exclude='tickets' -C "$HOME/Documents" .
```
