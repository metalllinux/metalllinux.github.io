---
title: "rsync to tails"
category: "storage-and-filesystems"
tags: ["storage-and-filesystems", "rsync", "crontab"]
---

```
# rsync to tails
0 0 * * * rsync --ignore-existing -azvr --progress /mnt/pool-echo/directory6/ user@192.168.1.x:/mnt/pool-foxtrot/directory6/
0 0 * * * rsync --ignore-existing -azvr --progress /mnt/pool-echo/directory7/ user@192.168.1.x:/mnt/pool-foxtrot/directory7/
0 0 * * * rsync --ignore-existing -azvr --progress /mnt/pool-echo/directory2/ user@192.168.1.x:/mnt/pool-foxtrot/directory2/
0 0 * * * rsync --ignore-existing -azvr --progress /mnt/pool-echo/directory8/ user@192.168.1.x:/mnt/pool-foxtrot/directory8/
0 0 * * * rsync --ignore-existing -azvr --progress /mnt/pool-echo/directory9/ user@192.168.1.x:/mnt/pool-foxtrot/directory9/
0 0 * * * rsync --ignore-existing -azvr --progress /mnt/pool-echo/directory11/ user@192.168.1.x:/mnt/pool-foxtrot/directory11/
0 0 * * * rsync --ignore-existing -azvr --progress /mnt/pool-echo/directory10/ user@192.168.1.x:/mnt/pool-foxtrot/directory10/
0 0 * * * rsync --ignore-existing -azvr --progress /mnt/pool-echo/directory3/ user@192.168.1.x:/mnt/pool-foxtrot/directory3/
0 0 * * * rsync --ignore-existing -azvr --progress /mnt/pool-echo/directory4/ user@192.168.1.x:/mnt/pool-foxtrot/directory4/
0 0 * * * rsync --ignore-existing -azvr --progress /mnt/pool-echo/directory1/ user@192.168.1.x:/mnt/pool-foxtrot/directory1/
0 0 * * * rsync --ignore-existing -azvr --progress /mnt/pool-echo/directory5/ user@192.168.1.x:/mnt/pool-foxtrot/directory5/
```