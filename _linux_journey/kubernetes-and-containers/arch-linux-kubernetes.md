---
title: "Do this for all nodes"
category: "kubernetes-and-containers"
tags: ["kubernetes-and-containers", "arch", "linux", "kubernetes"]
---

```
# Do this for all nodes
sudo pacman -S kubeadm kubelet
```
```
# Firewalld Ports
sudo firewall-cmd --permanent --add-port=6443/tcp
sudo firewall-cmd --permanent --add-port=10250/tcp
sudo firewall-cmd --reload
```
```
# Enable the kubelet service
sudo systemctl enable --now kubelet
```
```
# Install kubectl on the Control Plane Node
sudo pacman -S kubectl
```
```
# Do this for all nodes
sudo pacman -S containerd
```
```
# Forwarding ipv4 and allowing iptables to see bridged traffic
sudo vim /etc/modules-load.d/k8s.conf
overlay
br_netfilter

sudo vim /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-iptables  = 1
net.bridge.bridge-nf-call-ip6tables = 1
net.ipv4.ip_forward                 = 1
```
```
# Apply the above without rebooting
sudo sysctl --system
```
```
# Disable swap
sudo swapoff /dev/sdxy

# To permanently disable swap, find the systemd unit
sudo systemctl --type swap
systemctl disable --now <systemd unit>
```
```
# Check that config.toml exists
ls -l /etc/containerd 
# If not, then create it with the following
sudo mkdir -p /etc/containerd/
su -
containerd config default > /etc/containerd/config.toml
exit

sudo systemctl restart containerd

# Use the systemd cgroup driver in /etc/containerd/config.toml with runc, set the following options
sudo vim /etc/containerd/config.toml
[plugins."io.containerd.grpc.v1.cri".containerd.runtimes.runc]
  ...
  [plugins."io.containerd.grpc.v1.cri".containerd.runtimes.runc.options]
    SystemdCgroup = true
	
# Restart containerd
sudo systemctl restart containerd
```
```
# Install kubeadm
sudo pacman -S kubeadm
```
```
# Make sure the .kube directory is set up on the Control Plane node with the right config
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
# Then you can run commands as a non-root user
```
```
# Creating the cluster
sudo systemctl enable --now kubelet.service
```
```
# Control Plane initialisation
kubeadm init --cri-socket /run/containerd/containerd.sock
```
```
# Set up Calico as a CNI
openssl req -newkey rsa:4096 \
           -keyout cni.key \
           -nodes \
           -out cni.csr \
           -subj "/CN=calico-cni"

sudo openssl x509 -req -in cni.csr \
                  -CA /etc/kubernetes/pki/ca.crt \
                  -CAkey /etc/kubernetes/pki/ca.key \
                  -CAcreateserial \
                  -out cni.crt \
                  -days 365

# Add this file to every node in the cluster
vim cni.kubeconfig

APISERVER=$(kubectl config view -o jsonpath='{.clusters[0].cluster.server}')
kubectl config set-cluster kubernetes \
    --certificate-authority=/etc/kubernetes/pki/ca.crt \
    --embed-certs=true \
    --server=$APISERVER \
    --kubeconfig=cni.kubeconfig

kubectl config set-credentials calico-cni \
    --client-certificate=cni.crt \
    --client-key=cni.key \
    --embed-certs=true \
    --kubeconfig=cni.kubeconfig

kubectl config set-context default \
    --cluster=kubernetes \
    --user=calico-cni \
    --kubeconfig=cni.kubeconfig

kubectl config use-context default --kubeconfig=cni.kubeconfig

# Run the following
kubectl apply -f - <<EOF
kind: ClusterRole
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: calico-cni
rules:
  # The CNI plugin needs to get pods, nodes, and namespaces.
  - apiGroups: [""]
    resources:
      - pods
      - nodes
      - namespaces
    verbs:
      - get
  # The CNI plugin patches pods/status.
  - apiGroups: [""]
    resources:
      - pods/status
    verbs:
      - patch
 # These permissions are required for Calico CNI to perform IPAM allocations.
  - apiGroups: ["crd.projectcalico.org"]
    resources:
      - blockaffinities
      - ipamblocks
      - ipamhandles
    verbs:
      - get
      - list
      - create
      - update
      - delete
  - apiGroups: ["crd.projectcalico.org"]
    resources:
      - ipamconfigs
      - clusterinformations
      - ippools
    verbs:
      - get
      - list
EOF

# Do these steps on every node in the cluster:
sudo su

curl -L -o /opt/cni/bin/calico https://github.com/projectcalico/cni-plugin/releases/download/v3.14.0/calico-amd64

chmod 755 /opt/cni/bin/calico

curl -L -o /opt/cni/bin/calico-ipam https://github.com/projectcalico/cni-plugin/releases/download/v3.14.0/calico-ipam-amd64

chmod 755 /opt/cni/bin/calico-ipam

mkdir -p /etc/cni/net.d/

cp cni.kubeconfig /etc/cni/net.d/calico-kubeconfig

chmod 600 /etc/cni/net.d/calico-kubeconfig

cat > /etc/cni/net.d/10-calico.conflist <<EOF
{
  "name": "k8s-pod-network",
  "cniVersion": "0.3.1",
  "plugins": [
    {
      "type": "calico",
      "log_level": "info",
      "datastore_type": "kubernetes",
      "mtu": 1500,
      "ipam": {
          "type": "calico-ipam"
      },
      "policy": {
          "type": "k8s"
      },
      "kubernetes": {
          "kubeconfig": "/etc/cni/net.d/calico-kubeconfig"
      }
    },
    {
      "type": "portmap",
      "snat": true,
      "capabilities": {"portMappings": true}
    }
  ]
}
EOF
```
```
# Install kompose on the Control Node
curl -L https://github.com/kubernetes/kompose/releases/download/v1.34.0/kompose-linux-amd64 -o kompose

chmod +x kompose

sudo mv ./kompose /usr/local/bin/kompose
```