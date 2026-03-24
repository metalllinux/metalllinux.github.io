---
title: "My Awk Commands"
category: "editors-and-tools"
tags: ["editors-and-tools", "awk", "commands"]
---

awk '/FAILED/ {print $0}'

Looks for all failed messages in a file.

grep "<text>" <file> | awk '{print $4,$5,$7,$9,$11,$14,$15,$16,$17,$18,$19}'