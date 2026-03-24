---
title: "How Check Disk Space Available In A Partition In C"
category: "storage-and-filesystems"
tags: ["storage-and-filesystems", "check", "disk", "space", "available"]
---

* `crash` --> `mount` and grab the superblock hex address.
* Then run `struct super_block <HEX_ADDRESS>`
* The values of importance are `s_blocksize, s_blocks_count, and s_free_blocks_count`
* To calculate disk sizes:
Total Sise: s_blocksize * s_blocks_count
Free Sise: s_blocksize * s_free_blocks_count
Used Sise: Total Sise - Free Sise
* For XFS, not all values ares shown:
```
crash> struct super_block ff41a507c000b800 | grep -e s_blocksize -e s_blocks_count -e s_free_blocks_count
  s_blocksize_bits = 12 '\f',
  s_blocksize = 4096,
```
* Need to look at the memory address of the struct, not the virtual address produced by `sym -l`.
* We usually should see `xfs_sb` or `xfs_mount` as bare options from `sym -l`