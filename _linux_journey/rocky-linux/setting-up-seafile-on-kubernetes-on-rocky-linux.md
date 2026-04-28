---
title: "Setting Up Seafile on Kubernetes on Rocky Linux"
category: "rocky-linux"
tags: ["rocky-linux", "setting", "seafile", "kubernetes", "rocky"]
---

# Setting Up Seafile on Kubernetes on Rocky Linux

## Seafile 13 Steps

* Label your worker node and say that it has local storage available:

```
kubectl label nodes <your-worker-node> local-storage-available=true
```

* Create the `namespace`:

```
kubectl create ns seafile
```

* Install EPEL:

```
dnf install -y epel-release
```

* Install `pwgen`:

```
dnf install -y pwgen
```

* To make the `jwt private key`, run:

```
pwgen -s 40 1
```

* Create the `secretMap`:

```
kubectl create secret generic seafile-secret --namespace seafile \
--from-literal=JWT_PRIVATE_KEY='<your-jwt-private-key>' \
--from-literal=SEAFILE_MYSQL_DB_PASSWORD='<your-secure-password>' \
--from-literal=INIT_SEAFILE_ADMIN_PASSWORD='<your-secure-password>' \
--from-literal=INIT_SEAFILE_MYSQL_ROOT_PASSWORD='<your-secure-password>' \
--from-literal=REDIS_PASSWORD='<your-secure-password>' \
--from-literal=S3_SECRET_KEY='' \
--from-literal=S3_SSE_C_KEY=''
```

* Create the `seafile-k8s-yaml` directory:

```
mkdir -p /opt/seafile-k8s-yaml
```

* Create the `mysql` directory

```
mkdir -p /opt/mysql-k8s-yaml
```

* Create the `mysql-data` directory to store all of the database data in `/root`:

```
mkdir -p /root/mysql-data
mkdir -p /root/redis-data
mkdir -p /root/elasticsearch-data
```

* Pull down all of the required `yaml` files for `seafile`:

```
wget -P /opt/seafile-k8s-yaml https://manual.seafile.com/13.0/repo/k8s/cluster/seafile-backend-deployment.yaml
wget -P /opt/seafile-k8s-yaml https://manual.seafile.com/13.0/repo/k8s/cluster/seafile-persistentvolume.yaml
wget -P /opt/seafile-k8s-yaml https://manual.seafile.com/13.0/repo/k8s/cluster/seafile-persistentvolumeclaim.yaml
wget -P /opt/seafile-k8s-yaml https://manual.seafile.com/13.0/repo/k8s/cluster/seafile-service.yaml
wget -P /opt/seafile-k8s-yaml https://manual.seafile.com/13.0/repo/k8s/cluster/seafile-env.yaml
```

* Set `seafile-persistentvolume.yaml` to the following:

```
cat << "EOF" | tee /opt/seafile-k8s-yaml/seafile-persistentvolume.yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: seafile-data
spec:
  capacity:
    storage: 10.9Ti
  volumeMode: Filesystem
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  storageClassName: local-storage
  hostPath:
    path: <your-storage-path>
EOF
```

* Set the `seafile-persistentvolumeclaim.yaml` as the following:

```
cat << "EOF" | tee /opt/seafile-k8s-yaml/seafile-persistentvolumeclaim.yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: seafile-data
  namespace: seafile
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 10.9Ti
  storageClassName: local-storage
EOF
```

* Set `seafile-backend-deployment.yaml` as the following:

```
cat << "EOF" | tee /opt/seafile-k8s-yaml/seafile-backend-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: seafile-backend
  namespace: seafile
spec:
  replicas: 1
  selector:
    matchLabels:
      app: seafile-backend
  template:
    metadata:
      labels:
        app: seafile-backend
    spec:
      enableServiceLinks: false
      initContainers:  
        - name: set-ownership  
          image: busybox  
          command: ['sh', '-c', 'chown -R root:root /shared']  
          volumeMounts:  
          - name: seafile-data  
            mountPath: /shared
      containers:
        - name: seafile-backend
          image: seafileltd/seafile-pro-mc:13.0-latest
          env:
            - name: CLUSTER_SERVER
              value: "true"
            - name: CLUSTER_MODE
              value: "backend"
          envFrom:
            - configMapRef:
                name: seafile-env 
            - secretRef:
                name: seafile-secret
          volumeMounts:
            - name: seafile-data
              mountPath: /shared
      volumes:
        - name: seafile-data
          persistentVolumeClaim:
            claimName: seafile-data
      restartPolicy: Always
      imagePullSecrets:
        - name: regcred
EOF
```

