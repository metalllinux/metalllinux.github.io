---
title: "Good While Loop To Go Through Each Line Of A File"
category: "storage-and-filesystems"
tags: ["storage-and-filesystems", "good", "while", "loop", "through"]
---

```
file="/path/to/file"
while read line; do
  echo "${line}"
done < "${file}"
```