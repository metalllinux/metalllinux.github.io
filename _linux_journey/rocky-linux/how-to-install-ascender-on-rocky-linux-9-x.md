---
title: "How To Install Ascender On Rocky Linux 9.X"
category: "rocky-linux"
tags: ["rocky-linux", "install", "ascender", "rocky", "linux"]
---

* Update all packages:
```
sudo dnf upgrade -y
```
* Install a GUI:
```
sudo dnf group install -y "Server with GUI"
sudo systemctl set-default graphical
sudo reboot
```
* Set a fully qualified domain name:
```
sudo hostnamectl set-hostname ascender.apptainer.test
```
* Update `/etc/hosts` file:
```
cat << "EOF" | sudo tee /etc/hosts
192.168.1.50 ascender.apptainer.test ascender
192.168.1.50 react.apptainer.test react
192.168.1.50 ledger.apptainer.test ledger
192.168.1.51 
EOF
```
* Install `git`:
```
sudo dnf install -y git
```
* Clone the `ascender-install` repository:
```
git clone https://github.com/ctrliq/ascender-install.git
```
* Change into the `ascender-install` directory:
```
cd ascender-install
```
* Two files need to be configured:
* `default.config.yml` this is the kube config for Kubernetes. This will run K3S. It will install on the Rocky node.
* Example `inventory` file:
![Screenshot 2025-02-21 at 14.13.57.png](../_resources/Screenshot%202025-02-21%20at%2014.13.57.png)
* The ability to connect to a remote host is available under the `[ascender]` header, aside from the `local` part.
* `[localhost]` is connecting to itself.
* Example `default.config.yml` file:
![Screenshot 2025-02-21 at 14.15.46.png](../_resources/Screenshot%202025-02-21%20at%2014.15.46.png)
* A hostname for Ascender is important:
![Screenshot 2025-02-21 at 14.16.24.png](../_resources/Screenshot%202025-02-21%20at%2014.16.24.png)
* Update passwords:
![Screenshot 2025-02-21 at 14.17.21.png](../_resources/Screenshot%202025-02-21%20at%2014.17.21.png)
* Need to create static DNS entries:
![Screenshot 2025-02-21 at 14.18.47.png](../_resources/Screenshot%202025-02-21%20at%2014.18.47.png)
* This can be manged via the hostfile on the machine. Add the local DNS entry into there.
* When connecting into Ascender, it is going to use the domain name as a way to connect to Kubernetes.
* Install is unsecured:
![Screenshot 2025-02-21 at 14.31.30.png](../_resources/Screenshot%202025-02-21%20at%2014.31.30.png)
* Apply this `default.config.yml` file:
```
cat << "EOF" | tee ./default.config.yml
---
# ---Kubernetes-specific variables---

# This variable specificies which Kubernetes platform Ascender and its components will be installed on.
k8s_platform: k3s # Options include k3s, eks and dkp, with more to come.

# Determines whether to use HTTP or HTTPS for Ascender and Ledger.
# If set to https, you MUST provide certificate/key options for the Installer to use.
k8s_lb_protocol: http #options include http and https

# Routable IP address for the K8s API Server
# (This could be a Load Balancer if using 3 K8s control nodes)
kubeapi_server_ip: "127.0.0.1"

# This value being set to "true" means that some work needs to be done to set up a
# cluster before proceeding. Here is ther behavior for different values of k8s_platforms:
# k3s: A single-node k3s cluster will be set up on the inventory server
#      named "ascender_host"
# eks: N/A, as this is handled by the EKS_CLUSTER_STATUS variable
# rke2: N/A, as you must use Labyrinth Labs' Ansible role to set up a fresh kubernetes cluster
kube_install: true

# Offline Install - Whether to use local assets to complete the install
k8s_offline: false 

# Specify an INTERNAL container registry and namespace where the k8s cluster can access Ascender images
k8s_container_registry: ""

# Kubernetes secret containing the login credentials required for the INTERNAL registry holding the ASCENDER images
#LEAVE AS NONE if no such secret is required
k8s_image_pull_secret: None

# Kubernetes secret containing the login credentials required for the INTERNAL registry holding the EXECUTION ENVIRONMENT images
#LEAVE AS NONE if no such secret is required
k8s_ee_pull_credentials_secret: None

# Indictates whether or not the kubeconfig file needs to be downloaded to the Ansible controller
download_kubeconfig: true

# ---k3s variables---

# IP address for the K3s Master/Worker node
# Required for local DNS and k3s install
# This IP Address must be close reachable by the server from which this installer is running
k3s_master_node_ip: "127.0.0.1"

# ---eks variables---

# Determines whether to use Route53's Domain Management (which is automated)
# Or a third-party service (e.g., Cloudflare, GoDaddy, etc.)
#If this value is set to false, you will have to manually set a CNAME record for 
# {{ASCENDER_HOSTNAME }} and {{ LEDGER_HOSTNAME }} to point to their corresponding
# AWS Loadbalancers
USE_ROUTE_53: yes

# If desired, this indicates an AWS IAM user that can be set up in order to have minimum 
# permissions to set up a new eks cluster and install Ascender and its associoated components
EKS_USER: ascenderuser

# The name of the eks cluster to set up
EKS_CLUSTER_NAME: ascender-eks-cluster

# Determines what to do with the eks cluster Ascender wil be installed on:
# provision: Provision a new EKS cluster from scratch
# configure: use the cluster specified by the variable EKS_CLUSTER_NAME, and configure it with 
#            policies for loa balancer creation and elastic block service access
# no_action: use the cluster specified by the variable EKS_CLUSTER_NAME, but make no changes to it before
#            installing Ascender.
EKS_CLUSTER_STATUS: no_action

# The AWS region hosting the eks cluster
EKS_CLUSTER_REGION: us-east-1

# The eks cluster subnet in CIDR notation
# Only required if EKS_CLUSTER_STATUS is set to provision.
EKS_CLUSTER_CIDR: "10.10.0.0/16"

# The kubernetes version for the eks cluster; available kubernetes versions can be found here:
# https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions.html
EKS_K8S_VERSION: "1.28"

# The worker node instance types 
EKS_INSTANCE_TYPE: t3.large

# The minimum number of worker nodes that the cluster will run
EKS_MIN_WORKER_NODES: 2

# The maximum number of worker nodes that the cluster will run
EKS_MAX_WORKER_NODES: 6

# The desired number of worker nodes for the eks cluster
EKS_NUM_WORKER_NODES: 3

# The size of the Elastic Block Storage volume for each worker node
EKS_WORKER_VOLUME_SIZE: 100

# The ARN for the SSL certificate; required when k8s_lb_protocol is https.
# The same certificate is used for all components (currently Ascender and Ledger); 
# as such, we recommend that the certificate is set for a wildcard domain
# (e.g., *.example.com)
EKS_SSL_CERT: arn:aws:acm:<region>:xxxxxxxxxx:certificate/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx

# The Amazon Elastic Block Store Container Storage Interface (CSI) Driver provides
# a CSI interface used by Container Orchestrators to manage the lifecycle of Amazon EBS volumes.
# This variable specifies the version in use by the cluster; all releases can be found here:
# https://github.com/kubernetes-sigs/aws-ebs-csi-driver/releases
EKS_EBS_CSI_DRIVER_VERSION: "v1.24.0"

# ---aks variables---
# The name of the aks cluster to install Ascender on - if it does not already exist, the installer can set it up
AKS_CLUSTER_NAME: ascender-aks-cluster

# Determines whether to use Azure DNS' Domain Management (which is automated)
# Or a third-party service (e.g., Cloudflare, GoDaddy, etc.)
#If this value is set to false, you will have to manually set an A record for 
# {{ASCENDER_HOSTNAME }} and {{ LEDGER_HOSTNAME }} to point to their corresponding
# Azure Loadbalancers
USE_AZURE_DNS: true

# Specifies whether the AKS cluster needs to be provisioned (provision), exists but needs to be configured to support Ascender (configure), or exists and needs nothing done before installing Ascender (no_action)
AKS_CLUSTER_STATUS: provision

# The Azure region hosting the aks cluster
AKS_CLUSTER_REGION: southcentralus

# The kubernetes version for the aks cluster; available kubernetes versions can be found here:
# https://learn.microsoft.com/en-us/azure/aks/supported-kubernetes-versions?tabs=azure-cli
AKS_K8S_VERSION: "1.29"

# The aks worker node instance types
AKS_INSTANCE_TYPE: "Standard_D2_v2"

# The desired number of aks worker nodes
AKS_NUM_WORKER_NODES: 3

# The volume size of aks worker nodes in GB
AKS_WORKER_VOLUME_SIZE: 100

# ---dkp variables---
# The name of the dkp cluster you wish to deploy Ascender to and/or create
# See a list of all dkp clusters with the command 
# NOTE: This must be done while pointing to the DKP Bootstrap Cluster
DKP_CLUSTER_NAME: dkp-cluster

# ---rke2 variables---

# The URL to the binary file rke2.linux-amd64. If you want to choose a different 
# release, you can choose here:
# https://github.com/rancher/rke2/releases
RKE2_BINARY_URL: https://github.com/rancher/rke2/releases/download/v1.25.16%2Brke2r1/rke2.linux-amd64


# ---Local artifact variables---

# TLS Certificate file, required when deploying HTTPS in K3s
tls_crt_path: "~/ascender.crt"

# TLS Private Key file, required when deploying HTTPS in K3s
tls_key_path: "~/ascender.key"

# Set to false if using an external DNS server for resolution
# Set to true if not
use_etc_hosts: true

# A directory in which to place both temporary artifacts
# and timestamped Kubernetes Manifests to make Ascender/Ledger easy
# to uninstall
tmp_dir: "{{ playbook_dir }}/../ascender_install_artifacts"

# ---Ascender install variables---

# DNS resolvable hostname for Ascender service. This is required for install.
ASCENDER_HOSTNAME: ascender.apptainer.test

# The domain name for all components; required when k8s_platorm=="eks"
ASCENDER_DOMAIN: example.local

# k8s namespace for Ascender k8s objects
ASCENDER_NAMESPACE: ascender

# Administrator username for Ascender
ASCENDER_ADMIN_USER: admin

# Administrator password for Ascender
ASCENDER_ADMIN_PASSWORD: "gnxzWOenKc*d$I1"

# The OCI container image for Ascender
ASCENDER_IMAGE: ghcr.io/ctrliq/ascender

# The image tag indicating the version of Ascender you wish to install
ASCENDER_VERSION: 24.0.1

# The version of the AWX Operator used to install Ascender and its components
ANSIBLE_OPERATOR_VERSION: 2.13.1

# Determines whether to keep the secrets required to encrypt within Ascender (important when backing up)
ascender_garbage_collect_secrets: true

# Setup extra demo playbooks after installation
ascender_setup_playbooks: true

# # External PostgreSQL ip or url resolvable by the cluster
# ASCENDER_PGSQL_HOST: "ascenderpghost.example.com"

# # External PostgreSQL port, this usually defaults to 5432
# ASCENDER_PGSQL_PORT: 5432

# # External PostgreSQL username
# ASCENDER_PGSQL_USER: ascender

# # External PostgreSQL password
# NOTE: Do NOT use the special characters in the postgres password (Django requirement)
# ASCENDER_PGSQL_PWD: cklBpJeOPWX7R7s

# # External PostgreSQL database name used for Ascender (this DB must exist)
# ASCENDER_PGSQL_DB: ascenderdb


### All of these options are unnecessary to change, but will allow you to tweak your Ascender deployment if you choose to change them
ascender_replicas: 1
ascender_image_pull_policy: Always

# ---Ascender React install variables---
# Determines whether or not Ascender React will be installed
REACT_INSTALL: false

# DNS resolvable hostname for Ascender React service. This is required for install.
REACT_HOSTNAME: react.apptainer.test

# k8s namespace for Ascender React k8s objects
REACT_NAMESPACE: react

# Administrator username for Ascender React
REACT_ADMIN_USER: admin

# Administrator password for Ascender React
REACT_ADMIN_PASSWORD: "gnxzWOenKc*d$I1"

# The version of the EDA Operator used to install Ascender React and its components
REACT_OPERATOR_VERSION: 1.0.2

# The OCI container image for Ascender React
REACT_IMAGE: quay.io/ansible/eda-server
REACT_IMAGE_VERSION: main

# The OCI container image for Ascender React UI
REACT_IMAGE_WEB: quay.io/ansible/eda-ui
REACT_IMAGE_WEB_VERSION: 2.4.1132

# TLS Certificate file, required when deploying HTTPS in K3s
react_tls_crt_path: "~/ascender.crt"

# TLS Private Key file, required when deploying HTTPS in K3s
react_tls_key_path: "~/ascender.key"

# # External PostgreSQL ip or url resolvable by the cluster
# REACT_PGSQL_HOST: "reactpghost.example.com"

# # External PostgreSQL port, this usually defaults to 5432
# REACT_PGSQL_PORT: 5432

# # External PostgreSQL username
# REACT_PGSQL_USER: react

# # External PostgreSQL password
# NOTE: Do NOT use the special characters in the postgres password (Django requirement)
# REACT_PGSQL_PWD: cklBpJeOPWX7R7s

# # External PostgreSQL database name used for Ascender (this DB must exist)
# REACT_PGSQL_DB: reactdb

# ---Ledger install variables---

# Determines whether or not Ledger will be installed
LEDGER_INSTALL: false

# DNS resolvable hostname for Ledger service. This is required for install.
LEDGER_HOSTNAME: ledger.apptainer.test

# The OCI container image for Ledger
LEDGER_WEB_IMAGE: ghcr.io/ctrliq/ascender-ledger/ledger-web

# The number of ledger web pods - this is good to ensure high availability
ledger_web_replicas: 1

# The OCI container image for the Ledger Parser
LEDGER_PARSER_IMAGE: ghcr.io/ctrliq/ascender-ledger/ledger-parser

# The number of ledger parser pods - this is good to ensure high availability
ledger_parser_replicas: 1

# The OCI container image for the Ledger Database
LEDGER_DB_IMAGE: ghcr.io/ctrliq/ascender-ledger/ledger-db

# The image tag indicating the version of Ledger you wish to install
LEDGER_VERSION: latest

# The Kubernetes namespace in which Ledger objects will live
LEDGER_NAMESPACE: ledger

# Admin password for Ledger (the username is admin by default)
LEDGER_ADMIN_PASSWORD: "gnxzWOenKc*d$I1"

# Password for Ledger database
LEDGER_DB_PASSWORD: "gnxzWOenKc*d$I1"
EOF
```
* Edit the `playbooks/roles/setup_playbooks/vars/main.yml` file to look like the following, to bypass the CIS Hardening Timeouts
```
cat << "EOF" | tee ./playbooks/roles/setup_playbooks/vars/main.yml
inventories:
  - name: Default Inventory

projects:
  - name: Ascender Playbooks
    description: Administrative Playbooks for Rocky Linux
    scm_type: git
    scm_url: https://github.com/ctrliq/ascender-playbooks.git
    scm_update_on_launch: false

templates:
  - name: Configure SELinux
    description: ""
    job_type: run
    inventory: Default Inventory
    project: Ascender Playbooks
    playbook: selinux.yml
    survey_enabled: true
    survey_file: surveys/selinux.json
    ask_credential_on_launch: true
    diff_mode: true

  - name: Gather System Facts
    description: ""
    job_type: run
    inventory: Default Inventory
    project: Ascender Playbooks
    playbook: gather_facts.yml
    ask_credential_on_launch: true

  - name: Patch Enterprise Linux
    description: ""
    job_type: run
    inventory: Default Inventory
    project: Ascender Playbooks
    playbook: patching.yml
    survey_enabled: true
    survey_file: surveys/patching.json
    ask_credential_on_launch: true
EOF
```
* No need to edit the `inventory` file.
* Once done, run `setup.sh`:
```
sudo ./setup.sh
```
* Once the installation is complete, re-apply the original `main.yml` file:
```
cat << "EOF" | tee ./playbooks/roles/setup_playbooks/vars/main.yml
inventories:
  - name: Default Inventory

projects:
  - name: Ascender Playbooks
    description: Administrative Playbooks for Rocky Linux
    scm_type: git
    scm_url: https://github.com/ctrliq/ascender-playbooks.git
    scm_update_on_launch: false

  - name: Ansible Lockdown - CIS - EL9
    description: CIS Benchmark Hardening for Enterprise Linux 9
    scm_type: git
    scm_url: https://github.com/ansible-lockdown/RHEL9-CIS.git
    scm_update_on_launch: false

  - name: Ansible Lockdown - CIS - EL8
    description: CIS Benchmark Hardening for Enterprise Linux 8
    scm_type: git
    scm_url: https://github.com/ansible-lockdown/RHEL8-CIS.git
    scm_update_on_launch: false

  - name: Ansible Lockdown - STIG - EL8
    description: STIG Hardening for Enterprise Linux 8
    scm_type: git
    scm_url: https://github.com/ansible-lockdown/RHEL8-STIG.git
    scm_update_on_launch: false

templates:
  - name: Configure SELinux
    description: ""
    job_type: run
    inventory: Default Inventory
    project: Ascender Playbooks
    playbook: selinux.yml
    survey_enabled: true
    survey_file: surveys/selinux.json
    ask_credential_on_launch: true
    diff_mode: true

  - name: Gather System Facts
    description: ""
    job_type: run
    inventory: Default Inventory
    project: Ascender Playbooks
    playbook: gather_facts.yml
    ask_credential_on_launch: true

  - name: Patch Enterprise Linux
    description: ""
    job_type: run
    inventory: Default Inventory
    project: Ascender Playbooks
    playbook: patching.yml
    survey_enabled: true
    survey_file: surveys/patching.json
    ask_credential_on_launch: true

  - name: CIS Benchmark Hardening for Enterprise Linux 9
    description: CIS Benchmark Hardening for Enterprise Linux 9
    job_type: run
    inventory: Default Inventory
    project: Ansible Lockdown - CIS - EL9
    playbook: site.yml
    ask_credential_on_launch: true
    diff_mode: true

  - name: CIS Benchmark Hardening for Enterprise Linux 8
    description: CIS Benchmark Hardening for Enterprise Linux 8
    job_type: run
    inventory: Default Inventory
    project: Ansible Lockdown - CIS - EL8
    playbook: site.yml
    ask_credential_on_launch: true
    diff_mode: true

  - name: STIG Hardening for Enterprise Linux 8
    description: STIG Hardening for Enterprise Linux 8
    job_type: run
    inventory: Default Inventory
    project: Ansible Lockdown - STIG - EL8
    playbook: site.yml
    ask_credential_on_launch: true
    diff_mode: true
EOF
```
* Run the `ansible-playbook` command to create the `CIS` and `STIG` projects within Ascender:
```
ansible-playbook -i ./inventory -v playbooks/setup_playbooks.yml
```
* Access Ascender by running `ascender.apptainer.test` in a browser



