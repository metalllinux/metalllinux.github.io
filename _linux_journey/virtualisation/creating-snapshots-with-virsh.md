---
title: "Creating Snapshots With Virsh"
category: "virtualisation"
tags: ["virtualisation", "creating", "snapshots", "virsh"]
---

Creating snapshot backup in KVM environment needs virsh command. Just type the command below,

virsh snapshot-create-as domain snapshot-name

Domain is the name of the KVM VM, and snapshot-name is the name you give to the snapshot.

To check the list of KVM VM snapshots, type the command below:

virsh snapshot-list domain

To restore VM from KVM VM snapshot, type the command below:

virsh snapshot-revert domain snapshot-name

To delete one KVM VM snapshot, type the command below:

virsh snapshot-delete domain snapshot-name