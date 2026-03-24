---
title: "Backup And Restore Methods"
category: "cka-certification"
tags: ["cka-certification", "backup", "restore", "methods"]
---

* Backup Candidates:
	* Resource configuration - pod definition files etc/
	* ETCD Cluster - where all cluster-related information is stored.
	* Persistent Volumes
* Imperative Commands:
	* `kubectl create namespace new-namespace`
	* `kubectl create secret`
	* `kubectl create configmap`
* Declarative Approach:
	* Creating a definition file.
	* Then run `kubectl apply -f <filename>`
	* Ideally store these on source code repositories such as GitHub.
	* Don't need to stick to certain standards.
* A good way is to query the `kube-api server`.
	* Can save all definition files for all objects created on the cluster as a copy.
* A good command to use in a backup script:
```
kubectl get all -all-namespaces -o yaml > all-deploy-services.yaml
```
* Many other resource groups that must be considered.
* Useful tools such as Velero that can do this for you and takes backups using the `kube-apiserver`.
* `ETCD` contains information about the state of the cluster.
* Can backup the `ETCD` server.
* The `ETCD` cluster is hosted on the Master Nodes.
* In the `etcd.service` file, everything will be stored in the `--data-dir=/var/lib/etcd` by default.
	* This can be backupped by a backup tool.
* Can also take snapshots of the `ETCD` data using the following command
```
ETCDCTL_API=3 etcdctl \
     snapshot save snapshot.db 
```
* The output file is the following:
```
snapshot.db
```
* Can view the status of the backup using the `snapshot status` command:
```
ETCDCTL_API=3 etcdctl \
     snapshot status snapshot.db
```
* To restore the cluster from a later point in time:
	* Stop the ETCD service with:
```
sudo service kube-apiserver stop
```
* Then run the `snapshot restore` command and set the path to the backup file:
```
ETCDCTL_API=3 etcdctl \
 snapshot restore snapshot.db
 --data-dir /var/lib/etcd-from-backup
```
* When ETCD is restored from backup, it initialises a new cluster configuration.
* It also prevents new ETCD members from joining an existing cluster.
* Then reconfigure the `etcd.service` file to use the new `--data-dir` directory.
* Reload the service daemon:
```
sudo systemctl daemon-reload
```
* Restart the `etcd` service:
```
sudo service etcd restart
```
* Start the `kube-apiserver` service:
```
sudo service kube-apiserver start
```
* With all `etcd` command, specify the certificate for authentication:
```
ETCDCTL_API=3 etcdctl \
     snapshot save snapshot.db \
     --endpoints=https://127.0.0.1:2379
     --cacert=/etc/etcd/ca.crt \
     --cert=/etc/etcd/etcd-server.crt \
     --key=/etc/etcd/etcd-server.key
```
* If using a managed kubernetes environment, likely do not have access to the `etcd` cluster.
	* In that case, backup by querying the `kube-apiserver` is the best way.
* 