---
title: "How to Downgrade All Packages to a Particular Rocky Linux Version"
category: "rocky-linux"
tags: ["rocky-linux", "downgrade", "all", "packages", "particular"]
---

# How to Downgrade All Packages to a Particular Rocky Linux Version

 cp /etc/yum.repos.d/rocky.repo /etc/yum.repos.d/rocky.repo.bak
 cp /etc/yum.repos.d/rocky-extras.repo /etc/yum.repos.d/rocky-extras.repo.bak
 
 sed -i 's|enabled=1|enabled=0|g' /etc/yum.repos.d/rocky-extras.repo
 sed -i 's|enabled=1|enabled=0|g' /etc/yum.repos.d/rocky.repo
 
 cat<<'EOF' > /etc/yum.repos.d/rocky-vault.repo
 [baseos-vault]
 name=Rocky Linux $releasever - BaseOS - Vault
 baseurl=http://dl.rockylinux.org/vault/rocky/9.4/BaseOS/$basearch/os/
 gpgcheck=1
 enabled=1
 countme=1
 metadata_expire=6h
 gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-Rocky-9
 
 [appstream-vault]
 name=Rocky Linux $releasever - AppStream - Vault
 baseurl=http://dl.rockylinux.org/vault/rocky/9.4/AppStream/$basearch/os/
 gpgcheck=1
 enabled=1
 countme=1
 metadata_expire=6h
 gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-Rocky-9
 
 [extras-vault]
 name=Rocky Linux $releasever - Extras - Vault
 baseurl=http://dl.rockylinux.org/vault/rocky/9.4/extras/$basearch/os/
 gpgcheck=1
 enabled=1
 countme=1
 metadata_expire=6h
 gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-Rocky-9
 EOF
 
 dnf clean all
 
 dnf distrosync
 
 review
 
 reboot
 
 # cat /etc/redhat-release
 Rocky Linux release 9.4 (Blue Onyx)

