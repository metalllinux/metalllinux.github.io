---
title: "Slurm installation"
category: "rocky-linux"
tags: ["rocky-linux", "slurm", "installation", "rocky", "linux"]
---

#### Slurm installation

* I set up and updated all packages on a fresh Rocky Linux 8.10 VM. This is the `slurm` Contoller Node.
* I switched to the `root` user:
```
su - root
```
* I read through [this slurm guide](https://www.ni-sp.com/slurm-build-script-and-container-commercial-support/) and pulled this `slurm` install script:
```
wget --no-check-certificate https://raw.githubusercontent.com/NISP-GmbH/SLURM/main/slurm_install.sh
```
* I set the version as `20.11.9`:
```
export VER=20.11.9
```
* I ran the `slurm` installation script:
```
bash slurm_install.sh
```
* I did not enable `slurm accounting` support after checking the [accounting documentation](https://slurm.schedmd.com/accounting.html).
* I tested that the `slurm` installation completed successfully and this was the case:
```
[root@rocky-linux-8-slurm-head-node ~]# sinfo
PARTITION AVAIL  TIMELIMIT  NODES  STATE NODELIST
test*        up   infinite      1   idle rocky-linux-8-slurm-head-node
```