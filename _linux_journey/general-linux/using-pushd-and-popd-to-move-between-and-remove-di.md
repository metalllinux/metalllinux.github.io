---
title: "Using Pushd And Popd To Move Between And Remove Di"
category: "general-linux"
tags: ["pushd", "popd", "move", "between", "remove"]
---

`dirs -v`
* Shows the list of directories and number.
`pushd +<number>`
* Allows you to switch into that directory of choice.
* To change into the directory at the bottom of the stack, you can use `pushd -0`
* `popd +1` will remove directory `1` from the stack.
* Similarly we can remove the bottom directory with `popd -0`