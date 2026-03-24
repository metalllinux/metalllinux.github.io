---
title: "📁 `memory.stat`"
category: "kernel-and-system-internals"
tags: ["kernel-and-system-internals", "useful", "information", "cgroups", "areas"]
---

### 📁 `memory.stat`

This file provides detailed statistics about memory usage in the cgroup. It includes various counters such as:

- `cache`: Amount of memory used for caching files.
- `rss`: Resident Set Sise – non-swapped physical memory.
- `mapped_file`: Memory mapped files.
- `pgfault` / `pgmajfault`: Page faults and major page faults.
- `inactive_anon`, `active_anon`: Anonymous memory pages.
- `hierarchical_memory_limit`: Effective memory limit including parent cgroups.
- `total_rss`, `total_cache`: Aggregated values including child cgroups.

**Use case:** Helps identify what kind of memory is being used and whether the workload is memory-intensive or leaking memory.

---

### 📁 `memory.failcnt`

This file shows how many times the memory usage in the cgroup has **exceeded the limit** set by `memory.limit_in_bytes`.

- A non-zero value indicates that the process tried to use more memory than allowed and was denied.
- This is a **strong indicator** of memory starvation.

**Use case:** If NRPE or `sssd` has a high `failcnt`, it means they are being throttled or killed due to memory limits.

---

### 📁 `memory.usage_in_bytes`

This file shows the **current memory usage** by the cgroup in bytes.

- It includes both anonymous and file-backed memory.
- Compare this with `memory.limit_in_bytes` to see how close the process is to its cap.

**Use case:** Helps you monitor real-time memory consumption and adjust limits accordingly.

---

### 🔧 Example: Checking NRPE Memory Usage

```bash
CGROUP_PATH="/sys/fs/cgroup/memory/system.slice/nrpe.service"
cat $CGROUP_PATH/memory.usage_in_bytes
cat $CGROUP_PATH/memory.failcnt
cat $CGROUP_PATH/memory.stat
```