---
title: "Operator Framework"
category: "cka-certification"
tags: ["cka-certification", "operator", "framework"]
---

* Previously created a custom resource definition.
	* Have to deploy the Controller as a pod.
* Can package together both the Custom Resource Definition and Controller.
	* Deployed as a single entity and deployed using an Operator Framework.
* The Operator Framework deploys the Controller as a Deployment.
* The Operator Framework does more than just the above.
* Most popular Operators is the `etcd` Operator.
	* Deploys and manages an `etcd` cluster in Kubernetes.
* Has an `etcd` CRD and an `etcd` Controller.
	* This also includes an `etcd` Backup CRD and Backup Operator Custom Controller
* Then also `etcd` Restore as the CRD and the Restore Operator Custom Controller
* Kubernetes Operators do what a Human Operator typically does.
	* Installing, maintaining and taking backups.
* All Operators are available at [OperatorHub.io](https://operatorhub.io/)
	* Find lots of Operators such as Prometheus are available.