---
title: "Mock Exam 2"
category: "cka-certification"
tags: ["cka-certification", "mock", "exam"]
---

# Mock Exam 2

* **Question 1**

* Create a StorageClass named local-sc with the following specifications and set it as the default storage class:

    The provisioner should be kubernetes.io/no-provisioner
    The volume binding mode should be WaitForFirstConsumer
    Volume expansion should be enabled

* ssh into the cluster.

* Check the documentation and pick a `storageclass` example configuration.

* https://kubernetes.io/docs/concepts/storage/storage-classes/

* Use this example:

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

* Edit the file so it looks like this:

```
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: local-sc
  annotations:
    storageclass.kubernetes.io/is-default-class: "true"
provisioner: kubernetes.io/no-provisioner
allowVolumeExpansion: true
volumeBindingMode: WaitForFirstConsumer
```

* Apply it with `kubectl apply -f <file.yaml>`

* **Question 2**

* Create a deployment named logging-deployment in the namespace logging-ns with 1 replica, with the following specifications:

The main container should be named app-container, use the image busybox, and should run the following command to simulate writing logs:

sh -c "while true; do echo 'Log entry' >> /var/log/app/app.log; sleep 5; done"

Add a sidecar container named log-agent that also uses the busybox image and runs the command:

tail -f /var/log/app/app.log

log-agent logs should display the entries logged by the main app-container

* Check the deployment documentation on the Kubernetes website.

https://kubernetes.io/docs/concepts/workloads/controllers/deployment/

* Use this example deployment file:

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80
```

* Edit the file like so:

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: logging-deployment
  namespace: logging-ns
spec:
  replicas: 1
  selector:
    matchLabels:
      app: logger
  template:
    metadata:
      labels:
        app: logger
    spec:
      volumes: 
        - name: log-volume
          emptyDir: {}
      containers:
      - name: app-container
        image: busy-box
        volumeMounts: 
          - name: log-volume
            mount: /var/log/app
        command: 
          - sh
          - c
          - "while true; do echo 'Log entry' >> /var/log/app/app.log; sleep 5; done"
      - name: log-agent
        image: busybox
        volumeMounts: 
          - name: log-volume
            mount: /var/log/app
        command:
          - tail
          - -f
          - /var/log/app/app.log
```

`/var/log/app` is the same directory in both containers.

* Then we apply the configuration:

```
kubectl apply -f <file.yaml>
```

* Check if it is logging or not:

```
kubectl logs logging-deployment-<container-name> -c log-agent -n logging-ns
```

* To follow the logs, use the `-f` flag:

```

kubectl logs logging-deployment-<container-name> -c log-agent -n logging-ns -f
```

* **Question 3**

* A Deployment named webapp-deploy is running in the ingress-ns namespace and is exposed via a Service named webapp-svc.

Create an Ingress resource called webapp-ingress in the same namespace that will route traffic to the service. The Ingress must:

    Use pathType: Prefix
    Route requests sent to path / to the backend service
    Forward traffic to port 80 of the service
    Be configured for the host kodekloud-ingress.app

Test app availablility using the following command:

curl -s http://kodekloud-ingress.app/

* Check the deployment with the following:

```
kubectl get deploy -n ingress-nss
```

* Check the service that is in use:

```
kubectl get svc -n ingress-nss
```

* Check the documentation and look for Ingress:

https://kubernetes.io/docs/concepts/services-networking/ingress/

* We create an Ingress Resource:

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: minimal-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  ingressClassName: nginx-example
  rules:
  - http:
      paths:
      - path: /testpath
        pathType: Prefix
        backend:
          service:
            name: test
            port:
              number: 80
```

* As this:

```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: webapp-ingress
  namespace: ingress-ns
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
    rules:
      - host: kodekloud-ingress.app
spec:
  ingressClassName: nginx
  rules:
  - host: kodekloud-ingress.app
  - http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: webapp-svc
            port:
              number: 80

```

* Apply the file:

```
kubectl apply -f <file.yaml>
```

* Run `kubectl get ingressclass` 

* Run a `curl` command to make sure it can connect to the app:

```
curl -s http://kodekloud-ingress.app
```

* **Question 4**

* Create a new deployment called nginx-deploy, with image nginx:1.16 and 1 replica. Next, upgrade the deployment to version 1.17 using rolling update.

* `kubectl create deployment nginx-deploy --image=nginx:1.16 --dry-run=client -o yaml > <file.yaml>`

* This would create a deployment file like so:

```
apiVersion: apps/v1
kind: Deployment
metadata: 
  creationTimestamp: null
  labels:
    app: nginx-deploy
  name: nginx-deploy
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx-deploy
  strategy: {}
  template:
    metadata:
      creationTimestamp: null
      labels:
        app: nginx-deploy
    spec:
      containers: 
      - image: nginx:1.16
        name: nginx
        resources: {}
