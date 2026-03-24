---
title: "Volume Driver Plugins In Docker"
category: "cka-certification"
tags: ["cka-certification", "volume", "driver", "plugins", "docker"]
---

* Storage drivers help manage storage on images and containers.
* If want to persist storage, need to create volumes.
	* Volumes **are not** handled by storage drivers.
	* Volumes are handled by `Volume Driver` plugins.
	* Default plugin is `Local`
		* Helps create a volume on the `docker` host.
			* Stores data under `/var/lib/docker/volumes` directory.
	* Other volume drivers include:
		* `Azure File Storage`, `Convoy`, `DigitalOcean Block Storage`, `Flocker`, `gce-docker`, `GlusterFS`, `NetApp`, `RexRay`, `Portworx`, `VMware vSphere Storage`
* `RexRay` storage driver can help to provision on AWS EBS, S3, EMC storage arrays (Isilon and ScaleIO), Google Persistent Disk or OpenStack Cinder,
* When running a `docker` container, can choose a specific volume driver as in the below example:
```
docker run -it --name mysql --volume-driver rexray/ebs --mount src=ebs-vol,target=/var/lib/mysql mysql
```
* The above provisions a volume from Amazon EBS.
* When the container exists, the data is still safe in the cloud.