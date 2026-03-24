---
title: "How Do I use LDAP / Active Directory Users with Rootless Podman, Buildah or Skopeo?"
category: "kubernetes-and-containers"
tags: ["kubernetes-and-containers", "ldap", "active", "directory", "users"]
---

# How Do I use LDAP / Active Directory Users with Rootless Podman, Buildah or Skopeo?

## Environment

-   Red Hat Enterprise Linux 7
-   Red Hat Enterprise Linux 8
-   Red Hat Enterprise Linux 9

## Issue

-   I have a system which uses LDAP or Active Directory for user management and authentication.
-   How do we ensure users can use rootless podman and other container-tools even when they are not local users?

## Resolution

-   Currently, no automatic method of adding the necessary subuid or subgid ranges to allow for rootless containerisation exists.
-   For each user that logs in, a separate entry to the `/etc/subuid` and `/etc/subgid` files must be added in order for rootless podman to function, in order to allocate user namespaces to the rootless user.
-   For information on how to properly update the `/etc/subuid` and `/etc/subgid` ranges, please refer to the following articles:
    -   [Running rootless Podman as a rootless user](https://www.redhat.com/sysadmin/rootless-podman-makes-sense)
    -   [`/etc/subuid` and `/etc/subgid` configuration](https://access.redhat.com/bounce/?externalURL=https%3A%2F%2Fgithub.com%2Fcontainers%2Fpodman%2Fblob%2Fmain%2Fdocs%2Ftutorials%2Frootless_tutorial.md%23etcsubuid-and-etcsubgid-configuration)
    -   [What needs to be configured for a user to execute rootless Podman commands without using SSH?](https://access.redhat.com/solutions/6204862)
-   In the below "Root Cause" section, the current efforts to automate this process is discussed. No solution exists at the time of writing this article, but solutions are being explored.

## Root Cause

-   The `container-tools` utilities such as `podman`, `buildah`, or `skopeo` rely on the `newuidmap` and `newgidmap` binaries provided by the `shadow-utils` package in order to allocate user namespace ranges for rootless users.
-   Currently, the `shadow-utils` package does not support automatic adding or updating sub-UID or sub-GID ranges automatically for non-local users. When creating a local user via `adduser` or `useradd`, the ranges can be automatically updated; however, no such process exists for remote users.
-   A [Github Request for Feature Enhancement to Podman](https://access.redhat.com/bounce/?externalURL=https%3A%2F%2Fgithub.com%2Fcontainers%2Fpodman%2Fissues%2F5196) was added discussing allowing `podman` to support such a system to allow remote users access to user namespaces automatically, where it was noted that first the `shadow-utils` package must first accommodate any utilities that desire this automation.
-   A [Github Issue against the `shadow-maint` package](https://access.redhat.com/bounce/?externalURL=https%3A%2F%2Fgithub.com%2Fshadow-maint%2Fshadow%2Fissues%2F154) discusses the issue in more detail, specifically how the new addition of `libsubid` will allow utilities such as `newuidmap` and `newgidmap` to allow for mapping ranges of user ID's without needing to manually configure files.
-   The addition of `libsubid` was added to `shadow-maint` in [this Github Commit](https://access.redhat.com/bounce/?externalURL=https%3A%2F%2Fgithub.com%2Fshadow-maint%2Fshadow%2Fcommit%2F8492dee6632e340dee76eee895c3e30877bebf45).
-   A new release of `shadow-utils` with the above `libsubid` addition is necessary upstream first, and when that is completed, the core `containers/storage` package that `podman`, `skopeo`, and `buildah` rely on can take advantage of `libsubid` via this [Github discussion](https://access.redhat.com/bounce/?externalURL=https%3A%2F%2Fgithub.com%2Fcontainers%2Fstorage%2Fpull%2F882).
-   Effectively, the steps to involve automatically allocated user namespace ID's to remote users can only be added when:
    -   A new version of `shadow-utils` is shipped upstream with `libsubid` support.
    -   The container library `containers/storage` adopts the usage of `libsubid`.
    -   Red Hat has ample time to QA and test the above additions prior to releasing them into a version of container tooling that is available to customers.
-   Attempts to keep this article updated with upstream developments will be made as this feature nears closer to release.

-   **Product(s)**
-   [Red Hat Enterprise Linux](https://access.redhat.com/search?q=Red+Hat+Enterprise+Linux&documentKind=Article%26Solution)

-   **Component**
-   [buildah](https://access.redhat.com/search?q=buildah&documentKind=Article%26Solution)
-   [container-tools](https://access.redhat.com/search?q=container-tools&documentKind=Article%26Solution)
-   [podman](https://access.redhat.com/search?q=podman&documentKind=Article%26Solution)
-   [skopeo](https://access.redhat.com/search?q=skopeo&documentKind=Article%26Solution)

-   **Category**
-   [Configure](https://access.redhat.com/search?q=Configure&documentKind=Article%26Solution)

-   **Tags**
-   [active\_directory](https://access.redhat.com/search?q=active_directory&documentKind=Article%26Solution)
-   [buildah](https://access.redhat.com/search?q=buildah&documentKind=Article%26Solution)
-   [containers](https://access.redhat.com/search?q=containers&documentKind=Article%26Solution)
-   [ldap](https://access.redhat.com/search?q=ldap&documentKind=Article%26Solution)
-   [podman](https://access.redhat.com/search?q=podman&documentKind=Article%26Solution)
-   [skopeo](https://access.redhat.com/search?q=skopeo&documentKind=Article%26Solution)