status: {}
```

* Change the file to the following:

```
apiVersion: apps/v1
kind: Deployment
metadata: 
  creationTimestamp: null
  labels:
    app: nginx-deploy
  name: nginx-deploy
spec:
  strategy:
    type: RollingUpdate
  replicas: 1
  selector:
    matchLabels:
      app: nginx-deploy
  strategy: {}
  template:
    metadata:
      creationTimestamp: null
      labels:
        app: nginx-deploy
    spec:
      containers: 
      - image: nginx:1.16
        name: nginx
        resources: {}
status: {}
```

* Technically `RollingUpdate` is the default, so you don't need the following:

```
strategy:
  type: RollingUpdate
```

* Then apply the file with:

```
kubectl apply -f <file.yaml>
```

* Check for the Deployment with:

```
kubectl get deployment
```

* Check out the rollout history with:

```
kubectl rollout history deployment nginx-deploy
```

* To show more information about the `rollout`, run the following:

```
kubectl rollout history deployment nginx-deploy --revision=1
```

* Now to change the version of `nginx` to `1.17`, run:

```
kubectl set image deployment/nginx-deploy nginx=nginx:1.17
```

* If you again run `rollout history`, there are two versions shown:

```
kubectl rollout history deployment nginx-deploy
```

* Checking the latest version should show `1.17`:

```
kubectl rollout history deployment nginx-deploy --revision=1
```

* **Question 5**

* Create a new user called john. Grant him access to the cluster using a csr named john-developer. Create a role developer which should grant John the permission to create, list, get, update and delete pods in the development namespace . The private key exists in the location: /root/CKA/john.key and csr at /root/CKA/john.csr.

Important Note: As of kubernetes 1.19, the CertificateSigningRequest object expects a signerName.

Please refer to the documentation to see an example. The documentation tab is available at the top right of the terminal.

* A `csr` is a Certificate Signing Request.

* However, we need to create a Kubernetes object, for John to join the Kubernetes cluster.

* Go to the documentation and search for `Issue a Certificate for a Kubernetes API Client Using a CertificateSigningRequest`

* We create the CertificateSigningRequest object from this file:

```
cat <<EOF | kubectl apply -f -
apiVersion: certificates.k8s.io/v1
kind: CertificateSigningRequest
metadata:
  name: myuser # example
spec:
  # This is an encoded CSR. Change this to the base64-encoded contents of myuser.csr
  request: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURSBSRVFVRVNULS0tLS0KTUlJQ1ZqQ0NBVDRDQVFBd0VURVBNQTBHQTFVRUF3d0dZVzVuWld4aE1JSUJJakFOQmdrcWhraUc5dzBCQVFFRgpBQU9DQVE4QU1JSUJDZ0tDQVFFQTByczhJTHRHdTYxakx2dHhWTTJSVlRWMDNHWlJTWWw0dWluVWo4RElaWjBOCnR2MUZtRVFSd3VoaUZsOFEzcWl0Qm0wMUFSMkNJVXBGd2ZzSjZ4MXF3ckJzVkhZbGlBNVhwRVpZM3ExcGswSDQKM3Z3aGJlK1o2MVNrVHF5SVBYUUwrTWM5T1Nsbm0xb0R2N0NtSkZNMUlMRVI3QTVGZnZKOEdFRjJ6dHBoaUlFMwpub1dtdHNZb3JuT2wzc2lHQ2ZGZzR4Zmd4eW8ybmlneFNVekl1bXNnVm9PM2ttT0x1RVF6cXpkakJ3TFJXbWlECklmMXBMWnoyalVnald4UkhCM1gyWnVVV1d1T09PZnpXM01LaE8ybHEvZi9DdS8wYk83c0x0MCt3U2ZMSU91TFcKcW90blZtRmxMMytqTy82WDNDKzBERHk5aUtwbXJjVDBnWGZLemE1dHJRSURBUUFCb0FBd0RRWUpLb1pJaHZjTgpBUUVMQlFBRGdnRUJBR05WdmVIOGR4ZzNvK21VeVRkbmFjVmQ1N24zSkExdnZEU1JWREkyQTZ1eXN3ZFp1L1BVCkkwZXpZWFV0RVNnSk1IRmQycVVNMjNuNVJsSXJ3R0xuUXFISUh5VStWWHhsdnZsRnpNOVpEWllSTmU3QlJvYXgKQVlEdUI5STZXT3FYbkFvczFqRmxNUG5NbFpqdU5kSGxpT1BjTU1oNndLaTZzZFhpVStHYTJ2RUVLY01jSVUyRgpvU2djUWdMYTk0aEpacGk3ZnNMdm1OQUxoT045UHdNMGM1dVJVejV4T0dGMUtCbWRSeEgvbUNOS2JKYjFRQm1HCkkwYitEUEdaTktXTU0xMzhIQXdoV0tkNjVoVHdYOWl4V3ZHMkh4TG1WQzg0L1BHT0tWQW9FNkpsYWFHdTlQVmkKdjlOSjVaZlZrcXdCd0hKbzZXdk9xVlA3SVFjZmg3d0drWm89Ci0tLS0tRU5EIENFUlRJRklDQVRFIFJFUVVFU1QtLS0tLQo=
  signerName: kubernetes.io/kube-apiserver-client
  expirationSeconds: 86400  # one day
  usages:
  - client auth
