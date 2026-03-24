---
title: "Set IRQ Analysis on CentOS Kernel"
category: "rocky-linux"
tags: ["rocky-linux", "irq", "affinity", "analysis", "centos"]
---

# Set IRQ Analysis on CentOS Kernel

We confirmed irqbalance was no longer running and therefore not the cause for the set_irq_affinity failure
 set_irq_affinity successfully set the affinity for 87 / 128 em3 IRQs, and failed for 41 / 128 of them
 Ask them to run scripts/set_irq_affinity -X 1-7,64-71 em3 again and provide the output again

