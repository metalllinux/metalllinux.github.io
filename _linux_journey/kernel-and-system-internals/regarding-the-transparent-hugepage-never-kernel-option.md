---
title: "Regarding the transparent_hugepage Kernel Option"
category: "kernel-and-system-internals"
tags: ["kernel-and-system-internals", "regarding", "transparent", "hugepage", "never"]
---

# Regarding the transparent_hugepage Kernel Option
The kernel parameter `transparent_hugepage=never` is used to **disable Transparent Huge Pages (THP)** in Linux. Here's what that means and why you might want to use it:

---

### 🔧 `transparent_hugepage=never`

This tells the kernel to **never use Transparent Huge Pages**, regardless of memory access patterns or application behaviour.

---

### 🧠 What Are Transparent Huge Pages?

- Normally, Linux uses **4 KB pages** for memory management.
- THP allows the kernel to use **2 MB pages** (on x86_64) automatically, which can:
  - ✅ Reduce TLB (Translation Lookaside Buffer) misses.
  - ✅ Improve performance for memory-intensive workloads.
- But THP can also:
  - ❌ Introduce latency spikes due to page compaction or allocation.
  - ❌ Cause performance regressions in real-time or latency-sensitive applications.

---

### 🔍 Modes of THP

You can control THP with:

- `always`: Kernel tries to use THP whenever possible.
- `madvise`: Only uses THP when applications explicitly request it via `madvise()`.
- `never`: Disables THP entirely.

---

### ✅ Use Cases for `transparent_hugepage=never`

- **Real-time systems**: Avoids unpredictable latency from THP allocation/compaction.
- **Databases** (e.g., PostgreSQL, Oracle): Some DBs recommend disabling THP for stability.
- **Benchmarks or HPC**: When you want consistent memory behaviour.

---

### 🔍 How to Check Current THP Status

```bash
cat /sys/kernel/mm/transparent_hugepage/enabled
```

---

Here are two authoritative sources that explain the **latency and performance issues** associated with Transparent Huge Pages (THP):

1. **Latency spikes due to compaction and allocation**:
   - Red Hat explains that **direct memory compaction** during huge page allocation can cause **higher latencies**, especially during frequent page faults. Disabling direct compaction can help reduce this risk[2](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/7/html/performance_tuning_guide/sect-red_hat_enterprise_linux-performance_tuning_guide-configuring_transparent_huge_pages).

2. **Performance regressions in real-time or NUMA-sensitive workloads**:
   - Another Red Hat article documents that enabling THP caused **up to 10% performance degradation** on some NUMA nodes due to THP scanning and conversion. Disabling THP restored consistent performance across nodes[1](https://access.redhat.com/solutions/2728441).

Let me know if you'd like help disabling THP on your system or tuning it for specific workloads.

[2](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/7/html/performance_tuning_guide/sect-red_hat_enterprise_linux-performance_tuning_guide-configuring_transparent_huge_pages): [Red Hat Performance Tuning Guide – Transparent Huge Pages](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/7/html/performance_tuning_guide/sect-red_hat_enterprise_linux-performance_tuning_guide-configuring_transparent_huge_pages)  
[1](https://access.redhat.com/solutions/2728441): [Red Hat Knowledgebase – NUMA performance issues with THP](https://access.redhat.com/solutions/2728441)
