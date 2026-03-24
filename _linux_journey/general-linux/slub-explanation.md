---
title: "🔧 Purpose of SLUB"
category: "general-linux"
tags: ["slub", "explanation"]
---

The **SLUB allocator** (the **S**lab allocator **U**nqueued **B**uffer) is a memory management subsystem in the Linux kernel, designed to efficiently allocate and deallocate memory for small objects. It is one of several slab allocators in Linux, alongside SLAB and SLOB, and is the default allocator in many modern Linux distributions due to its simplicity and performance.

### 🔧 Purpose of SLUB
SLUB is optimised for:
- **Low fragmentation**
- **High performance**
- **Scalability on multi-core systems**

It is particularly well-suited for allocating memory for kernel objects like inodes, task structures, and file descriptors.

---

### 🧱 Key Concepts

#### 1. **Slab Allocation**
- Memory is divided into **caches**, each designed for objects of a specific size.
- Each cache contains one or more **slabs**, which are contiguous memory blocks divided into equal-sised **objects**.
- When an object is needed, the allocator returns a free object from a slab.

#### 2. **SLUB vs SLAB**
| Feature        | SLUB                          | SLAB                          |
|----------------|-------------------------------|-------------------------------|
| Queues         | No per-CPU queues             | Uses per-CPU queues           |
| Complexity     | Simpler design                | More complex                  |
| Performance    | Better on large systems       | Can be better on small systems|
| Debugging      | Better support (e.g., KASAN)  | Limited                       |

#### 3. **Per-CPU Caches**
- SLUB uses **per-CPU partial slab lists** to reduce contention and improve performance on SMP (Symmetric Multi-Processing) systems.

#### 4. **Object Tracking and Debugging**
- SLUB supports **debugging features** like red-zoning, poisoning, and object tracking, which help detect memory corruption and leaks.

---

### ⚙️ How It Works

1. **Initialisation**: When the kernel boots, SLUB initializes caches for frequently used object sizes.
2. **Allocation**: When a kernel component requests memory, SLUB finds a suitable cache and returns a free object.
3. **Deallocation**: When the object is freed, it is returned to the slab for reuse.
4. **Slab Reclamation**: If slabs are no longer needed, they can be returned to the system.

---

### 🔍 Debugging with SLUB
You can enable SLUB debugging with kernel boot parameters like:
```bash
slub_debug=FZP
```
Where:
- `F` = Free object checking
- `Z` = Red zoning
- `P` = Poisoning

---

Would you like a diagram to visualise how SLUB works, or maybe a comparison with other allocators like SLOB or SLAB in more detail?