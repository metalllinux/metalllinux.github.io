---
title: "How to Spread a SoftIRQ Load Across Multiple CPUs"
category: "kernel-and-system-internals"
tags: ["kernel-and-system-internals", "spread", "softirq", "load", "across"]
---

# How to Spread a SoftIRQ Load Across Multiple CPUs

And customer is asking if removing their isolcpus configuration will spread out softirq load to more CPUs, when I told them in the 9/26 meeting that the only way to spread softirq load is by spreading the IRQs to more CPUs.
