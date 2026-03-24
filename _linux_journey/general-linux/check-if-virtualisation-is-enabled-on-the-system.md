---
title: "Check If Virtualisation Is Enabled On The System"
category: "general-linux"
tags: ["check", "virtualisation", "enabled", "system"]
---

egrep -c '(vmx|svm)' /proc/cpuinfo

grep -E --colour '(vmx|svm)' /proc/cpuinfo