---
title: "Lookbehind Assertions"
category: "learning-regular-expressions"
tags: ["learning-regular-expressions", "lookbehind", "assertions"]
---

* True if grouped expression is (or is not) behind the current position.
* Similar to lookahead assertions.
* Group is not included in the match or captured.
* Javascript support is available.
	* Metacharacters are `?<=` Group is a positive lookbehind assertion.
	* `?<!` Group is a negative lookbehind assertion.
* A example: `/(?<=base)ball/` matches "ball" in "baseball", but not "football".
	* Looks backwards at the word it initially matches.
* `/(?<!base)ball/` matches "ball" in "football", but not "baseball".
* `/(?<=\bfor\s)\b\w+/` matches first word after "for".
* `/\b\w+(?<!er)\b/` matches words not ending in "er".
* An example is "I like baseball and football."
* `/(?<=base)ball/` will match the ball in "baseball", but not "football".
	* Changing the regex to `/(?<!base)ball/` then matches the "ball" in "football" instead.
* Next example is:
John Smith
Mr. Smith
Ms. Smith
Mrs. Smith
Mr. John Smith
* Can match "Mr", "Ms" and "Mrs" with
	* `/(?<=(Mr|Ms|Mrs)\. )Smith/`
* Most regex engines do not allow expressions with variable widths.
	* Must have the same width.
* Perl, Ruby and Java support alternations of different widths.
* 