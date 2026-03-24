---
title: "Solution Backreferences"
category: "learning-regular-expressions"
tags: ["learning-regular-expressions", "solution", "backreferences"]
---

* Challenge --> Regex that captures and replaces a string.
* `/^\d+,(.+),(\d{4}),(\d{0,4}),.+,.+https:.+$/`
* This regex will match a string, which is "1,George Washington,1789,1797,Independent,Virginia,https://en.wikipedia.org/wiki/George_Washington"
* We can then replace the text with `\2-\3: \1` which will format the text such as
1789-1797: George Washington
Can put it into a database, html or other such format.