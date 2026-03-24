---
title: "To Append Text To A File"
category: "general-linux"
tags: ["append", "text", "file"]
---

echo "TEST" | tee -a /<file>
If there is no existing file, the `tee` command will automatically create one.