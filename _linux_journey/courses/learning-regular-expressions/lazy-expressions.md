---
title: "Lazy Expressions"
category: "learning-regular-expressions"
tags: ["learning-regular-expressions", "lazy", "expressions"]
---

* `?` makes a preceding quantifier lazy.
	* This mark was also used for repetition, to say that something should happen either 0 or 1 time.
	* In this use case, its context has a different meaning.
* Examples:
	* `*?`
		* Something should be zero or one time.
	* `+?`
		* Should use lazy behaviour to do the above.
	* `{min,max}?`
* `??`
* Instructs a quantifier to use a "lazy strategy" for making choices. Instead of the "greedy strategy".
* Match as little as possible before giving control to the next expression part.
* Still defers to overall match.
* Not necessarily faster or slower.
*  `/.*?[0-9]+/`, which would match "Page 266".
	* The `?` was added here, so the repetition should be lazy.
	* Therefore the wildcard happens at the start of the string.
	* Once it gets to `2`, it says "can I give up yet"?
		* That is this part of the expression: `.*?[0-9]`
	* However, it does not give up and switches to `+/`, so therefore it goes through the numbers of "66" 
* Thus all of the above matches "Page 266".
* Another example is `/.*?[0-9]+?/` while trying to match "Page 266"
	* It would only return "Page 2"
* Another example is `/\d+\w+\d+/` which finds "01_FY_07_report_99"
	* This is a greedy example.
* Then with the `?` with `/\d+\w+?\d+/` would only match "01_FY_07" and nothing else.
	* Tries to give up as quickly as it can, because it is lazy.
* A third example is: `/".+", ".+"/` would match "Milton", "Waddams", "Initech, Inc." (including the commas as well)
	* Whereas `/".+?", ".+?"/` would match "Milton", "Waddams" and "Initech, Inc."