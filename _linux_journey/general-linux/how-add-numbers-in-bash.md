---
title: "How Add Numbers In Bash"
category: "general-linux"
tags: ["add", "numbers", "bash"]
---

Arithmetic in POSIX shells is done with $ and double parentheses (( )):

echo "$(($num1+$num2))"

You can assign from that; also note the $ operators on the variable names inside (()) are optional):

num1="$((num1+num2))"

There is also expr:

expr $num1 + $num2

In scripting $(()) is preferable since it avoids a fork/execute for the expr command.
