---
title: "Information on the Rocky Linux Testing Team"
category: "rocky-linux"
tags: ["rocky-linux", "information", "rocky", "linux", "testing"]
---

# Information on the Rocky Linux Testing Team

Lots of confusion emanating here.
Rocky test team uses openqa to test new releases (like 9.6 and 10.0 right now).  It's a way to put the iso in and simulate the user experience of installing, then checking the installed system.
It's very necessary to ensure a successful Rocky release, but it has basically nothing to do with kernel testing.
Normal kernel updates (like in current 8.10) are tested, but it takes way less than a week.  More like a half a day or less.  And openqa is not used for that.
It's important to test Rocky kernels, especially in the area of secureboot signing - that's a difference between the RH and Rocky kernels, despite having the same code base.  Red Hat does excellent QA work on these kernels though, they have to be commended (they also commit a gigantic amount of resources to it)

Rocky package releases will trail redhat's by necessity.  In practice, package updates are prety fast (1-2 days).  However, there is NO SLA on Rocky package releases, and there likely never will be.
It's a community project - it's unclear what would even happen in the event of a hypothetical sla violation?

It sounds to me like company people read about Rocky testing procedure for a release (every 6 months) and assumed it applies to all package updates (every week, or even several times a week).
They are not the same thing
