---
title: "How Recursively Compress Png Images"
category: "general-linux"
tags: ["recursively", "compress", "png", "images"]
---

find . -type f -name '*.png' | xargs pngcrush -brute_force --extraneous

ls *.png | while read line; do pngcrush -brute $line compressed/$line; done

This is the best one:

find . -iname '*png' -exec pngcrush -ow -brute {} {}.crush \;