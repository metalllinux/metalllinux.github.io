---
title: "Having Or Not Having Fips Libraries Doesn T Help"
category: "security"
tags: ["security", "having", "having", "fips", "libraries"]
---

Just looked at their test code. All they're using is sys_getrandom(). They're not using the FIPS libraries at all. So no, FIPS libraries won't help them. All that matters is the random number generator in the kernel.

Dug a bit deeper into the kernel drbg code. It's a little hard to read (typical of the Linux crypto subsystem :slightly_smiling_face: ) but I think the long and the short of it is that getting entropy in FIPS mode is slower.