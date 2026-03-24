---
title: "If Run Dnf Install Y Ciq And Receive A Repomd.Xml"
category: "rocky-linux"
tags: ["rocky-linux", "run", "dnf", "install", "ciq"]
---

I’m getting this error with dnf install -y ciq
[root@mirrorshades 5.15.34-v8.1.el8]# dnf install -y ciq
CIQ Public Packages for Rocky Linux 8 - Release                                                                                                                         112  B/s |  52  B     00:00
Errors during downloading metadata for repository ‘public-release’:
Status code: 404 for https://elasticrepo.build.ctrliq.cloud/v1/public/subscriptions/public8/Release/aarch64/repodata/repomd.xml (IP: 44.238.64.62)
Error: Failed to download metadata for repo ‘public-release’: Cannot download repomd.xml: Cannot download repodata/repomd.xml: All mirrors were tried
Mustafa Gezen
  2 years ago
Unfortunately, the old cluster doesn't have support for aarch64, so it's not available. With Docker Desktop for Mac you can do docker run --platform linux/amd64 --rm -it rockylinux/rockylinux