---
title: "My For Loops"
category: "general-linux"
tags: ["loops"]
---

```
for month in {01..06}; do for day in {01..31}; do for hour in {00..23}; do echo "Checking log.gz for 2023-${month}-${day} for hour ${hour}"; hdfs -text /<directory>/2023-$month-$day/${hour}*log.gz; done; done; done
```

```
for month in {01..01}; do for day in {01..08}; do for hour in {00..23}; do echo "Checking log.gz for 2024-${month}-${day} for hour ${hour}"; hdfs -text /<directory>/2024-$month-$day/${hour}*log.gz; done; done; done
```