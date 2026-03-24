---
title: "Ansible Host Setup for mighty"
category: "ansible-playbooks"
tags: ["ansible-playbooks", "ansible", "host", "setup", "mighty"]
---

# Ansible Host Setup for mighty

* Install `ansible-core`:

```
sudo dnf install -y ansible-core
```

* requirements.yaml setup:

cat << "EOF" | tee $HOME/requirements.yaml 
---

collections:
- name: community.crypto

- name: community.general

- name: community.mysql

- name: ansible.posix
EOF

* Manual Commands are below if needed:

* For `OpenSSH` support, install this collection:

```
ansible-galaxy collection install community.crypto
```

* Install the Ansible Community Collection:

```
ansible-galaxy collection install community.general
```

* Install the `mysql` community package for the `mariadb` database operations:

```
ansible-galaxy collection install community.mysql
```

* Install the `posix` collection for handling `ssh` keys and use of `rsync`:

```
ansible-galaxy collection install ansible.posix
```

* Install the `kubernetes@ collection:

```
ansible-galaxy collection install kubernetes.core
```

* Edit `/etc/ansible/hosts`

* Add the following:

```
cat << "EOF" | sudo tee /etc/ansible/hosts
[kubernetes_control_planes]
shin-ray ansible_ssh_host=192.168.1.101 

[kubernetes_worker_nodes]
green-hills ansible_ssh_host=192.168.1.100 

[rocky-linux8-slurm]
rocky-linux8-slurm-controller-node ansible_ssh_host=192.168.1.120
rocky-linux8-slurm-compute-node ansible_ssh_host=192.168.1.121

[rocky_linux10desktops]
shadow ansible_ssh_host=192.168.1.102 
amy ansible_ssh_host=192.168.1.105 

[rocky_linux10vms]
rocky-linux10-vm1 ansible_ssh_host=192.168.1.125

[rocky_linux9vms]
rocky-linux9-vm1 ansible_ssh_host=192.168.1.126

[rocky_linux8vms]
rocky-linux8-vm1 ansible_ssh_host=192.168.1.127

[control]
shin-ray ansible_ssh_host=192.168.1.101

[workers]
green-hills ansible_ssh_host=192.168.1.100
EOF
```

* Generate an `ssh` key pair:

```
ssh-keygen -t rsa -b 4096
```

* Use `ssh-copy-id` to access each server from the `ansible` host.

* Create the `group_vars` directory:

```
sudo mkdir /etc/ansible/group_vars
```

* Create the `rocky_linux_10desktops` configuration file:

```

cat << "EOF" | sudo tee /etc/ansible/group_vars/rocky_linux_10desktops
---
ansible_ssh_user: root
EOF
```

* Make the `kubernetes_control_planes` configuration file:

```
cat << "EOF" | sudo tee /etc/ansible/group_vars/kubernetes_control_planes
---
ansible_ssh_user: root
EOF
```

* Make the `kubernetes_worker_nodes` configuration file:

```
cat << "EOF" | sudo tee /etc/ansible/group_vars/kubernetes_worker_nodes
---
ansible_ssh_user: root
EOF
```

* Create the `rocky-linux8-slurm` configuration file:

```
cat << "EOF" | sudo tee /etc/ansible/group_vars/rocky-linux8-slurm
---
ansible_ssh_user: root
EOF
```

* Create the `rocky_linux10vms` configuration file:

```
cat << "EOF" | sudo tee /etc/ansible/group_vars/rocky_linux10vms
---
ansible_ssh_user: root
EOF
```

* Create the `rocky_linux9vms` configuration file:

```
cat << "EOF" | sudo tee /etc/ansible/group_vars/rocky_linux9vms
---
ansible_ssh_user: root
EOF
```

* Create the `rocky_linux8vms` configuration file:

```
cat << "EOF" | sudo tee /etc/ansible/group_vars/rocky_linux8vms
---
ansible_ssh_user: root
EOF
```

* Generate the `group_vars/all` file:

```
cat << "EOF" | sudo tee /etc/ansible/group_vars/all
---
rocky_linux8_slurm_controller_node_ip: 192.168.1.120
rocky_linux8_slurm_compute_node_ip: 192.168.1.121
EOF
```

* Test that the machines can be connected to:

```
ansible -m ping all
ansible -m ping <group_name>
ansible -m ping <host>
ansible -m ping <host1>:<host2>
ansible -m shell -a 'free -m' <host>
```
