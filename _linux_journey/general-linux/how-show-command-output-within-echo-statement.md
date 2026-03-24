---
title: "How Show Command Output Within Echo Statement"
category: "general-linux"
tags: ["show", "command", "output", "within", "echo"]
---

To save the output from a command in a variable just use:

var=$(command)

And remember to quote the variable when you use it:

echo "Hello $var, happy to see you again"
