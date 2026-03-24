---
title: "Solution Kubeconfig"
category: "cka-certification"
tags: ["cka-certification", "solution", "kubeconfig"]
---

* `dev-user` wants to access `test-cluster-1`, set the current context.
* To use a specific context, run:
```
kubectl config --kubeconfig=/root/my-kube-config use-context research
```
* Find out the current context:
```
kubectl config --kubeconfig=/root/my-kube-config current-context
```
* How to set a custom KubeConfig file as the default one? In this example we want to overerite `~/.kube/config` with `my-kube-config`.
* Open `bashrc`:
```
vim ~/.bashrc
```
* Export the variable with this line:
```
export KUBECONFIG=/root/my-kube-config
```
* Then `source` `~/.bashrc`:
```
source ~/.bashrc
```

* With a specific cluster's context set to `research`, there are problems when accessing the cluster.
* Running `kubectl get pods` shows the following:
```
controlplane ~ ➜  kubectl get pods
error: unable to read client-cert /etc/kubernetes/pki/users/dev-user/developer-user.crt for dev-user due to open /etc/kubernetes/pki/users/dev-user/developer-user.crt: no such file or directory
```
* Check the contents of `~/.kube/config`
* Check the `/etc/kubernetes/pki/users/dev-user/developer-user.crt`
* Edit the `~/.kube/config` file
* Then commands such as `kubectl get nodes` will work.

* How to find the home directory:
```
echo $HOME
```
* How to change to a specific context:
```
kubectl config use-context research --kubeconfig /root/my-kube-config
```
* To set a custom KubeConfig file as the Default Config, overwrite the default file with:
```
mv <custom_config_file> ~/.kube/config
```
* Check the configuration with `kubectl config view`