---
title: "CKA Training Schedule"
category: "cka-certification"
tags: ["cka-certification", "cka", "training", "schedule"]
---

# CKA Training Schedule

## Set Up Your Practice Environment

Yes, absolutely practice these mock exam questions on your own Kubernetes setup. This is crucial because:
- You'll develop muscle memory for kubectl commands
- You'll learn to troubleshoot real errors
- You'll get comfortable navigating between nodes, checking logs, and fixing issues

## Target Your Weak Areas

### Troubleshooting (highest priority)
Practice these scenarios repeatedly:
- Break things intentionally (wrong image names, incorrect ports, bad YAML syntax)
- Practice the troubleshooting flow: `kubectl get` → `kubectl describe` → `kubectl logs` → check system pods in kube-system
- Master checking component logs: kubelet, kube-apiserver, controller-manager
- Create a checklist for common issues (ImagePullBackOff, CrashLoopBackOff, Pending pods)

### Services and Networking
- Create services of all types (ClusterIP, NodePort, LoadBalancer) without looking at docs
- Practice Network Policies until you can write them from memory
- Set up Ingress controllers and routes multiple times
- Practice service discovery and DNS troubleshooting (nslookup, dig commands)

### Cluster Architecture, Installation & Configuration
- Install a cluster with kubeadm at least 5 times from scratch
- Practice joining/removing nodes
- Backup and restore etcd
- Upgrade cluster versions
- Configure different CNI plugins

## Practical Training Strategy

1. **Time-boxed practice**: Do each mock exam question with a timer (6-8 minutes per question)

2. **Build a command reference**: Create your own cheat sheet of frequently used commands:
   ```bash
   # Your most-used imperatives
   kubectl run pod --image=nginx --dry-run=client -o yaml
   kubectl create deployment name --image=image --replicas=n
   kubectl expose pod/deployment --port=x --target-port=y
   ```

3. **Practice without documentation first**, then with documentation to simulate exam conditions

4. **Daily drills** (30 minutes):
   - Monday: Troubleshooting broken deployments
   - Tuesday: Creating and configuring services
   - Wednesday: Network policies and ingress
   - Thursday: RBAC and security contexts
   - Friday: Storage (PV, PVC, StorageClass)
   - Weekend: Full mock exams

5. **Create failure scenarios**: Since troubleshooting is your weakest area, deliberately break working configurations and fix them:
   - Change image tags to non-existent ones
   - Modify port numbers in services
   - Delete critical labels that selectors depend on
   - Corrupt static pod manifests

## Exam-Specific Tips

- Bookmark these documentation pages: Pods, Deployments, Services, PersistentVolumes, NetworkPolicy, RBAC
- Learn to use `kubectl explain` efficiently: `kubectl explain pod.spec.containers`
- Master using `--dry-run=client -o yaml` for generating YAML templates
- Practice using `kubectl edit` vs creating new YAML files (know when each is faster)
- Get fast at using `grep`, `less`, and editing with `vi/vim`

## Red Flags to Address

Looking at your mock exams, ensure you can do these without thinking:
- Set up volumes shared between containers (emptyDir)
- Configure init containers
- Use ConfigMaps and Secrets as environment variables
- Create and troubleshoot static pods
- Modify deployments with rolling updates

Since you mentioned these mock questions appear in the actual exam, yes, practice them repeatedly until you can solve each one in under 5 minutes. But don't just memorise - understand why each step works.

The user wants deliberately broken Kubernetes scenarios to practice troubleshooting. This is a great request for their CKA exam prep since troubleshooting was their weakest area. I should create realistic broken scenarios that mirror what they might see in the exam, with varying difficulty levels. Each scenario should have clear symptoms, require specific troubleshooting steps, and have defined solutions. I'll organise them by category and include the commands to create the broken state and hints about what to look for.

## Deliberately Broken Kubernetes Scenarios for Troubleshooting Practice

### Scenario Set A: Pod/Deployment Issues

**Scenario 1: The Typo Hunter**
```bash
# Setup the broken deployment
kubectl create deployment web-app --image=nginx:1.23 --replicas=3
kubectl set image deployment/web-app nginx=nginxx:1.23
```
**Symptoms**: Deployment shows 0/3 ready
**Your mission**: Fix the deployment without deleting it
**Hidden issues**: Typo in image name + ImagePullBackOff

---

**Scenario 2: The Init Container Trap**
```yaml
# Apply this broken pod
apiVersion: v1
kind: Pod
metadata:
  name: app-pod
spec:
  initContainers:
  - name: init-db
    image: busybox
    command: ['sh', '-c', 'until nslookup mydb; do echo waiting for mydb; sleep 2; done']
  containers:
  - name: app
    image: nginx
```
**Symptoms**: Pod stuck in Init:0/1
**Your mission**: Make the pod run successfully
**Hint**: The service it's waiting for doesn't exist

---

