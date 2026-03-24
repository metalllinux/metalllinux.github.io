---
title: "What is MOFED?"
category: "general-linux"
tags: ["mofed"]
---

# What is MOFED?

MOFED stands for **Mellanox OpenFabrics Enterprise Distribution**. It's a software package provided by Mellanox Technologies (now part of NVIDIA) that includes drivers, libraries, and tools for their high-performance networking hardware, particularly InfiniBand and Ethernet network adapters.

## Key Components

MOFED includes:
- **Device drivers** for Mellanox network adapters (ConnectX series, BlueField DPUs, etc.)
- **Kernel modules** for InfiniBand and RoCE (RDMA over Converged Ethernet)
- **User-space libraries** like libibverbs for RDMA programming
- **Diagnostic and performance tools** for network troubleshooting and optimisation
- **MPI implementations** optimised for Mellanox hardware

## Purpose and Use Cases

MOFED is primarily used in:
- **High-Performance Computing (HPC)** clusters where low latency and high bandwidth are critical
- **Data centres** requiring RDMA capabilities for storage and compute acceleration
- **AI/ML workloads** that benefit from GPUDirect and high-speed interconnects
- **Cloud environments** needing SR-IOV and virtualisation support

## Installation and Management

On Linux systems, MOFED can be installed as a complete package that replaces the inbox drivers with Mellanox's optimised versions. It supports major Linux distributions including RHEL, Ubuntu, SLES, and others. The installation typically involves downloading the MOFED package for your specific OS version and running the installation script, which handles driver compilation and configuration.

The package is particularly important for enabling advanced features like RDMA, which allows direct memory access between servers without involving the CPU, significantly reducing latency and CPU overhead in distributed computing environments.

