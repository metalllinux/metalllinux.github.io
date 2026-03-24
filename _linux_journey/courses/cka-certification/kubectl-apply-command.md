---
title: "Kubectl Apply Command"
category: "cka-certification"
tags: ["cka-certification", "kubectl", "apply", "command"]
---

* `kubectl apply` is used to manage objects in a Declarative way.
* The `apply` command takes into account the local definition file and the live object definition in Kubernetes.
	* This is before making any configuration changes.
* Therefore when running the `apply` command, if the object does not already exist, the object is then created.
	* It firstly converts it into a `JSON` format.
	* This is stored as the `last applied configuration`.
* Then in Kubernetes, the same definition file is created, similarly with what was generated locally.
	* As mentioned previously, this one has additional fields to store the status of the object.
* For any updates, all three configurations (those being the `Local file`, `Last applied Configuration` and `Kubernetes Memory`) are then checked.
	* For example, the `nginx` image in the local file is updated to version `1.19` (it would look like `image: nginx:1.19`) and then the `kubectl apply -f nginx.yaml` command is ran, the value of `image` is compared with the value in the live Kubernetes configuration. If there are any differences, the live configuration is updated with the new value. The `Last Applied Configuration` is also updated as well.
* If a field such as `type: *"front-end-service"` is removed in the `Local File`, this then means it is removed from the Kubernetes memory as well. The `Last Applied Configuration` helps us to manage the changes.
* Where are the JSON files that have the `Last Applied Configuration`?
	* This is stored on the cluster itself. Under `metadata` --> `annotations`
* `kubectl apply` / `kubectl replace` commands do not store those values.
* Must bear in mind to not mix `Imperative` and `Declarative` approaches.