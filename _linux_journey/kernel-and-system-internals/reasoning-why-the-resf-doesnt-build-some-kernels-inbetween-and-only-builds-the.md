---
title: "Reasoning Why the RESF Doesn't Build Some Kernels Inbetween and Only Builds the Latest Kernel"
category: "kernel-and-system-internals"
tags: ["kernel-and-system-internals", "reasoning", "resf", "doesnt", "build"]
---

# Reasoning Why the RESF Doesn't Build Some Kernels Inbetween and Only Builds the Latest Kernel

From Neil:

It's basically that Rocky will always target the latest available version, so if a new version rolls in, unless that version was on the way out the door, it would "reset" the process. It typically only takes a couple days for the team to build, test, and release a new kernel, but around release times are always special circumstances--partly because there's a lot of movement inside RH to keep track of, too.

