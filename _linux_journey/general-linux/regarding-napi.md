---
title: "Regarding Napi"
category: "general-linux"
tags: ["regarding", "napi"]
---

Possible Confusion with NAPI: Linux has a well‑established subsystem called NAPI (New API) for network drivers. NAPI reduces the interrupt load under high network traffic by switching to a polling mechanism. In discussions of driver performance or patch series, one might see developers “bifurcating” or splitting code paths within this framework to optimise handling of different traffic types or hardware conditions. However, this is usually discussed in terms of “NAPI” rather than “SNAPI.” It’s possible that in some specific patch or vendor-specific modification someone might have introduced the term “SNAPI” (perhaps standing for a “split” or “streamlined” version of NAPI) along with “bifurcation” to describe diverging code paths or functional splits. In the mainline kernel—and in common documentation—the term “SNAPI bifurcation” isn’t used. For background on NAPI in Linux, you can review the 