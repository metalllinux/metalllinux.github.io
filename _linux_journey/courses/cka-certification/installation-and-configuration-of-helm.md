---
title: "Installation and Configuration of Helm"
category: "cka-certification"
tags: ["cka-certification", "installation", "configuration", "helm"]
---

# Installation and Configuration of Helm

* Need a functional Kubernetes cluster and `kubectl` installed and available on your local machine.

* Helm can be installed on Linux, MacOS and Windows.

* Systems with `snap` can install Helm with:
```
sudo snap install helm
```

* Use the `--classic` option to provide a more relaxed sandbox and provide more access to the host system.

    * With using the `--classic` option, it allows Helm to access the kube config in the home directory.
    
* For Debian / Ubuntu, run the following commands to install Helm:
```
curl https://baltocdn.com/helm/signing.asc | sudo apt-key add -
sudo apt-get install apt-transport-https --yes
echo "deb https://baltocdn.com/helm/stable/debian/ all main" | sudo tee /etc/apt/sources.list.d/helm-stable-debian.li
sudo apt-get update
sudo apt-get install helm
```

* For `package` systems, use:
```
pkg install helm
```