**Scenario 3: The Command Confusion**
```yaml
# Apply this broken deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: logger
spec:
  replicas: 2
  selector:
    matchLabels:
      app: logger
  template:
    metadata:
      labels:
        app: logger
    spec:
      containers:
      - name: logger
        image: busybox
        args:
        - /bin/sh
        - -c
        - while true; do echo "logging" >> /var/log/app.log; sleep 5
```
**Symptoms**: CrashLoopBackOff
**Your mission**: Fix the container command
**Hidden issue**: Missing 'done' in the bash loop

### Scenario Set B: Service/Networking Issues

**Scenario 4: The Selector Mismatch**
```bash
# Create these mismatched resources
kubectl run backend --image=nginx --labels="app=backend,version=v1"
kubectl expose pod backend --name=backend-svc --port=80 --selector="app=back-end"
kubectl run test --image=busybox --rm -it --restart=Never -- wget backend-svc
```
**Symptoms**: Service has no endpoints
**Your mission**: Fix the service without recreating the pod

---

**Scenario 5: The Port Puzzle**
```yaml
# Apply this broken service setup
apiVersion: v1
kind: Pod
metadata:
  name: web
  labels:
    app: web
spec:
  containers:
  - name: web
    image: nginx
    ports:
    - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: web-svc
spec:
  selector:
    app: web
  ports:
  - port: 8080
    targetPort: 8080
```
**Symptoms**: Connection refused when accessing service
**Your mission**: Fix the service configuration

---

**Scenario 6: The Network Policy Blocker**
```yaml
# First, create a working app
kubectl run app --image=nginx --labels="tier=frontend"
kubectl expose pod app --port=80

# Then apply this network policy
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny
spec:
  podSelector: {}
  policyTypes:
  - Ingress
```
**Symptoms**: All pod-to-pod communication blocked
**Your mission**: Allow traffic to the app pod only

### Scenario Set C: Storage Issues

**Scenario 7: The Binding Blocker**
```yaml
# Create PV first
apiVersion: v1
kind: PersistentVolume
metadata:
  name: data-pv
spec:
  capacity:
    storage: 1Gi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: /data/pv1
  storageClassName: fast
---
# Create PVC that won't bind
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: data-pvc
spec:
  accessModes:
    - ReadWriteMany
  resources:
    requests:
      storage: 1Gi
  storageClassName: fast
```
**Symptoms**: PVC stuck in Pending
**Your mission**: Make PVC bind to PV without modifying PV

---

**Scenario 8: The Mount Mishap**
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: data-pod
spec:
  containers:
  - name: app
    image: nginx
    volumeMounts:
    - name: config
      mountPath: /etc/nginx/nginx.conf
      subPath: nginx.conf
  volumes:
  - name: config
    configMap:
      name: nginx-config
```
**Symptoms**: Pod in CrashLoopBackOff or CreateContainerError
**Your mission**: Fix the pod (ConfigMap doesn't exist)

### Scenario Set D: Cluster Component Issues

**Scenario 9: The Scheduler Strike**
```bash
# Break the scheduler (run on control plane)
sudo mv /etc/kubernetes/manifests/kube-scheduler.yaml /tmp/
# Or edit the static pod manifest and change the image name
```
**Symptoms**: New pods stuck in Pending state
**Your mission**: Restore scheduler functionality
**Debugging path**: Check kube-system pods → Static pod manifests

---

**Scenario 10: The Controller Crisis**
```bash
# Edit controller manager static pod
sudo vi /etc/kubernetes/manifests/kube-controller-manager.yaml
# Change: --bind-address=127.0.0.1 to --bind-address=127.0.0.2
```
**Symptoms**: Deployments not creating ReplicaSets, no pods created
**Your mission**: Fix the controller manager

---

**Scenario 11: The Kubelet Rebellion**
```bash
# On a worker node
sudo systemctl stop kubelet
# Or corrupt kubelet config
sudo vi /var/lib/kubelet/config.yaml
# Change clusterDNS IP to wrong address
```
**Symptoms**: Node becomes NotReady, pods can't resolve DNS
**Your mission**: Restore node to Ready state

### Scenario Set E: RBAC/Security Issues

**Scenario 12: The Permission Puzzle**
```bash
# Create service account and deployment
kubectl create sa app-sa
kubectl create deployment app --image=nginx
kubectl set sa deployment/app app-sa

# Pod tries to list services but can't
kubectl exec -it deployment/app -- sh -c "wget --spider --timeout=1 https://kubernetes.default/api/v1/namespaces/default/services"
```
**Symptoms**: 403 Forbidden errors from pod
**Your mission**: Grant minimal permissions needed

---

**Scenario 13: The Taint Trap**
```bash
# Taint all worker nodes
kubectl taint nodes node01 dedicated=special-user:NoSchedule
kubectl taint nodes node02 dedicated=special-user:NoSchedule
# Try to deploy
kubectl create deployment test --image=nginx --replicas=3
```
**Symptoms**: All pods Pending
**Your mission**: Make deployment run without removing taints

### Progressive Difficulty Challenges

**Challenge 1 - The Chain Reaction** (Multiple issues)
```yaml
# Apply this manifest with 4 deliberate errors
apiVersion: apps/v1
kind: Deployment
metadata:
  name: complex-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: complex-app
  template:
    metadata:
      labels:
        app: complex
    spec:
      serviceAccountName: app-runner
      containers:
      - name: app
        image: ngix:latest
        ports:
        - containerPort: 8080
        env:
        - name: DB_HOST
          valueFrom:
            secretKeyRef:
              name: db-secret
              key: host