* The setup for `seafile-env.yaml`:

```
cat << "EOF" | tee /opt/seafile-k8s-yaml/seafile-env.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: seafile-env
  namespace: seafile
data:
  # for Seafile server
  TIME_ZONE: "Asia/Tokyo"
  SEAFILE_LOG_TO_STDOUT: "true"
  SITE_ROOT: "/"
  SEAFILE_SERVER_HOSTNAME: "<your-worker-node-ip>:30007"
  SEAFILE_SERVER_PROTOCOL: "http"

  # for database
  SEAFILE_MYSQL_DB_HOST: "mysql"
  SEAFILE_MYSQL_DB_PORT: "3306"
  SEAFILE_MYSQL_DB_USER: "seafile"
  SEAFILE_MYSQL_DB_CCNET_DB_NAME: "ccnet_db"
  SEAFILE_MYSQL_DB_SEAFILE_DB_NAME: "seafile_db"
  SEAFILE_MYSQL_DB_SEAHUB_DB_NAME: "seahub_db"

  # for cached
  CACHE_PROVIDER: "redis" # or "memcached"

  ## for redis
  REDIS_HOST: "redis-leader"
  REDIS_PASSWORD: "<your-secure-password>"
  REDIS_PORT: "6379"

  ## for memcached
  MEMCACHED_HOST: "<your-worker-node-ip>"
  MEMCACHED_PORT: "11211"

  # for s3
  SEAF_SERVER_STORAGE_TYPE: "disk"
  S3_COMMIT_BUCKET: ""
  S3_FS_BUCKET: ""
  S3_BLOCK_BUCKET: ""
  S3_KEY_ID: ""
  S3_USE_V4_SIGNATURE: "true"
  S3_AWS_REGION: "us-east-1"
  S3_HOST: ""
  S3_USE_HTTPS: "true"
  S3_PATH_STYLE_REQUEST: "false"

  # for notification
  ENABLE_NOTIFICATION_SERVER: "false"
  NOTIFICATION_SERVER_URL: ""

  # for seadoc
  ENABLE_SEADOC: "true"
  SEADOC_SERVER_URL: "<your-worker-node-ip>" # only valid in ENABLE_SEADOC = true

  # initialization (only valid in first-time deployment and CLUSTER_INIT_MODE = true)
  CLUSTER_INIT_MODE: "true"

  ## for Seafile admin
  INIT_SEAFILE_ADMIN_EMAIL: "admin@example.com"

  ## for cluster basic service
  CLUSTER_INIT_ES_HOST: "elasticsearch"
  CLUSTER_INIT_ES_PORT: "9200"

  # Seafile AI
  ENABLE_SEAFILE_AI: "yes"
  SEAFILE_AI_SERVER_URL: "<your-worker-node-ip>"

  # Matedata server
  MD_FILE_COUNT_LIMIT: "0"
EOF
```

```
chown -R 1000:1000 /root/elasticsearch-data
```

```
restorecon -R -v /root/elasticsearch-data
```

* `seafile-service.yaml` configuration:

```
cat << "EOF" | tee /opt/seafile-k8s-yaml/seafile-service.yaml
apiVersion: v1
kind: Service
metadata:
  name: seafile
  namespace: seafile
spec:
  selector:
    app: seafile-frontend
  type: NodePort
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
      nodePort: 30007
EOF
```

* Create the `seafile-http` service for the file server (required for file uploads and downloads):

```
cat << "EOF" | tee /opt/seafile-k8s-yaml/seafile-http-service.yaml
apiVersion: v1
kind: Service
metadata:
  name: seafile-http
  namespace: seafile
spec:
  selector:
    app: seafile-frontend
  type: NodePort
  ports:
    - protocol: TCP
      port: 8082
      targetPort: 8082
      nodePort: 30008
EOF
```

* Create the following `mysql` `yaml` files:

