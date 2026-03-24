---
title: "Custom Controllers"
category: "cka-certification"
tags: ["cka-certification", "custom", "controllers"]
---

* Follows on from the flighttickets.
* A Controller is a any process or loop that continually monitors the ETCD cluster and listens for events of any objects being changed - for example the flight ticket object.
* Can write a Custom Controller in Python - can watch for changes or calls to the Flightticket API
* Developing in Go allows for the use of the Kubernetes Go client - shared informers.
* https://github.com/kubernetes/sample-controller
* To create a sample controller:
	* Set up `GoLang`
	* Clone the Sample Controller.
	* Change into the `sample-controller` directory.
	* Customise the Controller with your own logic.
		* For example add code to poll flight booking API to book the tickets.
	* Then build the program with `go build -o sample-controller .`
	* `./sample-controller -kubeconfig=$HOME/.kube/config`
* How to distribute the Controller? Can package the Controller inside a Docker image and run the Controller inside the `pod`.
* Maybe questions in the exam to build custom resource definition files.