```
**Issues to find**: 
1. Label mismatch
2. ServiceAccount doesn't exist
3. Image typo
4. Secret doesn't exist

---

**Challenge 2 - The Time Bomb** (Fix in order)
```bash
# Execute these in sequence
kubectl delete deployment coredns -n kube-system
kubectl create deployment critical-app --image=nginx
# Wait 30 seconds
kubectl expose deployment critical-app --port=80
# Try to access service by name - won't work
```
**Mission**: Restore cluster DNS and verify app works

### Practice Workflow for Each Scenario

1. **Observe symptoms** (30 seconds max)
   ```bash
   kubectl get pods/deploy/svc
   kubectl describe [resource]
   ```

2. **Gather evidence** (1 minute)
   ```bash
   kubectl logs [pod]
   kubectl get events --sort-by='.lastTimestamp'
   kubectl get endpoints
   ```

3. **Form hypothesis** (30 seconds)

4. **Fix and verify** (2 minutes)

5. **Document the fix** in your notes

### Troubleshooting Command Toolbox

Keep these handy during practice:
```bash
# Quick status checks
kubectl get all -A | grep -v Running
kubectl get events -A --sort-by='.lastTimestamp' | tail -20

# Pod debugging
kubectl describe pod [name] | grep -A 5 "Events:"
kubectl logs [pod] --previous  # For crash loops
kubectl exec -it [pod] -- sh

# Service debugging
kubectl get endpoints
kubectl run test --rm -it --image=busybox --restart=Never -- wget -O- service-name

# Node debugging
kubectl describe node | grep -i taint
kubectl get nodes -o wide
journalctl -u kubelet -f

