---
title: "How The Control Plane And Nodes Work Together"
category: "learning-kubernetes"
tags: ["learning-kubernetes", "control", "plane", "nodes", "work"]
---

* How these work together, in order to create a pod.
* Time Sequence Diagram --> Shows the sequential order of actions.
![Screenshot from 2024-03-07 11-56-56.png](../../_resources/Screenshot%20from%202024-03-07%2011-56-56.png)
* How does a pod get scheduled on to a node?
* Kube config file gives permissions to `kubectl` to communicate with the Kubernetes cluster.
* `kubectl` command sends information to the `kube-api` server. That then saves the new deployment spec in `etcd`
![Screenshot from 2024-03-07 11-59-23.png](../../_resources/Screenshot%20from%202024-03-07%2011-59-23.png)
* While this is occurring, the Kube Controller Manager is checking the Kube API Server, to see if there has been any changes since its last loop:
![Screenshot from 2024-03-07 12-00-23.png](../../_resources/Screenshot%20from%202024-03-07%2012-00-23.png)
* Since there is a new deployment, the Kube Scheduler checks the Kube API Server, to see if there are any new pods that have not been assigned a node.
![Screenshot from 2024-03-07 14-18-56.png](../../_resources/Screenshot%20from%202024-03-07%2014-18-56.png)
* Kube API Server tells the Scheduler that there is a new pod, that has not been placed on a specific node.
![Screenshot from 2024-03-07 14-20-12.png](../../_resources/Screenshot%20from%202024-03-07%2014-20-12.png)
* Therefore, the Dcheduler chooses a node for the pod and sends the information back to the Kube API Server:
![Screenshot from 2024-03-07 14-20-52.png](../../_resources/Screenshot%20from%202024-03-07%2014-20-52.png)
* The API Server saves the state of the cluster in `etcd`:
![Screenshot from 2024-03-07 14-21-54.png](../../_resources/Screenshot%20from%202024-03-07%2014-21-54.png)
* Regarding the Worker Node, the kubelet checks the API Server, to see if there are any new pods that it has been assigned.
![Screenshot from 2024-03-07 14-55-14.png](../../_resources/Screenshot%20from%202024-03-07%2014-55-14.png)
![Screenshot from 2024-03-07 14-55-47.png](../../_resources/Screenshot%20from%202024-03-07%2014-55-47.png)
* Kube API Server then sends the pod spec for the new pod to the Kubelet. This pulls the image and then creates the container, using the container runtime:
![Screenshot from 2024-03-07 14-57-12.png](../../_resources/Screenshot%20from%202024-03-07%2014-57-12.png)
![Screenshot from 2024-03-07 14-57-35.png](../../_resources/Screenshot%20from%202024-03-07%2014-57-35.png)
* Once the pod has been created, the Kubelet sends the pod status (healthy or unhealthy), back to the API server:
![Screenshot from 2024-03-07 14-58-51.png](../../_resources/Screenshot%20from%202024-03-07%2014-58-51.png)
* This then saves the state to `etcd`:
![Screenshot from 2024-03-07 14-59-20.png](../../_resources/Screenshot%20from%202024-03-07%2014-59-20.png)
* Kube API Server processes thousands of requests to keep the server running.
* Useful talk called "Beyond Block Diagrams" on this subject.