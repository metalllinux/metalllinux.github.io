---
title: "How Show Values In A File Higher Than A Certain Th"
category: "general-linux"
tags: ["show", "values", "file", "higher", "than"]
---

`threshold=<value_you_want_to_see_higher>`
`cat sa21-* | awk -v threshold="$threshold" '$3 > threshold'`
