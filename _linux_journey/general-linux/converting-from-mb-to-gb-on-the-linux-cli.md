---
title: "Converting From Mb To Gb On The Linux Cli"
category: "general-linux"
tags: ["converting", "linux", "cli"]
---

echo "scale=2; 500/1024" | bc

In this command:

    echo is used to output the value to be converted.
    scale=2 sets the number of decimal places to 2.
    500/1024 calculates the result of dividing 500 MB by 1024 MB (which is equal to 1 GB).
    | (pipe) is used to redirect the output of the echo command to the input of the bc command.
    bc calculates the result of the expression and outputs it to the command line.

The output of this command will be: