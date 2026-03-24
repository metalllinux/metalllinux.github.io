---
title: "Multiple Schedulers"
category: "cka-certification"
tags: ["cka-certification", "multiple", "schedulers"]
---

* The Default Scheduler has an algorithm that shares pods evenly across nodes.
	* Takes into consideration Taints and Tolerations, as well as Node Affinity.
* Can write your own Scheduler and can assign that to the cluster as well as the Default Scheduler (both are fine to have running at the same time). You can specify certain applications to you a particular scheduler.
* The default scheduler is named `default-scheduler`.
* The name is created using the following file:
```
scheduler-config.yaml
apiVersion: kubescheduler.config.k8s.io/v1
kind: KubeSchedulerConfiguration
profiles:
- schedulerName: default-scheduler
```
* For the other `scheduler` files, you set the name like so:
```
scheduler-config.yaml
apiVersion: kubescheduler.config.k8s.io/v1
kind: KubeSchedulerConfiguration
profiles:
- schedulerName: my-scheduler
```
* To deploy a scheduler, an example one is the `kube-scheduler` and then run it is a service:
```
wget https://storage.googleapis.com/kubernetes-release/release/v1.12.0/bin/linux/amd64/kube-scheduler
```
* Service file:
```
kube-scheduler.service
ExecStart=/usr/local/bin/kube-scheduler \\
   --config=/etc/kubernetes/config/kube-scheduler.yaml
```
* Each scheduler has its own configuration file and each file has its own name:
```
my-scheduler-2.service
ExecStart=/usr/local/bin/kube-scheduler \\
   --config=/etc/kubernetes/config/my-scheduler-2.yaml
```
* There are other options that can be passed in, such as the `kube config` option.
* The above is not necessarily how you deploy a scheduler, mostly the work is done by `kubeadm`.
* Can deploy a scheduler as a pod:
* Example custom scheduler yaml file:
```
my-custom-scheduler.yaml
apiVerson: v1
kind: Pod
metadata:
  name: my-custom-schedule
  namespace: kube-system
spec:
  containers:
  - command:
	 - kube-scheduler
	 - --address=127.0.0.1
	 - --kubeconfig=/etc/kubernetes/scheduler.conf
	 - --config=/etc/kubernetes/my-scheduler-config.yaml
	 image: k8s.gcr.io/kube-scheduler-amd64:v1.11.3
	 name: kube-scheduler
```
* Similarly the `my-scheduler-config.yaml` file:
```
apiVersion: kubescheduler.config.k8s.io/v1
kind: KubeSchedulerConfiguration
profiles:
- schedulerName: my-scheduler
leaderElection:
  leaderElect: true
  resourceNamespace: kube-system
  resourceName: lock-object-my-scheduler
```
* `leaderElect` option is used when you have different copies of the Scheduler running on different Master Nodes (a form of High Availability).
	* If multiple copies of the same scheduler are running on different Master Nodes, only one can be active at a time.
	* The `leaderElect` option thus helps to schedule a leader in these scenarios.
* How to deploy an additional scheduler as a deployment?
* [Useful Kubernetes Documentation on Schedulers](https://kubernetes.io/docs/tasks/extend-kubernetes/configure-multiple-schedulers/)
* View schedulers in the `kube-system` namespace with `kubectl get pods --namespace=kube-system`
* How do you configure a pod or deployment to use a new scheduler?
* Example pod definition file (the important part is the `schedulerName` part):
```
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - image: nginx
    name: nginx
  schedulerName: my-custom-scheduler
```
* Then `kubectl create -f pod-definition.yaml`
* If the Pod is in a `Pending` state, check the logs under the `kubectl describe` command.
* How do you which Scheduler picked up pod X?
* Use the `kubectl get events -o wide` command.
	* Lists all events in the current namespace and it shows the source of the event.
	* Can also view the logs of the scheduler like so: `kubectl logs my-custom-scheduler --name-space=kube-system`
		* Can add the pod name or the deployment name.