---
title: "What Does the nvidia-smi Command Do?"
category: "desktop-and-distributions"
tags: ["desktop-and-distributions", "nvidia", "smi", "command"]
---

# What Does the nvidia-smi Command Do?

`nvidia-smi -q` is a command-line tool that provides **detailed diagnostics and status information** for NVIDIA GPUs installed on a Linux system.

### ✅ What It Does

It **queries and displays extensive GPU information**, including:

* **Driver version**
* **CUDA version**
* **GPU name and UUID**
* **Temperature**
* **Fan speed**
* **Memory usage**
* **ECC errors**
* **Power usage**
* **Clock speeds**
* **Running processes using the GPU**

---

### ✅ Usage Example

```bash
nvidia-smi -q
```

Output: A **long, verbose report** covering the health and status of each GPU in the system.

If you want it to be more readable, pipe it through `less`:

```bash
nvidia-smi -q | less
```

---

### ✅ Real-World Use Cases

* Troubleshooting GPU overheating or underclocking
* Monitoring ECC memory errors on data centre GPUs
* Checking if a process is hogging GPU memory
* Validating that driver and CUDA versions are correct
