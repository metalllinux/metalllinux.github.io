---
title: "[[Bjonnh.net](https://www.bjonnh.net/)]# _"
category: "storage-and-filesystems"
tags: ["storage-and-filesystems", "switching", "your", "nvme", "ssd"]
---

# \[[Bjonnh.net](https://www.bjonnh.net/)\]# _

[Blog](https://www.bjonnh.net/article/) [Projects](https://www.bjonnh.net/categories/projects/) [Publications](https://www.bjonnh.net/categories/publications/) [About](https://www.bjonnh.net/about/) [RSS Feed](https://www.bjonnh.net/index.xml)

## [Articles](https://www.bjonnh.net/article/) / [Switching your NVME ssd to 4k](https://www.bjonnh.net/article/20210721_nvme4k/) \>

  

July 21, 2021

category [computer](https://www.bjonnh.net/categories/computer) tags [nvme](https://www.bjonnh.net/tags/nvme) [performance](https://www.bjonnh.net/tags/performance)

```
# You may want to replace 0 by your drive number. Make sure you check the serial number
# to not erase the one you didn' want.
nvme id-ns -H /dev/nvme0n1
```

Look at the last lines:

If it says:

```
LBA Format  0 : Metadata Size: 0   bytes - Data Size: 512 bytes - Relative Performance: 0 Best (in use)
```

Your disk only handles 512 bytes sectors.

If it says:

```
LBA Format  0 : Metadata Size: 0   bytes - Data Size: 512 bytes - Relative Performance: 0x2 Good  (in use)
LBA Format  1 : Metadata Size: 0   bytes - Data Size: 4096 bytes - Relative Performance: 0x1 Better
```

It means your drive supports 4k sectors, but it is currently set to 512 bytes.

To set it to 4k. Careful, this will erase everything on your drive:

```
nvme format --lbaf=1 /dev/nvme0n1   # This will delete everything on that drive!
```

If it says that:

```
NVMe status: ACCESS_DENIED: Access to the namespace and/or LBA range is denied due to lack of access rights(0x4286)
```

It means it is locked. If you used the drive (partition, read or write), it is usually locked by its firmware. I was able to unlock it by just suspending the machine and waking it up, but I heard it doesn’t work all the time. You may want to reboot it may solve it as well.

I did see a 10% improvement on my ext4 really basic benchmarks. There is really little reason to keep it to 512 except for compatibility anyway the disk seems to use 4k internally.

© 2021 Bjonnh.net - [CC BY-SA 4.0](http://creativecommons.org/licences/by-sa/4.0/) unless stated otherwise.