# Component checks
kubectl get pods -n kube-system
sudo crictl ps  # On nodes
systemctl status kubelet
```

### Success Metrics

- Scenario 1-5: Should solve in <3 minutes each
- Scenario 6-10: Should solve in <5 minutes each  
- Scenario 11-13: Should solve in <4 minutes each
- Challenges: Should solve in <8 minutes total

Practice these scenarios repeatedly until you can diagnose and fix each one without referencing documentation. The key is developing intuition for what's wrong based on symptoms.

* Check these channels:

https://m.youtube.com/@jaydemytech

https://m.youtube.com/@ITKiddie

https://github.com/RahulKumar1119/cka-practice-questions

## Question 1

Create a new HorizontalPodAutoscaler (HPA) named apache-server in the autoscale namespace.
This HPA must target the existing Deployment called apache-server in the same namespace.

Set the HPA to target 50% CPU usage per Pod.

Configure the HPA to have a minimum of 1 Pod and a maximum of 4 Pods.

Additionally, set the downscale stabilisation window to 30 seconds.

---

kubectl create namespace autoscale

apiVersion: apps/v1
kind: Deployment
metadata:
  name: apache-server
  labels:
    app: httpd
spec:
  replicas: 3
  selector:
    matchLabels:
      app: httpd
  template:
    metadata:
      labels:
        app: httpd
    spec:
      containers:
      - name: httpd
        image: httpd:latest
        ports:
        - containerPort: 80

---

kubectl autoscale deployment apache-server \
  --cpu-percent=50 \
  --min=1 \
  --max=4 \
  -n autoscale \
  --name=apache-server

kubectl edit hpa apache-server -n autoscale

---

apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: apache-server
  namespace: autoscale
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: apache-server
  minReplicas: 1
  maxReplicas: 4
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilisation
        averageUtilisation: 50
  behaviour:
    scaleDown:
      stabilizationWindowSeconds: 30

---

## Question 2

An NGINX Deployment named nginx-static is running in the nginx-static namespace.
It is configured using a ConfigMap named nginx-config.

👉 Update the nginx-config ConfigMap to allow only TLSv1.3 connections.
Re-create, restart, or scale resources as necessary.

You can test the changes using the following command:

curl --tls-max 1.2 https://web.k8s.local


As TLSv1.2 should not be allowed anymore, the above command should fail.

---

apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-static
  namespace: nginx-static
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
      - name: nginx-static
        image: nginx:1.14.2
        ports:
        - containerPort: 80
        env:
        - name: SPECIAL_LEVEL_KEY
          valueFrom:
            configMapKeyRef:
              name: nginx-static
              key: akey

---
# 1. Namespace
apiVersion: v1
kind: Namespace
metadata:
  name: nginx-static

---
# 2. ConfigMap with initial NGINX configuration (allows TLSv1.2 and TLSv1.3)
apiVersion: v1
kind: ConfigMap
metadata:
  name: nginx-config
  namespace: nginx-static
data:
  nginx.conf: |
    events {
        worker_connections 1024;
    }
    http {
        server {
            listen 80;
            server_name web.k8s.local;
            
            location / {
                return 301 https://$server_name$request_uri;
            }
        }
        
        server {
            listen 443 ssl;
            server_name web.k8s.local;
            
            ssl_certificate     /etc/nginx/tls/tls.crt;
            ssl_certificate_key /etc/nginx/tls/tls.key;
            
            # Initially allows both TLSv1.2 and TLSv1.3
            ssl_protocols TLSv1.2 TLSv1.3;
            ssl_prefer_server_ciphers on;
            ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384;
            
            location / {
                root /usr/share/nginx/html;
                index index.html;
            }
        }
    }

---
# 3. Secret for TLS certificates (self-signed for testing)
apiVersion: v1
kind: Secret
metadata:
  name: nginx-tls
  namespace: nginx-static
type: kubernetes.io/tls
data:
  # These are base64 encoded self-signed certificates for testing
  # In production, use proper certificates
  tls.crt: |
    LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSURQekNDQWllZ0F3SUJBZ0lVZjhKbTdh
    L3VoZHJyOHZYMTF3NWxXbVpKcFRvd0RRWUpLb1pJaHZjTkFRRUwKQlFBd0x6RUxNQWtHQTFV
    RUJoTUNWVk14Q3pBSkJnTlZCQWdNQWtOQk1STXdFUVlEVlFRRERBcDNaV0l1CmF6aHpMbXh2
    WTJGc01CNFhEVEkwTURFeE9ERXpNVFF3TkZvWERUSTFNREV4TnpFek1UUXdORm93THpFTE1B
    a0cKQTFVRUJoTUNWVk14Q3pBSkJnTlZCQWdNQWtOQk1STXdFUVlEVlFRRERBcDNaV0l1YXpo
    ekxteHZZMkZzCk1JSUJJakFOQmdrcWhraUc5dzBCQVFFRkFBT0NBUThBTUlJQkNnS0NBUUVB
    MHVyRWtyY1JMMjZsNldLMGpGZW8KZVdJNlN3aDJRa1hVZ2F5N01qQzFTUGx3NCtDb3NkQU9V
    VUJzU0JXQ2ZtWHhmSm5aUGNRV2lGRGQyNmNSUgpTS1BNazJIeGUvVjE5cUJSZU9LYjJ3R1Jy
    VENSb1NCdC9NL1dtRE9KYjg5aEhXMG45RWlZZnhhUEtGdXdzCkl0b3haWGl3NFQ5Z0FsdlJT
    bE14OG9HWTJhY3k3QjhqZkRnZHJ2dVJBT1BXdDh0dHp1VzJpT1BOQ3VRSGYKNGtXcUpIY2NP
    T2pZUmFPYkFDWGxueFJvL0V2R3JqRElPeG1XOG5zZnI3WlhIRGNGR2FBczMxREsvR2VVNQpZ
    SzBZUnFrdWFQQktTTWNWT0VhRFdleTY0dW1wQ0JadWg3VGUzVG5OaGh3aEtxanV3cDRxemRX
    Q0xJQmpsCjJRSURBUUFCbzFNd1VUQWRCZ05WSFE0RUZnUVVLNGVnMHgrOEgyZnN6MGU2RjdY
    VTZlUnJTcGN3SHdZRApWUjBqQkJnd0ZvQVVLNGVnMHgrOEgyZnN6MGU2RjdYVTZlUnJTcGN3
    RHdZRFZSMFRBUUgvQkFVd0F3RUIKL3pBTkJna3Foa2lHOXcwQkFRc0ZBQU9DQVFFQW53dGlD
    NnArQXdvcVRBaW9oeGRlL3BsUm9kWFRVOFgzVgpWMGkwRnFDY3FlU1hOSkQ5OHlQSWlabE4r
    UFBzSnpCcU55RlpBWU16N1FQWThaQmlyb1ROTDBidlVGQmdRClYzWGxBdStQdVpKa2VsS0Zs
    T0NvdC84a1owMXhTTE5tQkdQTmZ6dGJZUGVpNmtTZ3o3R1I3dnpTRjAzWHoKSGhMQjRVRGhx
    RVRWZGlpRVBJcVQ3RHJSZzExRGwrcGJRdFh4ZDhoQndFNUFGQkRpVGxoQW1wSTJpczBWTQpT
    azIrUFVNMVdhQkFJTGR5MFlmRnJJTm9zQXVjRjdub1RkaFRIcjFKaGdZZkhUQmlmT2hCb01L
    VnhXY0JECnBuT05heG5KWGFaQ1RsNGhONlJlQjQ1dDh3K3pFSE05dGJ3aWJFa21GTElVRGJN
    SGJ6VzN5dU5JbnEwOEcKamc9PQotLS0tLUVORCBDRVJUSUZJQ0FURS0tLS0t
  tls.key: |
    LS0tLS1CRUdJTiBQUklWQVRFIEtFWS0tLS0tCk1JSUV2UUlCQURBTkJna3Foa2lHOXcwQkFR
    RUZBQVNDQKTV3TUlJRWl3SUJBQUtDQVFFQTB1ckVrcmNSTDIKNmw2V0swalplb2VXSTZTd2gy
    UWtYVWdheTdNakMxU1BsdzQrQ29zZEFPVVVCc1NCVytmbVh4ZkpuWlBjUQpXaUZEZDI2Y1JS
    U0tQTWsySHhlL1YxOXFCUmVPS2Iyd0dSclRDUm9TQnQvTS9XbURPSmI4OWhIVzBuOUVpCllm
    eGFQS0Z1d3NJdG94WlhpdzRUOWdBbHZSU2xNeDhvR1kyYWN5N0I4amZEZ2RydnVSQU9QV3Q4
    dHR6dVcKMmlPUE5DdVFIZjRrV3FKSGNjT09qWVJhT2JBQ1hsbnhSby9FdkdyakRJT3htVzhu
    c2ZyN1pYSERjRkdhQQpzMzFESy9HZVU1WUswWVJxa3VhUEJLU01jVk9FYURXZXk2NHVtcENC
    WnVoN1RlM1RuTmhod2hLcWp1d3A0CnF6ZFdDTElCamwyUUlEQVFBQkFvSUJBQkoyU0h2NFNR
    OE1BT3N0NmlHSGJnMTVJa3pkUHZSU3MxUktCK3oKZ2ZXTDZIbXRaOTk4elM3Q2hYQzNHTUk4
    OXZyRFlIY1kxWGN4RUV6dUU4QnRQNllPL1lMS21hT1BCQWh1RApjbzRaT3RIUTRrVTM0b29B
    d09zRDdXQWRqQnhQbkhaR09xN0hBRzM2UE1qd3oyUTBOdmtRRUlZN05IU2s4ClV6VGJNSnph
    cThQRE9rREo0TnJodmJ3a0hiQW00UERqaDNueUFUdDREWnJrL3RBeEtJTHdDOG9tRW9EdzYK
    NjZLOE5KRVl2QUF3YXQvOHJQTGxBOE50MlgzQStuYUFJQUQyWVVhaURXNUlrOXBQQndGbGpW
    aXphS1JQTQpGRU1jQUFYaWlCRUpwSjZLN0J2dW1kSHJIY3VRNlJLUUc5WEhJQ1JzSUhrTUVu
    aTdyRXRvUXBKSyt0ZTRJCkJZekNnWUVBNlpnRUhNZ1BXc3JrRzlBQUdwZ1pLV3pWMTNOSGxw
    QzlXNXFmY2k1TGl4QjdSVGppU1I2RUoKd1FHcXBObE9jZFhjdERyUGxGQk5TTnNKSEdtQzRt
    UjJoRXJ0dzVxWldnNEJGTkhPOGpQdlpUQ3lxVllPZgpFeU5hRmxERGFzNEg2VWQwbnBaSmRY
    Sm9oWXpQWmdnR0I0RUtwUGdGVENJMXRsRjVNRXNDZ1lFQTU0MU1uCm51TVB4d1FpQkRQY0pY
    Mk93L0xXV09aUFhQc3ZrbE1LRWRCbStjRnhCSVRTMXdZb2NabmwrSnRyaGxOSnMKNHJOZzhs
    VmpCTVNyNG1FSVhwS0g3SHJJSWdUb2hxRXQxeXBXR1RMSStPQ1pYcjZ3Y2xJYlJCWXdYQWxF
    dgpJeFhXTEVOdGhOVDJkVTJXUlVOMGo5dzJQRnRRMnBxWnVabVhOYzhDZ1lFQTJOaGxoQllX
    NjdGQWNqZ3VGClppT2J5elJYdUpCaGFvUitBTmxWRU5GUGJxV2hkRHNWRWRYdkpGaGFGRTJr
    UmlBSzdGRzdxRzRJT1NUSXoKbS9mMEF0RDFNL0FGRzRUY1p3T0JaTnVQQ0RkMkxSSGVqUUdI
    UktiVGl6azJsOGMyTzZvNG54ZE5LNUhtbgpFdTJoQ1o2NUpOVXMwZVFSc2xLa0JrbFFjQ01D
    Z1lFQXgzdGw1M0E5aFlKcFNkdXppQkQ4UkFoZ3hJSFh2CnJoMVBISXFSeHBMWWFncTNUQ0J5
    WFhjT3d0QmpGNEFEQitIa09aQTV3ZXNSZ0JnSEVwSFpycnN4Y3JwT0IKK0dyVGxOQU5TcVZC
    TEdvbnJaMEJJY2FJeTNQK1RXOEdVT29xazE0NlZqN3hDUFViUlY0RWM3Q24xQzhJaApudVBu
    OGdCbFhIZGdnRFVDZ1lFQXY0Y2hzUW5NTmxFQ3BUdGtXdlhzQ1JTbjBnVDJGQUdJTENTTUJN
    YzRLCkZCUWJGb1NHSk5GQ1JQUHRiREcwcFBWa1Z4QktqK1QwQXhsSUt5dmNUeWJsbnVSSzRu
    MUpLbHBJSldjS2gKbkFhdGx5YkVpRGIxdnNLcHRmVGNDQ1hGVGJGdEZUUVdteWU0enFCODdZ
    eDdNa3c3Q3hnUUNTYTJjZnJaagpWdVU9Ci0tLS0tRU5EIFBSSVZBVEUgS0VZLS0tLS0=

---
# 4. Static HTML content ConfigMap
apiVersion: v1
kind: ConfigMap
metadata:
  name: nginx-html
  namespace: nginx-static
data:
  index.html: |
    <!DOCTYPE html>
    <html>
    <head>
        <title>NGINX TLS Test</title>
    </head>
    <body>
        <h1>NGINX Static Content</h1>
        <p>TLS Configuration Test Page</p>
        <p>This page is served over HTTPS with specific TLS version requirements.</p>
    </body>
    </html>

---
# 5. NGINX Deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-static
  namespace: nginx-static
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx-static
  template:
    metadata:
      labels:
        app: nginx-static
    spec:
      containers:
      - name: nginx
        image: nginx:alpine
        ports:
        - containerPort: 80
          name: http
        - containerPort: 443
          name: https
        volumeMounts:
        - name: nginx-config
          mountPath: /etc/nginx/nginx.conf
          subPath: nginx.conf
        - name: nginx-tls
          mountPath: /etc/nginx/tls
          readOnly: true
        - name: nginx-html
          mountPath: /usr/share/nginx/html
        resources:
          requests:
            memory: "64Mi"
            cpu: "100m"
          limits:
            memory: "128Mi"
            cpu: "200m"
      volumes:
      - name: nginx-config
        configMap:
          name: nginx-config
      - name: nginx-tls
        secret:
          secretName: nginx-tls
      - name: nginx-html
        configMap:
          name: nginx-html

---
# 6. Service to expose NGINX
apiVersion: v1
kind: Service
metadata:
  name: nginx-static
  namespace: nginx-static
spec:
  type: NodePort
  selector:
    app: nginx-static
  ports:
  - port: 80
    targetPort: 80
    protocol: TCP
    name: http
    nodePort: 30080
  - port: 443
    targetPort: 443
    protocol: TCP
    name: https
    nodePort: 30443

---
# 7. Ingress (Optional - if you have an Ingress controller)
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: nginx-static
  namespace: nginx-static
spec:
  rules:
  - host: web.k8s.local
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: nginx-static
            port:
              number: 443

## Question 3

You are tasked with migrating an existing web application from Ingress to the Gateway API while maintaining HTTPS access.

    A GatewayClass named nginx is already installed in the cluster.

    An existing Ingress resource named web exposes a Deployment via a Service named web-svc, using TLS with a Secret named web-tls.

You must:

1. Create a Gateway named web-gateway with hostname gateway.web.k8s.local that maintains the existing TLS configuration.

2. Create an HTTPRoute named web-route with hostname gateway.web.k8s.local that maintains the same routing rules as the current Ingress (web).

3. Test access using:

curl -k https://gateway.web.k8s.local

Finally, delete the old Ingress resource named web.

⚡ Note: The Deployment and Service for web already exist in the cluster.

apiVersion: gateway.networking.k8s.io/v1
kind: GatewayClass
metadata:
  name: nginx
spec:
  controllerName: example.com/gateway-controller
 
 The user wants me to create the test environment setup steps for this specific CKA practice question about migrating from Ingress to Gateway API. I need to create the setup that provides the initial state WITHOUT including the solution. 

So I need to set up:
1. A GatewayClass named nginx (mentioned as already installed)
2. An existing Ingress resource named "web" 
3. A TLS Secret named "web-tls"
4. A Deployment and Service named "web-svc" that the Ingress exposes
5. The initial setup should have the Ingress working with HTTPS

The user will then need to:
- Create the Gateway
- Create the HTTPRoute
- Test it
- Delete the old Ingress

Let me create comprehensive setup steps for their two-node Kubernetes cluster.

Here are the test environment setup steps for this Gateway API migration scenario on your two-node Kubernetes cluster:

## Test Environment Setup Steps

### Prerequisites
```bash
# Ensure you're on the correct cluster context
kubectl config current-context

