---
title: "How to Setup Rootless Podman in a Custom Directory"
category: "kubernetes-and-containers"
tags: ["kubernetes-and-containers", "setup", "rootless", "podman", "custom"]
---

# How to Setup Rootless Podman in a Custom Directory

* Booted up a fresh Rocky Linux 8.10 VM and fully upgraded all packages.

* Disabled SELinux:

```
sudo setenforce 0
sudo sed -i 's/^SELINUX=.*/SELINUX=permissive/' /etc/selinux/config
```

* Created the `/local` directory:

```
sudo mkdir -p /local
sudo chmod 1777 /local
```

* Generated the subdirectory for `rootless podman`:

```
sudo mkdir -p /local/podman
sudo chmod 777 /local/podman
```

* Created a per-user Podman storage directory (in this case for my user):

```
mkdir -p /local/podman/$USER
```

* Generated my local `containers` directory:

```
mkdir -p ~/.config/containers
```

* Overrode my `graphroot` and `runroot` values and pointed those to the `/local/podman` location:

```
cat << "EOF" | tee ~/.config/containers/storage.conf 
[storage]
driver = "overlay"
graphroot = "/local/podman/$USER/containers/storage"
runroot = "/local/podman/$USER/containers/run"
EOF
```

* Ran my Rocky Linux 8.10 container:

```
podman run -it --rm rockylinux:8 bash
```

