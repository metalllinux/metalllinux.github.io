---
title: "Journal File Systems And Data Loss"
category: "general-linux"
tags: ["journal", "file", "systems", "data", "loss"]
---

* File systems such as EXT4 and XFS are journal file systems and are `Crash Consistent`. If there is a power outage, they will remove the half written data (checking the journal) and then carry on.