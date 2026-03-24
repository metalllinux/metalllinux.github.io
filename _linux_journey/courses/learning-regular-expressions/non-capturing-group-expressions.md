---
title: "Non Capturing Group Expressions"
category: "learning-regular-expressions"
tags: ["learning-regular-expressions", "non", "capturing", "group", "expressions"]
---

* Grouped expressions are automatically captured by default.
	* We can also prevent automatic capturing of group expressions.
	* Useful for groups which are not used for backreferences.
* Frees up storage for other captures.
	* If we have an expression that has a lot of groups, you could potentially end up with more than 9 backreferences.
* If supress capturing the ones we don't need, we can simplify it.
	* May improve the speed of large or complex searches.
* Supported by most regex engines, but not Unix tools.
* Non-capturing was added with PERL Compatible regex.
* To disable capturing for a group, we can perform:
	* `?:` --> Disable capturing for this group.
		* The `?` acts as a modifier for the group.
			* The character after the `?` indicates the type of modification.
			* The `:` tells the regex engine not to capture the group.
* An example is "I like pizza."
	* This can be found with `/I (love|like) (.+)\./` captures "like" and "pizza".
	* The first group is using alternation.
	* If we do `/I (?:love|like) (.+)\./` captures "pizza".
		* It has become a non-capturing group.
* Another example is:
I like pizza.
I love coffe.
* `/I (like|love) (.+)\./` matches both of the above.
* `/I (?:like|love) (.+)\./`makes it a non-capturing group.