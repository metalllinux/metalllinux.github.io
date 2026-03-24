---
title: "Useful Cut Command To Show Everything From A Point"
category: "general-linux"
tags: ["useful", "cut", "command", "show", "everything"]
---

cut -d ' ' -f15-

$ cut -d' ' -f5- file
This is line one
This is line two 
This is line three 
This is line four
This says: on space-separated fields, print from the 5th up to the end of the line.

If you happen to have multiple spaces in between fields, you may initially want to squeeze them with tr -s' '.