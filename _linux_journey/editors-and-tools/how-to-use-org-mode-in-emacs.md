---
title: "How to use Org Mode in Emacs"
category: "editors-and-tools"
tags: ["editors-and-tools", "org", "mode", "emacs"]
---

# How to use Org Mode in Emacs

* Create a file and give it the `.org` extension.

* Doom Emacs uses EVIL ORG mode.

* To create an outline you use `asterix`.

#+title:  Org Mode Basics in Doom Emacs
#+description: An org mode document
#+author: Example User

* A new headline
 ** Level 2 headline
   *** Leve 4

* Check Org Mode manual with:

```
M-x org-info
```

* org-toggle-heading: SPC-m-h

You can Toggle it back off with SPC-m-h

Can also do SPC-m-i for org-toggle-item

Can do an unordered with with the + sign
+ ITEM 1
  - Item 2
    + Item 3
      1. TEMP
      2. Add more Items with `ctrl + return`
      3.
Can unfold varios subtress.
Hit the Tab key to fold and unfold trees. Place the cursor at the headline. Shift Tab allows you to fold, unfolding and really unfolding everything.
Can also do z + c   or z + o

Can do z + M to fold the entire buffer.

Can do z + R to unfold the entire buffer.

Standard vim keybindings also work here.

Can go down headings by using g + k  and g + j - these move to the child elements.

If you hit ctrl + return, it gives you a new level i

If you want to promote or demote a heading.

* Use M + l and this make it one level lower.
* M + h makes it a higher level.

* You can move whole subtrees by using M + k and M + k

* What if yo want to move a line instead of the whole tree - M + shift + j

* select an element: v + a + e
* delete an element: d + a + e

* To select an entire subtree v + a + R
* To delete a subtree d + a + R

* For snippetes - SPC + i + s For example with bash scripts:

#!/usr/bin/env bash

* To add the current time SPC + i + s and add the current time.

