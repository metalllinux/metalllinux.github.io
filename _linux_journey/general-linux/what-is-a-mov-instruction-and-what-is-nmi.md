---
title: "What is a MOV Instruction and What is NMI?"
category: "general-linux"
tags: ["mov", "instruction", "nmi"]
---

# What is a MOV Instruction and What is NMI?

You're dealing with a complex kernel crash scenario, and you're absolutely right to focus on the low-level details. Let's break down the two key concepts you asked about — **MOV** and **NMI** — in the context of your vmcore analysis.

---

### 🔧 What is `MOV` in This Context?

The `MOV` instruction is an **x86 assembly instruction** used to **copy data from one location to another**. It’s one of the most fundamental instructions in the x86 instruction set.

#### In your case:
- The `MOV` instruction is being used to **dereference a per-CPU variable address**.
- The address is first computed and stored in the `RAX` register.
- Then, a `MOV` instruction tries to read from that address (i.e., dereference it).
- But the address in `RAX` is **invalid or corrupted**, leading to a **General Protection Fault (#GP)**.

This is a classic symptom of **hardware failure** — the CPU is executing valid instructions, but the data it's working with is corrupted, likely due to internal CPU register or cache corruption.

---

### ⚠️ What is an `NMI`?

An **NMI (Non-Maskable Interrupt)** is a **high-priority interrupt** that **cannot be ignored or masked** by the CPU. It’s typically used for critical events like:
- Hardware failures
- Watchdog timers
- Debugging traps

#### In your case:
- After the initial `MOV`-induced general protection fault on **CPU38**, the CPU experienced **nested NMIs**.
- NMIs kept triggering recursively — possibly due to watchdogs or other critical error handlers trying to intervene.
- Eventually, the system hit the **NMI nesting limit** (15 levels deep), which is enforced by this line:
  ```c
  BUG_ON(in_nmi() == NMI_MASK);
  ```
- This caused a **BUG** (kernel panic), but due to how `BUG_ON()` is implemented on x86, CPU38 **escaped the double fault handler** and executed a `UD2` instruction (undefined instruction), which brought it back to the general protection fault handler.

This is **highly abnormal behaviour** and strongly suggests **CPU38 is malfunctioning at the hardware level** — it’s not just crashing, it’s behaving unpredictably even in fault handlers.

---

### 🧠 Summary of What Happened

1. **CPU38** tried to access a per-CPU variable.
2. The address was corrupted → **General Protection Fault**.
3. The CPU entered a cascade of **nested NMIs**.
4. It hit the **NMI nesting limit** and should have halted in the double fault handler.
5. Instead, due to a quirk in `BUG_ON()` implementation, it **escaped** and continued running.
6. While running in this corrupted state, it likely **corrupted kernel memory**, leading to faults on other CPUs later.

---

### ✅ Final Diagnosis

- **MOV**: Triggered the fault by dereferencing a bad address.
- **NMI**: System tried to handle the fault but spiraled into nested interrupts.
- **CPU38**: Almost certainly suffering from **hardware degradation** — possibly due to age, heat, or manufacturing defects.

---
