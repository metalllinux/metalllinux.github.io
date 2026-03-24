---
title: "Setting Up And Installing K3S On Rocky Linux 9"
category: "rocky-linux"
tags: ["rocky-linux", "setting", "installing", "k3s", "rocky"]
---

* Update all machines:
```
sudo dnf upgrade -y
```
* Set the hostname per machine:
```
sudo hostnamectl set-hostname "rocky-linux-9-k3s-master-node"
sudo hostnamectl set-hostname "rocky-linux-9-k3s-worker-node"
```
* Add the IP and hostname entries to each node's `/etc/hosts` file:
```
sudo tee -a /etc/hosts <<EOF
10.25.96.3 rocky-linux-9-k3s-master-node
10.25.96.4 rocky-linux-9-k3s-worker-node
EOF
```
* Disable the firewall on both the Master Node and Worker Nodes:
```
sudo systemctl disable --now firewalld
```
* Install the required packages to download and install `k3s`:
```
sudo dnf install -y curl wget
```
* Run the `pipe to bash` script on the Master Node only:
```
curl -fL https://get.k3s.io | K3S_TOKEN=LinuxRocks sh -s - server --cluster-init
```
* Check that `k3s` is running on the Master Node:
```
sudo systemctl status k3s
```
* Configure `kubectl` on the Master Node:
```
export KUBECONFIG=~/.kube/config
mkdir ~/.kube 2> /dev/null
sudo /usr/local/bin/k3s kubectl config view --raw > "$KUBECONFIG"
chmod 600 "$KUBECONFIG"
```
* Permanently add the `KUBECONFIG` to your path:
```
tee -a ~/.bashrc <<EOF
# k3s path export
export KUBECONFIG=~/.kube/config
EOF
```
* Check that the cluster is functioning on the Master Node:
```
kubectl get nodes
kubectl cluster-info
```
* Connect each Worker Node:
```
curl -sfL https://get.k3s.io | K3S_URL=https://10.25.96.3:6443 K3S_TOKEN=LinuxRocks sh -
```
* How to retrieve your `node-token` from the Master Node:
```
sudo cat /var/lib/rancher/k3s/server/node-token
```