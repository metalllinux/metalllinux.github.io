---
title: "Demo - Deployment with kubeadm"
category: "cka-certification"
tags: ["cka-certification", "demo", "deployment", "kubeadm"]
---

# Demo - Deployment with kubeadm

* Currently latest version of Kubernetes is 1.31

* Before using `kubeadm`, need a container runtime.

* First thing you need to do is download public signing keys for kubernetes repos.

    * Need to select the versions (1.31 in this case).
    
    * Paste the `curl` command in all three nodes.
    
* Add the specific Kubernete's repository - run the command in all three nodes.

* Update packages in all three nodes.

* Install the `kubelet`, `kubeadm` and `kubectl` packages.

    * The above packages are installed on all three nodes.
    
* Check the version of `kubeadm` with `kubeadm version`.

* Enable the `kubelet` service with `systemctl enable --now kubelet`.

* A container runtime needs to be installed on all three nodes.

* Control Plane components are installed as Pods on the Master Node.

* Install the container runtime (best is `containerd`).

* Install the `containerd` package. Run this on every node.

* `cgroups` allow you to specify resource groups on your containers.

* `cgroupfs` is the default driver and then you also have `systemd`.

* Both the `kubelet` and the `container runtime` need to use the same `cgroup` driver.

* If you `init` system is `systemd`, then need to use the `systemd` driver.

* How to verify - `ps -p 1` and it tells you whether this is `systemd` or not.

    * Need to create a kubelet configuration.
    
    * If under the configuration a `cgroup` driver is not set, it defaults to `systemd`.
    
* Kubernetes 1.22 defaults automatically to `systemd`.

* Need to set the `container runtime` to use the `systemd` driver.

    * Create a file for `containerd` - this is set in `/etc/containerd/config.toml` 
    
    * Usually need to manually create the above directory.
    
    * Needs to be done on all nodes.
    
* `containerd` allows the generation of default configurations.

* Good command for generating the configuration:
```
containerd config default | sed 's/SystemdCgroup = false/SystemdCgroup = true/' | sudo tee /etc/containerd/config.toml
```

* Run the above command on all nodes.

* Then restart `containerd` on all nodes.
```
systemctl restart containerd
```

* Initialise the Control Plane node.

    * If have multiple Master Nodes, need to pick one that you'll run the command on first.
    
* If planning to have more multiple Control Plane nodes, need to pass in `--control-plane-endpoint=<VIRTUAL=IP>` and point it to a load balancer.

    * Then don't need to change anything afterwards.
    
    * For a single Control Plane node, no need to pass in the above value.

* With `--pod-network-cider=`, this will be the IP address pool that the pods grab their IPs from.

    * Fpr example, `10.0.0.0/16` - all pods would get an IP address from this subnet.
    
* `kubeadm` tries to detect a runtime by using a list of well-known endpoints.

* Optional is if you need to manually pass in a socket with `--cri-socket=<PATH_TO_SOCKET>`

* For the `kubeadm` utility, there is the flag `--apiserver-advertise-address` flag.

    * When working with a single Control Plane node cluster,  `--apiserver-advertise-address` tells the cluster what the IP address of your `kube-apiserver` is.
    
    * `--apiserver-advertise-address` is set as the IP of the Master Node.
    
        * This is the standard IPv4 or IPv6 address.
        
    * If you have multiple interfaces, the above flag is a good way to find that interface.
    
* Then run the following `kubeadm` command:
```
sudo kubeadm init --apiserver-advertise-address 192.168.56.11 --pod-network-cidr "10.244.0.0/16" --upload-certs
```
    
* `--pod-network-cidr` is the subnet the pods pull all of their IP addresses from.

* `--upload-certs` places all certificates into a `secret` and then all nodes have access to this. 

* The above command will generate the CA certificates for the API server and all of the certificates for the `etcd` server. You can see the configuration file for your kubelet. It also provisions the static pod manifest for the different components and it brings in other components.

* Once complete, the command provisions a config file.

    * Can check the file at `/etc/kubernetes/admin.conf`.
    
        * This has a kube-config file, then we can talk to the master node.
        
        * We copy this to the home directory at `mkdir -p $HOME/.kube` and then the following commands:
        
```
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
```

* Running `kubectl get nodes` will show the Control Plane node in a `NotReady` state. This is expected, have not set up Network Plugin we need.

* Need to deploy a pod network for the cluster.

* Join the worker nodes up with the provided command.

* When setting up multiple Master Nodes, the command to join multiple Control Plane nodes will also be given.

    * One Master Node would not see the above output displayed.
    
* Then we install the Pod Network Addon

* A good option is Flannel 

    * A Kubernetes Manifest is given to apply the Pod Network Addon.
    
    * If using a custom CIDR network (i.e. not `10.244.0.0/16`) , have to download the manifest and modify the network to match your own.
    
        * You can `wget` the `kube-flannel.yaml` file.
        
        * Once you open the file, you configure the Pod Network under the `net-conf.json` title, under where it says `Network`.
        
            * Need to make sure the IP range given also matches the `--pod-network-cidr` command that was initially given as well.
            
    * Then do `kubectl apply -f <flannel.yaml>`
    
* Then check with `kubectl get pod -n kube-system` namespace as well.

* Also check with `kubectl get pod -n kube-flannel`

* Finally have the other worker nodes join the cluster without issue.

* When the `kube-flannel` namespace is checked again with `kubectl get pod -n kube-flannel`, it deploys the network plugin agent on every single nodes - that is why the amount of pods increases.

* Run a test pod with `kubectl run web --image=nginx`.
