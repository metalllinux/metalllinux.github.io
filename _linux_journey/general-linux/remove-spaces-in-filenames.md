---
title: "Remove Spaces In Filenames"
category: "general-linux"
tags: ["remove", "spaces", "filenames"]
---

for f in *\ *; do mv "$f" "${f// /_}"; done