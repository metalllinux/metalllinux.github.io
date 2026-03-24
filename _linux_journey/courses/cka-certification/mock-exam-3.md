---
title: "Mock Exam 3"
category: "cka-certification"
tags: ["cka-certification", "mock", "exam"]
---

* **Question 1**

* You are an administrator preparing your environment to deploy a Kubernetes cluster using kubeadm. Adjust the following network parameters on the system to the following values, and make sure your changes persist reboots:

net.ipv4.ip_forward = 1
net.bridge.bridge-nf-call-iptables = 1

* The above two changes are required, essentially before Kubernetes is deployed.

* Check the documentation for a guide on how to create a cluster with kubeadm:

https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/

* The first step you need to do is install a container runtime:

https://kubernetes.io/docs/setup/production-environment/container-runtimes/

* We need to enable IPV4 Packet Forwarding

* We run the following, which satisfies the `net.ipv4.ip_forward = 1` and `net.bridge.bridge-nf-call-iptables = 1` parts:
```
# sysctl params required by setup, params persist across reboots
cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-iptables = 1
net.ipv4.ip_forward = 1
EOF

# Apply sysctl params without reboot
sudo sysctl --system
```

* **Question 2**

* Create a new service account with the name pvviewer. Grant this Service account access to list all PersistentVolumes in the cluster by creating an appropriate cluster role called pvviewer-role and ClusterRoleBinding called pvviewer-role-binding.
Next, create a pod called pvviewer with the image: redis and serviceAccount: pvviewer in the default namespace.

* Create the Service Account:

```
kubectl create serviceaccount pvviewer
```

* Good tip for the exam, make sure to copy and paste the name.

* Check that the Service Account was created:

* Create the `clusterrole`:

```
kubectl create clusterrole pvviewer-role --resource=persistentvolumes --verb=list
```

* Creates a clusterrole and we can list persistent volumes.

* We can then check to make sure it is created successfully:

```
kubectl describe clusterrole pvviewer-role
```

* It will show that the `Resource` can list them.

* Then need to create a rolebinding, to bind the service account:

```
kubectl create clusterrolebinding pvviewer-role-binding --clusterole=pvviewer-role --serviceaccount=default:pvviewer
```

* Then to check the `clusterrolebinding`, run the following:

```
kubectl describe clusterrolebinding pvviewer-role-binding
```

* You'll see that the `pvviewer` service account is linked to the `pvviewer` role.

* Then we need to create a pod called `pvviewer`. We need to create a file for this:

```
apiVersion: v1
kind: Pod
metadata: 
  name: pvviewer
spec:
  serviceAccountName: pvviewer 
  containers: 
    - name: pvviewer
      image: redis
```

* Apply the above file:

```
kubectl apply -f <file.yaml>
```

* Check for the pod:

```
kubectl get pod
```

* Run the `kubectl describe pod pvviewer` command and make sure that `Service Account` is set to `pvviewer`.

* **Question 3**

* Create a StorageClass named rancher-sc with the following specifications:

The provisioner should be rancher.io/local-path.
The volume binding mode should be WaitForFirstConsumer.
Volume expansion should be enabled.

* Go to the documentation and search for `storageclass`:

https://kubernetes.io/docs/concepts/storage/storage-classes/

* Use this example configuratoin from the documentation:

```
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: low-latency
  annotations:
    storageclass.kubernetes.io/is-default-class: "false"
provisioner: csi-driver.example-vendor.example
reclaimPolicy: Retain # default value is Delete
allowVolumeExpansion: true
mountOptions:
  - discard # this might enable UNMAP / TRIM at the block storage layer
volumeBindingMode: WaitForFirstConsumer
parameters:
  guaranteedReadWriteLatency: "true" # provider-specific
```

* Create a file and paste in the above configuration.

* We change the above configuration to the following:

```
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: rancher-sc
provisioner: rancher.io/local-path
allowVolumeExpansion: true
volumeBindingMode: WaitForFirstConsumer
```

* Then we apply the file:

```
kubectl apply -f <file.yaml>
```

* **Question 4**

* Create a ConfigMap named app-config in the namespace cm-namespace with the following key-value pairs:

ENV=production
LOG_LEVEL=info

