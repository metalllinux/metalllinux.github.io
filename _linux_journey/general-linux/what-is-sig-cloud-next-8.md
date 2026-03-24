---
title: "What is SIG-Cloud-Next-8?"
category: "general-linux"
tags: ["sig", "cloud", "next"]
---

# What is SIG-Cloud-Next-8?

SIG-Cloud-Next-8 isn’t a Linux kernel signal — it actually refers to a branch in **Rocky Linux’s “SIG Cloud Next” project**, specifically targeting Rocky Linux 8. Here’s a breakdown:

---

### 🏗️ What is SIG-Cloud-Next-8?

* **Rocky Linux “SIG Cloud Next”** is a community-backed initiative (part of the Special Interest Group infrastructure) aimed at building and maintaining cloud-optimised container images for Rocky Linux.
* Projects under this SIG include branch images like `el8.cloudnext`, which are automatically built, tagged, and tested for deployment in cloud environments. The “Next” series often includes newer package versions or build optimizations ahead of the main `.cloud` stream ([github.com][1], [peridot.build.resf.org][2]).

---

### 📋 Where did the name come from?

Rocky Linux uses scripts like `sig-cloud-instance-images` to generate container and VM images. When they produce a new “cloud-next” build for major release 8 (e.g., `el8.cloudnext`), that image family is informally called **SIG‑Cloud‑Next‑8** ([github.com][1]).

These images are tagged with the major version (“8”) and built regularly, often ahead of the stable stream, enabling testing or use of newer components in cloud environments.

---

### ✅ What does it mean for you?

* If you're running Rocky Linux 8–and want the latest cloud-optimised images with newer packages or features before they hit the stable `.cloud` release–this is the branch aimed at you.
* It's fully compatible with Rocky Linux 8, just built from the "next" pipeline in the SIG image project.

---

**In short:** **SIG‑Cloud‑Next‑8** = Rocky Linux 8 “cloud-next” images from the SIG Cloud images project—cutting-edge builds of VM/container images optimised for cloud deployments.

---

Let me know if you’d like help pulling or using one of the `el8.cloudnext` images!

[1]: https://github.com/rocky-linux/sig-cloud-instance-images?utm_source=chatgpt.com "rocky-linux/sig-cloud-instance-images - GitHub"
[2]: https://peridot.build.resf.org/?utm_source=chatgpt.com "Peridot Build"


