---
title: "Rsync Command Copy Main Directories"
category: "storage-and-filesystems"
tags: ["storage-and-filesystems", "rsync", "command", "copy", "main"]
---

rsync -AvPr /mnt/pool-charlie/directory1/* /mnt/pool-delta/directory1/; rsync -AvPr /mnt/pool-charlie/directory2/* /mnt/pool-delta/directory2/; rsync -AvPr /mnt/pool-charlie/directory4/* /mnt/pool-delta/directory4/; rsync -AvP /mnt/pool-charlie/directory3/* /mnt/pool-delta/directory3/; rsync -AvP /mnt/pool-charlie/directory10/* /mnt/pool-delta/directory10/; rsync -AvP /mnt/pool-charlie/directory5/* /mnt/pool-delta/directory5/

rsync -AvP /mnt/pool-charlie/directory3/* /mnt/pool-bravo/directory3/; rsync -AvP /mnt/pool-charlie/directory10/* /mnt/pool-bravo/directory10/; rsync -AvP /mnt/pool-charlie/directory5/* /mnt/pool-bravo/directory5/; rsync -AvP /mnt/pool-charlie/directory6/* /mnt/pool-bravo/directory6/
