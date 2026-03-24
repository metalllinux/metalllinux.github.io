---
title: "Configuring Scheduler Profiles"
category: "cka-certification"
tags: ["cka-certification", "configuring", "scheduler", "profiles"]
---

* Example pod definition file:
```
apiVersion: v1
kind: Pod
metadata:
  name: simple-webapp-color
spec:
  priorityClassName: high-priority
  containers:
  - name: simple-webapp-color
    image: simple-webapp-color
	resources:
       requests:
          memory: "1Gi"
		  cpu: 10
```
* There are 4 nodes.
* Each node has a set amount of CPU utilisation available.
* When pods are created, they end up in a scheduling queue.
* Pods are sorted based on priority defined on the pods.
* To set a priority, you have to create a field called `priorityClassName`. Pods with a `priority` of `high-priority` are placed at the beginning of the queue.
* The above is called the `Sorted Phase`
* The next phase is the `Filtering Phase` - this filters out any nodes that do not have the resources available to host the container.
* The next phase is the `Scoring Phase` - nodes are scored with different weights. With the remaining nodes, the scheduler issues a score to each node based on the free space available that it will have, after reserving the CPU requirements from the pod. For example if the node has a CPU score of 20, then minus the CPU request of the pod by the resource amount (in this case 10). The remaining total in this example would be 10.
* Finally there is the `Binding Phase` - the pod is bound to the node with the highest score.
* All operations are achieved with certain plugins:
	* `Scheduling Queue` - `PrioritySort` plugin is used to sort the pods into a order based on the priority configured on the pods.
	* `Filtering Stage` - `NodeResourcesFit` plugin is needed to filter out the right resources. Another one in this stage is the `NodeName` plugin, checks if a pod has a `nodeName` to assign it to a particular node in the pod specification file. A third one is the `NodeUnschedulable` plugin filters out nodes that have the `Unschedulable` flag set to `true` - you can check this with `kubectl describe node <node_name> | grep Unschedulable` 
	* `Scoring Phase` - the `NodeResourcesFit` plugin allocates a score to a node. Another plugin is the `ImageLocality` plugin - associate a high score to nodes that already have the container image used by the pods among the different nodes.
	* `Binding` phase uses the `DefaultBinder` plugin that provides the Binding mechanism.
* It is also possible to write your own plugin - use `Extension Points`. Each stage has an `Extension Point` that can be jacked into.
	* `Scheduling Queue` has `queueSort`
	* `Filtering Queue` has `filter`
	* `Scoring Queue` has `score`
	* `Binding Queue` has `bind`
		* All of the above mentioned plugins are attached to each of the extensions.
	* There are extensions that come in before the phases and look like this:
	* `Filtering Queue` --> `preFilter` --> `filter` --> `postFilter`
	* `Scoring Queue` --> `preScore` --> `score` --> `reserve`
	* `Binding Queue` --> `permit` --> `preBind` --> `bind` --> `postBind`
	* `Scheduling Queue` does not have any additional phases.
* Further plugins that are available:
	* `Filtering Stage`
		* `NodeName`
		* `NodeUnschedulable`
		* `NodeResourcesFit`
		* `TaintToleration`
		* `NodePorts`
		* `NodeAffinity`
	* `Scoring Stage`
		* `ImageLocality`
		* `NodeResourcesFit`
		* `TaintToleration`
		* `NodeAffinity`
* How we can change how the plugins are called?
* We have 3 schedulers, `my-scheduler-2`, `my-scheduler` and `defualt-scheduler`. Each has the following `yaml` file:
```
apiVersion: kubescheduler.config.k8s.io/v1
kind: KubeSchedulerConfiguration
profiles:
- schedulerName: my-scheduler-2
```
* The only part that is different with the `yaml` file across all three schedulers is the `schedulerName`.
	* Each scheduler runs under a separate process.
		* This can cause race conditions, when making scheduling decisions.
			* A scheduler can schedule a workload on a node, with another scheduler not being aware and trying to schedule the load at the same time.
* `v1.18` feature in Kubernetes was released - a feature to support multiple profiles in a single scheduler was introduced.
	* Can add more profiles into the scheduler configuration profile.
		* Each profile creates a separate scheduler name. This allows you to run multiple schedulers in the same binary. For example you have `my-scheduler-2` which is assigned to `Profile 1`, then `my-scheduler-3` for `Profile 2` and so on. The profiles are added into the `yaml` file:
```
apiVersion: kubescheduler.config.k8s.io/v1
kind: KubeSchedulerConfiguration
profiles:
- schedulerName: my-scheduler-2
- schedulerName: my-scheduler-3
```
* How do you then configure each scheduler differently.
* An example of `my-scheduler-2-config.yaml` file disabling certain plugins:
```
apiVersion: kubescheduler.config.k8s.io/v1
kind: KubeSchedulerConfiguration
profiles:
- schedulerName: my-scheduler-2
  plugins:
    score:
	  disabled:
       - name: TaintToleration
       enabled:
		- name: MyCustomPluginA
		- name: MyCustomPluginB

- schedulerName: my-scheduler-2
  plugins:
    preScore:
	  disabled:
       - name: '*'
    score:
	  disabled:
	   - name: '*'

- schedulerName: my-scheduler-2

```