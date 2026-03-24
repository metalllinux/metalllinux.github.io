---
title: "Tar An Entire Directory"
category: "general-linux"
tags: ["tar", "entire", "directory"]
---

tar cvf name_of_archive.tar dirname/

Gzipping the File as well:

tar cvf test.tar ./test && gzip -9 test.tar

Makes multiple smaller files:

split -b 500M test.tar "test.tar.part"