---
title: "Print a well known symbol in hex"
category: "kernel-and-system-internals"
tags: ["kernel-and-system-internals", "useful", "crash", "commands"]
---

# Print a well known symbol in hex
crash> px jiffies
# Read contents of memory and display formatted output
crash> rd -S dff12e80 36
# Print the backtrace/stack frame of a context
crash> bt –f
# Display all available symbol table information concerning a data type or a data symbol.
Crash> whatis
# Display stack traces for all tasks
Crash>foreach bt


# Display all kmalloc() slab data
Crash> kmem –S
#Dump the contents of a linked list
crash> ps | grep arg64
  24082   8547  12  ffff810123824100  IN   0.0    3644    376  arg64
crash> list task_struct.tasks ffff810123824100
ffff810123824100
ffff8100640948b8
ffff810064094988
ffff8100b8f744c0
400000006
# Search for a given value in addr space
crash> search -u 400000006
1a747348: 400000006
1a9d8b48: 400000006
# Search symbol table for data/type information
crash> whatis pipe_read
ssize_t pipe_read(struct file *, char *, size_t, loff_t *);

# Show specific backtrace information about a PID

bt <pid>

# Display the status of a specific PID
`ps <pid>`

# Virtual Memory Usage of a PID.
`vm <pid>`

# Display Files Open by a Specific Process
`files <pid>`