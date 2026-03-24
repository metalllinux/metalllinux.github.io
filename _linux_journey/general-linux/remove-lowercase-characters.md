---
title: "Remove Lowercase Characters"
category: "general-linux"
tags: ["remove", "lowercase", "characters"]
---

for i in $( ls | grep [A-Z] ); do mv -i $i `echo $i | tr 'A-Z' 'a-z'`; done