EOF
```

* Change the above to the following:

```
apiVersion: certificates.k8s.io/v1
kind: CertificateSigningRequest
metadata:
  john-developer
spec:
  signerName: kubernetes.io/kube-apiserver-client 
  request: <base64-encoding-output-from-the-below-cat-command>
  usages:
    - digital signature
    - key encipherment
    - client auth
```

* To get the Certificate Signing Request, however the `request` property needs to be base64 encoded.

* `cat /root/CKA/john.csr`

```
cat /root/CKAjohn.csr | base64 | tr -d '\n'
```

* Once all done we apply the object with `kubectl apply -f <file.yaml>`.

* Check the Certificate Signing Request with the following:

```
kubectl get csr
```

* You can see that the certificate signing request is waiting for approval.

* To approve or reject it:

```
kubectl certificate approve john-developer
```

* The nrun `kubectl get csr` again to see it approved.

* Further checks:

```
kubectl get csr john-developer -o yaml 
```

* Under `Status`, that is the certificate that the user uses to access the cluster.

* To allow John to `create`, `list`, `get`, `update` and `delete` pods, we need an RBAC role. We create a new file:

```
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: developer 
  namespace: development
rules:
  - apiGroups: [""]
    resources: ["pods"]
    verbs: ["create", "list", "get", "update", "delete"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata: 
  name: john-developer-role-binding
  namespace: development
subjects: 
  - kind: User
    name: john
    apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: role
  name: developer
  apiGroup: rbac.authorization.k8s.io
```

* You can create multiple Kubernetes objects in one file with the `---` syntax.

* Apply the above role binding:

```
kubectl apply -f <role-binding>
```

* To test access that a user (current user) can do:

```
kubectl auth can-i create pods 
```

* We need to test with user john:

```
kubectl auth can-i create pods --as=john -n development
```

* The answer will be `yes`.

* If this is done in a namespace where John doesn't have permissions:

```
kubectl auth can-i create pods --as=john -n default
```

* The answer will be `no`.

* Regarding `apiGroups`, this is empty like `[""]`, we're giving permissions for pods as part of the `core` group. When using the `core` group, it is left empty like so `[""]`.

* You can then see the certificate available.

* Take the long line it outputs and place that in the `request` line.

* **Question 6**

* Create an nginx pod called nginx-resolver using the image nginx and expose it internally with a service called nginx-resolver-service. Test that you are able to look up the service and pod names from within the cluster. Use the image: busybox:1.28 for dns lookup. Record results in /root/CKA/nginx.svc and /root/CKA/nginx.pod

* Create the `nginx` pod with the following command:

```
kubectl run nginx-resolver --image=nginx
```

* `Expose it internally` from the question above basically means `ClusterIP`.

* If you want access outside of the cluster, use `NodePort` or `LoadBalancer`.

* Need to expose the pod:

```
kubectl expose pod nginx-resolver --name=nginx-resolver --port=80 --target-port=80 --type=ClusterIP
```

* Verify the service was created:

```
kubectl get svc
```

```
kubectl describe svc nginx-resolver-service
```

* The above will show one endpoint, which is the pod.

* Check the IP address of the `nginx-resolver`:

```
kubectl get pod -o wide
```

* Now we know the service is working as intended.

* We need to bring up an ephemeral container that runs one command.

```
kubectl run test-nslookup --image=busybox:1.28 --rm -it --restart=Never -- nslookup nginx-resolver-service
```

* From the above command, that should resolve the IP address of the service.

* The `--rm` means once we detach from the pod, it will be destroyed.

* Now will run the same command as above, but output the file into `/root/CKA/nginx.svc` and `/root/CKA/nginx.pod`.

```
kubectl run test-nslookup --image=busybox:1.28 --rm -it --restart=Never -- nslookup nginx-resolver-service > /root/CKA/nginx.svc
```

* Then to create a DNS entry for the pod IP like so:

```
kubectl run test-nslookup --image=busybox:1.28 --rm -it --restart=Never -- nslookup 172-17-1-18.default.pod
```

* Then we save the above output to a file:

```
kubectl run test-nslookup --image=busybox:1.28 --rm -it --restart=Never -- nslookup 172-17-1-18.default.pod > /root/CKA/nginx.pod
```

* **Question 7**

* Create a static pod on node01 called nginx-critical with the image nginx. Make sure that it is recreated/restarted automatically in case of a failure.

For example, use /etc/kubernetes/manifests as the static Pod path.

* Have to create a manifest / file on Node1.

* Run the `kubectl run` command:

```
kubectl run nginx-critical --image=nginx --dry-run=client -o yaml > static.yaml
```

* If you `cat` the above file, you'll observe this:

```
apiVersion: v1
kind: Pod
metadata:
  creationTimeStamp: null
  labels:
    run: nginx-critical
  name: nginx-critical
spec:
  containers: 
  - image: nginx
    name: nginx-critical
    resources: {}
  dnsPolicy: ClusterFirst
  restartPolicy: Always
status: {}
```

* `ssh` into Node1.

* Navigate towards `/etc/kubernetes/manifests`

* Create a file called `static.yaml`.

* Then in the `/etc/kubernetes/manifests` directory, we create a manifest for a pod that we want to create statically.

* Check the pods with:

```
kubectl get pod -o wide 
```

* When a pod is created statically, it is assigned to the node name.

* That's how you create a static pod in Kubernetes.

* **Question 8**

* Create a Horizontal Pod Autoscaler with name backend-hpa for the deployment named backend-deployment in the backend namespace with the webapp-hpa.yaml file located under the root folder.
Ensure that the HPA scales the deployment based on memory utilisation, maintaining an average memory usage of 65% across all pods.
Configure the HPA with a minimum of 3 replicas and a maximum of 15.

* Open up `web-app-hpa.yaml`:

```
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: webapp-hpa
  namespace: backend
spec:
  scaleTargetRef: 
    apiVersion: app/v1
    kind: Deployment
    name: kkapp-deploy
  minReplicas: 3
  maxReplicas: 15
```

* We change the above file to the following:

```
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: backend-hpa
  namespace: backend
spec:
  scaleTargetRef: 
    apiVersion: app/v1
    kind: Deployment
    name: backend-deployment
  minReplicas: 3
  maxReplicas: 15
  metrics:
    - type: Resource
      resource: 
        name: memory
        target:
          type: Utilization
          averageUtilization: 65
```

* Apply the file with:

```
kubectl apply -f webapp-hpa.yaml
```

* Do a describe to see what it shows:

```
kubectl describe hpa -n backend
```

* From the above command, you see the minimum and maximum replicas and the metrics that were previously set.

* **Question 9**

* Modify the existing web-gateway on cka5673 namespace to handle HTTPS traffic on port 443 for kodekloud.com, using a TLS certificate stored in a secret named kodekloud-tls.

* `ssh` into `cluster1-controlplane`.

* Check for the existing gateway:

```
kubectl get gateway -n cka5673
```

* You should be a ble to see some form of gateway created.

* Output the above gateway file to yaml:

```
kubectl get gateway -n cka5673 -o yaml > <file.yaml>
```

* Check the secrets:

```
kubectl get secret -n cka-5673
```

* This will show the TLS certificates.

* Open `file.yaml` and it will be a very large file. Items changed are:

```
port: 80 --> port: 443
protocol: HTTP --> protocol: HTTPS
hostname: kodekloud.com
tls:
  certificateRefs: 
    - name: kodekloud-tls
    
```

* The `kodekloud-tls` part points to the secret that we saw earlier.

* `kubectl apply -f <file.yaml>`

* **Question 10**

* On the cluster, the team has installed multiple helm charts on a different namespace. By mistake, those deployed resources include one of the vulnerable images called kodekloud/webapp-colour:v1. Find out the release name and uninstall it. 

* Need to find out what `helm` charts are installed, therefore:

```
helm list -A
```

* The `-A` is for all namespaces.

* Need to find the release that has an image that matches the name.

* Show the manifest generated by a Helm release:

```
helm get manifest <helm_chart> -n <namespace> | grep -i webapp-color:v1
```

* In this example, this shows the following:

```
image: "kodekloud/webapp-color:v1"
```

* Then we uninstall the chart with:

```
helm uninstall <release-name> -n <namespace>
```

* **Question 11**

* You are requested to create a NetworkPolicy to allow traffic from frontend apps located in the frontend namespace, to backend apps located in the backend namespace, but not from the databases in the databases namespace. There are three policies available in the /root folder. Apply the most restrictive policy from the provided YAML files to achieve the desired result. Do not delete any existing policies.

* Good command for namespaces:

```
kubectl get ns --show-labels
```

* Example NetworkPolicy that works for the above question:

```
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: net-policy-3
  namespace: backend
spec:
  podSelector: {}
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          name: frontend
    ports:
    - protocol: TCP
      port: 80
```

* An ingress policy will only apply the above configuration.

* Apply the above file:

```
kubectl apply -f <file.yaml>
```