# Create a namespace for this exercise (optional, or use default)
kubectl create namespace gateway-migration
kubectl config set-context --current --namespace=gateway-migration
```

### Step 1: Install Gateway API CRDs
```bash
# Install the Gateway API CRDs (if not already installed)
kubectl apply -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.0.0/standard-install.yaml

# Verify CRDs are installed
kubectl get crd gatewayclasses.gateway.networking.k8s.io
kubectl get crd gateways.gateway.networking.k8s.io
kubectl get crd httproutes.gateway.networking.k8s.io
```

### Step 2: Set up NGINX Gateway Controller
```bash
# Install NGINX Gateway Fabric (Gateway API implementation)
kubectl apply -f https://raw.githubusercontent.com/nginxinc/nginx-gateway-fabric/v1.2.0/deploy/manifests/nginx-gateway.yaml

# Wait for the controller to be ready
kubectl wait --timeout=5m -n nginx-gateway deployment/nginx-gateway --for=condition=Available

# Create the GatewayClass named 'nginx'
cat <<EOF | kubectl apply -f -
apiVersion: gateway.networking.k8s.io/v1
kind: GatewayClass
metadata:
  name: nginx
spec:
  controllerName: gateway.nginx.org/nginx-gateway-controller
EOF
```

### Step 3: Create the Web Application Deployment
```bash
cat <<EOF | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
      - name: nginx
        image: nginx:alpine
        ports:
        - containerPort: 80
        volumeMounts:
        - name: html
          mountPath: /usr/share/nginx/html
      initContainers:
      - name: setup
        image: busybox
        command: ['sh', '-c', 'echo "<h1>Web Application - Ingress Version</h1><p>Hostname: \$(hostname)</p>" > /usr/share/nginx/html/index.html']
        volumeMounts:
        - name: html
          mountPath: /usr/share/nginx/html
      volumes:
      - name: html
        emptyDir: {}
