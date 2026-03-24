---
title: "🔍 What `dis -l` Does in `crash`"
category: "kernel-and-system-internals"
tags: ["kernel-and-system-internals", "dis"]
---

```bash
dis -l
```

is used to **disassemble kernel code** and **include source line information** if available.

---

### 🔍 What `dis -l` Does in `crash`

- `dis` stands for **disassemble**.
- The `-l` option tells `crash` to **include source code line numbers** in the disassembly output, assuming the kernel was compiled with debugging symbols (like `-g`).

---

### ✅ Example Usage

```bash
crash> dis -l do_fork
```

This would:
- Disassemble the `do_fork` function.
- Show the corresponding **source code line numbers** alongside the assembly instructions.

---

### 🧠 Useful Notes
- This is helpful for **correlating assembly instructions with source code**, especially when debugging crashes or analyzing performance.
- If the kernel was not compiled with debug info, the `-l` option may not show line numbers.