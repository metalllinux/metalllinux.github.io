---
title: "My Find Commands"
category: "editors-and-tools"
tags: ["editors-and-tools", "find", "commands"]
---

Find a certain file type between certain dates and move the files to  directory afterwards.

find /path/to/source_directory -type f -newermt "2023-04-01" ! -newermt "2023-05-01" -name "pattern*" -exec mv {} /path/to/destination_directory \;