EOF
```

### Step 4: Create the Service
```bash
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Service
metadata:
  name: web-svc
spec:
  selector:
    app: web
  ports:
  - port: 80
    targetPort: 80
    protocol: TCP
EOF
```

### Step 5: Create TLS Certificate and Secret
```bash
# Generate a self-signed certificate for testing
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout tls.key -out tls.crt \
  -subj "/CN=gateway.web.k8s.local/O=gateway-migration" \
  -addext "subjectAltName = DNS:gateway.web.k8s.local"

# Create the TLS secret
kubectl create secret tls web-tls \
  --cert=tls.crt \
  --key=tls.key

# Clean up the local certificate files
rm tls.crt tls.key
```

### Step 6: Install NGINX Ingress Controller (for the existing Ingress)
```bash
# Install NGINX Ingress Controller
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.10.0/deploy/static/provider/baremetal/deploy.yaml

# Wait for the ingress controller to be ready
kubectl wait --timeout=5m -n ingress-nginx deployment/ingress-nginx-controller --for=condition=Available

# Get the NodePort for the ingress controller (for testing)
kubectl get svc -n ingress-nginx ingress-nginx-controller
```

### Step 7: Create the Existing Ingress Resource
```bash
cat <<EOF | kubectl apply -f -
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: web
  annotations:
    nginx.ingress.kubernetes.io/ssl-redirect: "true"
