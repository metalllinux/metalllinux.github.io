---
title: "Installation on All Nodes"
category: "rocky-linux-kubernetes-setup"
tags: ["rocky-linux-kubernetes-setup", "installation", "all", "nodes"]
---

# Installation on All Nodes

```
sudo tee /etc/hosts <<EOF
192.168.1.103 ray
192.168.1.104 mighty
EOF
```

```
sudo swapoff -a
sudo sed -i '/ swap / s/^\(.*\)$/#\1/g' /etc/fstab
```

```
sudo setenforce 0
sudo sed -i --follow-symlinks 's/SELINUX=enforcing/SELINUX=permissive/g' /etc/sysconfig/selinux
```

```
sudo firewall-cmd --permanent --add-port=6443/tcp
sudo firewall-cmd --permanent --add-port=10250/tcp
sudo firewall-cmd --reload
```

```
cat <<EOF | sudo tee /etc/modules-load.d/k8s.conf
overlay
br_netfilter
EOF
```

```
sudo modprobe overlay
sudo modprobe br_netfilter
```

```
cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
net.ipv4.ip_forward = 1
EOF
```

```
sudo sysctl --system
```

```
sudo dnf config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
```

```
sudo dnf install -y containerd.io
```

```
containerd config default | sudo tee /etc/containerd/config.toml >/dev/null 2>&1
```

```
sudo sed -i 's/SystemdCgroup \= false/SystemdCgroup \= true/g' /etc/containerd/config.toml
```

```
sudo systemctl enable --now containerd
```

```
cat <<EOF | sudo tee /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=https://pkgs.k8s.io/core:/stable:/v1.33/rpm/
enabled=1
gpgcheck=1
gpgkey=https://pkgs.k8s.io/core:/stable:/v1.33/rpm/repodata/repomd.xml.key
EOF
```

```
sudo dnf install -y kubelet kubeadm kubectl
```

```
sudo dnf install -y 'dnf-command(versionlock)'
```

```
sudo dnf versionlock add kubelet kubeadm kubectl
```

```
sudo systemctl enable --now kubelet
```

* Run this step on the Control Plane Node only:

```
sudo kubeadm init --control-plane-endpoint=mighty
```

* Run this on the Control Plane Node only: 

```
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
```

* Copy the token provided and run it on the Worker Node. Run the command as `sudo`.

* Set up Flannel on the Control Plane node:

```
curl -LO https://raw.githubusercontent.com/flannel-io/flannel/v0.20.2/Documentation/kube-flannel.yml
```

* Perform the following:

```
* Open the `kube-flannel.yml` file.
```

```
* You can use a custom POD CIDR, for example `172.17.0.0/16`, instead of the default `10.244.0.0/16` when bootstrapping `Flannel`.
```

```
* Need to edit this:

net-conf.json: |
    {
      "Network": "10.244.0.0/16", # Update this to match the custom PodCIDR
      "Backend": {
        "Type": "vxlan"
      }
```

```
* Locate the `args` section within the `kube-flannel` container definition.

  args:
  - --ip-masq
  - --kube-subnet-mgr
```


```
* Now apply the `Flannel` config:
kubectl apply -f kube-flannel.yml
```

* Edit the following file:

```
/etc/kubernetes/manifests/kube-controller-manager.yaml
```

* Add the following lines under `- --use-service-account-credentials=true` 

```
- --allocate-node-cidrs=true
- --cluster-cidr=172.17.0.0/16
```
