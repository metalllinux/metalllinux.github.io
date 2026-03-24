---
title: "Recursive Search"
category: "general-linux"
tags: ["recursive", "search"]
---

ctrl + r

That searches backwards through your history. To search forward instead, use Ctrl + S, but you may need to have set: stty -ixon (either by .bash_profile or manually) prior to that to disable the XON/XOFF feature which takes over Ctrl + S. If it happens anyway, use Ctrl + Q to re-enable screen output (More details here.)