---
title: "Updating the CentOS 8.5 repositories"
category: "rocky-linux"
tags: ["rocky-linux", "centos", "rocky", "linux", "migration"]
---

* Run the below commands as either `root` or a user with `sudo` privileges:
## Updating the CentOS 8.5 repositories
* Open a new script file in `vim` or your text editor of choice called `centos8_vault_repository_configuration.sh`.
* Add the below configuration to the file to update all repositories to point towards the CentOS Vault [credit goes to Alex Baranowski for the script](https://gist.github.com/AlexBaranowski/becfe334979e0d1404f94a0d0b0e0d73):
```
#!/usr/bin/env bash
cat > /etc/yum.repos.d/CentOS-Linux-AppStream.repo << EOF
# CentOS-Linux-AppStream.repo
#
# The mirrorlist system uses the connecting IP address of the client and the
# update status of each mirror to pick current mirrors that are geographically
# close to the client.  You should use this for CentOS updates unless you are
# manually picking other mirrors.
#
# If the mirrorlist does not work for you, you can try the commented out
# baseurl line instead.
[appstream]
name=CentOS Linux \$releasever - AppStream
baseurl=http://vault.centos.org/\$contentdir/\$releasever/AppStream/\$basearch/os/
gpgcheck=1
enabled=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-centosofficial
EOF
cat > /etc/yum.repos.d/CentOS-Linux-BaseOS.repo << EOF
# CentOS-Linux-BaseOS.repo
#
# The mirrorlist system uses the connecting IP address of the client and the
# update status of each mirror to pick current mirrors that are geographically
# close to the client.  You should use this for CentOS updates unless you are
# manually picking other mirrors.
#
# If the mirrorlist does not work for you, you can try the commented out
# baseurl line instead.
[baseos]
name=CentOS Linux \$releasever - BaseOS
baseurl=http://vault.centos.org/\$contentdir/\$releasever/BaseOS/\$basearch/os/
gpgcheck=1
enabled=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-centosofficial
EOF
cat > /etc/yum.repos.d/CentOS-Linux-ContinuousRelease.repo << EOF
# CentOS-Linux-ContinuousRelease.repo
#
# The mirrorlist system uses the connecting IP address of the client and the
# update status of each mirror to pick current mirrors that are geographically
# close to the client.  You should use this for CentOS updates unless you are
# manually picking other mirrors.
#
# If the mirrorlist does not work for you, you can try the commented out
# baseurl line instead.
#
# The Continuous Release (CR) repository contains packages for the next minor
# release of CentOS Linux.  This repository only has content in the time period
# between an upstream release and the official CentOS Linux release.  These
# packages have not been fully tested yet and should be considered beta
# quality.  They are made available for people willing to test and provide
# feedback for the next release.
[cr]
name=CentOS Linux \$releasever - ContinuousRelease
baseurl=http://vault.centos.org/\$contentdir/\$releasever/cr/\$basearch/os/
gpgcheck=1
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-centosofficial
EOF
cat > /etc/yum.repos.d/CentOS-Linux-Debuginfo.repo << EOF
# CentOS-Linux-Debuginfo.repo
#
# All debug packages are merged into a single repo, split by basearch, and are
# not signed.
[debuginfo]
name=CentOS Linux \$releasever - Debuginfo
baseurl=http://debuginfo.centos.org/\$releasever/\$basearch/
gpgcheck=1
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-centosofficial
EOF
cat > /etc/yum.repos.d/CentOS-Linux-Devel.repo << EOF
# CentOS-Linux-Devel.repo
#
# The mirrorlist system uses the connecting IP address of the client and the
# update status of each mirror to pick current mirrors that are geographically
# close to the client.  You should use this for CentOS updates unless you are
# manually picking other mirrors.
#
# If the mirrorlist does not work for you, you can try the commented out
# baseurl line instead.
[devel]
name=CentOS Linux \$releasever - Devel WARNING! FOR BUILDROOT USE ONLY!
baseurl=http://vault.centos.org/\$contentdir/\$releasever/Devel/\$basearch/os/
gpgcheck=1
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-centosofficial
EOF
cat > /etc/yum.repos.d/CentOS-Linux-Extras.repo << EOF
# CentOS-Linux-Extras.repo
#
# The mirrorlist system uses the connecting IP address of the client and the
# update status of each mirror to pick current mirrors that are geographically
# close to the client.  You should use this for CentOS updates unless you are
# manually picking other mirrors.
#
# If the mirrorlist does not work for you, you can try the commented out
# baseurl line instead.
[extras]
name=CentOS Linux \$releasever - Extras
baseurl=http://vault.centos.org/\$contentdir/\$releasever/extras/\$basearch/os/
gpgcheck=1
enabled=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-centosofficial
EOF
cat > /etc/yum.repos.d/CentOS-Linux-FastTrack.repo << EOF
# CentOS-Linux-FastTrack.repo
#
# The mirrorlist system uses the connecting IP address of the client and the
# update status of each mirror to pick current mirrors that are geographically
# close to the client.  You should use this for CentOS updates unless you are
# manually picking other mirrors.
#
# If the mirrorlist does not work for you, you can try the commented out
# baseurl line instead.
[fasttrack]
name=CentOS Linux \$releasever - FastTrack
baseurl=http://vault.centos.org/\$contentdir/\$releasever/fasttrack/\$basearch/os/
gpgcheck=1
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-centosofficial
EOF
cat > /etc/yum.repos.d/CentOS-Linux-HighAvailability.repo << EOF
# CentOS-Linux-HighAvailability.repo
#
# The mirrorlist system uses the connecting IP address of the client and the
# update status of each mirror to pick current mirrors that are geographically
# close to the client.  You should use this for CentOS updates unless you are
# manually picking other mirrors.
#
# If the mirrorlist does not work for you, you can try the commented out
# baseurl line instead.
[ha]
name=CentOS Linux \$releasever - HighAvailability
baseurl=http://vault.centos.org/\$contentdir/\$releasever/HighAvailability/\$basearch/os/
gpgcheck=1
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-centosofficial
EOF
cat > /etc/yum.repos.d/CentOS-Linux-Media.repo << EOF
# CentOS-Linux-Media.repo
#
# You can use this repo to install items directly off the installation media.
# Verify your mount point matches one of the below file:// paths.
[media-baseos]
name=CentOS Linux \$releasever - Media - BaseOS
baseurl=file:///media/CentOS/BaseOS
        file:///media/cdrom/BaseOS
        file:///media/cdrecorder/BaseOS
gpgcheck=1
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-centosofficial
[media-appstream]
name=CentOS Linux \$releasever - Media - AppStream
baseurl=file:///media/CentOS/AppStream
        file:///media/cdrom/AppStream
        file:///media/cdrecorder/AppStream
gpgcheck=1
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-centosofficial
EOF
cat > /etc/yum.repos.d/CentOS-Linux-Plus.repo << EOF
# CentOS-Linux-Plus.repo
#
# The mirrorlist system uses the connecting IP address of the client and the
# update status of each mirror to pick current mirrors that are geographically
# close to the client.  You should use this for CentOS updates unless you are
# manually picking other mirrors.
#
# If the mirrorlist does not work for you, you can try the commented out
# baseurl line instead.
[plus]
name=CentOS Linux \$releasever - Plus
baseurl=http://vault.centos.org/\$contentdir/\$releasever/centosplus/\$basearch/os/
gpgcheck=1
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-centosofficial
EOF
cat > /etc/yum.repos.d/CentOS-Linux-PowerTools.repo << EOF
# CentOS-Linux-PowerTools.repo
#
# The mirrorlist system uses the connecting IP address of the client and the
# update status of each mirror to pick current mirrors that are geographically
# close to the client.  You should use this for CentOS updates unless you are
# manually picking other mirrors.
#
# If the mirrorlist does not work for you, you can try the commented out
# baseurl line instead.
[powertools]
name=CentOS Linux \$releasever - PowerTools
baseurl=http://vault.centos.org/\$contentdir/\$releasever/PowerTools/\$basearch/os/
gpgcheck=1
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-centosofficial
EOF
cat > /etc/yum.repos.d/CentOS-Linux-Sources.repo << EOF
# CentOS-Linux-Sources.repo
[baseos-source]
name=CentOS Linux \$releasever - BaseOS - Source
baseurl=http://vault.centos.org/\$contentdir/\$releasever/BaseOS/Source/
gpgcheck=1
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-centosofficial
[appstream-source]
name=CentOS Linux \$releasever - AppStream - Source
baseurl=http://vault.centos.org/\$contentdir/\$releasever/AppStream/Source/
gpgcheck=1
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-centosofficial
[powertools-source]
name=CentOS Linux \$releasever - PowerTools - Source
baseurl=http://vault.centos.org/\$contentdir/\$releasever/PowerTools/Source/
gpgcheck=1
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-centosofficial
[extras-source]
name=CentOS Linux \$releasever - Extras - Source
baseurl=http://vault.centos.org/\$contentdir/\$releasever/extras/Source/
gpgcheck=1
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-centosofficial
[plus-source]
name=CentOS Linux \$releasever - Plus - Source
baseurl=http://vault.centos.org/\$contentdir/\$releasever/centosplus/Source/
gpgcheck=1
enabled=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-centosofficial
EOF
```
* Run the script and it will update all of the repositories for you:
```
sh ~/centos8_vault_repository_configuration.sh
```
* Upgrade all packages:
```
yum upgrade -y
```
* Reboot:
```
reboot
```
## LEAPP installation
* Add the ELevate repository:
```
yum install -y http://repo.almalinux.org/elevate/elevate-release-latest-el$(rpm --eval %rhel).noarch.rpm
```
* Install the LEAPP packages:
```
yum install -y leapp-upgrade leapp-data-rocky
```
* Run pre-upgrade checks:
```
leapp preupgrade
```
* Check the `/var/log/leapp/` directory at the end for all of the upgrade issues. In particular check `leapp-report.txt` for all of the blocker issues and `leapp-preupgrade.log` for a full log and debug output of the upgrade process.
* The key piece of text you want to look for towards the bottom of the summary is `Upgrade has been inhibited due to the following problems`. The items listed underneath will prevent the upgrade from starting, even if you run the `leapp upgrade` command.
* For example, these were the blockers that the author came across and how they solved them:
## Example Blockers
### Detected VDO devices not managed by LVM
```
Risk Factor: high (inhibitor)
Title: Detected VDO devices not managed by LVM
Summary: VDO devices 'sda, sda1, sda2, sda3, sdb, sdb1, sdb2, sdb3, sdb4' require migration to LVM management.After performing the upgrade VDO devices can only be managed via LVM. Any VDO device not currently managed by LVM must be converted to LVM management before upgrading. The data on any VDO device not converted to LVM management will be inaccessible after upgrading.
Related links:
    - Importing existing VDO volumes to LVM: https://red.ht/import-existing-vdo-volumes-to-lvm
Remediation: [hint] Consult the VDO to LVM conversion process documentation for how to perform the conversion.
```
#### Solution
* Check the volume groups available with `vgdisplay`:
```
vgdisplay
VG Name               cl
```
* Confirm the logical volumes as well with `lvdisplay`:
```
lvdisplay
LV Path                /dev/cl/swap
LV Path                /dev/cl/home
LV Path                /dev/cl/root
```
* Output of `lsblk`:
```
NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
sda           8:0    0 232.9G  0 disk 
├─sda1        8:1    0   600M  0 part /boot/efi
├─sda2        8:2    0     1G  0 part /boot
└─sda3        8:3    0 231.3G  0 part 
  ├─cl-root 253:0    0    70G  0 lvm  /
  ├─cl-swap 253:1    0   7.8G  0 lvm  [SWAP]
  └─cl-home 253:2    0 153.5G  0 lvm  /home
```
* This inhibitor can be safely ignored, since all required partitions are already on an LVM.
* Remove the `vdo` package with:
```
yum remove -y vdo
```
* Then tell `leapp` to skip the `vdo` check:
```
leapp answer --section check_vdo.confirm=True
```
* Run the `leapp preupgrade` command again and observe that the `inhibitor` is now gone.
### Firewalld Configuration AllowZoneDrifting Is Unsupported
```
Risk Factor: high (inhibitor)
Title: Firewalld Configuration AllowZoneDrifting Is Unsupported
Summary: Firewalld has enabled configuration option "AllowZoneDrifiting" which has been removed in RHEL-9. New behavior is as if "AllowZoneDrifiting" was set to "no".
Related links:
    - Changes in firewalld related to Zone Drifting: https://access.redhat.com/articles/4855631
    - Leapp Preupgrade check fails with error - "Inhibitor: Firewalld Configuration AllowZoneDrifting Is Unsupported".: https://access.redhat.com/solutions/6969130
Remediation: [hint] Set AllowZoneDrifting=no in /etc/firewalld/firewalld.conf
[command] sed -i s/^AllowZoneDrifting=.*/AllowZoneDrifting=no/ /etc/firewalld/firewalld.conf
```
#### Solution
* Run this `sed` command to disable `AllowZoneDrifting`:
```
sed -i s/^AllowZoneDrifting=.*/AllowZoneDrifting=no/ /etc/firewalld/firewalld.conf
```
### Possible problems with remote login using root account
```
Risk Factor: high (inhibitor)
Title: Possible problems with remote login using root account
Summary: OpenSSH configuration file will get updated to RHEL9 version, no longer allowing root login with password. It is a good practice to use non-root administrative user and non-password authentications, but if you rely on the remote root login, this change can lock you out of this system.
Related links:
    - Why Leapp Preupgrade for RHEL 8 to 9 getting "Possible problems with remote login using root account" ?: https://access.redhat.com/solutions/7003083
Remediation: [hint] If you depend on remote root logins using passwords, consider setting up a different user for remote administration or adding a comment into the sshd_config next to the "PermitRootLogin yes" directive to prevent rpm replacing it during the upgrade.
```
#### Solution
* Comment out the `PermitRootLogin yes` line to prevent the RPM from changing it when the upgrade is on the way:
```
sed -i 's/PermitRootLogin yes/#PermitRootLogin yes/' /etc/ssh/sshd_config
```
### Packages from unknown repositories may not be installed
```
Risk Factor: high 
Title: Packages from unknown repositories may not be installed
Summary: 1 packages may not be installed or upgraded due to repositories unknown to leapp:
- python3-systemd (repoid: rocky8-baseos)
Remediation: [hint] In case the listed repositories are mirrors of official repositories for RHEL (provided by Red Hat on CDN) and their repositories IDs has been customized, you can change the configuration to use the official IDs instead of fixing the problem. You can also review the projected DNF upgrade transaction result in the logs to see what is going to happen, as this does not necessarily mean that the listed packages will not be upgraded. You can also install any missing packages after the in-place upgrade manually.
```
#### Solution
* In the above example, only one package `python3-systemd` from the `rocky8-baseos` base repository is highlighted. This can be safely reinstalled after the upgrade process.
### Detected custom leapp actors or files.
```
Risk Factor: high 
Title: Detected custom leapp actors or files.
Summary: We have detected installed custom actors or files on the system. These can be provided e.g. by third party vendors, Red Hat consultants, or can be created by users to customize the upgrade (e.g. to migrate custom applications). This is allowed and appreciated. However Red Hat is not responsible for any issues caused by these custom leapp actors. Note that upgrade tooling is under agile development which could require more frequent update of custom actors.
The list of custom leapp actors and files:
    - /usr/share/leapp-repository/repositories/system_upgrade/common/files/rpm-gpg/9/RPM-GPG-KEY-Rocky-9
Related links:
    - Customizing your Red Hat Enterprise Linux in-place upgrade: https://red.ht/customize-rhel-upgrade
Remediation: [hint] In case of any issues connected to custom or third party actors, contact vendor of such actors. Also we suggest to ensure the installed custom leapp actors are up to date, compatible with the installed packages.
```
#### Solution
* In the example above, this can also be ignored as well, as it is one of the `leapp` repositories.
### Leapp detected loaded kernel drivers which are no longer maintained in RHEL 9.
```
Risk Factor: high 
Title: Leapp detected loaded kernel drivers which are no longer maintained in RHEL 9.
Summary: The following RHEL 8 device drivers are no longer maintained RHEL 9:
     - ip_set
```
#### Solution
* Unload the driver:
```
modprobe -r ip_set
```
### SElinux will be set to permissive mode
```
Risk Factor: low 
Title: SElinux will be set to permissive mode
Summary: SElinux will be set to permissive mode. Current mode: enforcing. This action is required by the upgrade process to make sure the upgraded system can boot without beinig blocked by SElinux rules.
Remediation: [hint] Make sure there are no SElinux related warnings after the upgrade and enable SElinux manually afterwards. Notice: You can ignore the "/root/tmp_leapp_py3" SElinux warnings.
```
#### Solution
* No need to take any action. Ensure that after the upgrade, `SELinux` is running (if you set `SELinux` as `enforcing`) with:
```
sestatus
```
### Some enabled RPM repositories are unknown to Leapp
```
Risk Factor: low 
Title: Some enabled RPM repositories are unknown to Leapp
Summary: The following repositories with Red Hat-signed packages are unknown to Leapp:
- appstream
- baseos
- elevate
And the following packages installed from those repositories may not be upgraded:
- libsss_certmap
- samba-common-libs
- nss
- kernel-modules
- nss-softokn
- systemd-libs
- libwbclient
- sssd-ldap
- libsss_idmap
- python3-sssdconfig
- kernel-tools-libs
- python3-requests
- sssd-common
- leapp-upgrade-el8toel9-deps
- sssd-client
- sssd-common-pac
- nss-sysinit
- sssd-kcm
- sssd-ipa
- python3-urllib3
- libsss_nss_idmap
- samba-client-libs
- libsss_sudo
- systemd-pam
- kexec-tools
- leapp-data-rocky
- libgcc
- selinux-policy-targeted
- systemd-container
- libstdc++
- sssd-ad
- python3-pysocks
- sssd-nfs-idmap
- leapp
- python36
- bpftool
- python3-perf
- libipa_hbac
- python3-idna
- libgomp
- openssl-libs
- kernel-tools
- openssl
- samba-common
- sssd-proxy
- systemd
- sssd
- leapp-upgrade-el8toel9
- nss-util
- libsss_autofs
- sssd-krb5
- selinux-policy
- python3-chardet
- libsmbclient
- nss-softokn-freebl
- kernel
- leapp-deps
- sssd-krb5-common
- kernel-core
- python3-leapp
- python3-pip
- systemd-udev
- binutils
Remediation: [hint] You can file a request to add this repository to the scope of in-place upgrades by filing a support ticket
```
#### Solution
* It is okay to disregard the above warning.
### DNF execution failed with non zero exit code.
```
Risk Factor: high (error)
Title: DNF execution failed with non zero exit code.
Summary: {"STDOUT": "Last metadata expiration check: 0:01:04 ago on Fri Apr 11 13:27:41 2025.\n", "STDERR": "warning: Found bdb_ro Packages database while attempting sqlite backend: using bdb_ro backend.\nNo matches found for the following disable plugin patterns: subscription-manager\nRepository baseos is listed more than once in the configuration\nRepository baseos-source is listed more than once in the configuration\nRepository appstream is listed more than once in the configuration\nRepository appstream-source is listed more than once in the configuration\nRepository devel is listed more than once in the configuration\nRepository extras is listed more than once in the configuration\nRepository extras-source is listed more than once in the configuration\nRepository plus is listed more than once in the configuration\nRepository plus-source is listed more than once in the configuration\nwarning: Found bdb_ro Packages database while attempting sqlite backend: using bdb_ro backend.\nWarning: Package marked by Leapp to upgrade not found in repositories metadata: gpg-pubkey leapp leapp-upgrade-el8toel9 python3-leapp\nTransaction check: \n\n Problem: package dnf-plugins-core-4.3.0-16.el9.noarch from rocky9-baseos requires python3-dnf-plugins-core = 4.3.0-16.el9, but none of the providers can be installed\n  - package leapp-repository-deps-el9-5.0.9-100.202411180921Z.f50e3474.main.el9.noarch from @commandline requires dnf-command(config-manager), but none of the providers can be installed\n  - package python3-dnf-plugins-core-4.3.0-16.el9.noarch from rocky9-baseos requires python3-systemd, but none of the providers can be installed\n  - dnf-plugins-core-4.0.21-3.el8.noarch from @System  does not belong to a distupgrade repository\n  - conflicting requests\n", "hint": "If there was a problem reaching remote content (see stderr output) and proxy is configured in the YUM/DNF configuration file, the proxy configuration is likely causing this error. Make sure the proxy is properly configured in /etc/dnf/dnf.conf. It's also possible the proxy settings in the DNF configuration file are incompatible with the target system. A compatible configuration can be placed in /etc/leapp/files/dnf.conf which, if present, it will be used during some parts of the upgrade instead of original /etc/dnf/dnf.conf. In such case the configuration will also be applied to the target system. Note that /etc/dnf/dnf.conf needs to be still configured correctly for your current system to pass the early phases of the upgrade process."}
```
* Going through `/var/log/leapp/leapp-preupgrade.log` more clearly displays package-related issues in `dnf`:
```
2025-04-11 13:53:19.106 DEBUG    PID: 121104 leapp.workflow.TargetTransactionCheck.dnf_transaction_check:  Problem: package dnf-plugins-core-4.3.0-16.el9.noarch from rocky9-bas
eos requires python3-dnf-plugins-core = 4.3.0-16.el9, but none of the providers can be installed
2025-04-11 13:53:19.107 DEBUG    PID: 121104 leapp.workflow.TargetTransactionCheck.dnf_transaction_check:   - package python3-dnf-plugins-core-4.3.0-16.el9.noarch from rocky9-b
aseos requires python3-systemd, but none of the providers can be installed
2025-04-11 13:53:19.107 DEBUG    PID: 121104 leapp.workflow.TargetTransactionCheck.dnf_transaction_check:   - package leapp-repository-deps-el9-5.0.9-100.202411180921Z.f50e3474.main.el9.noarch from @commandline requires dnf-command(config-manager), but none of the providers can be installed
2025-04-11 13:53:19.111 DEBUG    PID: 121104 leapp.workflow.TargetTransactionCheck.dnf_transaction_check:   - conflicting requests
```
#### Solution
* Remove the problematic packages using the following command:
```
dnf remove dnf-plugins-core python3-systemd
```
* Run the `leapp preupgrade` command again and you will see that it completes successfully.
## Start the Upgrade
* Run this command to being the upgrade process:
```
leapp upgrade
```
* Once completed, `reboot` the machine:
```
reboot
```
* At the `GRUB` menu, select the `ELevate-Upgrade-Initramfs` option.
* The system will reboot twice.
* Then you will observe the Rocky Linux options in the `GRUB` menu. That is when you know the `initramfs` upgrade completed successfully.
* `SELinux` will then perform a relabel upon first boot.
* Then log in locally (you won't have access to the `root` account over `ssh` initially) and reenable `ssh` for `root`:
```
sed -i 's/#PermitRootLogin yes/PermitRootLogin yes/' /etc/ssh/sshd_config
```
* Remove any leftover packages from the previous CentOS 8.5 with:
```
rpm -qa | grep -E 'el8[.-]' | xargs rpm -e
```