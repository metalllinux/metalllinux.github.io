---
title: "Other Special Characters"
category: "learning-regular-expressions"
tags: ["learning-regular-expressions", "other", "special", "characters"]
---

* Spaces
	* These are also characters.
* Tabs (\t)
	* The above `\t` is often referred to as a control character.
* Line returns (\r, \n, \r\n)
	* `\r` is a return line.
	* `\n` is a new line.
		* Also called a `line feeder` character.
		* Some operating systems use one or the other or both together.
			* Depends if the file using was made on Windows, Mac or Linux.
* Example: `a\tb`
	* Matches "a	b"
* Example: `c\nd`
	* Matches:
abc
def
* `\n` allows for matching text across multiple lines.