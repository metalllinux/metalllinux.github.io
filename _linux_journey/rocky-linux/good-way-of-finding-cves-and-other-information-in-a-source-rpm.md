---
title: "A Good Way of Finding CVEs and Other Information in a Source RPM"
category: "rocky-linux"
tags: ["rocky-linux", "good", "way", "finding", "cves"]
---

# A Good Way of Finding CVEs and Other Information in a Source RPM

git grep CVE-2025-9230
SOURCES/0001-Fix-CVE-2025-9230.patch:Subject: [PATCH] Fix CVE-2025-9230.
SOURCES/0001-Fix-CVE-2025-9230.patch:   Fixes CVE-2025-9230
SPECS/openssl.spec:Patch702: 0001-Fix-CVE-2025-9230.patch
SPECS/openssl.spec:%patch702 -p1 -b 0001-Fix-CVE-2025-9230.patch
SPECS/openssl.spec:- Fixe CVE-2025-9230 - kek_unwrap_key(): Fix incorrect check of unwrapped key size

