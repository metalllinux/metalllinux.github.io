---
title: "Deployments"
category: "cka-certification"
tags: ["cka-certification", "deployments"]
---

* When new versions become available on the Docker registry, you want to deploy that to all of your instances.
* Upgrading one instance after the other, is called `rolling updates`.
* Want to pause, make all necessary changes and then resume after that!
* A `Deployment` is a Kubernetes object that comes higher in the hierarchy.
![スクリーンショット 2024-11-12 15.18.22.png](../../_resources/スクリーンショット%202024-11-12%2015.18.22.png)
* We firstly create a deployment definition file.
* The contents is similar to the replicaset definition file.
	* The only difference is that `kind` would be set to `Deployment`.
* When the file is ready, run the `kubectl create -f definition-file-name.yaml` command.
* To see the newly created deployment, run the `kubectl get deployments` command.
* The deployment automatically creates a `replicaset`, thus this will be shown when running the `kubectl get replicaset` command.
* The replicasets then ultimately create the pods, which can be seen from the `kubectl get pods` command. It shows the name of the pod and the replicaset.
![スクリーンショット 2024-11-12 15.28.44.png](../../_resources/スクリーンショット%202024-11-12%2015.28.44.png)
* To see all objects at once, run the `kubectl get all` command.
![スクリーンショット 2024-11-12 15.32.11.png](../../_resources/スクリーンショット%202024-11-12%2015.32.11.png)


