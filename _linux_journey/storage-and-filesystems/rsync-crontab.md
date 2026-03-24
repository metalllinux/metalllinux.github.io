---
title: "rsync documents from pool-alpha to pool-bravo"
category: "storage-and-filesystems"
tags: ["storage-and-filesystems", "rsync", "crontab"]
---

crontab -e

```
# rsync documents from pool-alpha to pool-bravo
0 0 * * * rsync --ignore-existing -azvr --progress /mnt/pool-alpha/directory2/ /mnt/pool-bravo/directory2/

# rsync movies from pool-alpha to pool-bravo
0 0 * * * rsync --ignore-existing -azvr --progress /mnt/pool-alpha/directory3/ /mnt/pool-bravo/directory3/

# rsync pictures from pool-alpha to pool-bravo
0 0 * * * rsync --ignore-existing -azvr --progress /mnt/pool-alpha/directory1/ /mnt/pool-bravo/directory1/
```
crontab -l

rsync --ignore-existing -azvr --progress /mnt/pool-alpha/directory1/* /mnt/pool-echo/directory1/; rsync --ignore-existing -azvr --progress /mnt/pool-alpha/directory6/* /mnt/pool-echo/directory6/; rsync --ignore-existing -azvr --progress /mnt/pool-alpha/directory7/* /mnt/pool-echo/directory7/; rsync --ignore-existing -azvr --progress /mnt/pool-alpha/directory8/* /mnt/pool-echo/directory8/; rsync --ignore-existing -azvr --progress /mnt/pool-alpha/directory9/* /mnt/pool-echo/directory9/; rsync --ignore-existing -azvr --progress /mnt/pool-alpha/directory10/* /mnt/pool-echo/directory10/; rsync --ignore-existing -azvr --progress /mnt/pool-alpha/directory3/* /mnt/pool-echo/directory3/; rsync --ignore-existing -azvr --progress /mnt/pool-alpha/directory4/* /mnt/pool-echo/directory4/; rsync --ignore-existing -azvr --progress /mnt/pool-alpha/directory5/* /mnt/pool-echo/directory5/