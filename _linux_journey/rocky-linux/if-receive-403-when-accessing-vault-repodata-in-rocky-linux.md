---
title: "If You Receive a 403 When Accessing Vault Repodata in Rocky Linux"
category: "rocky-linux"
tags: ["rocky-linux", "receive", "when", "accessing", "vault"]
---

# If You Receive a 403 When Accessing Vault Repodata in Rocky Linux

hi,
I’m trying to do a yum history undo on a Rocky 9.5 ec2 instance.
I’m getting a 403, here:

https://dl.rockylinux.org/vault/rocky/9.5/BaseOS/x86_64/os/repodata/

Hello, welcome to the forums.

This is intentional. This prevents our mirror manager from getting confused and using that repodata to determine if our mirrors are up to date.

We are not able to, at this time, to have multiple versions of packages in our repositories due to a build system flaw. As a compromise, we sync everything to the vault without repodata.