spec:
  tls:
  - hosts:
    - gateway.web.k8s.local
    secretName: web-tls
  rules:
  - host: gateway.web.k8s.local
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: web-svc
            port:
              number: 80
EOF
```

### Step 8: Configure Local DNS (for testing)
```bash
# Get the IP of one of your nodes
NODE_IP=$(kubectl get nodes -o jsonpath='{.items[0].status.addresses[?(@.type=="InternalIP")].address}')

# Add entry to /etc/hosts (you may need sudo)
echo "$NODE_IP gateway.web.k8s.local" | sudo tee -a /etc/hosts

# Note: If using NodePort, get the HTTPS port
INGRESS_HTTPS_PORT=$(kubectl get svc -n ingress-nginx ingress-nginx-controller -o jsonpath='{.spec.ports[?(@.name=="https")].nodePort}')
echo "Ingress HTTPS NodePort: $INGRESS_HTTPS_PORT"
```

### Step 9: Verify the Current Ingress Setup
```bash
# Check all resources are created
kubectl get deployment web-deployment
kubectl get service web-svc
kubectl get secret web-tls
kubectl get ingress web
kubectl get gatewayclass nginx

# Test the current Ingress (replace NodePort if needed)
curl -k https://gateway.web.k8s.local:$INGRESS_HTTPS_PORT

# You should see the web application response
```

### Step 10: Prepare Gateway API Testing
```bash
# Get the Gateway API controller service details
kubectl get svc -n nginx-gateway

