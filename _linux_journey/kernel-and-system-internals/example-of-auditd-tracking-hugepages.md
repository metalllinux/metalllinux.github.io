---
title: "Add audit rule to track modifications to HugePages settings"
category: "kernel-and-system-internals"
tags: ["kernel-and-system-internals", "example", "auditd", "tracking", "hugepages"]
---

# Add audit rule to track modifications to HugePages settings
echo "-w /proc/sys/vm/nr_hugepages -p wa -k hugepages" >> /etc/audit/rules.d/hugepages.rules
echo "-w /proc/sys/vm/nr_overcommit_hugepages -p wa -k hugepages" >> /etc/audit/rules.d/hugepages.rules

# Reload audit rules
auditctl -R /etc/audit/rules.d/hugepages.rules

# Verify the rule is active
auditctl -l | grep hugepages

# Check the logs:
ausearch -k hugepages --start today