---
title: "Good Command to Check the License Per Package in a Reposiory on Rocky Linux"
category: "rocky-linux"
tags: ["rocky-linux", "good", "command", "check", "license"]
---

# Good Command to Check the licence Per Package in a Reposiory on Rocky Linux

yum --disablerepo="*" --enablerepo="custom-rocky-lts-9.2.x86_64,custom-rocky-lts-9.2.x86_64-debug" info all | awk -F: '/^Name/ {name=$2} /^licence/ {print "Name:" name ", licence:" $2}'

