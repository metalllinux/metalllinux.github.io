---
title: "How To Convert Heic Files With Libheif"
category: "general-linux"
tags: ["convert", "heic", "files", "libheif"]
---

heif-convert input.heic output.jpg

How to convert multiple files at once:

for file in *.heic; do
    heif-convert "$file" "${file%.HEIC}.png"
done