---
title: "What Is Sig Cloud Next"
category: "general-linux"
tags: ["sig", "cloud", "next"]
---


Overview
What is CIQ SIG/Cloud Next?¶
CIQ SIG/Cloud Next has two primary purposes:

https://docs.ciq.com/scn/

To allow rapid iteration for SIG/Cloud development, providing an opportunity to try out new ideas that may or may not be feasible in Rocky SIG/Cloud
To host proprietary packages that can't be included in Rocky SIG/Cloud because of licensing issues
It is split into two parts. The first is CIQ SIG/Cloud Next, with open source software that adds features to Rocky Linux, and the second is CIQ SIG/Cloud Next - Nonfree for rpms that don't have a corresponding srpm. This could be propriety code to enable operation of certain hardware like the NVIDIA userspace. The Nonfree repo depends on the open repository, while the open repository can be used completely on its own (though some packages may not be particularly useful without the Nonfree repo).

What is CIQ SIG/Cloud Next not?¶
CIQ SIG/Cloud Next is not a replacement for Rocky SIG/Cloud. Every change in the Free section of CIQ SIG/Cloud Next should either have a corresponding pull request in Rocky SIG/Cloud or be reverted.

Background¶
Rocky SIG/Cloud was setup to provide packages and images that maximise the usefulness of Rocky Linux in private and public clouds. Unfortunately, this sometimes requires proprietary drivers, especially to drive AI workloads, and for very obvious security reasons, there are limits to what SIG contributors can upload without approval.

CIQ SIG/Cloud Next - Nonfree is the obvious choice to host these proprietary drivers, and CIQ SIG/Cloud Next allows CIQ employees to build quickly, while retaining the security guarantees offered by SecureBoot. When a concept is proven out, PRs will be created in Rocky SIG/Cloud to include the latest changes.

How to install¶
Rocky 10¶
To install CIQ SIG/Cloud Next, simply run:

sudo dnf install https://depot.ciq.com/public/download/ciq-sigcloud-next-10/ciq-sigcloud-next-10.x86_64/Packages/c/ciq-sigcloud-next-release-7-1.el10_0cld_next.noarch.rpm
To install both CIQ SIG/Cloud Next and CIQ SIG/Cloud Next - Nonfree, simply run:

sudo dnf install https://depot.ciq.com/public/download/ciq-sigcloud-next-10/ciq-sigcloud-next-10.x86_64/Packages/c/ciq-sigcloud-next-release-7-1.el10_0cld_next.noarch.rpm \
    https://depot.ciq.com/public/download/ciq-sigcloud-next-10/ciq-sigcloud-next-10-nonfree.x86_64/Packages/c/ciq-sigcloud-next-nonfree-release-4-1.el10_0cld_next.noarch.rpm
Rocky 9¶
To install CIQ SIG/Cloud Next, simply run:

sudo dnf install https://depot.ciq.com/public/download/ciq-sigcloud-next-9/ciq-sigcloud-next-9.x86_64/Packages/c/ciq-sigcloud-next-release-6-1.el9_5.cld_next.noarch.rpm
To install both CIQ SIG/Cloud Next and CIQ SIG/Cloud Next - Nonfree, simply run:

sudo dnf install https://depot.ciq.com/public/download/ciq-sigcloud-next-9/ciq-sigcloud-next-9.x86_64/Packages/c/ciq-sigcloud-next-release-6-1.el9_5.cld_next.noarch.rpm \
    https://depot.ciq.com/public/download/ciq-sigcloud-next-9/ciq-sigcloud-next-9-nonfree.x86_64/Packages/c/ciq-sigcloud-next-nonfree-release-3-1.el9_5.cld_next.noarch.rpm
Rocky 8¶
To install CIQ SIG/Cloud Next, simply run:

sudo dnf install https://depot.ciq.com/public/download/ciq-sigcloud-next-8/ciq-sigcloud-next-8.x86_64/Packages/c/ciq-sigcloud-next-release-6-1.el8_10.cld_next.noarch.rpm
To install both CIQ SIG/Cloud Next and CIQ SIG/Cloud Next - Nonfree, simply run:

sudo dnf install https://depot.ciq.com/public/download/ciq-sigcloud-next-8/ciq-sigcloud-next-8.x86_64/Packages/c/ciq-sigcloud-next-release-6-1.el8_10.cld_next.noarch.rpm \
    https://depot.ciq.com/public/download/ciq-sigcloud-next-8/ciq-sigcloud-next-8-nonfree.x86_64/Packages/c/ciq-sigcloud-next-nonfree-release-3-1.el8_10.cld_next.noarch.rpm
NVIDIA drivers¶
To install the NVIDIA Datacenter GPU drivers, after installing both SIG/Cloud Next repos, simply run:

sudo dnf install nvidia-dc-driver-latest kmod-nvidia-dc-open-latest
To stay on a major version of the driver (in this example, 580), run

sudo dnf install nvidia-dc-driver580 kmod-nvidia-dc-open580 --allowerasing
This will switch you to the 580 major version, and you will not be updated to another major version

Mellanox drivers¶
To actually make use of the NVIDIA Mellanox DOCA drivers, you'll need to enable the upstream DOCA repo. To do so, after installing both SIG/Cloud Next repos, simply run:

sudo dnf install doca-repo
You can then install the DOCA packages (including the kernel modules built for Rocky Linux) by running:

sudo dnf install doca-ofed
 Back to top
Copyright © 2025 CIQ, Inc.
Made with Material for MkDocs
