---
title: "How To Setup A Newly Installed Resf Rocky Linux Ma"
category: "rocky-linux"
tags: ["rocky-linux", "setup", "newly", "installed", "resf"]
---

* **Do not update the machine**
* Install the `depot` RPM:
```
sudo dnf install -y https://depot.ciq.com/public/files/depot-client/depot/depot.x86_64.rpm
```
* Login with your Portal username and password:
```
depot login -u <username> -t <password>
```
* Run `depot list` to see which repositories you have access to:
```
depot list
```
* Enable a repository with `depot enable <REPO_NAME>`
* Then run `dnf update` to update to all of the relevant packages.
* If you observe dependency errors, you may have to install specific packages only, like in the example below:
```
dnf install gnutls-devel kernel-debug-devel kernel-debug-devel-matched kernel-devel kernel-devel-matched kernel-selftests-internal libgcrypt-devel nss-devel nss-pkcs11-devel nss-softokn-devel perf rtla
```