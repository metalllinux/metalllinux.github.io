---
title: "Services"
category: "cka-certification"
tags: ["cka-certification", "services"]
---

* Services interact with various components inside and outside of the application.
* Allows to connect other applications or users together.
	* For example, a bunch of pods where a frontend is serving loads to users, a second group for running backup processes and a third group connected to an external data source.
	* The `services` enable the connectivity between the groups of pods.
	* Allows the frontend application to be made available to end users and helps provide connections between the backend pods as well.
	* Also allows connection to data sources (like a storage source for files).
* Pods communicate with each other via internal networking.
	* For example, how do we as an external user access the webpage and to access the node at `192.168.1.2`. The pod network in a range of `10.244.0.0` and the pod itself is assigned `10.244.0.2`
		* To see the webpage, we `ssh` into the node on `192.168.1.2` and then run `curl 10.244.0.2` to access the webpage directly.
		* However, ideally we want to just access `192.168.1.2` and see the webpage information directly.
			* There needs to be something in the middle to map the node IP request to the container.
				* This is where the Kubernetes `service` is used. Its an object like a replicaset or deployment as an example.
					* In this case, the `service` listens for requests on a port of the node and forwards those requests to the pod running the application. This service is called a `NodePort` service. The service listens to a port on the node and forwards the request to the pods.
* Multiple Service Types are available:
	* `NodePort` - makes an internal pod accessible via a port on the node.
	* `ClusterIP` - Creates a virtual IP inside the cluster, to facilitate communication between different services such as a set of frontend servers to a set of backend servers.
	* `LoadBalancer` - provisions a load balancer for the application for supported cloud providers. An example is distributing load across servers.
* `NodePort` in more detail - back to the webpage pod, the port running on the pod is `80` - this is the `TargetPort`, as the `service` is forwarding the outside request to this port.
	* The second port is the port on the `service` - it is just known as `Port` - the `service` can be thought of as a virtual server inside the node. The service has is own IP address and this known as the `ClusterIP` of the `service`.
	* The third port is the port on the Node itself, which is just called `NodePort`. The example port that this is set to in this case is `30008`. `NodePorts` can only be in the range of `30000 - 32767`
* To create the `Service`, you need a `service-definition.yml` file. The file looks like so:
```
apiVersion: v1
kind: Service
metadata:
     name: myapp-service
# Most important part of the file is spec to differ the services.
spec:
     type: NodePort
	 ports:
 	  - targetPorts: 80
		# Port on the service object. The "port" field is mandatory. If you do not provide a nodePort, then one is automatically allocated. Can have multiple port mappings in one service.
        port: 80
        nodePort: 30008
      selector:
          app: myapp
		  type: front-end
```
* Nothing in the `definition` file that connects the service to the target port.
	* Can use `labels` and `selectors` for linking.
	* The pod was created with a label and that same label needs to be brought into the `service definition` file. Under the `selector:` , we need to provide the labels from the `pod definition file`, in the above example this is `app` and `type`.
		* Once performed, this links the `service` to the `pod`.
* Create the `service` using the `kubectl create -f service-definition.yaml`
* To see the service, run `kubectl get services`.
	* It will show `Name`, `TYPE`, `CLUSTER-IP`, `EXTERNAL-UP`, `PORT(S)` and `AGE`
* We can then use the port `300008` and the IP of the node to successfully access the container running in the node.
```
curl http://192.168.1.2:30008
```
* What do you do if you have multiple pods. In the above example we had `10.244.0.2`, but we also may have two other pods with `10.244.0.3` and `10.244.0.4` respectfully.
* All of the pods would have the same `labels`:
```
labels:
	app: myapp
```
* The same `label` of `app: myapp` is used when creating the service.
* When the `service` is then created, it finds three pods, because each pod would have the same `label`.
	* No additional configuration is required on the `service` or `pod` side. The algorithm used is `Randon` with `SessionAffinity` set to `Yes`.
		* Thus this allows the `service` to act as a `Load Balancer` and distribute the load across different pods.
* What happens if the pods are distributed across multiple nodes.
	* Kubernetes automatically creates a `service` that spans all nodes in the cluster. The `TargetPort` is set as the same node port in the whole cluster.
		* That means you can access the cluster using the IP of any node in the cluster and using the same port number. For example nodes with `192.168.1.2`, `192.168.1.3` and `192.168.1.4`, all would work if you run `curl 192.168.1.<number>:30008`
* When `pods` are removed or added, the `service` is automatically updated.
* Once created, you don't need to make any configuration changes.