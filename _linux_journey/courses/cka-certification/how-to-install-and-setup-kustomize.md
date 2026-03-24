---
title: "How to Install and Setup Kustomize"
category: "cka-certification"
tags: ["cka-certification", "install", "setup", "kustomize"]
---

# How to Install and Setup Kustomise

* Need a Kubernetes cluster running first and `kubectl` installed on the machine to talk to the cluster.

* Can be installed on Linux, MacOS and Windows. Kustomise team has generated a nice script that installs `kustomize`.

* Run this command which downloads the script:
```
curl -s "https://raw.githubusercontent.com/kubernetes-sigs/kustomize/master/hack/install_kustomize.sh" | bash
```

* Verify that Kustomise was installed correctly using the following command:
```
kustomize version --short
```

* Any issues, just close and open the current terminal session.
