---
title: "Pre Requisite Security In Docker"
category: "cka-certification"
tags: ["cka-certification", "pre", "requisite", "security", "docker"]
---

* For example a host has Docker. It has a lot of processes such as the `docker daemon`.
* For example, run a `sleep` command:
```
docker run ubuntu sleep 3600
```
* Containers are isolated using namespaces in Linux. The host has its own namespace as well.
* All of the processes are run on the host - just in their own namespaces.
* By default, containers cannot see into other namespaces.
* Within a container, if you are running the `sleep` command and check `ps aux`, the `PID` will be set to `1`.
* When you run `ps -aux` on the host, the above `sleep` command for example will have a different PID.
* Processes can have different Process IDs in different namespaces.
* Docker host has `root` users and `non-root` users.
* Can run a process as a particular user:
```
docker run --user=1000 ubuntu sleep 3600
```
* Can also set this above in the `docker` image. `Dockerfile`:
```
FROM ubuntu

USER 1000
```
* Then run `docker build -t my-ubuntu-image .`
* Then run the image with:
```
docker run my-ubuntu-image sleep 3600
```
* What happens if you run a container as `root`?
	* Docker has a set of security features to limit the root user within the container.
	* Docker uses Linux Capabilities for the implementation process.
* See the full list of what the `root` user can do at this location: `/usr/include/linux/capability.h`
* An example of what the `root` user can do:
* `chown`
* `dac`
* `kill`
* `setfcap`
* `setpcap`
* `setgid`
* `setuid`
* `net_bind`
* `net_raw`
* `mac_admin`
* `broadcast`
* `net_admin`
* `sys_admin`
* `sys_chroot`
* `audit_write`
* If you wish to override the behaviour to restrict what the `root` user can do, add the `--cap-add` option. This looks like this:
```
docker run --cap-add MAC_ADMIN ubuntu
```
* Can drop `root` privileges as well, using the `--cap-drop` option. For example:
```
docker run --cap-drop KILL ubuntu
```
* To run the container with all privileges enabled:
```
docker run --privileged ubuntu
```