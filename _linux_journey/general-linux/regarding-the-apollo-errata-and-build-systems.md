---
title: "Regarding the Apollo Errata and Build Systems"
category: "general-linux"
tags: ["regarding", "apollo", "errata", "build", "systems"]
---

# Regarding the Apollo Errata and Build Systems

Apollo generates the errata and koji peridot imports/builds the rpms. The only thing I can think of is that Apollo is processing the peridot build logs and not “pub”.

Yes usually updates are pooled and released together. So should be released soon. Apollo scans from staging, so it will likely land in the nightly. Just checked, pending kernels once the signed ones are in from the SB environment all of the updates will be published

