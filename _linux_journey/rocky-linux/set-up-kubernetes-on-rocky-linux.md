---
title: "Add IPs of all hosts to each /etc/hosts file"
category: "rocky-linux"
tags: ["rocky-linux", "kubernetes", "rocky", "linux"]
---

```
# Add IPs of all hosts to each /etc/hosts file
sudo tee /etc/hosts <<EOF
192.168.1.104   server-c-rl9.kubernetes.local
192.168.1.103   amy-rl9.kubernetes.local

# Disable swap on each node
sudo swapoff -a
sudo sed -i '/ swap / s/^\(.*\)$/#\1/g' /etc/fstab

# Adjust SELinux
sudo setenforce 0
sudo sed -i --follow-symlinks 's/SELINUX=enforcing/SELINUX=permissive/g' /etc/sysconfig/selinux

# Firewalld Ports
sudo firewall-cmd --permanent --add-port=6443/tcp
sudo firewall-cmd --permanent --add-port=10250/tcp
sudo firewall-cmd --reload

# Add Kernel Modules and Parameters
sudo tee /etc/modules-load.d/containerd.conf <<EOF
overlay
br_netfilter
EOF

# Load the modules
sudo modprobe overlay
sudo modprobe br_netfilter

# Add these kernel parameters
sudo vim /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-iptables  = 1
net.ipv4.ip_forward                 = 1
net.bridge.bridge-nf-call-ip6tables = 1

# Add the parameters with the below command.
sudo sysctl --system

# Install Containerd Runtime
sudo dnf config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
sudo dnf install containerd.io

# Configure containerd so that it usses the systemd cgroup
containerd config default | sudo tee /etc/containerd/config.toml >/dev/null 2>&1
sudo sed -i 's/SystemdCgroup \= false/SystemdCgroup \= true/g' /etc/containerd/config.toml

# Enable containerd
sudo systemctl enable --now containerd

# Install the kubernetes tools
cat <<EOF | sudo tee /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=https://pkgs.k8s.io/core:/stable:/v1.28/rpm/
enabled=1
gpgcheck=1
gpgkey=https://pkgs.k8s.io/core:/stable:/v1.28/rpm/repodata/repomd.xml.key
exclude=kubelet kubeadm kubectl cri-tools kubernetes-cni
EOF

# Install Kubernetes
sudo dnf install kubelet kubeadm kubectl --disableexcludes=kubernetes

# Start the kubelet on each node
sudo systemctl enable --now kubelet

# Run this from the Control Plane Node Only
sudo kubeadm init --control-plane-endpoint=robotnik

# Set up the Control Plane Node Only
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config

# Install Calico on the Master Node Only
kubectl apply -f https://raw.githubusercontent.com/projectcalico/calico/v3.26.1/manifests/calico.yaml

# Check the Calico pods
kubectl get pods -n kube-system

sudo kubeadm join robotnik:6443 --token l7ryuc.ec6e4fjisocp3pgi \
	--discovery-token-ca-cert-hash sha256:8be936155f2d412cc99200c482fb6cc92d8c05a0ad6a1419656d71066c7646ed 
```