---
title: "How Show Values Over A Particular Percentage"
category: "general-linux"
tags: ["show", "values", "over", "particular", "percentage"]
---

`cat sa21-02.sar-A.20240827101311.out | awk '0+$3 >= 80 {print}'`