---
title: "How to Change the root Password and add a Public SSH Key to a QCOW2 Image and Flash That Image to an SSD"
category: "networking"
tags: ["networking", "change", "root", "password", "add"]
---

# How to Change the root Password and add a Public SSH Key to a QCOW2 Image and Flash That Image to an SSD

* Create the password hash:

```
openssl passwd -6 'MyNewPassword'
```

* Use `guestfish` to open the qcow2 image:

```
sudo guestfish --rw -a ./image.qcow2 -i
```

* Edit the `shadow` file:

```
edit /etc/shadow
```

* Find the `root` line and add in the hashed password like so:

```
root:$6$k1ZzD3M5$z2lFtIYwREEXAMPLEHASH/sCEzF/:19956:0::7:::
```

* For the public key, open the `authorized_keys` file. If you don't already have a public/private ssh key pair, generate it with `ssh-keygen -t rsa -b 4096`:

```
edit /root/.ssh/authorized_keys
```

* Add your public `ssh` key to the bottom of the file.

* `exit` from the image.

* Provide the following permissions on the local if needed:

```
chmod 700 /root/.ssh
chmod 600 /root/.ssh/authorized_keys
```

* Convert the `qcow2` image into `raw` format:

```
qemu-img convert -f qcow2 -O raw image.qcow2 image.raw
```

* When copying the image onto the USB stick, make sure the USB's filesystem is either XFS or EXT4. Create the partitions on the USB stick with `fdisk` and then `sudo mkfs.xfs /dev/<partition>` for the filesystem. Change the file permissions as well afterwards with `sudo chown myuser:myuser ./`

* Copy the `raw` image over to a USB stick and boot the target machine into the Rocky Linux recovery shell via a Ventoy USB (Rocky Linux 8.10 is a good choice).

* Flash the image and boot:

```
sudo dd if=image.raw of=/dev/sdX bs=4M status=progress conv=fsync
```
