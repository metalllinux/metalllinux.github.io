---
title: "Lightning Lab - Practice Exam"
category: "cka-certification"
tags: ["cka-certification", "lightning", "lab", "practice", "exam"]
---

# Lightning Lab - Practice Exam

* Example questions:

* Upgrade the current version of kubernetes from 1.32.0 to 1.33.0 exactly using the kubeadm utility. Make sure that the upgrade is carried out one node at a time starting with the controlplane node. To minimise downtime, the deployment gold-nginx should be rescheduled on an alternate node before upgrading each node.

Upgrade controlplane node first and drain node node01 before upgrading it. Pods for gold-nginx should run on the controlplane node subsequently.

* Print the names of all deployments in the admin2406 namespace in the following format:

DEPLOYMENT   CONTAINER_IMAGE   READY_REPLICAS   NAMESPACE

<deployment name>   <container image used>   <ready replica count>   <Namespace>
. The data should be sorted by the increasing order of the deployment name.

Example:

DEPLOYMENT   CONTAINER_IMAGE   READY_REPLICAS   NAMESPACE
deploy0   nginx:alpine   1   admin2406
Write the result to the file /opt/admin2406_data.

* A kubeconfig file called admin.kubeconfig has been created in /root/CKA. There is something wrong with the configuration. Troubleshoot and fix it.

* Create a new deployment called nginx-deploy, with image nginx:1.16 and 1 replica.
Next, upgrade the deployment to version 1.17 using rolling update and add the annotation message
Updated nginx image to 1.17.

* A new deployment called alpha-mysql has been deployed in the alpha namespace. However, the pods are not running. Troubleshoot and fix the issue. The deployment should make use of the persistent volume alpha-pv to be mounted at /var/lib/mysql and should use the environment variable MYSQL_ALLOW_EMPTY_PASSWORD=1 to make use of an empty root password.

Important: Do not alter the persistent volume.

* Take the backup of ETCD at the location /opt/etcd-backup.db on the controlplane node.

* Create a pod called secret-1401 in the admin1401 namespace using the busybox image. The container within the pod should be called secret-admin and should sleep for 4800 seconds.

The container should mount a read-only secret volume called secret-volume at the path /etc/secret-volume. The secret being mounted has already been created for you and is called dotfile-secret.
