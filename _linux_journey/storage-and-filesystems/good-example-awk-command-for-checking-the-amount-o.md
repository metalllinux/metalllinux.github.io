---
title: "Good Example Awk Command For Checking The Amount O"
category: "storage-and-filesystems"
tags: ["storage-and-filesystems", "good", "example", "awk", "command"]
---

```
awk '/logstash/ {print $6}' sos_commands/process/ps_-elfL | sort -n | uniq | wc -l
```