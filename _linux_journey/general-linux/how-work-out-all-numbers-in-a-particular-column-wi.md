---
title: "How Work Out All Numbers In A Particular Column Wi"
category: "general-linux"
tags: ["work", "out", "all", "numbers", "particular"]
---

`cat sa21-02.sar-A.20240827101311.out | grep -A50 "proc\/s" |  awk '{sum+=$2; count++} END {print sum/count}'`