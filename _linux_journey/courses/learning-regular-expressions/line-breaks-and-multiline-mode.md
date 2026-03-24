---
title: "Line Breaks And Multiline Mode"
category: "learning-regular-expressions"
tags: ["learning-regular-expressions", "line", "breaks", "multiline", "mode"]
---

* `/[a-z ]+/` will match:
milk
apple juice
sweet peas
	* It will match everything in the above list, if the global flag is set.
* `^/[a-z ]+/` will only match "milk" in the above list.
* With regex there is `Single-line mode` and `multiline mode`.
* Single-line mode is default.
	* `^` and `$` do not match at line breaks.
	* `\A` and `\Z` also do not match at line breaks.
* Can change the regex to evaluate in multiline mode.
	* `^` and `$` will match at the start and end of lines.
	* `\A` and `\Z` does not match at line breaks.
* Most Unix tools only support single-line mode.
	* Multiline came later on.
	* Most programming languages offer multiline options.
* An example of multiline per programming language:
![Capture.PNG](../../_resources/Capture.PNG)
* Doing `/^[a-z ]+$/` with global and multiline flags on selects all of the following 
"milk
"apple juice
"sweet peas"
"sweet peas (2)" --> This will not match
* If change `/^[a-z ]+$/` to `/\A[a-z ]+\Z/` , none of the above match, since we are refencing the entire string, not the beginning and end of a line.


