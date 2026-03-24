---
title: "How To Install Rocky Kernel Ml And Lt"
category: "rocky-linux"
tags: ["rocky-linux", "install", "rocky", "kernel"]
---

sudo dnf install -y https://publicpackages.build.ctrliq.cloud/ciq-public-release.rpm

sudo dnf install -y ciq

sudo ciq enroll --site-token b1b9287ca45892f2bdd401d135c72f27713a111df59f1035455c778163b45a74

sudo ciq enable --key kernels8

sudo dnf -y install rocky-kernel-ml # or -lt

Above token is for **INTERNAL USE ONLY**

