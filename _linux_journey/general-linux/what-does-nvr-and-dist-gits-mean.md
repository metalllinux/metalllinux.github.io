---
title: "🔧 Original Statement:"
category: "general-linux"
tags: ["nvr", "dist", "gits", "mean"]
---

### 🔧 Original Statement:
> "Basically I made some changes to our dist-gits so I could programmatically determine what the NVR should be when we do a release and can tag the kernel at the same time. The earlier ones you can see that they're not quite as consistent."

---

### 🧠 Explanation:

#### 1. **"dist-gits"**
This refers to **distribution Git repositories**—typically used in Linux distributions like Fedora, CentOS, or RHEL. These repos contain the packaging metadata (like spec files, patches, and build scripts) for building software packages, including the kernel.

#### 2. **"programmatically determine what the NVR should be"**
- **NVR** stands for **Name-Version-Release**.
- It's a standard naming convention in RPM-based distributions (like Fedora/RHEL) to uniquely identify a package.
  - Example: `kernel-5.14.0-123.el9`
    - `Name`: `kernel`
    - `Version`: `5.14.0`
    - `Release`: `123.el9`

The speaker is saying they automated the process of generating this NVR string, likely based on Git tags, commit history, or changelogs.

#### 3. **"when we do a release and can tag the kernel at the same time"**
- They’ve synchronised the **release process** with **Git tagging**.
- This means that when a new kernel version is released, a Git tag is created at the same time, and the NVR is automatically calculated and applied.

#### 4. **"the earlier ones you can see that they're not quite as consistent"**
- Before this automation, the NVRs or tags might have been manually created or inconsistently named.
- This could lead to confusion, mismatches, or difficulty tracking which kernel version corresponds to which release.

---

### ✅ Summary:
The person improved the kernel packaging workflow by modifying the distribution Git repositories to **automatically generate consistent NVRs** and **tag the kernel source** during releases. This replaces a previously inconsistent, possibly manual process.

---

Would you like a visual diagram of how this process works, or maybe a sample script that could automate NVR generation from Git tags?