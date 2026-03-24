---
title: "Control Plane Failure"
category: "cka-certification"
tags: ["cka-certification", "control", "plane", "failure"]
---

# Control Plane Failure

* Check the status of the nodes:

```
kubectl get nodes
```

* Check the status of the pods:

```
kubectl get pods
```

* Check Controlplane Pods, if the cluster was deployed with the `kubeadm` tool:

```
kubectl get pods -n kube-system
```

* If the Controlplane components are deployed as Services, check the status of the services:

```
service kube-apiserver status

service kube-controller-manager status

service kube-scheduler status
```

    * On the Worker Nodes, check the `kubelet` and the `kube-proxy` services:
    
```
service kubelet status

service kube-proxy status
```

* Check the logs of the Controlplane Components:

    * In the case of `kube-adm`, check these logs:

```
kubectl logs kube-apiserver-master -n kube-system
```

* On the Master Nodes, can also view the logs via the following command:

```
sudo journalctl -u kube-apiserver
```

* Reference this documentation for more information:

https://kubernetes.io/docs/tasks/debug/debug-cluster/
