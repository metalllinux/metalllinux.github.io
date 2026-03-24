---
title: "Services Cluster Ip"
category: "cka-certification"
tags: ["cka-certification", "services", "cluster"]
---

* A typical fullstack application has the following, `front-end`, `back-end` and a key-value store such as `redis`.
* The `front-end` servers need to communicate to the `back-end` servers and the `back-end` servers thus need to connect to the key-value store.
* All of the `pods` have IP addresses assigned to them.
	* The IPs are not `static` for the `pods`.
		* These IP addresses cannot be relied upon, due to `pods` going down or new pods coming up etc.
		* For example, a `front-end` `pod` with an IP of `10.244.0.3` needs to connect to one of the `back-end` `pods` , which would it connect to?
			* A Kubernetes `service` can help group these `pods` together and help to access the services as a group.
				* For example, a `service` can group all of the `back-end` pods together and create a single service to group all of the `back-end` `pods` together.
					* Any requests to the `back-end` `pods` would be assigned to a pod at random.
						* A similar `service` could be used to group the `redis` pods together in a similar way.
* Each `service` is given a name and IP.
* To create a `ClusterIP` `service`, here is an example definition file:
```
apiVersion: v1
kind: Service
metadata:
    name: back-end

spec:
     type: ClusterIP
     ports:
      - targetPort: 80
		port: 80

     selector:
        app: myapp
        type: back-end
```
* `ClusterIP` is the default `type`, so even if you do not specify `ClusterIP` under `spec`, that will be the default chosen anyway.
* The `app` and `type` fields are copied from the `pod` definition file.
* The service is then created with `kubectl create -f <service>.yaml`.
* Check the service with `kubectl get services`