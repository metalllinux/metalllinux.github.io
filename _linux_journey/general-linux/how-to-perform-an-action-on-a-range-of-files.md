---
title: "How To Perform An Action On A Range Of Files"
category: "general-linux"
tags: ["perform", "action", "range", "files"]
---

for file in file{10..50}.txt; do
    <action> "$file"
done