# Note the NodePort for HTTPS (you'll need this for testing after migration)
GATEWAY_HTTPS_PORT=$(kubectl get svc -n nginx-gateway nginx-gateway -o jsonpath='{.spec.ports[?(@.name=="https")].nodePort}' 2>/dev/null || echo "443")
echo "Gateway HTTPS Port: $GATEWAY_HTTPS_PORT"
```

## Question 4

Install and configure a Container Network Interface (CNI) of your choice that meets the specified requirements. 
You may choose from one of the following options:

Flannel using the manifest:

https://github.com/flannel-io/flannel/releases/download/v0.26.1/kube-flannel.yml


Calico using the manifest:

https://raw.githubusercontent.com/projectcalico/calico/v3.29.2/manifests/tigera-operator.yaml

Requirements:

Pods must be able to communicate with each other.

The CNI must support NetworkPolicy enforcement.

Install the CNI using manifest files only (do not use Helm).

Verify that the selected CNI is properly installed and configured in the cluster.

## Questino 5

Install Argo CD in the cluster:

Add the official Argo CD Helm repository with the name argo.

The Argo CD CRDs have already been pre-installed in the cluster.

Generate a Helm template of the Argo CD Helm chart version 7.7.3 for the argocd namespace and save it to /argo-helm.yaml.

Configure the chart to not install CRDs.

Install Argo CD using Helm with release name argocd, using the same version (7.7.3) and configuration as used in the template.

Install it in the argocd namespace and configure it to not install CRDs.

You do not need to configure access to the Argo CD server UI.

## Question 6

create a PriorityClass named high-priority with a value = (highest existing user-defined priority class value - 1).

Patch the existing Deployment busybox-logger in namespace priority to use this PriorityClass.

Ensure rollout works.

Other Pods in namespace may be evicted.

Do not modify other Deployments.

## Question 7

Reconfigure the existing Deployment front-end in namespace sp-culator:

Expose port 80/tcp of container nginx.

Create a Service front-end-svc:

Expose container port 80/tcp.

Type should be NodePort to expose pods individually.

## Question 8

Create a new StorageClass named low-latency that uses the existing provisioner rancher.io/local-path.

Set the VolumeBindingMode to WaitForFirstConsumer for this new StorageClass.

Make the new low-latency StorageClass the default for the cluster.

Do not modify any existing Deployments or PersistentVolumeClaims as part of this process.

## Question 9

iThe question presents a scenario where a legacy application needs its logs integrated into Kubernetes' logging system. The task is to:

Update an existing Deployment named synergy-deployment.

Add a new co-located container (a "sidecar") named sidecar to the Pod.

The sidecar container should use the busybox:stable image.

The sidecar container must run the command: /bin/sh -c "tail -n+1 -f /var/log/synergy-deployment.log".

Use a Volume mounted at /var/log to make the log file, synergy-deployment.log, accessible to both the main application container and the new sidecar container.

Do not modify the existing container's specification other than what is required to complete the task.

## Question 10

Task 1: List Custom Resource Definitions (CRDs)
Create a list of all cert-manager Custom Resource Definitions (CRDs).

Save this list to the file ~/resources.yaml.

You must use kubectl's default output format.

Do not explicitly set an output format with flags like -o yaml or -o json.

Task 2: Extract Documentation
Using kubectl, extract the documentation for the subject specification field of the Certificate Custom Resource.

Save this documentation to the file ~/subject.yaml.

You may use any output format that kubectl supports for this part.

## Question 11

The task is to adjust the resource requests for a WordPress application with 3 replicas in the relative-fawn namespace.

Here are the specific instructions:

The total node resources are CPU: 1 core and Memory: 2015360 Ki.

You need to divide these resources evenly among the 3 pods.

The application consists of both containers and init containers, and they should have the exact same requests.

You are not required to change any resource limits.

A helpful hint is provided: you may temporarily scale the Deployment to 0 replicas while making the changes.

After the updates, you must confirm that the WordPress Deployment has 3 replicas and all Pods are running and ready.

## Question 12

A user accidentally deleted the MariaDB Deployment in the mariadb namespace, which was configured with persistent storage.
Your responsibility is to re-establish the Deployment while ensuring data is preserved by reusing the available PersistentVolume.

The specific tasks are:

A PersistentVolume (PV) already exists and is retained for reuse.

Create a PersistentVolumeClaim (PVC) named mariadb in the mariadb namespace with the following specifications:

Access mode: ReadWriteOnce

Storage: 250Mi

Edit the MariaDB Deployment file located at ~/mariadb-deploy.yaml to use the PVC created in the previous step.

Apply the updated Deployment file to the cluster.

Ensure the MariaDB Deployment is running and Stable.

## Question 13

The task is to:

Create a new Ingress resource named echo in the echo-sound namespace.

Expose the Service echoserver-service on http://example.org/echo using Service port 8080.

The question also provides a command to check the availability of the service, curl -o /dev/null -s -w "%{http_code}\n" http://example.org/echo, which is expected to return 200.

## Question 14

The main objective is to prepare a Linux system for Kubernetes using kubeadm. Docker is already installed, and the user needs to configure it.

The specific tasks are:

Set up cri-dockerd:

Install the Debian package ~/cri-dockerd_0.3.9-0.ubuntu-jammy_amd64.deb.

Use dpkg to install the package.

Enable and start the cri-dockerd service.

Configure system parameters:

Set net.bridge.bridge-nf-call-iptables to 1.

Set net.ipv6.conf.all.forwarding to 1.

Set net.ipv4.ip_forward to 1.

Set net.netfilter.nf_conntrack_max to 131072.

## Question 15

The scenario involves a frontend deployment and a backend deployment, located in their respective namespaces (frontend and backend). The task is to establish communication between them.

The instructions are as follows:

Analyze: Inspect the existing frontend and backend deployments to understand their communication requirements.

Apply: From the ~/netpol folder, choose one of the provided NetworkPolicy YAML files to apply.

The chosen NetworkPolicy must:

Allow communication between the frontend and backend deployments.

Be as restrictive as possible (least permissive).

Not delete or change the existing "deny-all" network policies.

## Question 16

Fix a broken single-node Kubernetes cluster that was migrated to a new machine. The cluster was provisioned with kubeadm and uses an external etcd server.

Task:

Identify and investigate the broken cluster components.

Fix the configuration of all broken components.

Restart necessary services and components.

Ensure the cluster, node, and all pods are in a Ready state.
