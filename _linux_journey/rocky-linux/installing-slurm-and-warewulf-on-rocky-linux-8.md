---
title: "Ensure All Packages are Updated"
category: "rocky-linux"
tags: ["rocky-linux", "installing", "slurm", "warewulf", "rocky"]
---

* If using a Vultr instance, make sure a VPC 1.0 network is created for both the Controller Node and Compute Nodes to live in (the same region must be used).
# Ensure All Packages are Updated
```
dnf upgrade -y
```
# Install munge on the Controller Node
* Enable the `devel` repo to then install the `munge-devel` package.
```
dnf config-manager --set-enabled devel
```
* Install the `munge` packages.
```
dnf install -y munge munge-devel
```
* Check that the `munge` user was created successfully.
```
getent passwd munge
```
* Create the `munge` key.
```
create-munge-key
```
* Start `munged` before the Slurm services.
```
systemctl enable munge
```
* Restart the `munge` service.
```
systemctl restart munge
systemctl status munge
```
# Set Permissions for `munge` on the Controller Node
* Set the permissions for `munge` on the Controller Node.
```
sudo chown -R munge: /etc/munge/ /var/log/munge/ /var/lib/munge/ /run/munge/
sudo chmod 0700 /etc/munge/ /var/log/munge/ /var/lib/munge/
sudo chmod 0755 /run/munge/
sudo chmod 0700 /etc/munge/munge.key
sudo chown -R munge: /etc/munge/munge.key
```
# Install Warewulf on the Controller Node
* Install the Warewulf RPM.
```
dnf install -y https://github.com/warewulf/warewulf/releases/download/v4.5.8/warewulf-4.5.8-1.el8.x86_64.rpm
```
* Configure `firewalld` to allow the appropriate services through.
```
systemctl restart firewalld
firewall-cmd --permanent --add-service=warewulf
firewall-cmd --permanent --add-service=dhcp
firewall-cmd --permanent --add-service=nfs
firewall-cmd --permanent --add-service=tftp
firewall-cmd --reload
```
* Apply the `warewulf.conf` File
```
tee /etc/warewulf/warewulf.conf <<EOF
WW_INTERNAL: 45
ipaddr: <IP_ADDRESS_OF_THE_CONTROLLER_NODE>
netmask: <SUBNET_MASK_OF_YOUR_NETWORK>
network: <NETWORK_ADDRESS_HERE>
warewulf:
  port: 9873
  secure: false
  update interval: 60
  autobuild overlays: true
  host overlay: true
  syslog: false
  datastore: /usr/share
  grubboot: false
dhcp:
  enabled: true
  template: default
  range start: <START_OF_YOUR_DHCP_IP_LIST>
  range end: <END_OF_YOUR_DHCP_IP_LIST>
  systemd name: dhcpd
tftp:
  enabled: true
  tftproot: /var/lib/tftpboot
  systemd name: tftp
  ipxe:
    "00:00": undionly.kpxe
    "00:07": ipxe-snponly-x86_64.efi
    "00:09": ipxe-snponly-x86_64.efi
    00:0B: arm64-efi/snponly.efi
nfs:
  enabled: true
  export paths:
  - path: /home
    export options: rw,sync
    mount options: defaults
    mount: true
  - path: /opt
    export options: ro,sync,no_root_squash
    mount options: defaults
    mount: false
  systemd name: nfs-server
container mounts:
- source: /etc/resolv.conf
  dest: /etc/resolv.conf
  readonly: true
paths:
  bindir: /usr/bin
  sysconfdir: /etc
  localstatedir: /var/lib
  ipxesource: /usr/share/ipxe
  srvdir: /var/lib
  firewallddir: /usr/lib/firewalld/services
  systemddir: /usr/lib/systemd/system
  wwoverlaydir: /var/lib/warewulf/overlays
  wwchrootdir: /var/lib/warewulf/chroots
  wwprovisiondir: /var/lib/warewulf/provision
  wwclientdir: /warewulf
EOF
```
* Enable the `warewulfd` service.
```
systemctl enable --now warewulfd
```
* Configure all services on the Controller Node.
```
wwctl configure --all
```
* Set the appropriate permissions for SELinux for `tftpboot`
```
restorecon -Rv /var/lib/tftpboot/
```
* Import the `rockylinux-9` Docker container.
```
wwctl container import docker://ghcr.io/warewulf/warewulf-rockylinux:9 rockylinux-9 --build
```
* Set the `rockylinux-9` container as the default.
```
wwctl profile set default --container rockylinux-9
```
* Configure the subnet mask and gateway and set that as the default Warewulf profile.
```
wwctl profile set -y default --netmask=255.255.240.0 --gateway=10.25.96.3
wwctl profile list
```
* Add the Compute Node to the Warewulf Node List.
```
wwctl node add warewulf-compute-node-1-osaka --ipaddr=10.25.96.4 --discoverable=true
wwctl node list -a warewulf-compute-node-1-osaka
```
* Rebuild the Warewulf Overlay.
```
wwctl overlay build
```
# Install munge on the Compute Node Image
* As `root`, exec into the Rocky Linux 9 container.
```
wwctl container exec rockylinux-9 /bin/bash
```
* Install `munge` in the container.
```
dnf install -y munge
```
* Enable the `munge` service.
```
systemctl enable munge
```
* Run `exit` and the container will be rebuilt.
* Create the `munge` key overlay.
```
wwctl overlay import --parents wwinit /etc/munge/munge.key
```
* Set permissions for the `munge directories` on the Compute Node.
```
wwctl overlay chown wwinit /etc/munge/munge.key $(id -u munge) $(id -g munge)
wwctl overlay chmod wwinit /etc/munge/munge.key 0400
wwctl overlay chown wwinit /etc/munge $(id -u munge) $(id -g munge)
wwctl overlay chmod wwinit /etc/munge 0700
```
* Rebuild the overlay.
```
wwctl overlay build
```
# Add a Compute Node to the Cluster
* Select the Upload ISO --> iPXE Custom Script option in Vultr for the node you want to set up as a Compute Node.
* Setup the node with the amount of CPU, RAM and disk space 
* Start the Compute Node and it will then boot and download the image from the Controller Node.
* Test `munge` from the Controller Node to make sure it works.
```
munge -n
munge -n | unmunge
munge -n | ssh root@<YOUR_COMPUTE_NODE> unmunge
remunge
```
# Time Synchronisation Between the Controller Node and the Compute Node
```
sudo timedatectl set-timezone <Region>/<City>
wwctl overlay import wwinit /etc/localtime
```
* Exec into the `rockylinux-9` container.
```
wwctl container exec rockylinux-9 /bin/bash
```
* Install the `chrony` package in the `rockylinux-9` container.
```
dnf install -y chrony
```
* `exit` to rebuild the container.
* Rebuild the overlay after that.
```
wwctl overlay build
```
* `exit` out and return to the Controller Node.
# Install slurm on the Controller Node and Compute Node Image
* Enable the `powertools` repo.
```
dnf config-manager --set-enabled powertools
```
* Create the `slurm` user and group.
```
export SLURMUSER=900
groupadd -g $SLURMUSER slurm
useradd -m -c "SLURM workload manager" -d /var/lib/slurm -u $SLURMUSER -g slurm -s /bin/bash slurm
getent passwd 900
getent group 900
```
* Sync the `slurm` user and group with the `rockylinux-9` container.
```
wwctl container syncuser --write rockylinux-9 --build
```
* Set up the database for Slurm.
```
dnf install -y mariadb-server mariadb-devel
systemctl enable --now mariadb
# Respond `Yes` to all of the questions, aside from the one which asks to reset the root password.
mysql_secure_installation
```
* Install further `slurm` prerequisites
```
dnf install -y pam-devel readline-devel perl
```
* Further set up the `rockylinux-9` container for use on the Compute Node.
```
wwctl container exec rockylinux-9 /bin/bash
dnf config-manager --set-enabled crb
dnf install -y dnf-plugins-core
dnf install -y gcc gcc-c++ tar make python3 openssl openssl-devel pam-devel numactl-devel hwloc hwloc-devel lua lua-devel readline-devel rrdtool-devel ncurses-devel libibmad libibumad libevent libevent-devel dbus-devel
```
* `exit` from the container.
* Install `slurm` from SchedMD on the Controller Node.
```
wget https://download.schedmd.com/slurm/slurm-23.11.5.tar.bz2
```
* Build the `slurm` RPMs.
```
rpmbuild -ta slurm-23.11.5.tar.bz2
```
* Change into the `rpmbuild/RPMS/x86_64` directory and install each package.
```
cd rpmbuild/RPMS/x86_64
sudo dnf localinstall -y slurm-23.11.5-1.el8.x86_64.rpm
sudo dnf localinstall -y slurm-slurmctld-23.11.5-1.el8.x86_64.rpm
sudo dnf localinstall -y slurm-perlapi-23.11.5-1.el8.x86_64.rpm
sudo dnf localinstall -y slurm-slurmdbd-23.11.5-1.el8.x86_64.rpm
sudo dnf localinstall -y slurm-pam_slurm-23.11.5-1.el8.x86_64.rpm
sudo dnf localinstall -y slurm-example-configs-23.11.5-1.el8.x86_64.rpm
```
* Install `slurm` on the Compute Node image.
```
wwctl container exec rockylinux-9 /bin/bash
wget https://download.schedmd.com/slurm/slurm-23.11.5.tar.bz2
dnf install -y mariadb-devel munge-devel pam-devel readline-devel perl
dnf install -y rpm-build
rpmbuild -ta slurm-23.11.5.tar.bz2
cd /root/rpmbuild/RPMS/x86_64/
dnf localinstall -y slurm-23.11.5-1.el9.x86_64.rpm slurm-slurmd-23.11.5-1.el9.x86_64.rpm
cd ~
rm -Rf ./rpmbuild
```
* Then `exit` to write the changes to the container.
# Create a Spool Directory for the Controller Node
* A Spool is a place where data is written by a process, to be used later on or possibly by a different process as well.
```
mkdir /var/spool/slurmctld
chown slurm:slurm /var/spool/slurmctld
```
# Configure Slurm on the Controller Node
```
cd /etc/slurm/
cp slurm.conf.example slurm.conf
cp slurmdbd.conf.example slurmdbd.conf
```
* Edit `slurm.conf` and change `ClusterName` and `SlurmctldHost` to the hostname of the Controller Node.
* Enable `firewalld` ports.
```
firewall-cmd --permanent --zone=internal --add-port=6817/tcp
firewall-cmd --permanent --zone=internal --add-port=6819/tcp
firewall-cmd --reload
```
* Start the `slurm` daemon.
```
systemctl enable --now slurmctld
```
# Import slurm.conf into the Compute Node Image
```
wwctl overlay import --parents wwinit /etc/slurm/slurm.conf
# Check that it was imported correctly.
cat /var/lib/warewulf/overlays/wwinit/rootfs/etc/slurm/slurm.conf
```
# Get Compute Node Hardware Info
* `ssh` into the Compute Node
```
ssh <COMPUTE_NODE_IP>
slurmd -C
```
# Add the slurmd -C Output to the slurm.conf File on the Controller Node
* Edit `NodeName` in `/etc/slurm/slurm.conf` and add something similar like the below example.
```
NodeName=warewulf-compute-node-1-osaka CPUs=4 Boards=1 SocketsPerBoard=1 CoresPerSocket=2 ThreadsPerCore=2 RealMemory=7941 State=UNKNOWN
```
* Update `slurm.conf` in Warewulf on the Controller Node.
```
wwctl overlay del wwinit /etc/slurm/slurm.conf
wwctl overlay import wwinit /etc/slurm/slurm.conf
wwctl overlay build
```
# Create the Cgroup slurm Config and Add to the Overlay
```
cd /etc/slurm/
cp cgroup.conf.example cgroup.conf
cat cgroup.conf
wwctl overlay import wwinit /etc/slurm/cgroup.conf
```
# Setup the Database for Slurm on the Controller Node
```
vim /etc/slurm/slurmdbd.conf
```
* Set the following parameters and then save the file.
```
AuthType=auth/munge
DbdAddr=<Address_of_Controller_Node>
DbdHost=localhost
SlurmUser=slurm
DebugLevel=verbose
LogFile=/var/log/slurm/slurmdbd.log
PidFile=/var/run/slurmdbd.pid
```
* Configure MariaDB
```
mysql -u root -p
grant all on slurm_acct_db.* TO 'slurm'@'localhost'
# Then exit out back to the MariDB main CLI (looks like "MariaDB [(none)]>")
create database slurm_acct_db;
ctrl + d
```
# Finally, set the Following in slurm.conf on the Controller Node
```
vim /etc/slurm/slurm.conf
```
```
AccountingStorageType=accounting_storage/slurmdbd
JobCompType=jobcomp/none
JobAcctGatherFrequency=30
JobAcctGatherType=jobacct_gather/none
SlurmctldDebug=info
SlurmctldLogFile=/var/log/slurmctld.log
SlurmdDebug=info
SlurmdLogFile=/var/log/slurmd.log
```
# Bring Up the Compute Node
* Check the status of the Slurm Nodes, run the following from the Controller Node.
```
sinfo
```
* Bring up the Compute Node.
```
scontrol update nodename=warewulf-compute-node-1-osaka state=idle
```
# Create a Simple Slurm Script
```
#!/bin/bash
#SBATCH --job-name test
hostname
uptime
```
# Create a Batch Job for the Script
```
sbatch test.slurm
```
# Set up the Firewall so All Compute Node Addresses are Added to the Trusted Zone
```
sudo firewall-cmd --zone=trusted --add-source=10.25.96.0/24
```
# srun Then Becomes Available
```
srun --pty bash
```