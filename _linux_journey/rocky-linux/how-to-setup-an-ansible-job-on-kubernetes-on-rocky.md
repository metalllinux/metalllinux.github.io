---
title: "How To Setup An Ansible Job On Kubernetes On Rocky"
category: "rocky-linux"
tags: ["rocky-linux", "setup", "ansible", "job", "kubernetes"]
---

* I set up a fresh Rocky Linux 9.5 instance with `Kubernetes`. 
* Allowed pods to be assigned to the `Control Plane` node.
* Installed `docker`.
* I logged into `docker` with `docker login`.
* I then used this Rocky Linux `Ansible` `Dockerfile` from [geerlingguy's repository](https://github.com/geerlingguy/docker-rockylinux8-ansible):
```
cat << "EOF" | tee ~/Dockerfile
FROM rockylinux:8
LABEL maintainer="Jeff Geerling"
ENV container=docker

# See: https://github.com/geerlingguy/docker-rockylinux8-ansible/issues/6
ENV pip_packages "ansible<10.0"

# Install systemd -- See https://hub.docker.com/_/centos/
RUN rm -f /lib/systemd/system/multi-user.target.wants/*;\
rm -f /etc/systemd/system/*.wants/*;\
rm -f /lib/systemd/system/local-fs.target.wants/*; \
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
rm -f /lib/systemd/system/basic.target.wants/*;\
rm -f /lib/systemd/system/anaconda.target.wants/*;

# Install requirements.
RUN yum -y install rpm dnf-plugins-core \
 && yum -y update \
 && yum -y config-manager --set-enabled powertools \
 && yum -y install \
      epel-release \
      initscripts \
      sudo \
      which \
      hostname \
      libyaml-devel \
      python3 \
      python3-pip \
      python3-pyyaml \
      iproute \
 && yum clean all

# Upgrade pip to latest version.
RUN pip3 install --upgrade pip

# Install Ansible via Pip.
RUN pip3 install $pip_packages

# Disable requiretty.
RUN sed -i -e 's/^\(Defaults\s*requiretty\)/#--- \1/'  /etc/sudoers

# Install Ansible inventory file.
RUN mkdir -p /etc/ansible
RUN echo -e '[local]\nlocalhost ansible_connection=local' > /etc/ansible/hosts

VOLUME ["/sys/fs/cgroup"]
CMD ["/usr/lib/systemd/systemd"]
EOF
```
* I built the Ansible image:
```
docker build -t ansible-image .
```
* The build was successful.
* I created a repository on DockerHub called `ansible-image`.
* I tagged the image:
```
docker tag ansible-image:latest metalllinux/ansible-image:latest
```
* I pushed the image to DockerHub:
```
docker image push metalllinux/ansible-image:latest
```
* I set up the `inventory` directory:
```
mkdir ~/inventory
```
* I then made a directory called `playbooks`:
```
mkdir ~/playbooks
```
* Inside the `playbooks` directory I added the `update-the-node.yaml` playbook:
```
cat << "EOF" | tee ~/playbooks/update-the-node.yaml
---
- hosts: localhost
  gather_facts: false
  serial: 1
  
  tasks:
    - name: Check packages to upgrade
      dnf:
        list: updates
      register: packages

    - name: Show packages to upgrade
      debug:
        msg: >-
          {%- set output=[] -%}
          {%- for p in packages.results -%}
          {{ output.append('%-40s' % (p.name ~ '-' ~ p.version) ~ ' | repo: ' ~ p.repo) }}
          {%- endfor -%}
          {{ output }}
    
    - name: Upgrade all packages
      ansible.builtin.dnf:
        name: "*"
        state: latest
EOF
```
* I created the Kubernetes job definition file:
```
cat << "EOF" | tee ~/ansible-update-node.yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: ansible-update-node
spec:
  template:
    spec:
      containers:
      - name: ansible-image
        image: docker.io/metalllinux/ansible-image:latest
        command: ["ansible-playbook", "/etc/ansible/update-the-node.yaml"]
        volumeMounts:
        - name: ansible-playbook-volume
          mountPath: /etc/ansible/update-the-node.yaml
      restartPolicy: OnFailure
      volumes:
      - name: ansible-playbook-volume
        hostPath:
          path: /home/howard/playbooks/update-the-node.yaml
          type: File
      tolerations:
        - key: "node-role.kubernetes.io/control-plane"
          operator: "Exists"
          effect: "NoSchedule"
EOF
```
* Then I created the `job`:
```
kubectl create -f ~/ansible-update-node.yaml
```
* Checking `kubectl logs` for the `pod`, I can see that the job ran as required:
```
[howard@rocky-linux-95-kubernetes-ansible ~]$ kubectl logs -f ansible-update-node-9qg6z
[DEPRECATION WARNING]: Ansible will require Python 3.8 or newer on the 
controller starting with Ansible 2.12. Current version: 3.6.8 (default, Dec  4 
2024, 12:35:02) [GCC 8.5.0 20210514 (Red Hat 8.5.0-22)]. This feature will be 
removed from ansible-core in version 2.12. Deprecation warnings can be disabled
 by setting deprecation_warnings=False in ansible.cfg.

PLAY [localhost] ***************************************************************

TASK [Check packages to upgrade] ***********************************************
/usr/local/lib/python3.6/site-packages/ansible/parsing/vault/__init__.py:44: CryptographyDeprecationWarning: Python 3.6 is no longer supported by the Python core team. Therefore, support for it is deprecated in cryptography. The next release of cryptography will remove support for Python 3.6.
  from cryptography.exceptions import InvalidSignature
ok: [localhost]

TASK [Show packages to upgrade] ************************************************
ok: [localhost] => {
    "msg": [
        "epel-release-8                           | repo: epel"
    ]
}

TASK [Upgrade all packages] ****************************************************
changed: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```
* To capture the `pod` that is performing the `job` for Kubernetes, I created this BASH script:
```
cat << "EOF" | tee ~/record_pods_running_upgrade_jobs.sh
#!/bin/bash

# Add in the job definition file and file to record the pod output to
JOB_FILE=~/ansible-update-node.yaml
RECORD_POD_TO_FILE=~/all_pods_running_upgrade_jobs.txt

# Create the Kubernetes Job
kubectl create -f "$JOB_FILE"

# Wait for the pod to be created. This waits until the pod is running.
POD_NAME=$(kubectl get pods --selector=job-name=$(basename "$JOB_FILE" .yaml) -o jsonpath='{.items[0].metadata.name}')

# Get the current timestamp
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")

# Record the pod name and timestamp to the file
echo "$TIMESTAMP - $POD_NAME" >> "$RECORD_POD_TO_FILE"
echo "Pod name $POD_NAME with timestamp $TIMESTAMP recorded in $RECORD_POD_TO_FILE"
EOF
```
* From the file that is generated, you see an output similar to the below example:
```
2025-02-07 14:20:13 - Pod Name: ansible-update-node-f7dfm
2025-02-07 14:21:01 - Pod Name: ansible-update-node-9k25t
```