---
title: "Separate Fields Using Awk With =F"
category: "editors-and-tools"
tags: ["editors-and-tools", "separate", "fields", "awk"]
---

We’ll use that file and the -F (separator string) option to tell awk to use the colon (:) as the separator. We type the following to tell awk to print the name of the user account and the home folder:

awk -F: '{print $1,$6}' /etc/passwd