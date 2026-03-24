---
title: "Batch Convert Video With Ffmpeg"
category: "general-linux"
tags: ["batch", "convert", "video", "ffmpeg"]
---

for i in *.MOV; do ffmpeg -crf 29 -i "$i" "${i%.*}.mkv"; done

* Recursively with:
for i in ./*/*.MOV; do ffmpeg -crf 29 -i "$i" "${i%.*}.mkv"; done