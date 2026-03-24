---
title: "How To Extract The Spec File From A Source Rpm"
category: "rocky-linux"
tags: ["rocky-linux", "extract", "spec", "file", "source"]
---

`rpm2cpio <SOURCE_RPM_HERE> | cpio -civ '*.spec'`