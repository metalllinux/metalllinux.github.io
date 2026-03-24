---
title: "If You Want To Grep For A List Of Values Via A Fil"
category: "editors-and-tools"
tags: ["editors-and-tools", "you", "want", "grep", "list"]
---

Use:
```
grep -F <list.txt> <file.txt>
```
For the `list.txt` file, should also remove empty lines with `sed -i '/^$/d'`  and remove any whitespace at the beginning of each string with `awk '{$1=$1;print}'`