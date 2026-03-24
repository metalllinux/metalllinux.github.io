---
title: "Testing - Rocky Linux 9.5 Pacemaker Setup"
category: "rocky-linux"
tags: ["rocky-linux", "setup", "clustered", "lvm", "rocky"]
---

### Testing - Rocky Linux 9.5 Pacemaker Setup

* I set up two Rocky Linux 9.5 VMs:
```
rocky-linux-95-1
rocky-linux-95-2
```
* `rocky-linux-95-1` will be my ISCSI target. I attached a 20GB disk to this VM.
* `rocky-linux-95-2` is my cluster nodes.

* **Ran the following steps on all nodes:**
* Switched to the `root` user:
```
sudo su -
```
* Set FQDN hostnames on all nodes:
```
hostnamectl set-hostname rocky-linux-95-1.lvm.test
hostnamectl set-hostname rocky-linux-95-2.lvm.test
```
* Updated the `/etc/hosts` file to make all nodes aware of each other:
```
cat << "EOF" | sudo tee /etc/hosts
192.168.1.48 rocky-linux-95-1.lvm.test rocky-linux-95-1
192.168.1.49 rocky-linux-95-2.lvm.test rocky-linux-95-2
EOF
```
* Enabled the High Availability repository:
```
dnf config-manager --set-enabled highavailability
```
* Installed these packages:
```
dnf install -y pacemaker
dnf install -y pcs
```
* Started the `pcsd` service:
```
systemctl enable --now pcsd
```
* Confirmed the `pcsd` service was running on all nodes:
```
systemctl status pcsd
```
* Allowed `high-availability` services through `firewalld`:
```
firewall-cmd --add-service=high-availability --permanent 
firewall-cmd --reload 
```
* Set the cluster admin password on all nodes:
```
passwd hacluster 
```

* **Ran the following steps on the rocky-linux-95-2 node:**

* Configured the basic cluster settings:
```
pcs host auth rocky-linux-95-1.lvm.test rocky-linux-95-2.lvm.test -u hacluster
```
* Configured the cluster:
```
pcs cluster setup ha_cluster rocky-linux-95-1.lvm.test rocky-linux-95-2.lvm.test
```
* Started cluster services:
```
pcs cluster start --all
```
* Configured auto-start:
```
pcs cluster enable --all
```
* The status looked good from the corosync side:
```
pcs status corosync

Membership information
----------------------
    Nodeid      Votes Name
         1          1 rocky-linux-95-1.lvm.test
         2          1 rocky-linux-95-2.lvm.test (local)
```

### Testing - iSCSI Setup

* **All steps are ran on the `rocky-linux-95-1` node**
* Switched to the `root` account:
```
sudo su -
```
* Install the `targetcli` program:
```
dnf install -y targetcli 
```
* Started and enabled the `target` service:
```
systemctl enable --now target
```
* Ran `targetcli`:
```
targetcli
```
* Changed directory into the `fileio` directory:
```
cd backstores/ramdisk
```
* Created a 10GB backstore file:
```
create name=storage size=10G
```
* Changed into the `/iscsi` directory:
```
cd /iscsi
```
* Created the target:
```
create iqn.2025-03.test.lvm:rocky-linux-95-1
```
* Changed into the `iqn.2025-03.test.lvm:rocky-linux-95-1/tpg1/portals` directory:
```
cd iqn.2025-03.test.lvm:rocky-linux-95-1/tpg1/portals
```
* Created a portal to listen for incoming connections (if a message regarding the NetworkPortal already existing appears, this has already then been configured):
```
create 0.0.0.0 3260
```
* Switched to the `acls` directory:
```
cd ../acls
```
* Added `rocky-linux-95-2` and `rocky-linux-95-3` as initiators:
```
create iqn.2025-03.test.lvm.initiator:rocky-linux-95-2
```
* Switched to the `luns` directory:
```
cd ../luns
```
* Mapped the backstore to the iscsi target:
```
create /backstores/ramdisk/storage
```
* Changed back to the root directory:
```
cd ../../../..
```
* Saved the configuration:
```
saveconfig
```
* Then exited the session:
```
exit
```
* Allowed the `iscsi-target` traffic through `firewalld`:
```
firewall-cmd --add-service=iscsi-target --permanent
firewall-cmd --reload
```

* **These steps were ran on rocky-linux-95-2**:
* Installed the initiator utilities:
```
dnf install -y iscsi-initiator-utils 
```
* Created the `initiatorname.iscsi` file:
```
cat << "EOF" | sudo tee /etc/iscsi/initiatorname.iscsi
InitiatorName=iqn.2025-03.test.lvm.initiator:rocky-linux-95-2
EOF
```
* Discovered the node:
```
iscsiadm -m discovery -t sendtargets -p 192.168.1.48
```
* Logged into the node successfully:
```
iscsiadm -m node --targetname iqn.2025-03.test.lvm:rocky-linux-95-1 --portal 192.168.1.48:3260 --login
```
* Configured to log into the target on boot:
```
iscsiadm -m node --targetname iqn.2025-03.test.lvm:rocky-linux-95-1 --portal 192.168.1.48:3260 --op update --name node.startup --value automatic
```
* Restarted the `iscsid` service:
```
sudo systemctl restart iscsid
```
* Verified the iSCSI disk on `rocky-linux-95-1` was found:
```
lsblk
NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
sda           8:0    0    10G  0 disk
```

### Testing - LVM Setup

* **Steps performed on all nodes**:
* Changed the LVM System ID to `uname`:
```
sed -i 's/# system_id_source = "none"/system_id_source = "uname"/' /etc/lvm/lvm.conf 
```

* **Steps performed on rocky-linux-95-2**:
* Set the label as `gpt`:
```
parted --script /dev/sda "mklabel gpt" 
```
* Assigned 100% of the space to the primary partition:
```
parted --script /dev/sda "mkpart primary 0% 100%" 
```
* Enabled LVM:
```
parted --script /dev/sda "set 1 lvm on" 
```
* Created a physical volume:
```
pvcreate /dev/sda1 
```
* Created a volume group:
```
vgcreate --setautoactivation n vg_ha /dev/sda1 
```
* Confirmed the hostname and volume group match:
```
vgs -o+systemid

  VG    #PV #LV #SN Attr   VSize    VFree   System ID                
  rl      1   3   0 wz--n- <199.00g      0                           
  vg_ha   1   0   0 wz--n-  <10.00g <10.00g rocky-linux-95-2.lvm.test
```
* Created the logical volume:
```
lvcreate -l 100%FREE -n lv_ha vg_ha 
```
* Formatted the volume as ext4:
```
mkfs.ext4 /dev/vg_ha/lv_ha 
```
* Set the shared storage as a cluster resource:
```
pcs resource create lvm_ha ocf:heartbeat:LVM-activate vgname=vg_ha vg_access_mode=system_id group ha_group --future 
```
* Confirmed the status:
```
pcs status
```
* The shared LVM was then available:
```
lsblk
NAME            MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
sda               8:0    0    10G  0 disk 
└─sda1            8:1    0    10G  0 part 
  └─vg_ha-lv_ha 253:3    0    10G  0 lvm
```