```
cat << "EOF" | tee /opt/mysql-k8s-yaml/mysql-service.yaml
apiVersion: v1
kind: Service
metadata:
  name: mysql 
  namespace: seafile
spec:
  ports:
  - port: 3306
    protocol: TCP
    targetPort: 3306
  selector:
    app: mysql
EOF
```

```
cat << "EOF" | tee /opt/mysql-k8s-yaml/mysql-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mysql 
  namespace: seafile
spec:
  selector:
    matchLabels:
      app: mysql
  strategy:
    type: Recreate
  template:
    metadata:
      labels:
        app: mysql
    spec:
      containers:
      - image: mysql:9
        name: mysql
        env:
        - name: MYSQL_ROOT_PASSWORD
          value: password
        ports:
        - containerPort: 3306
          name: mysql
        volumeMounts:
        - name: mysql-persistent-storage
          mountPath: /var/lib/mysql
      volumes:
      - name: mysql-persistent-storage
        persistentVolumeClaim:
          claimName: mysql-pv-claim
EOF
```

```
cat << "EOF" | tee /opt/mysql-k8s-yaml/mysql-pv.yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: mysql-pv-volume 
  namespace: seafile
  labels:
    type: local
spec:
  storageClassName: manual
  capacity:
    storage: 20Gi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: "/root/mysql-data"
EOF
```

```
cat << "EOF" | tee /opt/mysql-k8s-yaml/mysql-pvc.yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: mysql-pv-claim
  namespace: seafile
spec:
  storageClassName: manual
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 20Gi
EOF
```

* Set up Elasticsearch

```
# 1️⃣ Host directory for persistence
sudo mkdir -p /root/elasticsearch-data

# 2️⃣ Apply PV & PVC
kubectl apply -f - <<'EOF'
apiVersion: v1
kind: PersistentVolume
metadata:
  name: es-pv-volume
  namespace: seafile
spec:
  storageClassName: manual
  capacity:
    storage: 30Gi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: "/root/elasticsearch-data"
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: es-pv-claim
  namespace: seafile
spec:
  storageClassName: manual
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 30Gi
EOF

# 3️⃣ Deploy ES
kubectl apply -f - <<'EOF'
apiVersion: apps/v1
kind: Deployment
metadata:
  name: elasticsearch
  namespace: seafile
spec:
  replicas: 1
  selector:
    matchLabels:
      app: elasticsearch
  template:
    metadata:
      labels:
        app: elasticsearch
    spec:
      containers:
        - name: elasticsearch
          image: docker.elastic.co/elasticsearch/elasticsearch:7.17.10
          env:
            - name: discovery.type
              value: "single-node"
            - name: ES_JAVA_OPTS
              value: "-Xms512m -Xmx512m"
          ports:
            - containerPort: 9200
          volumeMounts:
            - name: es-data
              mountPath: /usr/share/elasticsearch/data
      volumes:
        - name: es-data
          persistentVolumeClaim:
            claimName: es-pv-claim
---
apiVersion: v1
kind: Service
metadata:
  name: elasticsearch
  namespace: seafile
spec:
  selector:
    app: elasticsearch
  ports:
    - protocol: TCP
      port: 9200
      targetPort: 9200
  type: ClusterIP
EOF

# 4️⃣ Update Seafile ConfigMap (replace host)
sed -i 's/CLUSTER_INIT_ES_HOST:.*/CLUSTER_INIT_ES_HOST: "elasticsearch"/' /opt/seafile-k8s-yaml/seafile-env.yaml
sed -i 's/CLUSTER_INIT_ES_PORT:.*/CLUSTER_INIT_ES_PORT: "9200"/' /opt/seafile-k8s-yaml/seafile-env.yaml
kubectl apply -f /opt/seafile-k8s-yaml/seafile-env.yaml
```

* Deploy the `mysql` deployment:

```
kubectl apply -f /opt/mysql-k8s-yaml
```

* Deploy the `seafile` deployment:

```
kubectl apply -f /opt/seafile-k8s-yaml/
```

* Create the Redis directory:

```
mkdir -p /opt/redis-k8s-yaml
```

* Deploy the Redis instance:

