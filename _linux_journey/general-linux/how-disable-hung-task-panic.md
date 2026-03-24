---
title: "How Disable Hung Task Panic"
category: "general-linux"
tags: ["disable", "hung", "task", "panic"]
---

```
echo 0 > /proc/sys/kernel/hung_task_timeout_secs
```