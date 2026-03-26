---
title: "How To Change Username Of A User"
category: "general-linux"
tags: ["change", "username", "user"]
---

sudo usermod -l myuser -d /home/myuser -m howrd

The username at the end is the one that you want to change.

You may have to do this via `root`, as the user cannot be in use at the time of changing.