---
title: "How to Increase Verbosity in multipath.conf"
category: "storage-and-filesystems"
tags: ["storage-and-filesystems", "increase", "verbosity", "multipath", "conf"]
---

# How to Increase Verbosity in multipath.conf

* Add the following between `/etc/multipath.conf`

```
defaults {
    verbosity 3
}
```

A maximum verbosity of `9` is available, the default is `2`.
