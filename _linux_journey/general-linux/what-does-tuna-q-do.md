---
title: "What Does tuna -Q do?"
category: "general-linux"
tags: ["tuna"]
---

# What Does tuna -Q do?

The `tuna -Q` command is used to **query** the current system configuration and tuning profiles in the `tuna` tool.

`tuna` is a Linux performance tuning tool that helps optimise system performance by adjusting various kernel parameters, CPU affinity, and other system settings. The `-Q` or `--query` option allows you to:

- **Display current tuning profiles** that are active on the system
- **Show which CPUs are isolated** or assigned to specific tasks
- **List current kernel thread assignments** and their CPU affinities
- **View active tuning parameters** and their current values

For example, running `tuna -Q` might show you:
- Which CPUs are dedicated to specific processes
- Current interrupt routing configurations  
- Active real-time scheduling policies
- Memory and scheduling optimizations that are currently applied

This is particularly useful for system administrators working with real-time systems, high-performance computing environments, or when troubleshooting performance issues where you need to understand the current tuning state before making changes.

The query function helps you see what tuning is already in place before applying new performance optimizations with other `tuna` commands.


