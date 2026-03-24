---
title: "Command To List All Kernels In Use"
category: "general-linux"
tags: ["command", "list", "all", "kernels"]
---

cat sh_-c_rpm_--nodigest_-qa_--qf_-59_NVRA_INSTALLTIME_date_sort_-V  | grep -i 'xfs\|kernel'