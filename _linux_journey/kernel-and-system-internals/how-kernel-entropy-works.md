---
title: "How Kernel Entropy Works"
category: "kernel-and-system-internals"
tags: ["kernel-and-system-internals", "kernel", "entropy", "works"]
---

Kernel DRBG (Deterministic Random Bit Generator) is a cryptographic component implemented in the Linux kernel, based on the NIST SP 800-90A standard. It is used to generate cryptographically secure random numbers, which are essential for various security operations like key generation, secure communications, and more.

From Jason:

The way the Kernel DRBG works is the entropy pool is filled, the fill operation is nonblocking, After the pool is filled the entropy may or may not be conditioned(hashed), which adds an additional operation(delay).
In our FIPS kernel offering the filling of the entropy pool is a blocking operation and will not proceed until the pool is filled and then the pool is hashed.
The result is our offering provides max entropy for all operations. Where as the default will provide (random) level of entropy which is dangerous.
RNGD will not help feed the FIPS kernel unless the kernel is running as a container being feed by the base OS.