---
title: "Use Pipes as a Delimeter for sed Commands so You Don't Need to Escape Forward Slashes in URLs etc"
category: "editors-and-tools"
tags: ["editors-and-tools", "pipes", "delimeter", "sed", "commands"]
---

# Use Pipes as a Delimeter for sed Commands so You Don't Need to Escape Forward Slashes in URLs etc

Examples:

sed -i 's|#baseurl=https://download.example/pub/epel/.*/Everything/$basearch/|baseurl=https://dl.fedoraproject.org/pub/archive/epel/9.6/Everything/$basearch/|' /etc/yum.repos.d/epel.repo

sed -i '/^\[epel\]$/,/^\[/{s|^metalink=|#metalink=|}' /etc/yum.repos.d/epel.repo
