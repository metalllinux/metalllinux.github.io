---
title: "Cluster Installation Using kubeadm Solution"
category: "cka-certification"
tags: ["cka-certification", "cluster", "installation", "kubeadm", "solution"]
---

# Cluster Installation Using kubeadm Solution

* Perform this on all nodes:

```
cat <<EOF | sudo tee /etc/modules-load.d/k8s.conf
br_netfilter
EOF

cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
EOF

sudo sysctl --system
``

* We want to load the `br_netfilter` module - required in Kubernetes where bridge network functionality is necessary.

* Next we apply kernel parameters to `sysctl`.

    * The `net.bridge` settings ensure that iptables for both IPv4 and IPv6 see and process bridged network traffic.
    
    * Without the two `net.bridge` options, packets traversing bridge networks may bypass iptables rules.
    
        * These are required for Kubernetes.
        
* Running `sudo sysctl --system` reloads all system configuration files in `/etc/sysctl.conf`, `/usr/lib/sysctl.d/` and `/etc/sysctl.d/`. This command forces the kernel to apply the settigs.

* Next you would install the container runtime.

* Then install `kubeadm`, `kubectl` and `kubelet` on all node (steps listed below are for Debian / Ubuntu):

```
sudo apt-get update

sudo apt-get install -y apt-transport-https ca-certificates curl

curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.32/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg

echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.32/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list

sudo apt-get update

# To see the new version labels
sudo apt-cache madison kubeadm

sudo apt-get install -y kubelet=1.32.0-1.1 kubeadm=1.32.0-1.1 kubectl=1.32.0-1.1

sudo apt-mark hold kubelet kubeadm kubectl
```

* How to find the `kubelet` version:
```
kubelet --version
```
* Latest version is `1.32`.

* How to bootstrap a cluster with `kubeadm`:

* Use this `kubeadm init` command to spin up the cluster:
```
IP_ADDR=$(ip addr show eth0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}')
kubeadm init --apiserver-cert-extra-sans=controlplane --apiserver-advertise-address $IP_ADDR --pod-network-cidr=172.17.0.0/16 --service-cidr=172.20.0.0/16
```

* Using the above command, we set the following:
```
apiserver-advertise-address - Use the IP address allocated to eth0 on the controlplane node

apiserver-cert-extra-sans - Set it to controlplane

pod-network-cidr - Set to 172.17.0.0/16

service-cidr - Set to 172.20.0.0/16

Once done, set up the default kubeconfig file and wait for node to be part of the cluster.
```

* Then setup `kubeconfig`:
```
mkdir -p $HOME/.kube

sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config

sudo chown $(id -u):$(id -g) $HOME/.kube/config
```

* Copy the `kubeadm join` token:
```
kubeadm join 192.168.122.154:6443 --token iz8eis.83qld4oiu6t44u9t \
        --discovery-token-ca-cert-hash sha256:ea43615b4f62678085151f9617808486289e2516bd3e9c8c6dc90f5bdf71e437
```

* Install a network plugin.

    * Flannel is a good default choice.
    
    * For `inter-host` communication, use the `eth0` interface and update the `Network` field.
    
* For the official exam, you may not need to setup `Flannel`.

* Download the `Flannel` `yaml` file and save it:
```
curl -LO https://raw.githubusercontent.com/flannel-io/flannel/v0.20.2/Documentation/kube-flannel.yml
```
* Open the `kube-flannel.yml` file.

* You can use a custom POD CIDR, for example `172.17.0.0/16`, instead of the default `10.244.0.0/16` when bootstrapping `Flannel`.

    * Need to update the `Network` field in the `Flannel` configuration:
    
* We need to edit this part:
```
net-conf.json: |
    {
      "Network": "10.244.0.0/16", # Update this to match the custom PodCIDR
      "Backend": {
        "Type": "vxlan"
      }
```

* Locate the `args` section within the `kube-flannel` container definition.
```
  args:
  - --ip-masq
  - --kube-subnet-mgr
```
* Add this argument to the above list:
```
- --iface=eth0
```

* apply the modified manifest using `kubectl`:
```
kubectl apply -f kube-flannel.yml
```