Then, modify the existing Deployment named cm-webapp in the same namespace to use the app-config ConfigMap by setting the environment variables ENV and LOG_LEVEL in the container from the ConfigMap.

* We run `kubectl create configmap app-config -n cm-namespace --from-literal=ENV=production --from-literal=LOG_LEVEL=INFO`

* `kubectl get cm -n cm-namespace`

* Describe it as well:

```
kubectl describe cm app-config -n cm-namespace
```

* Then run:

```
kubectl get deployment -n cm-namespace
```

* To make changes in the exam, just run:

```
kubectl get deploy -o yaml
```

* Can also do it this way as well:

```
kubectl edit deployment cm-webapp -n cm-namespace
```

* Then we look for the container under `containers:` and pass in the configmap as environmental variables:

```
spec:
  containers:
  - image: nginx
    imagePullPolicy: Always
    name: nginx
    envFrom: 
      - configMapRef: 
          name: app-config
```

* The deployment will be updated automatically. All you then need to do is the following:

```
kubectl get pod -n cm-namespace
```

* **Question 5**

* Create a PriorityClass named low-priority with a value of 50000. A pod named lp-pod exists in the namespace low-priority. Modify the pod to use the priority class you created. Recreate the pod if necessary.

* Check the documentation for PriorityClass:

https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/

* We take this yaml file:

```
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata:
  name: high-priority
value: 1000000
globalDefault: false
description: "This priority class should be used for XYZ service pods only."
```

* Create a yaml file from it and change it to this:

```
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata:
  name: low-priority
value: 50000
globalDefault: false
description: "This is a lower priority class"
```

* Then run an `apply`:

```
kubectl apply -f <file.yaml>
```

* Check that the pod is running:

```
kubectl get pod -n low-priority
```

* We get the yaml from the pod:

```
kubectl get pod lp-pod -n low-priority -o yaml > file.yaml
```

* To set the priority in the file, we check under `spec`:

```
spec:
  priorityClassName: low-priority
```

* Remove the `priority: 0` value that is set there.

* Save the file.

* Can either delete the old pod or apply a new pod.

* Here we will `replace`:

```
kubectl replace -f <file.yaml> --force
```

* The `--force` ensures it deletes the old pod and creates the new one.

* If you get an error of `integer value of priority (0) must not be provided in the pod spec`.

  * Remove the `priority: 0` line in the manifest file. 

* **Question 6**

* We have deployed a new pod called np-test-1 and a service called np-test-service. Incoming connections to this service are not working. Troubleshoot and fix it.
Create NetworkPolicy, by the name ingress-to-nptest that allows incoming connections to the service over port 80.

Important: Don't delete any current objects deployed.

* Check the documentation for `Network Policies`:

https://kubernetes.io/docs/concepts/services-networking/network-policies/

* We take this example yaml file:

```
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: test-network-policy
  namespace: default
spec:
  podSelector:
    matchLabels:
      role: db
  policyTypes:
  - Ingress
  - Egress
  ingress:
  - from:
    - ipBlock:
        cidr: 172.17.0.0/16
        except:
        - 172.17.1.0/24
    - namespaceSelector:
        matchLabels:
          project: myproject
    - podSelector:
        matchLabels:
          role: frontend
    ports:
    - protocol: TCP
      port: 6379
  egress:
  - to:
    - ipBlock:
        cidr: 10.0.0.0/24
    ports:
    - protocol: TCP
      port: 5978
```

* Then check the labels the pod is currently using and then we can match those labels in the network policy:

```
kubectl get pod --show-labels
```

* Shows `np-test-1` as a label.

* We change the above yaml file to the following:

```
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: test-network-policy
  namespace: default
spec:
  podSelector:
    matchLabels:
      run: np-test-1
  policyTypes:
  - Ingress
  - Egress
  ingress:
    - ports: 
        - protocol: TCP 
          port: 80
```

* Then we apply the above manifest:

```
kubectl apply -f <file.yaml>
```

* The policy is then created.

* **Question 7**

* Taint the worker node node01 to be Unschedulable. Once done, create a pod called dev-redis, image redis:alpine, to ensure workloads are not scheduled to this worker node. Finally, create a new pod called prod-redis and image: redis:alpine with toleration to be scheduled on node01.

