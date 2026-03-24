---
title: "When Analysis Proc Stat"
category: "general-linux"
tags: ["when", "analysis", "proc", "stat"]
---

```
     no. of jiffies in user mode  user mode with low priority  system mode   idle task  I/O wait  IRQ(hardiq)  softirq
cpu  868478                       1153                         515105        177461535  9590      74852        11380       0 0 0
```

cpu — Measures the number of jiffies (1/100 of a second for x86 systems) that the system has been in user mode, user mode with low priority (nice), system mode, idle task, I/O wait, IRQ (hardirq), and softirq respectively. The IRQ (hardirq) is the direct response to a hardware event. The IRQ takes minimal work for queuing the "heavy" work up for the softirq to execute. The softirq runs at a lower priority than the IRQ and therefore may be interrupted more frequently. The total for all CPUs is given at the top, while each individual CPU is listed below with its own statistics. The following example is a 4-way Intel Pentium Xeon configuration with multi-threading enabled, therefore showing four physical processors and four virtual processors totaling eight processors. 