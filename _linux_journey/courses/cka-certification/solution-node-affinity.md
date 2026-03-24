---
title: "Solution Node Affinity"
category: "cka-certification"
tags: ["cka-certification", "solution", "node", "affinity"]
---

* How to count the amount of labels on a node:
```
kubectl describe node <node_name>
```
* What is the value set to a particular label?
	* Again checking via the `kubectl describe` command.
* How to apply a label to a node:
```
kubectl label node node01 color=blue
```
* How to create a new deployment called blue and 3 replicas:
```
kubectl create deployment blue --image=nginx --replicas=3
```
* How to check for taints:
```
kubectl describe node <node_name> | grep Taints
```
* Therefore the pods can be scheduled on the node if there are no Taints.
* How set Node Affinity to place pods on particular deployment:
```
kubectl edit deployment blue
```
Check under the pod specification:
```
spec:
   containers:
   - images: nginx
	 imagePullPolicy: Always
     name: nginx
	 resources: ()
	 terminationMessagePath: /dev/termination-log
     terminationMessagePolicy: File
    dnsPolicy: ClusterFirst
    restartPolicy: Always
    schedulerName: default-scheduler
    securityContext: ()
    terminationGracePeriodSeconds: 30
```
Then we add the Affinity Spec:
```
spec:
  affinity:
    nodeAffinity:
requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: color
            operator: In
            values:
            - blue
   containers:
   - images: nginx
	 imagePullPolicy: Always
     name: nginx
	 resources: ()
	 terminationMessagePath: /dev/termination-log
     terminationMessagePolicy: File
    dnsPolicy: ClusterFirst
    restartPolicy: Always
    schedulerName: default-scheduler
    securityContext: ()
    terminationGracePeriodSeconds: 30
```
* Save the file and the pod should then be edited.
* Find out which nodes pods are placed on:
```
kubectl get pod -o wide
```
* Create a new deployment called `red` and apply it to the `controlplane` node only. First we need the `yaml` file.
```
kubectl create deployment red --image=nginx --replicas=2 --dry-run=client -o yaml > <yaml_file_name>
```
Edit the file so it looks like this:
```
spec:
   affinity:
    nodeAffinity:
requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: node-role.kubernetes.io/master
            operator: Exists
            values:
            - blue
   containers:
   - images: nginx
	 imagePullPolicy: Always
     name: nginx
	 resources: ()
status()
```
* Then create the deployment with `kubectl create -f red.yaml`
