---
title: "My For Loops 1"
category: "general-linux"
tags: ["loops"]
---

for i in {1..8}; do grep <text> <file>; done
for i in *.tar; do tar -xvf "$i"; done
for i in *.tar; do rm "$i"; done