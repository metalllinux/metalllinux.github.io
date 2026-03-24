---
title: "Top Commands"
category: "general-linux"
tags: ["top", "commands"]
---

PID: Process identification number.
USER: The name of the user running the process.
PR: The scheduling priority for the process.
NI: The nice value of the process, with negative numbers indicating higher priority.
VIRT: The virtual memory amount used by the process.
RES: The resident (physical) memory amount used by the process.
SHR: The total shared memory used by the process.
S: The status of the process - R (running) or S (sleeping).
%CPU: The percentage of CPU usage.
%MEM: The memory usage percentage.
TIME+: Total CPU usage amount.
COMMAND: The name of the command that started the process.
While the top command is running, use the following options to interact with it or change the output format:

c: Display the absolute process path.
d: Change the output refresh rate to a user-defined value (in seconds).
h: Display the help window.
k: Kill a process by providing the PID.
M: Sort the list by memory usage.
N: Sort the list by PID.
r: Change the nice value (priority) of a process by providing the PID.
z: Change the output colour to highlight running processes.
q: Quit the command interface.			