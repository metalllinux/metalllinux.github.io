---
title: "Useful Command to Check for All CIQ Bridge CVEs in CIQ's CSAF Files and Create a CSV File"
category: "networking"
tags: ["networking", "useful", "command", "check", "all"]
---

# Useful Command to Check for All CIQ Bridge CVEs in CIQ's CSAF Files and Create a CSV File
```
find ./advisories/csaf/vex/cve/{2005..2025} -type f -name "*.json" 2>/dev/null -exec cat {} + | jq -s -r '
  def parse_pkg($s):
      ($s | split("-") | { package_name: .[0], package_version: (.[1:] | join("-")) });
  [ .[] |
    . as $doc |
    # For each vulnerability in the advisory
    ($doc.vulnerabilities[]? | { vuln: ., track: $doc.document.tracking } ) as $v |
    # For each fixed product that starts with "cbr-7.9:"
    $v.vuln.product_status.fixed[]? 
    | select(startswith("cbr-7.9:"))
    | (
         # Remove "cbr-7.9:" and split by ".ciqcbr." to separate package info from the RPM architecture
         split(":")[1] as $fix
         | ($fix | split(".ciqcbr.")) as $parts
         | ( parse_pkg($parts[0]) ) as $pkg
         | {
             cve: $v.vuln.cve,
             product_key: "cbr-7.9",
             product_name: "CIQ Bridge",
             rpm: $parts[1],
             package_name: $pkg.package_name,
             package_version: $pkg.package_version,
             impact: (( $v.vuln.threats[]? | select(.category=="impact") | .details ) // ""),
             status: $v.track.status,
             initial_release_date: $v.track.initial_release_date,
             score: (( $v.vuln.scores[0].cvss_v3.baseScore ) // ""),
             severity: (( $v.vuln.scores[0].cvss_v3.baseSeverity ) // "")
          }
      )
  ]
  | sort_by(.initial_release_date) | reverse
  | (["cve","product_key","product_name","rpm","package_name","package_version","impact","status","initial_release_date","score","severity"] | @csv),
    (.[] | [ .cve, .product_key, .product_name, .rpm, .package_name, .package_version, .impact, .status, .initial_release_date, .score, .severity ] | @csv)
' > bridge_cves.csv
```

