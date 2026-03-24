---
title: "Install rocky 10 on vmware failure"
category: "rocky-linux"
tags: ["rocky-linux", "install", "rocky", "vmware", "failure"]
---

#  Install rocky 10 on vmware failure

Install rocky 10 on vmware failure

https://forums.rockylinux.org/t/install-rocky-10-on-vmware-failure/18905


post by iwalker on Jun 23
iwalker
Community Team
Jun 23

Ah the fun and joy of propriertary software like VMware.

I use VMware ESXi and version 8.0 patch 3 and I can install Rocky 10 with a EL9 template. I expect the problem is VMware doesn’t support installing EL10 machines in VMware Workstation Pro. You’ll prob need to wait for a new version of VMware Workstation to be released.

post by sspencerwire on Jun 23
sspencerwire
Documentation Team Lead
Jun 23

Hi @aaadddzxc and @iwalker:

This is a Known Issue in 10: See this from the release notes for a workaround.

Good luck!
Steve

post by aaadddzxc on Jun 24
aaadddzxc
Jun 24

    VMware was unsuccessful

thanks.
it will be normal after turning off 3D acceleration

9 days later
post by joy0100 on Jul 3
joy0100
Jul 3

Confirmed working with VMware workstation pro 17.
17.6.2 build-24409262

Thanks about the 3D acceleration info

9 days later
post by mandrews on Jul 13
mandrews
sspencerwire
Jul 13

That worked for me. Thank you!

2 months later
Closed on Sep 11

Closed on Sep 11

This topic was automatically closed 60 days after the last reply. New replies are no longer allowed.

