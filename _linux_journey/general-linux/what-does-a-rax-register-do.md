---
title: "What Does a RAX Register Do?"
category: "general-linux"
tags: ["rax", "register"]
---

# What Does a RAX Register Do?

In an **x86_64 CPU architecture**, the `RAX` register is one of the **general-purpose registers**. Here's what it does:

### 🔹 What is `RAX`?
- `RAX` stands for **Register A Extended**.
- It is the **64-bit extension** of the `EAX` register, which itself is the 32-bit version of the original `AX` register from the 16-bit x86 architecture.

### 🔹 Primary Uses of `RAX`
1. **Accumulator Register**:
   - Traditionally used for arithmetic operations like multiplication and division.
   - For example, in `MUL` or `DIV` instructions, `RAX` is often implicitly used.

2. **Function Return Values**:
   - In the **System V AMD64 ABI** (used by Linux and many Unix-like systems), `RAX` is used to store the **return value** of a function.

3. **System Calls**:
   - In Linux, when making a **system call**, the system call number is placed in `RAX`.

### 🔹 Register Breakdown
- `RAX` (64-bit)
- `EAX` (lower 32 bits of RAX)
- `AX` (lower 16 bits of EAX)
- `AH` and `AL` (high and low 8 bits of AX)

This layered access allows for flexible manipulation of data sizes.
