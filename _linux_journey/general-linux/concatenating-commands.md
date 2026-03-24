---
title: "Concatenating Commands"
category: "general-linux"
tags: ["concatenating", "commands"]
---

Adding `&&` will only execute if the previous command executes correctly.

With `;` this executes the second command, even if the previous commands fails.

With `//` , this executes the second command, only if the preceding command returns an error.