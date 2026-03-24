---
title: "Surrounding the Devel Repo by the RESF and it Brekaing"
category: "general-linux"
tags: ["surrounding", "devel", "repo", "resf", "breaking"]
---

# Surrounding the Devel Repo by the RESF and it Brekaing

RESF will continue to break this particular repo (devel) until it's obsoleted or they stop using peridot v1.

Good example bug with `jansi-javadoc`:

```
https://bugs.rockylinux.org/view.php?id=8647
```

RESF's stance on Devel and fixing it:

> Devel issue is known but not a high priority fix. The devel repo is explicitly buildroot and not supported the same way the branded repos are. It'll get fixed but it is not a bug per-se. It's probably frustrating for their use case but devel will always be best-effort, just like CentOS devel. RHEL doesn't even provide devel fwiw. We did a cleanup of the branded repos before latest 9 release though so next round of cleanups would only be devel focused
