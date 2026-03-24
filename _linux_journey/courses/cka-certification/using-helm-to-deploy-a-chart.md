---
title: "Using Helm to Deploy a Chart Solution"
category: "cka-certification"
tags: ["cka-certification", "helm", "deploy", "chart"]
---

# Using Helm to Deploy a Chart Solution

* You can install the same `helm` chart multiple times on the same cluster.

* `helm search hub wordpress` is used to find `wordpress` charts.

* A good command to search for the `consul` package:

```
helm search hub consul
```

* How to add the `binami` `helm` chart repository to the Control Plane node:
```
helm repo add bitnami https://charts.bitnami.com/bitnami
```

* Then to search through the repository, run this command:
```
helm search repo wordpress
```

* To find how many `helm` charts there, use the `helm repo list` command.

* To deploy an `apache` application on the cluster, run this command:
```
helm install amaze-surf bitnami/apache
```

* To find the version of `apache` deployed, run the following:
```
helm list
```
* Check the `APP VERSION` of the release.

* To find the amount of releases there are of a particular application, run `helm list`

* Uninstall an application with `helm uninstall <release>`

* An example of removing the `hashicorp` repository:
```
helm repo remove hashicorp
```
