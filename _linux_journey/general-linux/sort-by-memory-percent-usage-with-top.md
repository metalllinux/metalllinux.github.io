---
title: "Sort By Memory Percent Usage With Top"
category: "general-linux"
tags: ["sort", "memory", "percent", "usage", "top"]
---

Use the top command in Linux/Unix:

top

    press shift+m after running the top command
    or you can interactively choose which column to sort on
        press Shift+f to enter the interactive menu
        press the up or down arrow until the %MEM choice is highlighted
        press s to select %MEM choice
        press enter to save your selection
        press q to exit the interactive menu

Or specify the sort order on the command line

# on OS-X
top -o MEM
# other distros
top -o %MEM
