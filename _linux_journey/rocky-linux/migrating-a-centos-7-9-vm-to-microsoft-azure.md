---
title: "Migrating A Centos 7.9 Vm To Microsoft Azure"
category: "rocky-linux"
tags: ["rocky-linux", "migrating", "centos", "microsoft", "azure"]
---

* Switch to the `root` account or a user with `sudo` privileges:
```
sudo su -
```
* Overwite the CentOS-Base repo in `/etc/yum.repos.d/CentOS-Base.repo` with the below config from CentOS Vault:
```
cat << "EOF" | sudo tee /etc/yum.repos.d/CentOS-Base.repo
[base]
name=CentOS-$releasever - Base
baseurl=http://vault.centos.org/7.9.2009/os/$basearch/
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7

[updates]
name=CentOS-$releasever - Updates
baseurl=http://vault.centos.org/7.9.2009/updates/$basearch/
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7

[extras]
name=CentOS-$releasever - Extras
baseurl=http://vault.centos.org/7.9.2009/extras/$basearch/
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7

[centosplus]
name=CentOS-$releasever - Plus
baseurl=http://vault.centos.org/7.9.2009/centosplus/$basearch/
gpgcheck=1
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7
EOF
```
* Install `yum-utils` to get access to `sudo yum-config-manager`:
```
sudo yum install -y yum-utils
```
* Update all packages:
```
sudo yum -y update
```
* Rebooted:
```
sudo reboot
```
* Switch to the OpenLogic mirrors:
```
cat << "EOF" | sudo tee /etc/yum.repos.d/CentOS-Base.repo
[openlogic]
name=CentOS-$releasever - openlogic packages for $basearch
baseurl=http://olcentgbl.trafficmanager.net/openlogic/$releasever/openlogic/$basearch/
enabled=1
gpgcheck=0

[base]
name=CentOS-$releasever - Base
#mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=os&infra=$infra
baseurl=http://olcentgbl.trafficmanager.net/centos/$releasever/os/$basearch/
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7

#released updates
[updates]
name=CentOS-$releasever - Updates
#mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=updates&infra=$infra
baseurl=http://olcentgbl.trafficmanager.net/centos/$releasever/updates/$basearch/
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7

#additional packages that might be useful
[extras]
name=CentOS-$releasever - Extras
#mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=extras&infra=$infra
baseurl=http://olcentgbl.trafficmanager.net/centos/$releasever/extras/$basearch/
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7

#additional packages that extend functionality of existing packages
[centosplus]
name=CentOS-$releasever - Plus
#mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=centosplus&infra=$infra
baseurl=http://olcentgbl.trafficmanager.net/centos/$releasever/centosplus/$basearch/
gpgcheck=1
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7
EOF
```
* Add the following lines to the `/etc/sysconfig/network` file:
```
cat << "EOF" | sudo tee -a /etc/sysconfig/network
NETWORKING=yes
HOSTNAME=localhost.localdomain
EOF
```
* Clean all metadata:
```
sudo yum clean all
```
* Update all packages if needed:
```
sudo yum -y update
```
* Make a backup of the `/etc/sysconfig/network-scripts/ifcfg-eth0` file:
```
cp /etc/sysconfig/network-scripts/ifcfg-eth0 ~
```
* Edit the `ifcfg-eth0` like so:
```
sed -i 's/DEVICE="<DEVICE_HERE>"/DEVICE="eth0"/' /etc/sysconfig/network-scripts/ifcfg-eth0
sed -i 's/DEVICE="<VALUE>"/ONBOOT="yes"/' /etc/sysconfig/network-scripts/ifcfg-eth0
sed -i 's/BOOTPROTO="<VALUE>"/BOOTPROTO="dhcp"/' /etc/sysconfig/network-scripts/ifcfg-eth0
sed -i 's/TYPE="<VALUE>"/TYPE="Ethernet"/' /etc/sysconfig/network-scripts/ifcfg-eth0

sed -i 's/USERCTL="<VALUE>"/USERCTL="no"/' /etc/sysconfig/network-scripts/ifcfg-eth0

# or if it does not exist

cat << "EOF" | sudo tee -a /etc/sysconfig/network-scripts/ifcfg-eth0
USERCTL="no"
EOF

sed -i 's/PEERDNS="<VALUE>"/PEERDNS="yes"/' /etc/sysconfig/network-scripts/ifcfg-eth0

# or if it does not exist

cat << "EOF" | sudo tee -a /etc/sysconfig/network-scripts/ifcfg-eth0
PEERDNS="yes"
EOF

sed -i 's/IPV6INIT="<VALUE>"/IPV6INIT="no"/' /etc/sysconfig/network-scripts/ifcfg-eth0

sed -i 's/NM_CONTROLLED="<VALUE>"/NM_CONTROLLED="no"/' /etc/sysconfig/network-scripts/ifcfg-eth0

# or if it does not exist

cat << "EOF" | sudo tee -a /etc/sysconfig/network-scripts/ifcfg-eth0
NM_CONTROLLED="no"
EOF
```
* An example is below:
```
sudo sed -i 's/DEVICE="eth0"/DEVICE="eth0"/' /etc/sysconfig/network-scripts/ifcfg-eth0
sudo sed -i 's/ONBOOT="yes"/ONBOOT="yes"/' /etc/sysconfig/network-scripts/ifcfg-eth0
sudo sed -i 's/BOOTPROTO="none"/BOOTPROTO="dhcp"/' /etc/sysconfig/network-scripts/ifcfg-eth0
sed -i 's/TYPE="Ethernet"/TYPE="Ethernet"/' /etc/sysconfig/network-scripts/ifcfg-eth0

cat << "EOF" | sudo tee -a /etc/sysconfig/network-scripts/ifcfg-eth0
USERCTL="no"
EOF

cat << "EOF" | sudo tee -a /etc/sysconfig/network-scripts/ifcfg-eth0
PEERDNS="yes"
EOF

sudo sed -i 's/IPV6INIT="yes"/IPV6INIT="no"/' /etc/sysconfig/network-scripts/ifcfg-eth0

cat << "EOF" | sudo tee -a /etc/sysconfig/network-scripts/ifcfg-eth0
NM_CONTROLLED="no"
EOF
```
* Take a backup of your `grub` kernel cmdline parameters:
```
sudo cp /etc/default/grub ~
```
* Modify the `udev` rules to not generate static rules for the Ethernet interfaces:
```
sudo ln -s /dev/null /etc/udev/rules.d/75-persistent-net-generator.rules
```
* Add these `grub` cmdline parameters:
```
rootdelay=300 console=ttyS0 earlyprintk=ttyS0 net.ifnames=0
```
* Remove these parameters:
```
rhgb quiet crashkernel=auto
```
* An example is below:
```
sudo sed -i 's/GRUB_CMDLINE_LINUX="crashkernel=auto rd.lvm.lv=centos\/root rd.lvm.lv=centos\/swap rhgb quiet"/GRUB_CMDLINE_LINUX="rd.lvm.lv=centos\/root rd.lvm.lv=centos\/swap rootdelay=300 console=ttyS0 earlyprintk=ttyS0 net.ifnames=0"/' /etc/default/grub
```
* Rebuild the `grub` configuration:
```
sudo grub2-mkconfig -o /boot/grub2/grub.cfg
```
* Add the `Hyper-V` drivers to the `initramfs`:
```
cat << "EOF" | sudo tee -a /etc/dracut.conf
add_drivers+=" hv_vmbus hv_netvsc hv_storvsc "
EOF
```
* Rebuild the `initramfs`:
```
sudo dracut -f -v
```
* Install the Azure Linux agent and dependencies for the Azure VM extensions:
```
sudo yum install -y python-pyasn1 WALinuxAgent
```
* Enable the `waagent` service:
```
sudo systemctl enable waagent
```
* Install `cloud-init` and its related packages for provisioning:
```
sudo yum install -y cloud-init cloud-utils-growpart gdisk hyperv-daemons
```
* Configure `waagent` for use with `cloud-init`:
```
sudo sed -i 's/Provisioning.Agent=auto/Provisioning.Agent=auto/g' /etc/waagent.conf

sudo sed -i 's/ResourceDisk.Format=y/ResourceDisk.Format=n/g' /etc/waagent.conf

sudo sed -i 's/ResourceDisk.EnableSwap=y/ResourceDisk.EnableSwap=n/g' /etc/waagent.conf

sudo sed -i '/ - mounts/d' /etc/cloud/cloud.cfg

sudo sed -i '/ - disk_setup/d' /etc/cloud/cloud.cfg

sudo sed -i '/cloud_init_modules/a\\ - mounts' /etc/cloud/cloud.cfg

sudo sed -i '/cloud_init_modules/a\\ - disk_setup' /etc/cloud/cloud.cfg

sudo cat > /etc/cloud/cloud.cfg.d/91-azure_datasource.cfg <<EOF
datasource_list: [ Azure ]
datasource:
    Azure:
        apply_network_config: False
EOF

if [[ -f /mnt/swapfile ]]; then
echo Removing swapfile - RHEL uses a swapfile by default
swapoff /mnt/swapfile
rm /mnt/swapfile -f
fi

cat >> /etc/cloud/cloud.cfg.d/05_logging.cfg <<EOF
output: {all: '| tee -a /var/log/cloud-init-output.log'}
EOF
```
* Deny the Linux Agent from creating swap space on the OS disk:
```
sudo sed -i 's/ResourceDisk.Format=y/ResourceDisk.Format=n/g' /etc/waagent.conf

sudo sed -i 's/ResourceDisk.EnableSwap=y/ResourceDisk.EnableSwap=n/g' /etc/waagent.conf
```
* De-provision the VM and prepare for provisioning on Azure:
```
sudo rm -f /var/log/waagent.log
sudo cloud-init clean
sudo waagent -force -deprovision+user
sudo rm -f ~/.bash_history
sudo export HISTSIZE=0
```
* Shutdown the VM:
```
sudo poweroff
```
* Convert the `qcow2` file to a `raw` format:
```
sudo qemu-img convert -f qcow2 -O raw <INPUT>.qcow2 <OUTPUT>.raw
```
* Set the MB variable:
```
MB=$((1024 * 1024))
```
* Verify the size of the image works with `1 MB`:
```
size=$(qemu-img info -f raw --output json "<INPUT>.raw" | gawk 'match($0, /"virtual-size": ([0-9]+),/, val) {print val[1]}')

rounded_size=$((($size/$MB + 1)*$MB))
```
# Running `rounded_size` above currently outputs token errors
* Resize the image if needed:
```
qemu-img resize <OUTPUT>.raw $rounded_size
```
# Cannot do the above, due to the `rounded_size` errors
* Convert the image:
```
qemu-img convert -f raw -o subformat=fixed,force_size -O vpc <INPUT>.raw <OUTPUT>.vhd
```
* An example of the steps is listed below:
```
sudo qemu-img convert -f raw -o subformat=fixed,force_size -O vpc centos79.raw centos79.vhd
```
* Export the `vhd` image to a safe location.
* Setup AzCopy:
```
https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10?tabs=dnf#download-and-install-azcopy
```
* For MacOS ARM, download the binary via this link:
```
https://aka.ms/downloadazcopy-v10-mac-arm64
```
* Install the Azure CLI:
```
https://learn.microsoft.com/en-us/cli/azure/install-azure-cli
```
* Example with MacOS ARM:
```
brew update && brew install azure-cli
```
* Run `az login`
* Sign into the Azure CLI:
```
https://learn.microsoft.com/en-us/cli/azure/get-started-with-azure-cli
```
* Get the size of the VHD file:
```
wc -c <INPUT>.vhd
```
* Run this via Azure CLI to create an empty managed disk:
```
az disk create -n <yourdiskname> -g <yourresourcegroupname> -l <yourregion> --os-type Linux --for-upload --upload-size-bytes 34359738880 --sku standard_lrs --hyper-v-generation <generation_here>
```
* An example is below:
```
az disk create -n howardtesting -g howard-test -l JapanEast --os-type Linux --for-upload --upload-size-bytes 10737418752 --sku standard_lrs --hyper-v-generation V2
```
* Create a writable SAS:
```
az disk grant-access -n <yourdiskname> -g <yourresourcegroupname> --access-level Write --duration-in-seconds 86400
```
* An example is below:
```
az disk grant-access -n test-disk -g test-group --access-level Write --duration-in-seconds 86400
```
* Upload the VHD image using `AzCopy`:
```
AzCopy copy "./<IMAGE>.vhd" "SAS-URL" --blob-type PageBlob
```
* An example is below:
```
~/AzCopy copy "./centos79-test.vhd" "https://md-impexp-k15zxkm5hzbp.z29.blob.storage.azure.net/gphqnjvbqmp3/abcd?sv=2018-03-28&sr=b&si=ab0543e6-115d-41a2-9544-86c2421b842e&sig=mXka7n81nD35KfmLvlQPfjZgTRjjLnpqBh0X5RoiLFM%3D" --blob-type PageBlob
```
* Revoke the SAS when no more data is needed to be written to the disk:
```
az disk revoke-access -n howardtesting -g howard-test
```
* Find the `storage-account` ID:
```
az disk show --name <Disk_Name> --resource-group <Resource_Group>
```
* Example is here:
```
az disk show -n howardtesting --resource-group howard-test
```
* Create a VM and attach a disk to that:
```
az vm create --name $virtualMachineName --resource-group $resourceGroupName --attach-os-disk $managedDiskId --os-type $osType
```
* An example can be found below:
```
az vm create --name howardtesting2 --resource-group howard-test --attach-os-disk "/subscriptions/5741f913-5ca2-45a1-8faa-dca48613c619/resourceGroups/howard-test/providers/Microsoft.Compute/disks/howardtesting" --os-type linux
```
* Clean up everything include the VM and resource groups using the following command:
```
az group delete --name myResourceGroupName
```