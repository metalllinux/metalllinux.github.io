---
title: "Quantified Repetition"
category: "learning-regular-expressions"
tags: ["learning-regular-expressions", "quantified", "repetition"]
---

* Previous metacharacters can be repeated 0, 1 or an infinite number of times.
* However, there are cases where you'll want to repeat something a certain number of times.
* `{`
	* Start quantified repetition of preceding item.
* `}`
	* End quantified repetition of preceding item.
	* `{min,max}`
* min and max are always positive numbers.
* min must always be included and can be zero.
* max is optional.
* Three syntaxes:
	* `\d{4,8}` matches numbers with 4 to 8 digits.
	* `\d{4}` matches numbers with exactly 4 digits (min is max).
	* `\d{4,}` matches numbers with 4 or more digits (max is infinite).
* `\d{0,}` is the same as `\d*`
* `\d{1,}` is the same as `\d+`
* `/\d{3}-\d{3}-\d{4}/` matches most US phone numbers.
* `/A{1,2} bonds/` matches "A bonds" and "AA bonds", but not "AAA bonds".
* A good example:
* `/\d\. \w+\s/`
	* `\s` indicates the line return at the end and the above regex matches the following:
1. a
2. ab
3. abc
4. abcd
5. abcde
6. abcdef
* Changing the above regex to:
* `/\d\. \w{2,5}\s/` would match all of the above words that are 2~5 characters long.
* 