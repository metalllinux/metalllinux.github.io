---
title: "Deploy kubeadm and Provision VMs with Vagrant"
category: "cka-certification"
tags: ["cka-certification", "deploy", "kubeadm", "provision", "vms"]
---

# Deploy kubeadm and Provision VMs with Vagrant

* Vagrant - automation tool to spin up multiple VMs with a specific configuration.

* A Vagrant File has all of the configurations required for the VMs.

* Clone this repository https://github.com/kodekloudhub/certified-kubernetes-administrator-course and it will contain the Vagrant File.

* Use `vagrant status` to check the current status if Kubernetes has been deployed to the nodes or not.

* `vagrant up` then provisions all of the VMs with whatever is in the Vagrant File.

* How do you connect to the cluster? Run `vagrant ssh <NODE_NAME>`. Find the name from `vagrant status`.

* To exit the session, run the command `logout`.
