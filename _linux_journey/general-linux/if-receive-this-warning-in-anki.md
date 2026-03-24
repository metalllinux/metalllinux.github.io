---
title: "If Receive This Warning In Anki"
category: "general-linux"
tags: ["receive", "warning", "anki"]
---

Anki starting...
Initial setup...
Running with temporary Qt5 compatibility shims.
Run with DISABLE_QT5_COMPAT=1 to confirm compatibility with Qt6.
Preparing to run...
  File "<string>", line 1, in <module>
  File "aqt", line 489, in run
  File "aqt", line 563, in _run
  File "aqt.profiles", line 133, in setupMeta
  File "aqt.profiles", line 413, in _loadMeta
resetting corrupt _global
Qt info: Could not load the Qt platform plugin "xcb" in "" even though it was found. 
Qt fatal: This application failed to start because no Qt platform plugin could be initialised. Reinstalling the application may fix this problem.

Available platform plugins are: minimalegl, xcb, linuxfb, eglfs, offscreen, vnc, minimal, wayland, wayland-egl, vkkhrdisplay.


MAKE SURE THE FOLLOWING PACKAGE IS INSTALLED: `libxcb-cursor0`