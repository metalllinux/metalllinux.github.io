---
title: "Configuring Grub"
category: "advanced-linux-kernel"
tags: ["advanced-linux-kernel", "configuring", "grub"]
---

* Some configurations for the Kernel can only be made at `boot` time.
* The bootloader is what passes the options to the Kernel when it is booted.
* GRUB2 is just called `GRUB` nowadays, in case people talk generally about `GRUB`.
* GRUB1 had a config file `grub.conf` and you edited that to add, remove or modify Kernel boot choices.
* For GRUB2 however:
* `/etc/default/grub`
	* Useful documentation to read, that is referenced in the file: `info -f grub -n 'Simple configuration'
* There is also `/etc/grub.d`
	* You would usually edit `40_custom`
	* Files in this directory can start with a number.
	* GRUB goes through each of these files in order, to provide a menu of choices on what you can boot.
	* You can affect the order that items are listed, by placing a number in front of the file.
	* You can have multiple Kernels to boot from or boot the same Kernel with different options.
* If you make changes, you generate the config file with: `grub2-mkconfig`
* GRUB Interactivity:
	* Can interrupt GRUB.
	* When editing in GRUB Interactive, you are not changing the file on the disk, just temporarily editing the GRUB configuration.
	* Can continue to boot with the changes with `'b'` or `Ctrl-x`