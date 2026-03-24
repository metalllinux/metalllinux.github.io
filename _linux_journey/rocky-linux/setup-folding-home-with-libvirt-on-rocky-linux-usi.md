---
title: "Setup Folding@Home With Libvirt On Rocky Linux Usi"
category: "rocky-linux"
tags: ["rocky-linux", "setup", "foldinghome", "libvirt", "rocky"]
---

* Set up libvirt.
* Create a directory for your virtual machine images.
```
mkdir vms
```
* Create an iso directory.
```
mkdir isos
cd isos
```
* Download the Ubuntu 22.04 ISO.
```
wget https://releases.ubuntu.com/22.04/ubuntu-22.04.5-live-server-amd64.iso
```
* Create a mount point and mount the image.
```
cd ..
mkdir mnt
sudo mount -o loop ~/isos/ubuntu-22.04.5-live-server-amd64.iso mnt
```
* Copy the `vmlinuz` and `initrd` files to the `isos` directory, else otherwise the `virt-install` command will fail due to a permissions error.
```
cp ~/mnt/casper/vmlinuz ~/isos/
cp ~/mnt/casper/initrd ~/isos/
```
* Install Ubuntu using `virt-install`.
```
virt-install --name ubuntu22.04 --ram=4096 --vcpus=3 --cpu host --hvm --disk path=~/vms/ubuntu22-04.qcow2,size=15 --cdrom ~/isos/ubuntu-22.04.5-live-server-amd64.iso --graphics none --console pty,target_type=serial --os-variant ubuntu22.04 --network bridge=virbr0,model=virtio --hvm --force --debug --boot kernel=/home/howard/isos/vmlinuz,initrd=/home/howard/isos/initrd,kernel_args="console=ttyS0"
```
* Detach with `ctrl + ]`
* Stop the VM
```
virsh destroy --domain ubuntu22.04
```
* Remove boot options from the VM.
```
virsh edit ubuntu22.04
# Remove these options.
<kernel>/home/howard/isos/vmlinuz</kernel><initrd>/home/howard/isos/initrd</initrd>
<cmdline>console=ttyS0</cmdline>
```
* Unmount the ISO.
```
sudo umount ~/mnt
```
* Remove the `vmlinuz` and `initrd` files.
```
rm ~/isos/vmlinuz
rm ~/isos/initrd
```
* Start the VM.
```
virsh start ubuntu22.04
```
* Connect to the VM.
```
virsh console ubuntu22.04
```
* Update the VM.
```
sudo apt update -y && sudo apt upgrade -y
```