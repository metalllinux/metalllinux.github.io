---
title: "The Kubernetes Control Plane"
category: "learning-kubernetes"
tags: ["learning-kubernetes", "kubernetes", "control", "plane"]
---

* Important Kubernetes vocabulary.
	* Cluster - instance of Kubernetes.
		* Each Cluster has a Control Plane and at least 1 Worker Node.
* A Control Plane is like the Air Traffic Control Tower.
	* Making sure that nodes and pods are created, modified and deleted without further issue.
	* Made up of several components and if you know the function of each one, better understand how Kubernetes works.
* Kubernetes Cluster:
![Screenshot from 2024-03-05 17-50-10.png](../../_resources/Screenshot%20from%202024-03-05%2017-50-10.png)
* The most important component, is the Kube API server:
![Screenshot from 2024-03-05 17-51-16.png](../../_resources/Screenshot%20from%202024-03-05%2017-51-16.png)
* The API server exposes the Kubernetes API.
* Each Kubernetes object, including the Pods, deployments and the horizontal pod autoscaler have API endpoints.
* Kubernetes API has a REST interface.
* `kubectl` and `kubeadm` are CLI tools to communicate with the Kubernetes API via HTTP requests.
* To see all of the Kubernetes Objects and their API version, run `kubectl api-resources`. This will output the following:
```
myuser@myhost:~$ kubectl api-resources
NAME                              SHORTNAMES   APIVERSION                             NAMESPACED   KIND
bindings                                       v1                                     true         Binding
componentstatuses                 cs           v1                                     false        ComponentStatus
configmaps                        cm           v1                                     true         ConfigMap
endpoints                         ep           v1                                     true         Endpoints
events                            ev           v1                                     true         Event
limitranges                       limits       v1                                     true         LimitRange
namespaces                        ns           v1                                     false        Namespace
nodes                             no           v1                                     false        Node
persistentvolumeclaims            pvc          v1                                     true         PersistentVolumeClaim
persistentvolumes                 pv           v1                                     false        PersistentVolume
pods                              po           v1                                     true         Pod
podtemplates                                   v1                                     true         PodTemplate
replicationcontrollers            rc           v1                                     true         ReplicationController
resourcequotas                    quota        v1                                     true         ResourceQuota
secrets                                        v1                                     true         Secret
serviceaccounts                   sa           v1                                     true         ServiceAccount
services                          svc          v1                                     true         Service
mutatingwebhookconfigurations                  admissionregistration.k8s.io/v1        false        MutatingWebhookConfiguration
validatingwebhookconfigurations                admissionregistration.k8s.io/v1        false        ValidatingWebhookConfiguration
customresourcedefinitions         crd,crds     apiextensions.k8s.io/v1                false        CustomResourceDefinition
apiservices                                    apiregistration.k8s.io/v1              false        APIService
controllerrevisions                            apps/v1                                true         ControllerRevision
daemonsets                        ds           apps/v1                                true         DaemonSet
deployments                       deploy       apps/v1                                true         Deployment
replicasets                       rs           apps/v1                                true         ReplicaSet
statefulsets                      sts          apps/v1                                true         StatefulSet
selfsubjectreviews                             authentication.k8s.io/v1               false        SelfSubjectReview
tokenreviews                                   authentication.k8s.io/v1               false        TokenReview
localsubjectaccessreviews                      authorization.k8s.io/v1                true         LocalSubjectAccessReview
selfsubjectaccessreviews                       authorization.k8s.io/v1                false        SelfSubjectAccessReview
selfsubjectrulesreviews                        authorization.k8s.io/v1                false        SelfSubjectRulesReview
subjectaccessreviews                           authorization.k8s.io/v1                false        SubjectAccessReview
horizontalpodautoscalers          hpa          autoscaling/v2                         true         HorizontalPodAutoscaler
cronjobs                          cj           batch/v1                               true         CronJob
jobs                                           batch/v1                               true         Job
certificatesigningrequests        csr          certificates.k8s.io/v1                 false        CertificateSigningRequest
leases                                         coordination.k8s.io/v1                 true         Lease
endpointslices                                 discovery.k8s.io/v1                    true         EndpointSlice
events                            ev           events.k8s.io/v1                       true         Event
flowschemas                                    flowcontrol.apiserver.k8s.io/v1beta3   false        FlowSchema
prioritylevelconfigurations                    flowcontrol.apiserver.k8s.io/v1beta3   false        PriorityLevelConfiguration
ingressclasses                                 networking.k8s.io/v1                   false        IngressClass
ingresses                         ing          networking.k8s.io/v1                   true         Ingress
networkpolicies                   netpol       networking.k8s.io/v1                   true         NetworkPolicy
runtimeclasses                                 node.k8s.io/v1                         false        RuntimeClass
poddisruptionbudgets              pdb          policy/v1                              true         PodDisruptionBudget
clusterrolebindings                            rbac.authorization.k8s.io/v1           false        ClusterRoleBinding
clusterroles                                   rbac.authorization.k8s.io/v1           false        ClusterRole
rolebindings                                   rbac.authorization.k8s.io/v1           true         RoleBinding
roles                                          rbac.authorization.k8s.io/v1           true         Role
priorityclasses                   pc           scheduling.k8s.io/v1                   false        PriorityClass
csidrivers                                     storage.k8s.io/v1                      false        CSIDriver
csinodes                                       storage.k8s.io/v1                      false        CSINode
csistoragecapacities                           storage.k8s.io/v1                      true         CSIStorageCapacity
storageclasses                    sc           storage.k8s.io/v1                      false        StorageClass
volumeattachments                              storage.k8s.io/v1                      false        VolumeAttachment
```
* Kube API server is a containerised application, run as a pod. You can see it, by listing all pods within the `kube-system` namespace with:
```
kubectl get pods -n kube-system
```
* The pod has Kube API Server at the beginning.
* Kube API Server is the most important component and handles the most requests from users inside the cluster.
	* Without it, a Kubernetes cluster cannot exist.
* Next component of the Kubernetes Control Plane is `etcd`:
![Screenshot from 2024-03-06 10-03-21.png](../../_resources/Screenshot%20from%202024-03-06%2010-03-21.png)
* `etcd` is an open source, highly available key-value store.
	* In a Kubernetes cluster, this saves all data about the state of the cluster.
* Only the Kube API Server cannot communicate with the `etcd` service.
	* `etcd` is also ran as a pod and has logs and can check how the service works.
* How to get information about pod:
```
kubectl logs etcd-minikube -n kube-system | jq .
```
* Next component is the Kube Scheduler.
	* This identifies newly created pods, that have not been assigned to a worker node.
		* It then chooses a node for the pod to run on.
	* The Kube Scheduler is run as a pod.
* Next component is the Kube Controller Manager.
	* The Controller Manager is a loop that runs continuously. Checks the status of the cluster, to make sure it is running properly and that all worker nodes are running.
	* If it finds that a node is broken, it will replace it with a new worker node.
	* The Controller Manager also checks other things in the cluster.
* The final component is the Cloud Controller Manager:
![Screenshot from 2024-03-06 11-52-36.png](../../_resources/Screenshot%20from%202024-03-06%2011-52-36.png)
* Allows you to connect the cluster, with a cloud provider's API, so you an use the Cloud Resources from AWS, Azure, GCP etc.
* The Control Plane manages the cluster and enables resilience and automation, that makes Kubernetes the popular container orchestrator.
* There are managed Kubernetes services such as AWS' EKS or Google's GKE, you will not be able to see Control Plane nodes using `kubectl`.
	* Cloud Provider hides the maintenance for these away from the user.