key: env_type, value: production, operator: Equal and effect: NoSchedule

* Search in the documentation for `taint`:

https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/

* Check the available nodes with:

```
kubectl get node
```

* This then shows the node that is available.

* Then we need to taint the node:

```
kubectl taint node node01 env_type=production:NoSchedule
```

* Check the taint applied with:

```
kubectl describe node <node> | grep -i taint
```

* Now to create the `dev-redis` pod:

```
kubectl run dev-redis --image=redis:alpine
```

* Create the next pod, which is `prod-redis`, this is not being done imperatively as performed above:

```
apiVersion: v1
kind: Pod
metadata:
  name: prod-redis
spec:
  tolerations: 
    - effect: NoSchedule
      key: env_type
      operator: Equal
      value: production
  containers:
    - name: prod-redis
      image: redis:alpine
```

* Then perform a `kubectl apply -f`:

```
kubectl apply -f <file.yaml>
```

* Check which pods are assigned to which nodes:

```
kubectl get pod -o wide 
```

* `dev-redis` is then assigned to the Control Plane Node and `prod-redis` is then assigned to the Worker Node, due to being assigned a toleration.

* **Question 8**

* A PersistentVolumeClaim named app-pvc exists in the namespace storage-ns, but it is not getting bound to the available PersistentVolume named app-pv.

Inspect both the PVC and PV and identify why the PVC is not being bound and fix the issue so that the PVC successfully binds to the PV. Do not modify the PV resource.

* Check out the `pv` first:

```
kubectl get pv
```

* Can see that it is `AVAILABLE`.

* Check the `pvc` with:

```
kubectl get pvc -n storage-ns -o yaml
```

* Need to take a look at the configurations for the `pv` and make sure that all of the configs match.

  * The configs needs to match, otherwise the `pv` cannot be bound properly.
  
  * Need to make sure that the CAPACITY is large enough.
  
* The problem here is the `pvc` is has `accessModes` set to `- ReadWriteMany` - this needs to be set to `ReadWriteOnce`

* Create a yaml file:

```
kubectl get pvc -n storage-ns -o yaml > file.yaml
```

* We then delete the `pvc`:

```
kubectl delete pvc app-pvc  -n storage-ns
```

* Apply the new `pvc`:

```
kubectl apply -f <file.yaml>
```

* Running `kubectl get pvc` again shows that the `pvc` is `Bound`:

* **Question 9**

* A kubeconfig file called super.kubeconfig has been created under /root/CKA. There is something wrong with the configuration. Troubleshoot and fix it.

* A question regarding an issue that needs fixing - verify the question first.

* Firstly, pass in the `kubeconfig` file:

```
kubectl get node --kubeconfig=/root/CKA/super.kubeconfig
```

* Run the above and observe a `connection refused` error.

* Check the `/root/CKA/super.kubeconfig` file.

* Check the port that the `kube-apiserver` is listening on:

```
sudo netstat -tulpn | grep kube-apiserver
```

* Observe that the `kube-apiserver` is listening on port `6443`.

* Therefore in the `super.kubeconfig` file, we change:

```
server: https://controlplane:9999
```

to

```
server: https://controlplane:6443
```

* Running the same command shows that it works:

```
kubectl get node --kubeconfig=/root/CKA/super.kubeconfig
```

* **Question 10**

* We have created a new deployment called nginx-deploy. Scale the deployment to 3 replicas. Has the number of replicas increased? Troubleshoot and fix the issue.

* Have a look at the deployment:

```
kubectl get deployment nginx-deploy
```

* Scale the deployment and replicas to `3`:

```
kubectl scale deploy nginx-deploy --replicas=3
```

* Run the `kubectl get deployment` command again and only `1/3` is available.

* If there is an issue with a deployment, run a `kubectl describe deployment` and check for any errors.

* The `Events` will tell us more information.

  * Never got a message from the `deployment-controller` to go from 1 to 3.
  
* Check the replicaset:

```
kubectl get rs
```

* Describe the replicaset:

```
kubectl describe rs
```

* The `deployment-controller` never did its job. Usually that is an issue with the Controlplane Node, that's what limits us from making changes.

