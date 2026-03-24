---
title: "Useful Command To Check For Timeouts"
category: "general-linux"
tags: ["useful", "command", "check", "timeouts"]
---

grep -i timeout <var/log/messages> | egrep -i 'dial|exceeded' | wc -l 