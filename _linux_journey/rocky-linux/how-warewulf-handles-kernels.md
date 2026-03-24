---
title: "How Warewulf Handles Kernels"
category: "rocky-linux"
tags: ["rocky-linux", "warewulf", "handles", "kernels"]
---

# How Warewulf Handles Kernels

Kernel Location
Warewulf does not require kernels to be present in /boot. As of Warewulf v4.6, the kernel discovery process checks two locations within the image:
/boot/vmlinuz-*
/lib/modules/<version>/vmlinuz
Many images, including several of the Pro images, store the kernel in /lib/modules/ rather than /boot. This is by design and fully supported. The official documentation at https://warewulf.org/docs/main/images/kernel.html shows examples of images with kernels only in /lib/modules/ that boot successfully.
 
The /boot Directory is Excluded by Default
Additionally, the /boot directory is listed in /etc/warewulf/excludes by default in the images. This means the contents of /boot are intentionally not transferred to nodes during provisioning. Warewulf extracts the kernel separately and serves it via PXE - the kernel never comes from /boot being copied to the node. So even if /boot appears empty or incomplete in the image, this has no bearing on whether the image will boot.
 
To verify what kernels Warewulf has detected in your imported images, please run:
wwctl image kernels
 
This will show all available kernels across all images, their paths, versions, and which is set as default. For example, here's the output from my testing of the OpenPBS image:
wwctl image kernels
IMAGE     KERNEL                                             VERSION          DEFAULT  NODES
-----     ------                                             -------          -------  -----
openpbs1  /lib/modules/5.14.0-570.39.1.el9_6.x86_64/vmlinuz  5.14.0-570.39.1  true     5
As you can see, the kernel is located in /lib/modules/ and Warewulf detects it correctly.
 
You can also verify the image information with:
wwctl image list -l
IMAGE NAME  NODES  KERNEL VERSION   CREATION TIME        MODIFICATION TIME    SIZE
----------  -----  --------------   -------------        -----------------    ----
openpbs1    5      5.14.0-570.39.1  05 Dec 25 13:25 UTC  05 Dec 25 13:08 UTC  1.4 GiB
 
Regarding the "Kernel Mismatch"
When you ran uname -r inside the image (via wwctl image shell or similar), the output reflects the kernel of the Warewulf server host, not the kernel that will be used when nodes boot from this image. This is expected behaviour when working inside a chroot/container environment. The actual kernel that Warewulf provisions to nodes is determined by wwctl image kernels output and any --kernelversion settings on your nodes or profiles.
 
Recommended Next Steps
Run wwctl image kernels and share the output so we can confirm Warewulf is detecting the kernels correctly.
Run wwctl image list -l to verify the kernel version is populated for your images.
If the kernel version column is empty or the image appears stale, try forcing a rebuild of the image: wwctl image build <image_name> --force
Verify your node/profile configuration with wwctl node list -a <nodename> to confirm the image and kernel settings.
If kernel panics persist after the above steps, please share the exact panic message from the console. This will help identify where the issue may lie.


