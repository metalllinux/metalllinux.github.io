---
title: "Solution Backup And Restore 2"
category: "cka-certification"
tags: ["cka-certification", "solution", "backup", "restore"]
---

* How to see how many clusters are defined:
```
kubectl config view
```
* How to switch to a particular cluster:
```
kubectl config use-context <cluster_name>
```
* How to take a backup and check the endpoints for `etcd`:
```
kubectl describe  pods -n kube-system etcd-cluster1-controlplane  | grep advertise-client-url

kubectl describe  pods -n kube-system etcd-cluster1-controlplane  | grep pki
```
* On restoring snapshots:
Step 1. Copy the snapshot file from the student-node to the etcd-server. In the example below, we are copying it to the /root directory:

student-node ~  scp /opt/cluster2.db etcd-server:/root
cluster2.db                                                                                                        100% 1108KB 178.5MB/s   00:00    

student-node ~ ➜

Step 2: Restore the snapshot on the cluster2. Since we are restoring directly on the etcd-server, we can use the endpoint https:/127.0.0.1. Use the same certificates that were identified earlier. Make sure to use the data-dir as /var/lib/etcd-data-new:

etcd-server ~ ➜  ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379 --cacert=/etc/etcd/pki/ca.pem --cert=/etc/etcd/pki/etcd.pem --key=/etc/etcd/pki/etcd-key.pem snapshot restore /root/cluster2.db --data-dir /var/lib/etcd-data-new
{"level":"info","ts":1721940922.0441437,"caller":"snapshot/v3_snapshot.go:296","msg":"restoring snapshot","path":"/root/cluster2.db","wal-dir":"/var/lib/etcd-data-new/member/wal","data-dir":"/var/lib/etcd-data-new","snap-dir":"/var/lib/etcd-data-new/member/snap"}
{"level":"info","ts":1721940922.060755,"caller":"mvcc/kvstore.go:388","msg":"restored last compact revision","meta-bucket-name":"meta","meta-bucket-name-key":"finishedCompactRev","restored-compact-revision":951}
{"level":"info","ts":1721940922.0667593,"caller":"membership/cluster.go:392","msg":"added member","cluster-id":"cdf818194e3a8c32","local-member-id":"0","added-peer-id":"8e9e05c52164694d","added-peer-peer-urls":["http://localhost:2380"]}
{"level":"info","ts":1721940922.0732546,"caller":"snapshot/v3_snapshot.go:309","msg":"restored snapshot","path":"/root/cluster2.db","wal-dir":"/var/lib/etcd-data-new/member/wal","data-dir":"/var/lib/etcd-data-new","snap-dir":"/var/lib/etcd-data-new/member/snap"}

etcd-server ~ ➜

Step 3: Update the systemd service unit file for etcd by running vi /etc/systemd/system/etcd.service and add the new value for data-dir:

[Unit]
Description=etcd key-value store
Documentation=https://github.com/etcd-io/etcd
After=network.target

[Service]
User=etcd
Type=notify
ExecStart=/usr/local/bin/etcd \
  --name etcd-server \
  --data-dir=/var/lib/etcd-data-new \
---End of Snippet---

Step 4: make sure the permissions on the new directory is correct (should be owned by etcd user):

etcd-server /var/lib ➜  chown -R etcd:etcd /var/lib/etcd-data-new

etcd-server /var/lib ➜ 


etcd-server /var/lib ➜  ls -ld /var/lib/etcd-data-new/
drwx------ 3 etcd etcd 4096 Jul 15 20:55 /var/lib/etcd-data-new/
etcd-server /var/lib ➜

Step 5: Finally, reload and restart the etcd service.

etcd-server ~ ➜  systemctl daemon-reload 
etcd-server ~ ➜  systemctl restart etcd
etcd-server ~ ➜  

Step 6 (optional): It is recommended to restart controlplane components (e.g. kube-scheduler, kube-controller-manager, kubelet) to ensure that they don't rely on some stale data.

* How to check that `etcd` is using a stacked or external ETCD server.
	* To verify, do a `kubectl get pods -n kube-system`. We know that a `stacked etcd` is being used, if there is an `etcd` pod running.