* Check the `kube-system` pods:

```
kubectl get pod -n kube-system
```

* In the above output, the `kube-controller-manager-controlplane` is in `ImagePullBackOff` mode.

* Remember, all of the Controlplane components are static pods. Can check the `controller-manager` under `/etc/kubernetes/manifests/kube-controller-manager.yaml`

  * Once the above file is opened, check the `image` line and it should say something like:
  
```
image: registry.k8s.io/kube-controller-manager:v1.32.0
```

* Check all of the typos that you see in the file.

* Once you save the changes, Kubernetes will automatically deploy a new pod, regarding the `kube-system` pods.

* Again running `kubectl get pod -n kube-system` should see the `controller-manager` running without any issues.

* `kubectl get deploy` should show all of the 3 `nginx` deployment pods.

* **Question 11**

* Create a Horizontal Pod Autoscaler (HPA) for the deployment named api-deployment located in the api namespace.
The HPA should scale the deployment based on a custom metric named requests_per_second, targeting an average value of 1000 requests per second across all pods.
Set the minimum number of replicas to 1 and the maximum to 20.

Note: Deployment named api-deployment is available in api namespace. Ignore errors due to the metric requests_per_second not being tracked in metrics-server

* Check in the documentation for Horizontal Pod Autoscaler:

https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/

* In this example, we create a file from scratch:

```
apiVersion: autoscaling /v2
kind: HorizontalPodAutoscaler
metadata: 
  name: api-hpa
  namespace: api
spec:
  scaleTargetRef: 
    apiVersion: apps/v1
    kind: Deployment
    name: api-deployment
  minReplicas: 1
  maxReplicas: 20
  metrics: 
    - type: Pods
      pods: 
        metric:
          name: requests_per_second
        target: 
          type: AverageValue
          averageValue: "1000"
```

* Save the above and run `kubectl apply -f <file.yaml>`

* Then to double-check what we deployed with:

```
kubectl describe hpa -n api
```

* **Question 12**

* Configure the web-route to split traffic between web-service and web-service-v2.The configuration should ensure that 80% of the traffic is routed to web-service and 20% is routed to web-service-v2.

Note: web-gateway, web-service, and web-service-v2 have already been created and are available on the cluster.

* Verify the above with `kubectl get service` and you see both of the `web-service`.

* Similarly with the `gateway`:

```
kubectl get gateway
```

* We create the HTTP Route with the following:

```
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: web-route
  namespace: default
spec:
  parentRefs: 
    - name: web-gateway
      namespace: default
  rules:
    - matches:
        - path:
            type: PathPrefix
            value: /
      backendRefs: 
        - name: web-service
          port: 80
          weight: 80
          
        - name: web-service-v2
          port: 80
          weight: 20
```

* Then run a `kubectl apply -f <file.yaml>`

* **Question 13**

* One application, webpage-server-01, is currently deployed on the Kubernetes cluster using Helm. A new version of the application is available in a Helm chart located at /root/new-version.

Validate this new Helm chart, then install it as a new release named webpage-server-02. After confirming the new release is installed, uninstall the old release webpage-server-01.

* To validate a chart, use this command:

```
helm lint /root/new-version
```

* It will say the chart looks good.

* Then install the chart:

```
helm install --generate-name /root/new-version
```

* The `--generate-name` makes Helm automatically create a name.

* Check it was created with `helm list`.

* Remove the old chart with:

```
helm uninstall webpage-server-01
```

* Then do a `helm list` and the old one is gone.

* **Question 14**

* Identify the pod CIDR network of the node 'controlplane' in the kubernetes cluster. This information is crucial for configuring the CNI plugin during installation. Output the pod CIDR network to a file at /root/pod-cidr.txt.

* To get the pod CIDR, do the following:

```
kubectl get node
```

* Can also get the `yaml` output of a node like so:

```
kubectl get node <node> -o yaml | less
```

* Then under `spec`, check this:

```
podCIDR: 172.17.0.0/24
```

* The above is the pod CIDR network.

* We want to grab the above `podCIDR` line and save it to a file.

```
kubectl get node -o jsonpath='{.items[0].spec.podCIDR}' > /root/pod-cidr.txt
```

* The following will then be stored in the file.
