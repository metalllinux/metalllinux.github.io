---
title: "How to Copy Files into a VM with libvirt, if the VM is using NAT?"
category: "virtualisation"
tags: ["virtualisation", "copy", "files", "into", "libvirt"]
---

# How to Copy Files into a VM with libvirt, if the VM is using NAT?

# Make sure the VM is shut down first
sudo virsh shutdown <vm-name>

# Copy the file
sudo virt-copy-in -a /var/lib/libvirt/images/<vm-disk>.qcow2 /path/to/tarball.tar.gz /destination/path/

# Start the VM again
sudo virsh start <vm-name>

# To copy out files:

# Make sure the VM is shut down first
sudo virsh shutdown <vm-name>

# Copy the file out
sudo virt-copy-out -a /var/lib/libvirt/images/<vm-disk>.qcow2 /path/in/vm/file.txt /local/destination/directory/

# Start the VM again
sudo virsh start <vm-name>
Important notes about virt-copy-out:

The last argument must be a directory on your local system (not a filename)
You can copy multiple files at once by listing them before the destination directory
To copy entire directories, use the -R (recursive) flag