* Can also describe the pod with the following:
```
kubectl describr epod kube-apiserver -n kube-system
```
* From the above command, you can check the `--etcd-server` output to see which IP address and port it is running on.
* How is `etcd` configured on a separate cluster?
	* `ssh` into the ControlPlane node.
	* Look at static pod configurations under `/etc/kubernetes/manifests`
		* If there are no `etcd`-related configurations, it is not a stacked `etcd` setting.
		* Can also check by running `kubectl get pods -n kube-system` and describing the pod with `kube-apiserver` in the title.
		* Look at the configuration from the output of the `describe` command and you'll potentially see it point to a separate server address.
			* If that is the case, it means an external `etcd` server is in use.
* What is the default data directory used for the `etcd` datastore in X cluster.
	* Run `kubectl get pods -n kube-system`
	* Then perform a `describe` on the `etcd-<title>` pod that is available.
		* Check the `--data-dir` flag from the output, that will be the default data directory.
* How to find the default data directory used for the `etcd` datastore used in <cluster>
	* `ssh` into the `etcd-server`.
	* Then run the following:
```
ps -ef | grep -i etcd
```
* Can find the `--data-dir` flag in the above `ps` p
* output.
* How many nodes are part of the `etcd` cluster that the `etcd-server` is part of?
	* Can do `etcdctl member list`, need version first:
```
ETCDCTL_API=3 etcdctl --endpoint=<get_the_listen-client-urls_address> --cacert=<--trusted-ca-file> --cert=<--cert-file --key=<--key-file>> member list
```
* Example version:
```
ETCDCTL_API=3 etcdctl --endpoints-https://127.0.0.1:2379 --cacert=/etc/etcd/pki/ca.pem --cert=/etc/etcd/pki/etcd.pem --key=/etc/etcd/pki/etcd-key.pem member list
```
* When you run the above, you see there is one entry so there is only one member in the cluster.
* Next question, take a backup of `etcd` on `cluster1` and save it on the `student-node` at `/opt/cluster1.db`
```
kubectl config use-context cluster1
```
* Using `etcd` in `stacked` mode, so it will be ran as a pod.
* `kubectl describe pod <etcd-pod>`
* Need the `--advertise-client-urls`, `--cert-file`, `--key-file` and `--trusted-ca`
* `ssh` into `cluster1-controlplane` node.
* Set to version 3: `ETCDCTL_API=3 etcdctl --endpoints=https://192.33.162.8:2379<taken from the --advertise-client-urls flag> --cacert=/etc/kubernetes/pki/etcd/ca.cert<taken from the --trusted-ca line> --cert=/etc/kubernetes/pki/etcd/server.crt <from the --cert-file flag> --key=/etc/kubernetes/pki/etcd/server.key <taken from the --key-file> snapshot save /opt/cluster1.db`
* The snapshot is then saved in `/opt`
* Copy the file with `scp`:
```
scp cluster1-controlplane:/opt/cluster1.db /opt
```
* Next question: An `ETCD` backup for `cluster2` is stored at `/opt/cluster2.db`. Use the snapshot file to carry out a restore on `cluster2` to a new path in `/var/lib/etcd-data-new`
* `scp` to the `etcd-server` machine:
```
scp /opt/cluster2.db etcd-server:/root
```
* Now to do a `snapshot restore` on the `etcd` server and set the snapshots to version 3:
```
ETCDCTL_API=3 etcdctl snapshot restore /root/cluster2.db --data-dir=/var/lib/etcd-data-new
```
* No need to connect to the `etcd` server. as we are just doing a restore.
* Make sure to change the owner of the `/var/lib/etcd-data-new` directory:
```
chown -R etcd:etcd etcd-data-new
```
* Change the configuration on he `etcd` process:
```
vim /etc/systemd/system/etcd.service
```
* Only need to change the `--data-dir` flag to point to the new `/var/lib/etcd-data-new` directory.
* Run `systemctl daemon-reload`
* Then `systemctl restart etcd`
* Need to restart all of the control plane components, so they do not use stale data.
```
kubectl get pods -n kube-system
```
* Delete these pods:
```
kubectl-controller-manager
kube-scheduler
```
* Check with `kubectl get pods -n kube-system` that they both come back up.
* `ssh` to the controlplane node.
* Do `systemctl restart kubelet`
* `systemctl status kubelet` for verification.
* 