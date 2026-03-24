---
title: "Replicasets"
category: "cka-certification"
tags: ["cka-certification", "replicasets"]
---

* Controllers are the brain behind Kubernetes.
* Replication Controller is the focus here.
* What is a replica and why do we need a replication controller?
	* What if an application crashes and the pod fails?
	* The users are then no longer able to access the application.
	* We need more than one instance of a pod running at the same time.
* The Replication Controller helps us run multiple instances of a pod in a Kubernetes cluster. This provides High Availability.
![b173dfbb4ecc78c0cdecc8e79ae1a8ad.png](../../_resources/b173dfbb4ecc78c0cdecc8e79ae1a8ad.png)
* A Replication Controller is useful even for a single pod, as it can bring up a new pod if the existing one fails.
![607b15e506d772f7aa6dac3537cbb249.png](../../_resources/607b15e506d772f7aa6dac3537cbb249.png)
* The Replication Controller ensures the specified number of pods are running at all times.
* Another use of the Replication Controller is Load Balancing and Scaling.
	* If a number of issues increases, we can increase the pod count to balance the load.
![fbef2435be6037979b4aba58e5755cf1.png](../../_resources/fbef2435be6037979b4aba58e5755cf1.png)
* If demand continues to increase and the resources of the first node are exhausted, can then deploy to another node in the cluster.
![fda7103ae1a9b85fa25b8cb77c65c140.png](../../_resources/fda7103ae1a9b85fa25b8cb77c65c140.png)
* There are two similar terms: `Replication Controller` and `Replica Set`
* `Replication Controller` is the older technology, that is being replaced by `Replica Set`. What was discussed previously is applicable to both of those technologies.
* How to create a `Replication Controller`
	* Create a `Replication Controller` definition file.
	* 4 sections:
		* apiVersion: v1 - Replication Controllers are supported in v1.
		* kind: ReplicationController
		* metadata: myapp-rc
		* labels: 
				* app: myapp
				* type: front-end
		* spec:
				* template: 
* For any Kubernetes Definition File, the `spec:` defines what is inside the object.
* The `Replication Controller` creates multiple instances of a pod.
* The `template:` section is used to create replicas.
* How do we define the `pod` `template:`?
	* Can reuse the contents of a `pod` definition file in the `template` section.
	* Can move all of the lines, aside from `apiVersion` and `kind`.
![0f04ccd06007ff7beea6d71be6575dc0.png](../../_resources/0f04ccd06007ff7beea6d71be6575dc0.png)
![c6dd37e54679d5a193fac4394cbc275e.png](../../_resources/c6dd37e54679d5a193fac4394cbc275e.png)
* The `Replication Controller` is the parent in the file and the `Pod Definition` being the child.
* We need to mention how many replicas are required in the `Replication Controller`.
* Add the property called `replicas:` to the file.
* `template:` and `replicas:` are children of the `spec` section.
![7d004d8d437474f0134d02ec000c2b4d.png](../../_resources/7d004d8d437474f0134d02ec000c2b4d.png)
* Once complete, run `kubectl create -f rc-definition.yaml`. It then creates the `Replication Controller`.
* To view the `Replication Controllers`, run the `kubectl get replicationcontroller` 
![d7a352ff40e310882d0fd034b7f86815.png](../../_resources/d7a352ff40e310882d0fd034b7f86815.png)
* Will observe the amount of replicas in the output.
* Then to check the pods that were created by the `Replication Controller`, run the `kubectl get pods` command.
![7ecce3c063cdcf65f91e07ac5294f3db.png](../../_resources/7ecce3c063cdcf65f91e07ac5294f3db.png)
* All of the pods will start with the name of the `Replication Controller`
* To view the created `Replication Controllers`, run `kubectl get replicationcontroller`
![b15a2ddc3b217250be188108f9320031.png](../../_resources/b15a2ddc3b217250be188108f9320031.png)
* Now we look at `replicaset`.
* Very similar to the `replicationcontroller`.
* We have `apiVersion`, `kind`, `metadata`and `spec`
* `apiversion` however is set to `app/v1`
* If you input that incorrectly, you will likely receive an error that looks like this:
![9f582b148069efd376b793d59485fdb5.png](../../_resources/9f582b148069efd376b793d59485fdb5.png)
* `kind` is `ReplicaSet`
* Add `name` and `labels` in the `metadata` section.
* `spec` is the same as `ReplicationController`
* The main difference is that `ReplicaSet` requires a `selector` definition.
* The `selector` part helps the `ReplicaSet` identify which pods fall under it.
* Why do you need to specify the pods that are underneath it though?
	* A `ReplicaSet` can also manage pods, which were not part of the `ReplicaSet` creation.
		* For example, pods created before the `ReplicaSet`, which matched labels.
			* The `ReplicaSet` will also take those pods into consideration, when creating the replicas.
