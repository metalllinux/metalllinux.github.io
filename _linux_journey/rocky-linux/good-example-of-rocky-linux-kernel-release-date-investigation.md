---
title: "Good Example of a Rocky Linux Kernel Release Date Investigation"
category: "rocky-linux"
tags: ["rocky-linux", "good", "example", "rocky", "linux"]
---

# Good Example of a Rocky Linux Kernel Release Date Investigation

* I checked under `https://git.rockylinux.org/explore` and there is a commit of [0c3421e2 - import kernel-4.18.0-553.53.1.el8_10](https://git.rockylinux.org/staging/rpms/kernel/-/commit/0c3421e27d54e2941ea7f96b7411769dfedf697e) for kernel `kernel-4.18.0-553.53.1.el8_10` from 5 days ago.

* Similarly under commit [bdfcd702 - import kernel-4.18.0-553.52.1.el8_10](https://git.rockylinux.org/staging/rpms/kernel/-/commit/bdfcd7026275e87d7d69251479ccf3cffcc41bad) from 7 days ago, this has kernel `kernel-4.18.0-553.52.1.el8_10` also accounted for.

* I checked the `kernel.spec` diff for both kernels and they have all of the CVE fixes from [RHSA-2025:7531](https://access.redhat.com/errata/RHSA-2025:7531) and [RHSA-2025:8056](https://access.redhat.com/errata/RHSA-2025:8056) included.

* From the `Identity Management & Release Engineering Lead` Louis Abel, [they make a good comment in issue #9307](https://bugs.rockylinux.org/view.php?id=9307) that all kernels need to be built first in the project's secure boot environment and tested before they are released. [They then link to the General Update Timeline documentation](https://wiki.rockylinux.org/rocky/version/#general-update-timeline), which in particular states the following:
> Updates for Rocky Linux are generally expected to be built and released between twenty-four (24) and fourty-eight (48) hours, assuming best effort allows the packages to build without any complications or unforeseen added dependencies by upstream mid-support cycle.

It is for certain that we will see both kernels released for Rocky Linux 8.10 in the near future, once the Rocky Engineering Team have deemed them fit for release after testing is complete.

