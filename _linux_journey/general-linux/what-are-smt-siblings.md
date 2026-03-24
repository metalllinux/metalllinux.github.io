---
title: "What are SMT Siblings?"
category: "general-linux"
tags: ["are", "smt", "siblings"]
---

# What are SMT Siblings?

Great question — this dives into how **Simultaneous Multithreading (SMT)** works on modern CPUs and why **disabling both SMT siblings** is necessary when one core is faulty.

---

### 🧠 What Are SMT Siblings?

**Simultaneous Multithreading (SMT)** — known as **Hyper-Threading** on Intel CPUs — allows a single physical CPU core to appear as **two logical CPUs** to the operating system. These two logical CPUs are called **SMT siblings**.

For example:
- **CPU18** and **CPU38** are **SMT siblings**.
- They share the **same physical core**, but each has its own architectural state (registers, program counter, etc.).
- They share **execution units**, **L1/L2 caches**, and **other core-level resources**.

---

### 🧨 Why Disabling Only One SMT Sibling Isn’t Enough

If **CPU38** is faulty, and you only disable it:

- **CPU18** (its sibling) still runs on the **same physical core**.
- If the fault is in **shared hardware** (e.g., execution units, cache, or internal buses), **CPU18 will also be affected**.
- This can lead to **unpredictable behaviour**, kernel crashes, or silent data corruption.

---

### ✅ Why This Command Is Used

```bash
echo 0 > /sys/devices/system/cpu/cpu18/online
echo 0 > /sys/devices/system/cpu/cpu38/online
```

This disables **both logical CPUs** (CPU18 and CPU38), effectively taking the **entire physical core** offline.

- `echo 0` → disables the CPU
- `/sys/devices/system/cpu/cpuX/online` → sysfs interface to control CPU hotplugging

This ensures that **no part of the faulty core is used**, eliminating the risk of further corruption or crashes.

---

### 🧩 How to Identify SMT Siblings

You can find SMT sibling relationships with:

```bash
cat /sys/devices/system/cpu/cpu38/topology/thread_siblings_list
```

This might return something like:
```
18,38
```

Which confirms that CPU18 and CPU38 are SMT siblings — i.e., they share the same physical core.

---

### 🛠️ Summary

| Term            | Meaning                                                                 |
|-----------------|-------------------------------------------------------------------------|
| SMT Siblings    | Logical CPUs sharing the same physical core                             |
| CPU18 & CPU38   | SMT siblings — same physical core                                       |
| Why disable both? | Fault in shared hardware affects both siblings                        |
| Command effect  | Fully disables the faulty physical core                                 |

---