```
cat << "EOF" | tee /opt/redis-k8s-yaml/redis-leader-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: redis-leader
  namespace: seafile
  labels:
    app: redis
    role: leader
    tier: backend
spec:
  selector:
    matchLabels:
      app: redis
  template:
    metadata:
      labels:
        app: redis
        role: leader
        tier: backend
    spec:
      containers:
      - name: leader
        image: "registry.k8s.io/redis@sha256:cb111d1bd870a6a471385a4a69ad17469d326e9dd91e0e455350cacf36e1b3ee"
        args: ["redis-server", "--requirepass", "password"]
        ports:
        - containerPort: 6379
EOF
```

* Create the Redis Leader Service:

```
cat << "EOF" | tee /opt/redis-k8s-yaml/redis-leader-service.yaml
apiVersion: v1
kind: Service
metadata:
  name: redis-leader
  namespace: seafile
  labels:
    app: redis
    role: leader
    tier: backend
spec:
  type: ClusterIP
  ports:
    - protocol: TCP
      port: 6379
  selector:
    app: redis
    role: leader
    tier: backend
EOF
```

* Apply the Redis yaml files:

```
kubectl apply -f /opt/redis-k8s-yaml/
```


* Download the `frontend` `seafile` deployment yaml:

```
wget -P /opt/seafile-k8s-yaml https://manual.seafile.com/13.0/repo/k8s/cluster/seafile-frontend-deployment.yaml
```

* Set the `seafile-frontend-deployment.yaml` to the following:

```
cat << "EOF" | tee /opt/seafile-k8s-yaml/seafile-frontend-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: seafile-frontend
  namespace: seafile
spec:
  selector:
    matchLabels:
      app: seafile-frontend
  template:
    metadata:
      labels:
        app: seafile-frontend
    spec:
      enableServiceLinks: false
      initContainers:  
        - name: set-ownership  
          image: busybox  
          command: ['sh', '-c', 'chown -R root:root /shared']  
          volumeMounts:  
          - name: seafile-data  
            mountPath: /shared
      containers:
        - name: seafile-frontend
          image: seafileltd/seafile-pro-mc:13.0-latest
          env:
            - name: CLUSTER_SERVER
              value: "true"
            - name: CLUSTER_MODE
              value: "frontend"
          envFrom:
            - configMapRef:
                name: seafile-env 
            - secretRef:
                name: seafile-secret
          ports:
            - containerPort: 80
          volumeMounts:
            - name: seafile-data
              mountPath: /shared
      volumes:
        - name: seafile-data
          persistentVolumeClaim:
            claimName: seafile-data
      restartPolicy: Always
      imagePullSecrets:
        - name: regcred
EOF
```

* Set `seafile-env` to the following:

```
cat << "EOF" | tee /opt/seafile-k8s-yaml/seafile-env.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: seafile-env
  namespace: seafile
data:
  # for Seafile server
  TIME_ZONE: "Asia/Tokyo"
  SEAFILE_LOG_TO_STDOUT: "true"
  SITE_ROOT: "/"
  SEAFILE_SERVER_HOSTNAME: "<your-worker-node-ip>:30007"
  SEAFILE_SERVER_PROTOCOL: "http"

  # for database
  SEAFILE_MYSQL_DB_HOST: "mysql"
  SEAFILE_MYSQL_DB_PORT: "3306"
  SEAFILE_MYSQL_DB_USER: "seafile"
  SEAFILE_MYSQL_DB_CCNET_DB_NAME: "ccnet_db"
  SEAFILE_MYSQL_DB_SEAFILE_DB_NAME: "seafile_db"
  SEAFILE_MYSQL_DB_SEAHUB_DB_NAME: "seahub_db"

  # for cached
  CACHE_PROVIDER: "redis" # or "memcached"

  ## for redis
  REDIS_HOST: "redis-leader"
  REDIS_PASSWORD: "<your-secure-password>"
  REDIS_PORT: "6379"

  ## for memcached
  MEMCACHED_HOST: "<your-worker-node-ip>"
  MEMCACHED_PORT: "11211"

  # for s3
  SEAF_SERVER_STORAGE_TYPE: "disk"
  S3_COMMIT_BUCKET: ""
  S3_FS_BUCKET: ""
  S3_BLOCK_BUCKET: ""
  S3_KEY_ID: ""
  S3_USE_V4_SIGNATURE: "true"
  S3_AWS_REGION: "us-east-1"
  S3_HOST: ""
  S3_USE_HTTPS: "true"
  S3_PATH_STYLE_REQUEST: "false"

  # for notification
  ENABLE_NOTIFICATION_SERVER: "false"
  NOTIFICATION_SERVER_URL: ""

  # for seadoc
  ENABLE_SEADOC: "true"
  SEADOC_SERVER_URL: "<your-worker-node-ip>" # only valid in ENABLE_SEADOC = true

  # initialization (only valid in first-time deployment and CLUSTER_INIT_MODE = true)
  CLUSTER_INIT_MODE: "false"

  ## for Seafile admin
  INIT_SEAFILE_ADMIN_EMAIL: "admin@example.com"

  ## for cluster basic service
  CLUSTER_INIT_ES_HOST: "elasticsearch"
  CLUSTER_INIT_ES_PORT: "9200"

  # Seafile AI
  ENABLE_SEAFILE_AI: "yes"
  SEAFILE_AI_SERVER_URL: "<your-worker-node-ip>"

  # Matedata server
  MD_FILE_COUNT_LIMIT: "0"
EOF
```

