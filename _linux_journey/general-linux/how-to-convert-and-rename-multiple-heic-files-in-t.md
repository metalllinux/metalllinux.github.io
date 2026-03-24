---
title: "How To Convert And Rename Multiple Heic Files In T"
category: "general-linux"
tags: ["convert", "rename", "multiple", "heic", "files"]
---

for file in ./2023*/*.HEIC; do     heif-convert "$file" "${file%.heic}.png"; done && rename 's/\.HEIC.png/\.png/' ./*/*.HEIC.png && rm ./*/*HEIC*