* The `selector` is one of the major differences between `ReplicationController` and `ReplicaSet`.
* The `selector` is not a required field for the `ReplicationController`.
	* When skipped, the `ReplicationController` assumes it is the same as the labels provided in the `pod` definition file.
* In the case of `ReplicaSet`, a user input is required for this property.
	* That is done using `matchLabels`
	* `matchLabels` specifies everything under it, to the labels on the pods.
* The `ReplicaSet` also provides other options for matching labels, that are not available in the `ReplicationController`.
* To create a `ReplicaSet`, run the `kubectl create` command, providing the `ReplicaSet` as input.
![b5897efe45f06489f7a6c34bfd89537a.png](../../_resources/b5897efe45f06489f7a6c34bfd89537a.png)
* To view the created replicas, run the `kubectl get replicaset` command.
![2918621c7233599b3b28f24dd8ba8a99.png](../../_resources/2918621c7233599b3b28f24dd8ba8a99.png)
* Of course for pods, run `kubectl get pods`
![82c4e3f38a5252e1cf8fb76ee37caf85.png](../../_resources/82c4e3f38a5252e1cf8fb76ee37caf85.png)
* Regarding `Labels` and `Selectors` - why do we label objectes in Kubernetes?
* For example, the front-end web app is deployed as 3 pods.
* If they are not created, the replicaset will create them for you.
* The role of the replicaset is that if any of the pods fail, it creates new ones.
	* The replicaset is a process that monitors the pods.
* How does the replicaset know which pods to monitor.
	* Labelling the pods during creation is necessary.
	* The labels provided are a filter for the replicaset.
![Screenshot from 2024-10-30 20-43-05.png](../../_resources/Screenshot%20from%202024-10-30%2020-43-05.png)
* The same concept of labels and connectors is used throughout Kubernetes.
* In the `replicaset-definition.yml`, there are 3 sections there.
![Screenshot from 2024-10-30 20-46-31.png](../../_resources/Screenshot%20from%202024-10-30%2020-46-31.png)
* In the above example, need to create a Replicaset to ensure the 3 pods are up at all times.
* When a new ReplicaSet instance is created, it is not going to automatically create a new POD pod, because there are already 3 available.
	* In that case, we always need a `template` section, in case a pod fails in the future.
* How to Scale a ReplicaSet - going from 3 --> 6 as an example.
![Screenshot from 2024-10-31 17-27-25.png](../../_resources/Screenshot%20from%202024-10-31%2017-27-25.png)
* To do this, update the number of replicas in the definition file to `6`
![Screenshot from 2024-10-31 17-28-16.png](../../_resources/Screenshot%20from%202024-10-31%2017-28-16.png)
* Then use `kubectl replace` to update the replica set.
```
kubectl replace -f replicaset-definition.yml
```
![Screenshot from 2024-10-31 17-29-38.png](../../_resources/Screenshot%20from%202024-10-31%2017-29-38.png)
* A second way to perform the same task, is via the `kubectl scale` command and provide the number of replicas to scale to.
```
kubectl scale --replicas=6 -f replicaset-definition.yml
```
* Can either put the definition file or the replicaset name in the `Type` / `Name` format.
![Screenshot from 2024-10-31 17-35-52.png](../../_resources/Screenshot%20from%202024-10-31%2017-35-52.png)
* Using the filename as input, will not automatically update all replicas in the file. The `replicaset-definition.yml` will still be 3.
* There are options to scale the replicas based on load as well.
* `kubectl create -f replicaset-definition.yml` creates the replicaset.
* `kubectl get replicaset` to show the replicasets created.
* `kubectl delete replicaset myapp-replicaset` will get rid of all of the replicasets. It also deletes all of the underlying pods as well.
* `kubectl replace -f replicaset-definition.yml` to increase the amount of replicas via modifying the file.
* `kubectl scale -replicas=6 -f replicaset-definition.yml` will scale the replicas, without modifying the yml file.