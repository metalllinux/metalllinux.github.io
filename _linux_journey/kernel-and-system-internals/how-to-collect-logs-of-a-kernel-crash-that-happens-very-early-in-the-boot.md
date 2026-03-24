---
title: "How to Collect Logs of a Kernel Crash that Happens Very Early in the Boot Process"
category: "kernel-and-system-internals"
tags: ["kernel-and-system-internals", "collect", "logs", "kernel", "crash"]
---

# How to Collect Logs of a Kernel Crash that Happens Very Early in the Boot Process

They can get a full log by enabling pstore on the machine, so the kernel log of the previous boot will be accessible when a panic happens.

Enable systemd's pstore service: sudo systemctl enable systemd-pstore.service

Add this to the kernel command line to enable pstore backed by EFI variable: efi_pstore.pstore_disable=0

Reboot the system, replicating the panic

Once the system boots back up successfully, dump out the kernel log of the previous boot with the following: sudo journalctl -b -1 -k -o short-monotonic --no-hostname > kernel-panic-log.txt

The resulting kernel-panic-log.txt file will contain the kernel panic messages from the previous boot, since they were backed up via pstore

Using pstore is how we get kernel panic logs from embedded systems, since you don't have the luxury of generating a coredump of an embedded system on the fly (like when your smartphone suffers a kernel panic).

* More information:

When the kernel panics during its init, there’s no chance for systemd to start recording the kernel log because userspace is not initialised yet; the init executable isn’t running at this point.

A convenient mechanism for capturing logs for such panics is the kernel Persistent Store (pstore) feature.

Pstore works by writing every kernel log message to some kind of storage that will persist after a machine reboots due to a kernel panic. Then, after the reboot finishes, the full kernel log from the previous boot including the kernel panic messages can be retrieved.

Pstore comes with a variety of storage type options for saving kernel logs. The easiest way to use pstore on a laptop or desktop is by using the EFI variable storage option; this stores kernel log messages into an EFI variable, which is physically backed by the NVRAM chip containing the UEFI bootloader of the machine (i.e., the BIOS). This chip is usually a few dozen megabytes in size at most.

Systemd comes with a pstore service that automatically retrieves pstore logs and appends them to the systemd journal for easy access via journalctl. The systemd pstore service also handles deleting the EFI variables created by pstore once the kernel logs are retrieved are retrieved from them. This is important since the BIOS NVRAM is quite small and free space on it is limited. The amount of EFI variable space that is free can be checked with df -h | grep efivarfs.

To enable pstore with the EFI variable backing:

    Enable systemd's pstore service: sudo systemctl enable systemd-pstore.service

    Add this to the kernel command line to enable pstore backed by EFI variable: efi_pstore.pstore_disable=0

    Reboot the system so the kernel now has pstore enabled

    Once a kernel panic occurs, wait for the system to finish rebooting after the panic

    Dump out the kernel log of the previous boot: sudo journalctl -b -1 -k -o short-monotonic --no-hostname > kernel-panic-log.txt

    The resulting kernel-panic-log.txt file will contain the kernel panic messages from the previous boot, since they were backed up via pstore

Note that pstore will only save kernel logs when a kernel panic or crash occurs. Pstore’s behaviour can be modified to always save kernel logs across a reboot, even a normal reboot, by adding this to the kernel command line: printk.always_kmsg_dump=1

Also, some mild caution should be exercised when making pstore always save logs to an EFI variable. The reason is because the BIOS NVRAM chip storing the EFI variables has a finite number of write cycles. Hence, printk.always_kmsg_dump=1 should not be carelessly left in the kernel command line after it’s no longer needed.
