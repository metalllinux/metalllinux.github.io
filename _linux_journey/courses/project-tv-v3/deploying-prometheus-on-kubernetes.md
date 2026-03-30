---
title: "Deploying Prometheus on Kubernetes"
category: "project-tv-v3"
tags: ["project-tv-v3", "prometheus", "monitoring", "kubernetes", "observability"]
---

## Deploying Prometheus on Kubernetes

Prometheus is an open-source monitoring and alerting toolkit designed for reliability and scalability. This guide covers deploying Prometheus on a kubeadm-managed Kubernetes cluster, with RBAC, service discovery, and persistent storage.

### Prerequisites

- A working Kubernetes cluster (kubeadm, with at least one control plane and one worker node)
- `kubectl` configured and able to reach the cluster
- A namespace for your workloads (this guide uses a dedicated namespace)

### Step 1: Create the namespace

If you haven't already, create a namespace for your applications:

```bash
kubectl create namespace my-namespace
```

### Step 2: Set up RBAC

Prometheus needs permission to discover and scrape pods and nodes. Create a ServiceAccount, ClusterRole, and ClusterRoleBinding:

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: prometheus
  namespace: my-namespace
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: prometheus
rules:
- apiGroups: [""]
  resources:
  - nodes
  - nodes/proxy
  - services
  - endpoints
  - pods
  verbs: ["get", "list", "watch"]
- apiGroups: [""]
  resources:
  - configmaps
  verbs: ["get"]
- nonResourceURLs: ["/metrics"]
  verbs: ["get"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: prometheus
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: prometheus
subjects:
- kind: ServiceAccount
  name: prometheus
  namespace: my-namespace
```

Apply it:

```bash
kubectl apply -f rbac.yaml
```

### Step 3: Create the Prometheus configuration

Store the Prometheus configuration in a ConfigMap. This example configures Prometheus to scrape itself, Kubernetes nodes, and any pods with the annotation `prometheus.io/scrape: "true"`:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: prometheus-config
  namespace: my-namespace
data:
  prometheus.yml: |
    global:
      scrape_interval: 15s
      evaluation_interval: 15s

    scrape_configs:
    - job_name: 'prometheus'
      static_configs:
      - targets: ['localhost:9090']

    - job_name: 'kubernetes-nodes'
      kubernetes_sd_configs:
      - role: node
      relabel_configs:
      - action: labelmap
        regex: __meta_kubernetes_node_label_(.+)

    - job_name: 'kubernetes-pods'
      kubernetes_sd_configs:
      - role: pod
        namespaces:
          names:
          - my-namespace
      relabel_configs:
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
        action: keep
        regex: true
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_path]
        action: replace
        target_label: __metrics_path__
        regex: (.+)
      - source_labels: [__address__, __meta_kubernetes_pod_annotation_prometheus_io_port]
        action: replace
        regex: ([^:]+)(?::\d+)?;(\d+)
        replacement: $1:$2
        target_label: __address__
      - action: labelmap
        regex: __meta_kubernetes_pod_label_(.+)
      - source_labels: [__meta_kubernetes_namespace]
        action: replace
        target_label: kubernetes_namespace
      - source_labels: [__meta_kubernetes_pod_name]
        action: replace
        target_label: kubernetes_pod_name
```

Apply it:

```bash
kubectl apply -f configmap.yaml
```

### Step 4: Create the Deployment

Deploy Prometheus with a hostPath volume for persistent data. If you have multiple nodes, you can use a `nodeSelector` to pin Prometheus to a specific worker node:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: prometheus
  namespace: my-namespace
  labels:
    app: prometheus
spec:
  replicas: 1
  selector:
    matchLabels:
      app: prometheus
  template:
    metadata:
      labels:
        app: prometheus
    spec:
      serviceAccountName: prometheus
      nodeSelector:
        kubernetes.io/hostname: my-worker-node
      containers:
      - name: prometheus
        image: prom/prometheus:latest
        args:
        - "--config.file=/etc/prometheus/prometheus.yml"
        - "--storage.tsdb.path=/prometheus"
        - "--storage.tsdb.retention.time=30d"
        - "--web.console.libraries=/usr/share/prometheus/console_libraries"
        - "--web.console.templates=/usr/share/prometheus/consoles"
        ports:
        - containerPort: 9090
          name: http
        volumeMounts:
        - name: config
          mountPath: /etc/prometheus
        - name: data
          mountPath: /prometheus
        resources:
          requests:
            memory: "256Mi"
            cpu: "200m"
          limits:
            memory: "512Mi"
            cpu: "500m"
        livenessProbe:
          httpGet:
            path: /-/healthy
            port: 9090
          initialDelaySeconds: 15
          periodSeconds: 30
        readinessProbe:
          httpGet:
            path: /-/ready
            port: 9090
          initialDelaySeconds: 5
          periodSeconds: 10
      volumes:
      - name: config
        configMap:
          name: prometheus-config
      - name: data
        hostPath:
          path: /var/lib/prometheus/data
          type: DirectoryOrCreate
```

Apply it:

```bash
kubectl apply -f deployment.yaml
```

> **Note:** Remove the `nodeSelector` block if you only have a single node, or replace `my-worker-node` with the hostname of your target node (check with `kubectl get nodes`).

### Step 5: Expose the service

Create a NodePort service so Prometheus is accessible from outside the cluster:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: prometheus
  namespace: my-namespace
  labels:
    app: prometheus
spec:
  type: NodePort
  selector:
    app: prometheus
  ports:
  - name: http
    port: 9090
    targetPort: 9090
    nodePort: 30090
```

Apply it:

```bash
kubectl apply -f service.yaml
```

### Step 6: Verify the deployment

Check that the pod is running:

```bash
kubectl get pods -n my-namespace -l app=prometheus
```

Expected output:

```
NAME                          READY   STATUS    RESTARTS   AGE
prometheus-5d4b7c8f9-x2k7m   1/1     Running   0          2m
```

Access the Prometheus web UI at `http://<node-ip>:30090`.

### Making your applications discoverable

To have Prometheus automatically scrape metrics from your applications, add these annotations to your pod spec:

```yaml
metadata:
  annotations:
    prometheus.io/scrape: "true"
    prometheus.io/port: "8080"
    prometheus.io/path: "/metrics"
```

Prometheus will pick up any pod in the namespace that has `prometheus.io/scrape: "true"` and scrape the specified port and path.

### Storage considerations

This guide uses `hostPath` volumes, which tie Prometheus data to a specific node. This is suitable for single-node or pinned deployments. For production clusters with multiple nodes, consider using a StorageClass with a PersistentVolumeClaim instead.

The `--storage.tsdb.retention.time=30d` flag keeps 30 days of metrics. Adjust this based on your storage capacity and monitoring needs.

### Next steps

- **Grafana**: Deploy Grafana and add Prometheus as a datasource for rich dashboards and visualisations
- **Alertmanager**: Configure alerting rules in Prometheus and route notifications via Alertmanager
- **Node Exporter**: Deploy the Prometheus Node Exporter as a DaemonSet to collect hardware and OS-level metrics from every node
