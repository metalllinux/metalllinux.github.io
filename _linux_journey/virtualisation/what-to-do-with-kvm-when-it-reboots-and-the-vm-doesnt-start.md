---
title: "What to Do with KVM When it Reboots and the VM doesnt Start"
category: "virtualisation"
tags: ["virtualisation", "kvm", "when", "reboots", "doesnt"]
---

# What to Do with KVM When it Reboots and the VM doesnt Start

virsh shutdown <domain> --mode agent
virsh start <domain>

