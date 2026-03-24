---
title: "Automatic Syncing With Rsync"
category: "storage-and-filesystems"
tags: ["storage-and-filesystems", "automatic", "syncing", "rsync"]
---

Automation via crontab:

$ (crontab -l; echo "*/15 * * * * rsync -avz - progress ~/Documents/ backup_server:~/Documents > /dev/null 2>&1";) | crontab

Local directories:

rsync -zvr ~/source/directory ~/destination/directory