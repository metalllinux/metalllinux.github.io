---
title: "Check If Sshd Is Running"
category: "general-linux"
tags: ["check", "sshd", "running"]
---

ps aux | grep sshd

netstat -plant | grep :22

telnet localhost 22

lsof -i