* Apply all of the yaml files again:

```
kubectl apply -f /opt/seafile-k8s-yaml/
```

## Troubleshooting: File Uploads and Downloads Not Working

If the Seahub web UI loads correctly but file uploads and downloads fail (from both the browser and the Seafile mobile app), the most likely cause is a misconfigured `SEAFILE_SERVER_HOSTNAME`.

### The Problem

When `SEAFILE_SERVER_HOSTNAME` is set without the NodePort (e.g., just the IP address), Seafile generates file operation URLs pointing to port 80:

- `SERVICE_URL = http://<ip>` (port 80)
- `FILE_SERVER_ROOT = http://<ip>/seafhttp`

If Seahub is exposed via NodePort (e.g., 30007), port 80 on the node is not serving Seafile. The browser and mobile app receive a connection refused error when attempting file operations.

### The Fix

Ensure `SEAFILE_SERVER_HOSTNAME` in `seafile-env.yaml` includes the NodePort:

```
SEAFILE_SERVER_HOSTNAME: "<your-worker-node-ip>:30007"
```

**Important:** In Seafile Pro 13.0, Seahub's Django `settings.py` computes `SERVICE_URL` and `FILE_SERVER_ROOT` from the `SEAFILE_SERVER_HOSTNAME` environment variable **after** loading `seahub_settings.py`. This means setting `SERVICE_URL` and `FILE_SERVER_ROOT` in `seahub_settings.py` alone will not work — the environment variable takes precedence.

