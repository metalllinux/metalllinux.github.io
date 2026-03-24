---
title: "How Recursively Replace Spaces With Underscores In"
category: "general-linux"
tags: ["recursively", "replace", "spaces", "underscores"]
---

Directories:
find . -name "* *" -type d | rename 's/ /_/g'

Files:
find . -name "* *" -type f | rename 's/ /_/g'