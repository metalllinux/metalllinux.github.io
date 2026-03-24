---
title: "Intro To Threads And Processes"
category: "python-essential-training"
tags: ["python-essential-training", "intro", "threads", "processes"]
---

* Computers have memory and file storage.
	* Short-term and long-term memory.
* Loading files from the disk is long-term memory.
	* A variable in a program is short-term memory in the processor.
* If you have two programs, once program can save a file to disk and the other program can pick it up `progA` and `progB`
	* However if `progA` writes something to memory, `progB` cannot access it.
* OS' place walls in between the programs.
* Very important for programmers to know where these are being stored and whom has access to what.
* OS's also allow placing two programs into the same process.
	* They then get to share memory.
	* Instead of separate processes, they are run on separate threads.
* A process can have multiple threads.
	* Can execute code at the same time in parallel.