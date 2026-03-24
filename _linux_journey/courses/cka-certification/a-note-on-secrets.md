---
title: "A Note On Secrets"
category: "cka-certification"
tags: ["cka-certification", "note", "secrets"]
---

* A `secret` is only sent to a node if a pod on the node requires it.
* The `kubelet` stores the `secret` in a `tmpfs`, therefore the `secret` is not written to storage.
* When the Pod that depends on the `secret` is deleted, the `kubelet` also deletes its local copy of the `secret` as well.
* Another good tool for handling `secrets` is `Helm Secrets` or `HashiCorp Vault`.