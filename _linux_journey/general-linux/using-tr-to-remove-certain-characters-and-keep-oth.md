---
title: "Using Tr To Remove Certain Characters And Keep Oth"
category: "general-linux"
tags: ["remove", "certain", "characters", "keep", "oth"]
---

tr -dc '[:alnum:]\n\r' | tr '[:upper:]' '[:lower:]'
* `tr` deletes special characters.
* `d` is delete.
* `c` is complement (invert the character set).
* `dc` is therefore, delete all characters, except those specified.
* Can preserve certain characters, such as `\n` and `\r` above.
* The second line translates uppercase characters to lowercase.