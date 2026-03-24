---
title: "Kubernetes Troubleshooting Steps"
category: "kubernetes-and-containers"
tags: ["kubernetes-and-containers", "kubernetes", "troubleshooting", "steps"]
---

```
Debugging Pods
Found that throughout the output of kubectl_get_pods_log, the following containers are in a constant state of Pending:
kube-system    coredns-9dcc44b79-vttv4                                                0/1     Pending   0               11d
robinio        robin-coredns-5546cc9b87-2j2hp                                         0/1     Pending   0               11d
The following command would help to identify why these pods are in a Pending state.
kubectl describe pods kube-system
kubectl describe pods robinio 
Is this normal behaviour for these pods?
Do these pods have enough CPU and memory resources?
Are any of these pods bound to a hostPort?
 
No pods are stuck in Waiting state.
No other pods aside from the previously discussed duapp-800-du1 are in a Terminating state.
Debugging Replication Controllers
The controllers either can or cannot create pods.
kubectl describe rc ${CONTROLLER_NAME}
Debugging Running Pods
Running the aforementioned kubectl get pods command on a loop is what we have done before.
If we can run kubectl describe pod <pod_name> until the point of the server hang
kubectl get events -all-namespaces running in a loop would also be a good way identify any pod issues and it does not come with all of the extra detail that kubectl describe pod provides.
Once particular problem pods are identified in a namespace, we can then run kubectl get events --namespace=<namespace_here>
Find the complete yaml output of a particular issue pod kubectl get pod <pod_name> -o yaml
Use kubectl logs ${POD_NAME} ${CONTAINER_NAME} to check the logs of an affected container.
Check previous crash logs of an affected container with kubectl logs --previous ${POD_NAME} ${CONTAINER_NAME}.
Access the pod directly with kubectl logs --previous ${POD_NAME} ${CONTAINER_NAME}
Debugging with ephemeral containers - useful for when a container has crashed.
kubectl debug -it <pod_name> --image=busybox:1.28 --target=<pod_name>
Check the state of the container after that.
kubectl describe pod <pod_name>
Remove the container once complete.
kubectl delete pod <pod_name>
Copy a pod and then add a new container. In this case we are adding an Ubuntu container for debug purposes.
kubectl debug <pod_name> -it --image=ubuntu --share-processes --copy-to=myapp-debug
We can delete this afterwards with.
kubectl delete pod <pod_name> <pod_name>-debug
Debugging Services
Verify endpoints for services are available. For every service object, the apiserver makes an endpoints resource available.
kubectl get svc
kubectl get endpoints ${SERVICE_NAME}
Ensure the endpoints match with the number of pods that you expect to be members.
If endpoints are missing, list pods using labels that Service uses.
kubectl get pods --selector=name=<pod_name>,type=<label_Service_uses>
Network Traffic Not Forwarding
Start up a busybox Pod to check what the Pod itself sees from the outside.
kubectl run -it --rm --restart=Never busybox --image=gcr.io/google-containers/busybox sh
Check by Pod label which pods are running:
kubectl get pods -l app=<pod_name>
Check that the pods are serving correctly.
kubectl get pods -l app=<pod_name> \
    -o go-template='{{range .items}}{{.status.podIP}}{{"\n"}}{{end}}'
That should then output a list of IPs:


 
Similarly within a pod, we can check connectivity to the corresponding pods:
for ep in <IP_1>:<PORT> <IP_2>:<PORT> <IP_3>:<PORT>; do
    wget -qO- $ep
done
That then provides a list like so:
If no responses are received, then kubectl logs is a good way to find out what is happening.
We can also kubectl exec into any affected pods and troubleshoot there as well.
Debugging Services
To check Service connectivity, we can use:
wget -O- hostnames
Check if a service actually exists:
kubectl get svc <service_name>
Are there any Network Policy Ingress rules affecting the target pods?
Check if the Service works by DNS name?
nslookup <service_name>
Ensure that the Pod and Service are not in different namespaces.
nslookup <service_name>.default
If that works, need to adjust the app to use a cross-namespace name / run your app and Service in the same namespace.
Try the fully-qualified name.
nslookup <Service_name>.default.svc.cluster.local
Can also try from a particular node.
nslookup hostnames.default.svc.cluster.local <Cluster_DNS_Service_IP>
Check from within a pod that resolv.conf is correct.
cat /etc/resolv.conf
namesaver in the output should show the Cluster DNS Service IP.
If all of the above fails, then DNS Lookups won't be working.
If there are issues with the Service proxy mechanism, we should check if kube-proxy is running.
From within a node, we can run:
ps auxw | grep kube-proxy
To check if kube-proxy is having trouble contacting the Master node, check /var/log/kube-proxy.log (I do not see this in the provided sosreports). The messages can also appear injournalctl
In the journalctl outputs, we can also check the mode that kube-proxy is running in (iptables)
Debugging the Cluster
Check that all nodes are registered correctly.
kubectl get nodes
Can run kubectl cluster-info dump to understand the overall health of the cluster.
To troubleshoot a node further, we can use kubectl describe nodes <node_name> and kubectl get nodes <node_name> -o yaml
Check the following Control Plane logs:
/var/log/kube-apiserver.log
/var/log/kube-scheduler.log
/var/log/kube-controller-manager.log
Check the Worker Node logs:
/var/log/kubelet.log
/var/log/kube-proxy.log
Issues with failing nodes also include.
VM shutdowns.
Network partitioning issues with the cluster or between the cluser and the users.
Crashes in Kubernetes itself.
Data loss or removal of persistent storage.
Misconfigurations in either Kubernetes or the applications themselves.
Troubleshooting references:
https://kubernetes.io/docs/tasks/debug/
https://kubernetes.io/docs/tasks/debug/debug-application/
https://kubernetes.io/docs/tasks/debug/debug-application/debug-pods/
https://kubernetes.io/docs/tasks/debug/debug-application/debug-service/
https://kubernetes.io/docs/tasks/debug/debug-application/debug-running-pod/
https://kubernetes.io/docs/tasks/debug/debug-cluster/
```