---
title: "Bash Script To Go Through Each File In A Directory"
category: "general-linux"
tags: ["bash", "script", "through", "each", "file"]
---

```
for file in *; do
    echo "===== $file ====="
    cat "$file"
    echo
done
```