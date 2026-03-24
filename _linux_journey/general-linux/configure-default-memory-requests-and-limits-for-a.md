---
title: "Configure Default Memory Requests And Limits For A"
category: "general-linux"
tags: ["configure", "default", "memory", "requests", "limits"]
---

[](https://kubernetes.io/)

- [Documentation](https://kubernetes.io/docs/)
- [Kubernetes Blog](https://kubernetes.io/blog/)
- [Training](https://kubernetes.io/training/)
- [Partners](https://kubernetes.io/partners/)
- [Community](https://kubernetes.io/community/)
- [Case Studies](https://kubernetes.io/case-studies/)
- <a id="navbarDropdown"></a>[Versions](#)
- <a id="navbarDropdownMenuLink"></a>[English](#)

- - <a id="m-docs-home"></a>[Documentation](https://kubernetes.io/docs/home/ "Kubernetes Documentation")
    - <a id="m-docs-setup"></a>[Getting started](https://kubernetes.io/docs/setup/)
    - <a id="m-docs-concepts"></a>[Concepts](https://kubernetes.io/docs/concepts/)
    - <a id="m-docs-tasks"></a>[Tasks](https://kubernetes.io/docs/tasks/)
        - <a id="m-docs-tasks-tools"></a>[Install Tools](https://kubernetes.io/docs/tasks/tools/)
        - <a id="m-docs-tasks-administer-cluster"></a>[Administer a Cluster](https://kubernetes.io/docs/tasks/administer-cluster/)
            - <a id="m-docs-tasks-administer-cluster-kubeadm"></a>[Administration with kubeadm](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/)
            - <a id="m-docs-tasks-administer-cluster-node-overprovisioning"></a>[Overprovision Node Capacity For A Cluster](https://kubernetes.io/docs/tasks/administer-cluster/node-overprovisioning/)
            - <a id="m-docs-tasks-administer-cluster-migrating-from-dockershim"></a>[Migrating from dockershim](https://kubernetes.io/docs/tasks/administer-cluster/migrating-from-dockershim/)
            - <a id="m-docs-tasks-administer-cluster-certificates"></a>[Generate Certificates Manually](https://kubernetes.io/docs/tasks/administer-cluster/certificates/)
            - <a id="m-docs-tasks-administer-cluster-manage-resources"></a>[Manage Memory, CPU, and API Resources](https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/)
                - <a id="m-docs-tasks-administer-cluster-manage-resources-memory-default-namespace"></a>[Configure Default Memory Requests and Limits for a Namespace](https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/memory-default-namespace/)
                - <a id="m-docs-tasks-administer-cluster-manage-resources-cpu-default-namespace"></a>[Configure Default CPU Requests and Limits for a Namespace](https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/cpu-default-namespace/)
                - <a id="m-docs-tasks-administer-cluster-manage-resources-memory-constraint-namespace"></a>[Configure Minimum and Maximum Memory Constraints for a Namespace](https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/memory-constraint-namespace/)
                - <a id="m-docs-tasks-administer-cluster-manage-resources-cpu-constraint-namespace"></a>[Configure Minimum and Maximum CPU Constraints for a Namespace](https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/cpu-constraint-namespace/)
                - <a id="m-docs-tasks-administer-cluster-manage-resources-quota-memory-cpu-namespace"></a>[Configure Memory and CPU Quotas for a Namespace](https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace/)
                - <a id="m-docs-tasks-administer-cluster-manage-resources-quota-pod-namespace"></a>[Configure a Pod Quota for a Namespace](https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/quota-pod-namespace/)
            - <a id="m-docs-tasks-administer-cluster-network-policy-provider"></a>[Install a Network Policy Provider](https://kubernetes.io/docs/tasks/administer-cluster/network-policy-provider/)
            - <a id="m-docs-tasks-administer-cluster-access-cluster-api"></a>[Access Clusters Using the Kubernetes API](https://kubernetes.io/docs/tasks/administer-cluster/access-cluster-api/)
            - <a id="m-docs-tasks-administer-cluster-extended-resource-node"></a>[Advertise Extended Resources for a Node](https://kubernetes.io/docs/tasks/administer-cluster/extended-resource-node/)
            - <a id="m-docs-tasks-administer-cluster-dns-horizontal-autoscaling"></a>[Autoscale the DNS Service in a Cluster](https://kubernetes.io/docs/tasks/administer-cluster/dns-horizontal-autoscaling/)
            - <a id="m-docs-tasks-administer-cluster-change-pv-access-mode-readwriteoncepod"></a>[Change the Access Mode of a PersistentVolume to ReadWriteOncePod](https://kubernetes.io/docs/tasks/administer-cluster/change-pv-access-mode-readwriteoncepod/)
            - <a id="m-docs-tasks-administer-cluster-change-default-storage-class"></a>[Change the default StorageClass](https://kubernetes.io/docs/tasks/administer-cluster/change-default-storage-class/)
            - <a id="m-docs-tasks-administer-cluster-switch-to-evented-pleg"></a>[Switching from Polling to CRI Event-based Updates to Container Status](https://kubernetes.io/docs/tasks/administer-cluster/switch-to-evented-pleg/)
            - <a id="m-docs-tasks-administer-cluster-change-pv-reclaim-policy"></a>[Change the Reclaim Policy of a PersistentVolume](https://kubernetes.io/docs/tasks/administer-cluster/change-pv-reclaim-policy/)
            - <a id="m-docs-tasks-administer-cluster-running-cloud-controller"></a>[Cloud Controller Manager Administration](https://kubernetes.io/docs/tasks/administer-cluster/running-cloud-controller/)
            - <a id="m-docs-tasks-administer-cluster-kubelet-credential-provider"></a>[Configure a kubelet image credential provider](https://kubernetes.io/docs/tasks/administer-cluster/kubelet-credential-provider/)
            - <a id="m-docs-tasks-administer-cluster-quota-api-object"></a>[Configure Quotas for API Objects](https://kubernetes.io/docs/tasks/administer-cluster/quota-api-object/)
            - <a id="m-docs-tasks-administer-cluster-cpu-management-policies"></a>[Control CPU Management Policies on the Node](https://kubernetes.io/docs/tasks/administer-cluster/cpu-management-policies/)
            - <a id="m-docs-tasks-administer-cluster-topology-manager"></a>[Control Topology Management Policies on a node](https://kubernetes.io/docs/tasks/administer-cluster/topology-manager/)
            - <a id="m-docs-tasks-administer-cluster-dns-custom-nameservers"></a>[Customising DNS Service](https://kubernetes.io/docs/tasks/administer-cluster/dns-custom-nameservers/)
            - <a id="m-docs-tasks-administer-cluster-dns-debugging-resolution"></a>[Debugging DNS Resolution](https://kubernetes.io/docs/tasks/administer-cluster/dns-debugging-resolution/)
            - <a id="m-docs-tasks-administer-cluster-declare-network-policy"></a>[Declare Network Policy](https://kubernetes.io/docs/tasks/administer-cluster/declare-network-policy/)
            - <a id="m-docs-tasks-administer-cluster-developing-cloud-controller-manager"></a>[Developing Cloud Controller Manager](https://kubernetes.io/docs/tasks/administer-cluster/developing-cloud-controller-manager/)
            - <a id="m-docs-tasks-administer-cluster-enable-disable-api"></a>[Enable Or Disable A Kubernetes API](https://kubernetes.io/docs/tasks/administer-cluster/enable-disable-api/)
            - <a id="m-docs-tasks-administer-cluster-encrypt-data"></a>[Encrypting Confidential Data at Rest](https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/)
            - <a id="m-docs-tasks-administer-cluster-decrypt-data"></a>[Decrypt Confidential Data that is Already Encrypted at Rest](https://kubernetes.io/docs/tasks/administer-cluster/decrypt-data/)
            - <a id="m-docs-tasks-administer-cluster-guaranteed-scheduling-critical-addon-pods"></a>[Guaranteed Scheduling For Critical Add-On Pods](https://kubernetes.io/docs/tasks/administer-cluster/guaranteed-scheduling-critical-addon-pods/)
            - <a id="m-docs-tasks-administer-cluster-ip-masq-agent"></a>[IP Masquerade Agent User Guide](https://kubernetes.io/docs/tasks/administer-cluster/ip-masq-agent/)
            - <a id="m-docs-tasks-administer-cluster-limit-storage-consumption"></a>[Limit Storage Consumption](https://kubernetes.io/docs/tasks/administer-cluster/limit-storage-consumption/)
            - <a id="m-docs-tasks-administer-cluster-controller-manager-leader-migration"></a>[Migrate Replicated Control Plane To Use Cloud Controller Manager](https://kubernetes.io/docs/tasks/administer-cluster/controller-manager-leader-migration/)
            - <a id="m-docs-tasks-administer-cluster-namespaces-walkthrough"></a>[Namespaces Walkthrough](https://kubernetes.io/docs/tasks/administer-cluster/namespaces-walkthrough/)
            - <a id="m-docs-tasks-administer-cluster-configure-upgrade-etcd"></a>[Operating etcd clusters for Kubernetes](https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/)
            - <a id="m-docs-tasks-administer-cluster-reserve-compute-resources"></a>[Reserve Compute Resources for System Daemons](https://kubernetes.io/docs/tasks/administer-cluster/reserve-compute-resources/)
            - <a id="m-docs-tasks-administer-cluster-kubelet-in-userns"></a>[Running Kubernetes Node Components as a Non-root User](https://kubernetes.io/docs/tasks/administer-cluster/kubelet-in-userns/)
            - <a id="m-docs-tasks-administer-cluster-safely-drain-node"></a>[Safely Drain a Node](https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node/)
            - <a id="m-docs-tasks-administer-cluster-securing-a-cluster"></a>[Securing a Cluster](https://kubernetes.io/docs/tasks/administer-cluster/securing-a-cluster/)
            - <a id="m-docs-tasks-administer-cluster-kubelet-config-file"></a>[Set Kubelet Parameters Via A Configuration File](https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/)
            - <a id="m-docs-tasks-administer-cluster-namespaces"></a>[Share a Cluster with Namespaces](https://kubernetes.io/docs/tasks/administer-cluster/namespaces/)
            - <a id="m-docs-tasks-administer-cluster-cluster-upgrade"></a>[Upgrade A Cluster](https://kubernetes.io/docs/tasks/administer-cluster/cluster-upgrade/)
            - <a id="m-docs-tasks-administer-cluster-use-cascading-deletion"></a>[Use Cascading Deletion in a Cluster](https://kubernetes.io/docs/tasks/administer-cluster/use-cascading-deletion/)
            - <a id="m-docs-tasks-administer-cluster-kms-provider"></a>[Using a KMS provider for data encryption](https://kubernetes.io/docs/tasks/administer-cluster/kms-provider/)
            - <a id="m-docs-tasks-administer-cluster-coredns"></a>[Using CoreDNS for Service Discovery](https://kubernetes.io/docs/tasks/administer-cluster/coredns/)
            - <a id="m-docs-tasks-administer-cluster-nodelocaldns"></a>[Using NodeLocal DNSCache in Kubernetes Clusters](https://kubernetes.io/docs/tasks/administer-cluster/nodelocaldns/)
            - <a id="m-docs-tasks-administer-cluster-sysctl-cluster"></a>[Using sysctls in a Kubernetes Cluster](https://kubernetes.io/docs/tasks/administer-cluster/sysctl-cluster/)
            - <a id="m-docs-tasks-administer-cluster-memory-manager"></a>[Utilising the NUMA-aware Memory Manager](https://kubernetes.io/docs/tasks/administer-cluster/memory-manager/)
            - <a id="m-docs-tasks-administer-cluster-verify-signed-artifacts"></a>[Verify Signed Kubernetes Artifacts](https://kubernetes.io/docs/tasks/administer-cluster/verify-signed-artifacts/)
        - <a id="m-docs-tasks-configure-pod-container"></a>[Configure Pods and Containers](https://kubernetes.io/docs/tasks/configure-pod-container/)
        - <a id="m-docs-tasks-debug"></a>[Monitoring, Logging, and Debugging](https://kubernetes.io/docs/tasks/debug/)
        - <a id="m-docs-tasks-manage-kubernetes-objects"></a>[Manage Kubernetes Objects](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/)
        - <a id="m-docs-tasks-configmap-secret"></a>[Managing Secrets](https://kubernetes.io/docs/tasks/configmap-secret/)
        - <a id="m-docs-tasks-inject-data-application"></a>[Inject Data Into Applications](https://kubernetes.io/docs/tasks/inject-data-application/)
        - <a id="m-docs-tasks-run-application"></a>[Run Applications](https://kubernetes.io/docs/tasks/run-application/)
        - <a id="m-docs-tasks-job"></a>[Run Jobs](https://kubernetes.io/docs/tasks/job/)
        - <a id="m-docs-tasks-access-application-cluster"></a>[Access Applications in a Cluster](https://kubernetes.io/docs/tasks/access-application-cluster/)
        - <a id="m-docs-tasks-extend-kubernetes"></a>[Extend Kubernetes](https://kubernetes.io/docs/tasks/extend-kubernetes/)
        - <a id="m-docs-tasks-tls"></a>[TLS](https://kubernetes.io/docs/tasks/tls/)
        - <a id="m-docs-tasks-manage-daemon"></a>[Manage Cluster Daemons](https://kubernetes.io/docs/tasks/manage-daemon/)
https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/memory-default-namespace/
# Configure Default Memory Requests and Limits for a Namespace

Define a default memory resource limit for a namespace, so that every new Pod in that namespace has a memory resource limit configured.

This page shows how to configure default memory requests and limits for a [namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces).

A Kubernetes cluster can be divided into namespaces. Once you have a namespace that has a default memory [limit](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#requests-and-limits), and you then try to create a Pod with a container that does not specify its own memory limit, then the [control plane](https://kubernetes.io/docs/reference/glossary/?all=true#term-control-plane) assigns the default memory limit to that container.

Kubernetes assigns a default memory request under certain conditions that are explained later in this topic.

## Before you begin

You need to have a Kubernetes cluster, and the kubectl command-line tool must be configured to communicate with your cluster. It is recommended to run this tutorial on a cluster with at least two nodes that are not acting as control plane hosts. If you do not already have a cluster, you can create one by using [minikube](https://minikube.sigs.k8s.io/docs/tutorials/multi_node/) or you can use one of these Kubernetes playgrounds:

- [Killercoda](https://killercoda.com/playgrounds/scenario/kubernetes)
- [Play with Kubernetes](https://labs.play-with-k8s.com/)

You must have access to create namespaces in your cluster.

Each node in your cluster must have at least 2 GiB of memory.

## Create a namespace

Create a namespace so that the resources you create in this exercise are isolated from the rest of your cluster.

```
kubectl create namespace default-mem-example
```

## Create a LimitRange and a Pod

Here's a manifest for an example [LimitRange](https://kubernetes.io/docs/concepts/policy/limit-range/). The manifest specifies a default memory request and a default memory limit.

[`admin/resource/memory-defaults.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/admin/resource/memory-defaults.yaml) <img width="25" height="25" src="../_resources/copycode_f4e42c6fa88a431eb9fb2214f219e040.svg"/>

```
apiVersion: v1
kind: LimitRange
metadata:

  name: mem-limit-range
spec:

  limits:

  - default:

      memory: 512Mi

    defaultRequest:

      memory: 256Mi

    type: Container
```

Create the LimitRange in the default-mem-example namespace:

```
kubectl apply -f https://k8s.io/examples/admin/resource/memory-defaults.yaml --namespace=default-mem-example
```

Now if you create a Pod in the default-mem-example namespace, and any container within that Pod does not specify its own values for memory request and memory limit, then the [control plane](https://kubernetes.io/docs/reference/glossary/?all=true#term-control-plane) applies default values: a memory request of 256MiB and a memory limit of 512MiB.

Here's an example manifest for a Pod that has one container. The container does not specify a memory request and limit.

[`admin/resource/memory-defaults-pod.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/admin/resource/memory-defaults-pod.yaml) <img width="25" height="25" src="../_resources/copycode_f4e42c6fa88a431eb9fb2214f219e040.svg"/>

```
apiVersion: v1
kind: Pod
metadata:

  name: default-mem-demo
spec:

  containers:

  - name: default-mem-demo-ctr

    image: nginx
```

Create the Pod.

```
kubectl apply -f https://k8s.io/examples/admin/resource/memory-defaults-pod.yaml --namespace=default-mem-example
```

View detailed information about the Pod:

```
kubectl get pod default-mem-demo --output=yaml --namespace=default-mem-example
```

The output shows that the Pod's container has a memory request of 256 MiB and a memory limit of 512 MiB. These are the default values specified by the LimitRange.

```
containers:
- image: nginx
  imagePullPolicy: Always
  name: default-mem-demo-ctr
  resources:
    limits:
      memory: 512Mi
    requests:
      memory: 256Mi
```

Delete your Pod:

```
kubectl delete pod default-mem-demo --namespace=default-mem-example
```

## What if you specify a container's limit, but not its request?

Here's a manifest for a Pod that has one container. The container specifies a memory limit, but not a request:

[`admin/resource/memory-defaults-pod-2.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/admin/resource/memory-defaults-pod-2.yaml) <img width="25" height="25" src="../_resources/copycode_f4e42c6fa88a431eb9fb2214f219e040.svg"/>

```
apiVersion: v1
kind: Pod
metadata:

  name: default-mem-demo-2
spec:

  containers:

  - name: default-mem-demo-2-ctr

    image: nginx

    resources:

      limits:

        memory: "1Gi"
```

Create the Pod:

```
kubectl apply -f https://k8s.io/examples/admin/resource/memory-defaults-pod-2.yaml --namespace=default-mem-example
```

View detailed information about the Pod:

```
kubectl get pod default-mem-demo-2 --output=yaml --namespace=default-mem-example
```

The output shows that the container's memory request is set to match its memory limit. Notice that the container was not assigned the default memory request value of 256Mi.

```
resources:
  limits:
    memory: 1Gi
  requests:
    memory: 1Gi
```

## What if you specify a container's request, but not its limit?

Here's a manifest for a Pod that has one container. The container specifies a memory request, but not a limit:

[`admin/resource/memory-defaults-pod-3.yaml`](https://raw.githubusercontent.com/kubernetes/website/main/content/en/examples/admin/resource/memory-defaults-pod-3.yaml) <img width="25" height="25" src="../_resources/copycode_f4e42c6fa88a431eb9fb2214f219e040.svg"/>

```
apiVersion: v1
kind: Pod
metadata:

  name: default-mem-demo-3
spec:

  containers:

  - name: default-mem-demo-3-ctr

    image: nginx

    resources:

      requests:

        memory: "128Mi"
```

Create the Pod:

```
kubectl apply -f https://k8s.io/examples/admin/resource/memory-defaults-pod-3.yaml --namespace=default-mem-example
```

View the Pod's specification:

```
kubectl get pod default-mem-demo-3 --output=yaml --namespace=default-mem-example
```

The output shows that the container's memory request is set to the value specified in the container's manifest. The container is limited to use no more than 512MiB of memory, which matches the default memory limit for the namespace.

```
resources:
  limits:
    memory: 512Mi
  requests:
    memory: 128Mi
```

#### Note:

A `LimitRange` does **not** check the consistency of the default values it applies. This means that a default value for the *limit* that is set by `LimitRange` may be less than the *request* value specified for the container in the spec that a client submits to the API server. If that happens, the final Pod will not be scheduleable. See [Constraints on resource limits and requests](https://kubernetes.io/docs/concepts/policy/limit-range/#constraints-on-resource-limits-and-requests) for more details.

## Motivation for default memory limits and requests

If your namespace has a memory [resource quota](https://kubernetes.io/docs/concepts/policy/resource-quotas/) configured, it is helpful to have a default value in place for memory limit. Here are three of the restrictions that a resource quota imposes on a namespace:

- For every Pod that runs in the namespace, the Pod and each of its containers must have a memory limit. (If you specify a memory limit for every container in a Pod, Kubernetes can infer the Pod-level memory limit by adding up the limits for its containers).
- Memory limits apply a resource reservation on the node where the Pod in question is scheduled. The total amount of memory reserved for all Pods in the namespace must not exceed a specified limit.
- The total amount of memory actually used by all Pods in the namespace must also not exceed a specified limit.

When you add a LimitRange:

If any Pod in that namespace that includes a container does not specify its own memory limit, the control plane applies the default memory limit to that container, and the Pod can be allowed to run in a namespace that is restricted by a memory ResourceQuota.

## Clean up

Delete your namespace:

```
kubectl delete namespace default-mem-example
```

## What's next

### For cluster administrators

- [Configure Default CPU Requests and Limits for a Namespace](https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/cpu-default-namespace/)
    
- [Configure Minimum and Maximum Memory Constraints for a Namespace](https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/memory-constraint-namespace/)
    
- [Configure Minimum and Maximum CPU Constraints for a Namespace](https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/cpu-constraint-namespace/)
    
- [Configure Memory and CPU Quotas for a Namespace](https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace/)
    
- [Configure a Pod Quota for a Namespace](https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/quota-pod-namespace/)
    
- [Configure Quotas for API Objects](https://kubernetes.io/docs/tasks/administer-cluster/quota-api-object/)
    

### For app developers

- [Assign Memory Resources to Containers and Pods](https://kubernetes.io/docs/tasks/configure-pod-container/assign-memory-resource/)
    
- [Assign CPU Resources to Containers and Pods](https://kubernetes.io/docs/tasks/configure-pod-container/assign-cpu-resource/)
    
- [Assign Pod-level CPU and memory resources](https://kubernetes.io/docs/tasks/configure-pod-container/assign-pod-level-resources/)
    
- [Configure Quality of Service for Pods](https://kubernetes.io/docs/tasks/configure-pod-container/quality-service-pod/)
    

## Feedback

Was this page helpful?

Last modified October 30, 2024 at 5:17 PM PST: [KEP 2837: Pod Level Resources Alpha (0374213f57)](https://github.com/kubernetes/website/commit/0374213f578681c5cb725530aa58449b23d0af25)

[Edit this page](https://github.com/kubernetes/website/edit/main/content/en/docs/tasks/administer-cluster/manage-resources/memory-default-namespace.md) [Create child page](https://github.com/kubernetes/website/new/main/content/en/docs/tasks/administer-cluster/manage-resources/memory-default-namespace.md?filename=change-me.md&value=---%0Atitle%3A+%22Long+Page+Title%22%0AlinkTitle%3A+%22Short+Nav+Title%22%0Aweight%3A+100%0Adescription%3A+%3E-%0A+++++Page+description+for+heading+and+indexes.%0A---%0A%0A%23%23+Heading%0A%0AEdit+this+template+to+create+your+new+page.%0A%0A%2A+Give+it+a+good+name%2C+ending+in+%60.md%60+-+e.g.+%60getting-started.md%60%0A%2A+Edit+the+%22front+matter%22+section+at+the+top+of+the+page+%28weight+controls+how+its+ordered+amongst+other+pages+in+the+same+directory%3B+lowest+number+first%29.%0A%2A+Add+a+good+commit+message+at+the+bottom+of+the+page+%28%3C80+characters%3B+use+the+extended+description+field+for+more+detail%29.%0A%2A+Create+a+new+branch+so+you+can+preview+your+new+file+and+request+a+review+via+Pull+Request.%0A) [Create documentation issue](https://github.com/kubernetes/website/issues/new?title=Configure%20Default%20Memory%20Requests%20and%20Limits%20for%20a%20Namespace) <a id="print"></a>[Print entire section](https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/_print/)

- [Before you begin](#before-you-begin)
- [Create a namespace](#create-a-namespace)
- [Create a LimitRange and a Pod](#create-a-limitrange-and-a-pod)
- [What if you specify a container's limit, but not its request?](#what-if-you-specify-a-container-s-limit-but-not-its-request)
- [What if you specify a container's request, but not its limit?](#what-if-you-specify-a-container-s-request-but-not-its-limit)
- [Motivation for default memory limits and requests](#motivation-for-default-memory-limits-and-requests)
- [Clean up](#clean-up)
- [What's next](#what-s-next)
    - [For cluster administrators](#for-cluster-administrators)
    - [For app developers](#for-app-developers)

© 2025 The Kubernetes Authors | Documentation Distributed under [CC BY 4.0](https://git.k8s.io/website/licence)

© 2025 The Linux Foundation ®. All rights reserved. The Linux Foundation has registered trademarks and uses trademarks. For a list of trademarks of The Linux Foundation, please see our [Trademark Usage page](https://www.linuxfoundation.org/trademark-usage)

ICP licence: 京ICP备17074266号-3

- [](https://youtube.com/kubernetescommunity)
- [](https://discuss.kubernetes.io)
- [](https://serverfault.com/questions/tagged/kubernetes)
- [](https://twitter.com/kubernetesio)

- [](https://k8s.dev/)
- [](https://github.com/kubernetes/kubernetes)
- [](https://slack.k8s.io)
- [](https://calendar.google.com/calendar/embed?src=calendar%40kubernetes.io)