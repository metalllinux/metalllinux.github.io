---
title: "Good Example of Messaging on How Patches Come from Upstream into RHEL, then Rocky Linux"
category: "rocky-linux"
tags: ["rocky-linux", "good", "example", "messaging", "patches"]
---

# Good Example of Messaging on How Patches Come from Upstream into RHEL, then Rocky Linux

I wanted to reach out with an update on the next steps for addressing the cp binary issue through the coreutils package.
 
As you know, the issue and proposed fix have already been raised with the upstream coreutils project. Once that fix is accepted, there is a natural progression of implementations that need to take place before the update reaches Rocky Linux. The typical path is as follows:
 

    Acceptance into the upstream coreutils project
    Inclusion into Fedora
    Adoption by RHEL
    Incorporation into Rocky Linux

 
Each stage depends on upstream decisions, so while this is the established process, the timeline is not defined and may vary. It is also possible that not every step will occur as expected, which could mean the fix may not reach Rocky Linux in the immediate future.
This is generally how fixes from upstream open source projects make their way downstream, and it ensures consistency and stability across the ecosystem.