To apply the fix without restarting the pod (which would trigger the init container's `chown -R` on the entire data volume), exec into the frontend pod and restart Seahub with the corrected environment variable:

```
kubectl exec <seafile-frontend-pod> -n seafile -- bash -c 'export SEAFILE_SERVER_HOSTNAME="<your-worker-node-ip>:30007" && /opt/seafile/seafile-pro-server-<version>/seahub.sh restart'
```

Then patch the ConfigMap so future pod starts use the correct value:

```
kubectl patch configmap seafile-env -n seafile --type merge -p '{"data":{"SEAFILE_SERVER_HOSTNAME":"<your-worker-node-ip>:30007"}}'
```

### Note on Elasticsearch

Elasticsearch is used solely for file search indexing. Warnings in the frontend logs about Elasticsearch security features not being enabled are informational only — they do not affect file uploads or downloads.

---

## Troubleshooting: Library Cannot Be Synced Due to Too Many Files

If the Seafile desktop client shows "Library cannot be synced since it has too many files", the library exceeds the default file count limit. This commonly occurs with large directories such as Steam game libraries, which can contain 200,000–500,000+ files.

![Library cannot be synced error](/assets/images/seafile-too-many-files-error.png)

### Two Separate File Count Limits

Seafile has two independent file count settings that are often confused:

1. **`max_sync_file_count`** in `seafile.conf` under `[fileserver]` — controls whether the desktop or mobile client can sync a library. Default: 100,000. **This is the setting that causes the sync error.**
2. **`MD_FILE_COUNT_LIMIT`** in the ConfigMap (environment variable) — controls whether the metadata management feature is enabled for a library. Default: 100,000. This does not affect sync.

Both should be raised for large libraries.

### The Fix (without pod restart)

Since `seafile.conf` lives on the shared PVC at `/opt/seafile/conf/seafile.conf`, it can be edited in-place via `kubectl exec` without restarting the pod (which would trigger the slow `chown -R` on the entire data volume).

* Add `max_sync_file_count` and `fs_id_list_request_timeout` under the `[fileserver]` section of `seafile.conf`:

```
kubectl exec <seafile-frontend-pod> -n seafile -- bash -c 'sed -i "/^\[fileserver\]/a max_sync_file_count = -1\nfs_id_list_request_timeout = -1" /opt/seafile/conf/seafile.conf'
```

Setting both values to `-1` removes the limit entirely (supported since Seafile Pro 8.0.4). The resulting `seafile.conf` should look like:

```
[fileserver]
max_sync_file_count = -1
fs_id_list_request_timeout = -1
port=8082

[cluster]
enable = true
```

* Restart the fileserver process inside the frontend pod (not the pod itself):

```
kubectl exec <seafile-frontend-pod> -n seafile -- /opt/seafile/seafile-pro-server-<version>/seafile.sh restart
```

* Since both frontend and backend pods share the same PVC, the config edit is already visible to the backend pod. Restart its fileserver process too:

```
kubectl exec <seafile-backend-pod> -n seafile -- /opt/seafile/seafile-pro-server-<version>/seafile.sh restart
```

* Verify the settings took effect by checking the startup logs for:

```
fileserver: max_sync_file_count = -1
fileserver: fs_id_list_request_timeout = -1
```

### Updating the Metadata File Count Limit

To also raise `MD_FILE_COUNT_LIMIT`, patch the live ConfigMap:

```
kubectl patch configmap seafile-env -n seafile --type merge -p '{"data":{"MD_FILE_COUNT_LIMIT":"0"}}'
```

Then update the on-disk manifest (`/opt/seafile-k8s-yaml/seafile-env.yaml`) to match:

```
  # Matedata server
  MD_FILE_COUNT_LIMIT: "0"
```

This change only takes effect on future pod restarts, since environment variables injected via `envFrom` require a pod restart to update.

---

## Data Transfer via NFS

* To transfer data, install `nfs-utils` on both the Worker Node and the Client:

```
sudo dnf install -y nfs-utils
```

* If on ZFS and using datasets, do the following instead:

```
sudo zfs set sharenfs='rw=@<your-client-ip>,no_root_squash' <your-zfs-dataset>
```

* Check to make sure NFS on ZFS was shared properly:

```
sudo zfs get sharenfs <your-zfs-dataset>
```

* ExportFS:

```
sudo exportfs -ra
```

* Restart the service:

```
sudo systemctl restart nfs-server rpcbind
```

* If on another filesystem or NOT using datasets with ZFS, use this method:

* Add the following into `/etc/exports` for the Worker Node:

```
cat << "EOF" | tee /etc/exports
<your-nfs-path> <your-client-ip>(rw,sync,no_subtree_check,no_root_squash)
EOF
```

* Enable the NFS server on the Worker Node:

```
sudo systemctl enable --now nfs-server
```

* Ensure these services are allowed through the Worker Node's firewall:

```
sudo firewall-cmd --zone=public --permanent --add-service=mountd
sudo firewall-cmd --zone=public --permanent --add-service=nfs
sudo firewall-cmd --zone=public --permanent --add-service=rpc-bind
sudo firewall-cmd --reload
```

* On the Client machine, create the following directory:

```
sudo mkdir -p <your-nfs-mount-point>
```

* Mount the NFS share on the Client:

```
sudo mount <your-worker-node-ip>:<your-nfs-path> <your-nfs-mount-point>
```

* Add the following into `/etc/fstab` on the Client:

```
cat << "EOF" | sudo tee -a /etc/fstab
<your-worker-node-ip>:<your-nfs-path> <your-nfs-mount-point> nfs auto,nofail,noatime,nolock,intr,tcp,actimeo=1800 0 0
EOF
```

---

## Setting Up the Seafile Sync Client on the Worker Node

These steps set up KDE Plasma, the Seafile desktop sync client (AppImage), and RustDesk remote desktop (Flatpak) on the Kubernetes worker node running Rocky Linux 9. All commands are run on the worker node via SSH.

### Prerequisites

* SSH access to the worker node as a user with `sudo` privileges
* `kubectl` access to the cluster (from the control plane or a machine with a valid kubeconfig)

### Cordon the Worker Node

Before installing packages and rebooting, cordon the worker node to prevent new pod scheduling. Run this from the control plane:

```
kubectl cordon <your-worker-node>
```

### Enable the CRB Repository

The KDE Plasma group on Rocky Linux 9 depends on packages from EPEL, which in turn require `aspell` from the CRB (Code Ready Builder) repository. CRB is disabled by default and must be enabled first:

```
sudo dnf config-manager --set-enabled crb
```

* Verify that EPEL is also installed:

```
sudo dnf install -y epel-release
```

### Install KDE Plasma Workspaces

```
sudo dnf groupinstall -y "KDE Plasma Workspaces"
```

This installs `plasma-desktop`, `plasma-workspace`, `sddm`, `konsole`, `dolphin`, `flatpak`, and all default KDE applications.

### Protect Kubernetes Networking from NetworkManager

The KDE group pulls in NetworkManager components that can interfere with CNI interfaces. Create a drop-in config to exclude all Kubernetes-managed interfaces before enabling any services:

```
sudo tee /etc/NetworkManager/conf.d/99-k8s-unmanaged.conf > /dev/null << "EOF"
[keyfile]
unmanaged-devices=interface-name:cni0;interface-name:flannel.*;interface-name:cali*;interface-name:veth*;interface-name:tunl0;interface-name:vxlan.calico;interface-name:kube-bridge;interface-name:kube-dummy*;interface-name:docker0
EOF
```

### Enable SDDM and Set the Graphical Target

```
sudo systemctl enable sddm
sudo systemctl set-default graphical.target
```

### Verify KDE Installation

```
rpm -q plasma-desktop plasma-workspace sddm
```

All three packages should show as installed.

### Install the Seafile Sync Client (AppImage)

* Install FUSE (required for AppImages to mount themselves):

```
sudo dnf install -y fuse fuse-libs
sudo modprobe fuse
```

* Create the `appimages` directory and download the Seafile AppImage:

```
mkdir -p ~/appimages
curl -L -o ~/appimages/Seafile-x86_64-9.0.18.AppImage \
  "https://sos-ch-dk-2.exo.io/seafile-downloads/Seafile-x86_64-9.0.18.AppImage"
```

* Make the AppImage executable:

```
chmod +x ~/appimages/Seafile-x86_64-9.0.18.AppImage
```

* Verify the download:

```
ls -la ~/appimages/Seafile-x86_64-9.0.18.AppImage
```

The file should be approximately 184 MB with the execute bit set.

### Install RustDesk via Flatpak

Flatpak is already installed as a dependency of the KDE group. Add the Flathub remote and install RustDesk:

```
sudo flatpak remote-add --system --if-not-exists flathub \
  https://flathub.org/repo/flathub.flatpakrepo
```

```
sudo flatpak install --system --noninteractive flathub com.rustdesk.RustDesk
```

* Verify:

```
flatpak list --system | grep -i rustdesk
```

### Reboot and Verify

* Reboot the worker node to activate SDDM and the graphical target:

```
sudo systemctl reboot
```

* After the node comes back up, verify all components:

```
systemctl is-active sddm
systemctl get-default
systemctl is-active kubelet
ls -la ~/appimages/Seafile-x86_64-9.0.18.AppImage
flatpak list --system | grep -i rustdesk
```

Expected results:

| Component | Check | Expected |
|---|---|---|
| KDE Plasma | `rpm -q plasma-desktop sddm` | plasma-desktop 5.27.12, sddm 0.20.0 |
| SDDM | `systemctl is-active sddm` | active |
| Default target | `systemctl get-default` | graphical.target |
| NM isolation | `nmcli device status` (k8s interfaces) | unmanaged |
| Seafile AppImage | `ls -la ~/appimages/Seafile-x86_64-9.0.18.AppImage` | ~184 MB, executable |
| RustDesk | `flatpak list --system \| grep rustdesk` | com.rustdesk.RustDesk 1.4.6 |
| kubelet | `systemctl is-active kubelet` | active |

### Uncordon the Worker Node

Once everything is verified, uncordon the node from the control plane:

```
kubectl uncordon <your-worker-node>
```

Confirm the node is `Ready` and schedulable:

```
kubectl get nodes
```
