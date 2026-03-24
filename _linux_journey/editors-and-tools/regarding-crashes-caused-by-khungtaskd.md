---
title: "Regarding Crashes Caused By Khungtaskd"
category: "editors-and-tools"
tags: ["editors-and-tools", "regarding", "crashes", "caused", "khungtaskd"]
---

For hung_task_panic events, a careful review of the current state of the task is necessary as the panic
task will be the "khungtaskd" process and not the actual task that has been within Uninterruptible sleep
state for greater than 120 seconds.