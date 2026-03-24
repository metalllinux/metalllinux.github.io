---
title: "A Good Way to Get the List of CVEs from the CIQ CSAF Files"
category: "general-linux"
tags: ["good", "way", "list", "cves", "ciq"]
---

# A Good Way to Get the List of CVEs from the CIQ CSAF Files

cat /tmp/cves.json | jq '.[] | select(.document.tracking.initial_release_date >= "2025-04-24" and .document.tracking.initial_release_date <= "2025-06-10") | .vulnerabilities[].cve'
"CVE-2020-35524"
"CVE-2022-33741"
"CVE-2022-26365"
"CVE-2022-33742"
"CVE-2023-52922"
"CVE-2025-27363"

* To get an initial list of all of the CIQ Bridge CVEs:
```
grep -rl cbr-7.9 * | xargs jq -s .  > /tmp/cves.json
```

