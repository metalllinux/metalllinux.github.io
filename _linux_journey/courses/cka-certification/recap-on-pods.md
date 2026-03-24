---
title: "Recap On Pods"
category: "cka-certification"
tags: ["cka-certification", "recap", "pods"]
---

* Assumption that the application has already been built into a `docker` image.
	* The image is available in a repository such as `docker` hub.
* The Kubernetes Cluster is also assumed to be setup and working.
* All the services need to be in a running state.
* The ultimate aim is to deploy an application across a set of machines, configured as Worker Nodes in the cluster.
![5d0c8af3de1af0ab968498afdfcdbd9c.png](../../_resources/5d0c8af3de1af0ab968498afdfcdbd9c.png)
* The container is not deployed directly on the Worker Nodes.
* The containers are encapsulated into a Kubernetes Object as pods.
* A pod is a single instance of an application.
* A pod is the smallest object you can create in Kubernetes.
* Example of a single Node running one application in a single container:
![42d0658926e2f98525c86b6df5b24e76.png](../../_resources/42d0658926e2f98525c86b6df5b24e76.png)
* As the number of users increases, you need to scale your application to share the load.
![055cb4debae62790041203a843b8a4ca.png](../../_resources/055cb4debae62790041203a843b8a4ca.png)
* Where would we bring up additional instances.
	* For example, bringing up a container within the same pod?
	* No, we create a separate pod with a new instance of the application.
![2fcd1e0b1c55126f246be504ef81e196.png](../../_resources/2fcd1e0b1c55126f246be504ef81e196.png)
* What if the user base increases further and the node has no sufficient capacity.
* Can deploy additional pods on a new node in the cluster.
![727a61134c6e5ae2bc79ed3b7e2d4d9a.png](../../_resources/727a61134c6e5ae2bc79ed3b7e2d4d9a.png)
* Pods have a 1:1 relationship with containers on the same application.
* To scale up, you create new pods and to scale down, you delete existing pods.
* Don't add additional containers to an existing pod to scale the application.
* Regarding multi-container pods.
* We are not restricted to having 1 container in 1 pod.
	* A single pod can have multiple containers, just not of the same kind.
	* There are containers such as `Helper Containers` - for example performing a supporting task for the web application.
![5cb0864ff59e3aef380ca3c9dfe37c8c.png](../../_resources/5cb0864ff59e3aef380ca3c9dfe37c8c.png)
* When scaling the application, the helper container comes with it.
	* When the application container dies, the helper container also dies, due to them both being part of the same pod.
* Each container can communicate to each other directly, by referring to one another as localhost.
	* They can easily share the same network and storage space.
![a68fdc0b6ea7370df6feb502b6e85274.png](../../_resources/a68fdc0b6ea7370df6feb502b6e85274.png)
* Focusing on `docker` containers, for example we try to deploy our application on a `docker` host.
	* We deploy the application using a `docker run python-app` command.
		* The users can access the `python-app` without issue.
	* When the load increases, more instances of the application are loaded.
	* A helper container comes in to process and fetch data from elsewhere.
	* 1 helper container is required per application.
	* We need to maintain a map of which app and helper container is connected to each other.
		* Need to establish network connectivity between the containers, using links and custom networks.
		* Need to create shareable volumes and distribute these among the containers
		* Need to monitor the state of the application container and kill the helper container when the application container dies as well.
		* For a new container, a helper container would need to be deployed as well.
![897565568ae33af8c0c017902aa8a0eb.png](../../_resources/897565568ae33af8c0c017902aa8a0eb.png)
* With pods, Kubernetes does all of the above automatically.
	* We define what containers are included in X pod.
	* The containers in the pod will by default have access to the same storage, same network and same namespace.
	* These are created together and destroyed together.
		* Pods allow for architectural changes and scaling in the near future.
* Multi-container pods are rare to see in the wild.
* The course will stick to single containers per pod.
* What does `kubectl` do? It deploys a `docker` container by creating a pod.
* In the below example, Kubernetes deploys the `nginx` application image.
![c41d3b1060d2e993207987b5de17337e.png](../../_resources/c41d3b1060d2e993207987b5de17337e.png)
	* Using `kubectl`, you usually have to specify the image name.
* Where does `kubectl` get the image from? Use the `--image` flag.
![b77f6535b4edf199cbbc3e1a79db1e08.png](../../_resources/b77f6535b4edf199cbbc3e1a79db1e08.png)
* Docker Hub keeps of the latest images for images.
* Kubernetes can pull for a very bad situation. 
* How do we see the list of pods available - `kubectl` command.
* `get pods` output:
![084d187dfc2a337910283b7d0b3be17b.png](../../_resources/084d187dfc2a337910283b7d0b3be17b.png)
* Haven't talked about the concepts how a user can access the nginx web server. In this instance, the server has not been made available to exensive users.
![ccf97a0673c75813def17c2859ca2253.png](../../_resources/ccf97a0673c75813def17c2859ca2253.png)