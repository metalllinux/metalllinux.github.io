---
title: "How to Make a VM Startup Automatically in vm-manager"
category: "virtualisation"
tags: ["virtualisation", "make", "startup", "automatically", "virt"]
---

# How to Make a VM Startup Automatically in vm-manager

Using the Virtual Machine Manager (GUI):

    Open virt-manager and select your virtual machine.

    Click on View → Details (or just open the VM’s details).

    Go to the Boot Options tab.

    Check the option labeled "Start virtual machine on host boot up" and apply the changes. This tells libvirt to mark the VM for autostart so that the next time your host boots, the VM is automatically started.

