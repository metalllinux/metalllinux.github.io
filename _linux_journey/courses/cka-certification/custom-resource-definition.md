---
title: "Custom Resource Definition"
category: "cka-certification"
tags: ["cka-certification", "custom", "resource", "definition"]
---

* When creating a cluster, such as this deployment:
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name; myapp-deployment
spec:
  template:
	 metadata:
      name: myapp-pod
	  labels:
      type: front-end
	 spec:
       containers:
	   - image: nginx
  replicas: 3
  selector:
	 matchLabels:
		 type: front-end
```
* Then create the deployment:
```
kubectl create -f deployment.yaml
```
* Once ran, the above is stored in the ETCD store.
* Delete the deployment with `kubectl delete -f <deployment_name>`
* When a Deployment is made, it creates replicas that are equal to what is available in the deployment yaml file.
* Deployment Controller is already part of the cluster.
	* Process that runs in the background - continues to monitor resources that it needs to manage.
* Deployment Controller is written in Go.
* Resources available are the following:
	* ReplicaSet
	* Deployment
	* Job
	* CronJob
	* Statefulset
	* Namespace
* Controllers that help with those.
	* ReplicaSet
	* Deployment
	* Job
	* CronJob
	* Statefulset
	* Namespace
An example of a `Resource` paired with a `Controller`:
* Flight Ticket:
```
apiVersion: flights.com/v1
kind: FlightTicket
metadata:
  name: my-flight-ticket
spec:
  from: Mumbai
  to: London
  number: 2
```
* Create the flight ticket:
```
kubectl create -f flightticket.yaml
```
* Want the above to book a flight ticket.
	* For example an API that can be called at `book-flight.com/api`
	* How do we call this API, we need a Controller?
* The Custom Controller is written in `Go` and watch for any changes and monitoring the `ETCD-server` as well.
* Will make API call to book and delete the flight tickets.
* There is a Custom Resource and a Custom Controller.
* Can't create a resource without configuring it in the Kubernetes API.
* Have to define the resource first.
	* Need a Custom Resource Definition.
	* Example of that:
```
flightticket-custom-definition.yml

apiVersion: apiextensions
kind: CustomResourceDefinition
metadata:
  name: flighttickets.flights.com
spec:
  scope: Namespaced
  group: flights.com
  names:
	kind: FlightTicket
	singular: flightticket
	plural: flighttickets
	shortnames:
	  - ft
   versions:
	- name: v1
	  served: true
	  storage: true
   schema:
	 openAPIV3Schema:
		type: object
	    properties:
		  spec:
			type: object
			propertie:
			  from:
				type: string
			  to:
				type: string
			  number:
				type: integer
				minimum: 1
				maximum: 10
```
* Pods, replicas etc are `Scoped` objects.
* Persistent volumes, Nodes etc are non-`Scoped` objects.
* `group` - API group that is provided in the API version.
* `singular` - the name that shows up when you run `kubectl api-resources`
* `plural` - used by the Kubernetes API resource - this is also what shows up in the `plural` format.
* `shortnames` - can refer to the resource as a shorter name, for example running `kubectl get ft`
* `versions` - each resource can be given multiple versions as it passes through the various stages of its lifecycle.
	* If it is a new resource, can start at Alpha or Beta versions.
	* If you have multiple versions, only 1 version can be marked as the `storage` version.
* `schema` - defines all of the parameters under the `spec` section.
	* Defines which fields are supported and what type of value the field supports etc.
* Can specify the minimum and maximum value under the `from:`, `to:` and `number:` columns.
	* If the values do not fit within the `minimum` and `maximum` ranges, the user can't create anything.
 * Create the Custom Definition:
```
kubectl create -f flightticket-custom-definition.yml
```
* Once the above is done, you can then create, check the status and delete the flight ticket:
```
kubectl create -f flighticket.yml
kubectl get flighticket
kubectl delete -f flightticket.yml
```
* Without a Controller, the Resource will just sit there in the ETCD Data Store.
* 