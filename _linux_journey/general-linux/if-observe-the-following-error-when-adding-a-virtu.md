---
title: "If Observe The Following Error When Adding A Virtu"
category: "general-linux"
tags: ["observe", "following", "error", "when", "adding"]
---

```
Error starting network 'default': error creating bridge interface virbr0: "File exists"
```
* The above error occurs when you try to start the `default` network that is in `inactive` state.
* When creating a new virtual machine, at `Step 5`, go to `Network selection` and choose `Bridge device...` and set the `Device name` as `virbr0` (it should already be pre-populated).