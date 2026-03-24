---
title: "How to Output the virt-install Logs and Terminal Output to a File"
category: "virtualisation"
tags: ["virtualisation", "output", "virt", "install", "logs"]
---

# How to Output the virt-install Logs and Terminal Output to a File

virt-install \
    --name livenetroot_test  \
    --memory 4096 \
    --vcpus 2 \
    --disk none \
    --os-variant centos-stream10 \
    --network bridge=virbr0,model=virtio \
    --graphics none \
    --console pty,target_type=serial \
    --boot kernel=$HOME/images/images/pxeboot/vmlinuz,initrd=$HOME/images/images/pxeboot/initrd.img,kernel_args="root=live:http://192.168.1.127/install.img ip=dhcp rd.debug rd.live.debug console=ttyS0,115200n8" \
    --transient \
    --destroy-on-exit \
--> This is the important part:    2>&1 | tee virt-install.log


