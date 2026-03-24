---
title: "Escaping Metacharacters"
category: "learning-regular-expressions"
tags: ["learning-regular-expressions", "escaping", "metacharacters"]
---

* `\`
	* Escape the next character.
* Tells the regex engine to treat the metacharacter as a literal character.
* To match a literal period, you would use `/\./`
* An example would be `/9\.00/` matches "9.00", but not "9500" or "9-00".
* Match a backslash by escaping a backslash with `\\`
* Escaping is only done for metacharacters.
* Literal characters should never be escaped.
* Quotation marks are not metacharacters and do not need to be escaped.
* `/h.._export.txt/g` would match "his_export.txt" and "her_export.txt"
* Another good example is `/resume.\.txt/` which will match "resume1.txt", "resume2.txt" and then not match "resume3_txt.zip", because it then matches the number and not the `_` after it.