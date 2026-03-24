---
title: "!/bin/sh"
category: "general-linux"
tags: ["count", "incrementally", "date", "comma"]
---

```
# !/bin/sh

DATE=2024-01-01

for i in {0..10}
do
	NEXT_DATE=$(date +%Y-%m-%d -d "$DATE + $i day")
	echo "$NEXT_DATE"
done
