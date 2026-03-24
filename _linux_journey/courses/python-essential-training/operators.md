---
title: "Operators"
category: "python-essential-training"
tags: ["python-essential-training", "operators"]
---

* These perform operations on variables and values.
	* Variables are the data and operators are the instructions.
* Arithmetic Operator
	* `1 + 1` = `2`
	* `4 * 5` = `20`
	* exponent: `5 ** 2`
		* The above is 5 raised to the power of 2, which is `25`.
	* Division is with `20 / 5` = `4.0`
		* Always will return a float value, 
	* Modulus Operator.
		* Provides the remainder after any division.
			* For example, if we do `20 % 6`, we receive `2` back.
				* 20/6 = 18 with a remainder of 2!
* Arithmetic Operators with Strings
	* String concatenation --> `'string 1' + 'string 2'` = `string 1 string 2` and this sticks them together.
	* Can also do string multiplication:
		* `'- string 1 - ' * 4` = `'- string 1 - - string 1 - - string 1 - - string 1 -'`
		* `'1' + 4` will not work however.
* Comparison Operators
	* They evaluate two variables/values and produce a Boolean --> true or false.
	* `True == True` = `True`
	* `4 < 5`  = `True`
	* `5 <= 5` = `True`
	* `5 > 2` = `True`
	* `5 >= 2` = `True`
* Logical Operators (and, or, not)
	* `True and True` = `True`
	* `True and False` = `False`
	* `True or False` = `True`
	* `False or False` = `False`
	* `not True` = `False`
	* `not False` = `True`
* Membership Operators
	* `1 in [1,2,3,4,5]` = `True`
	* `10 in [1,2,3,4,5]` = `False`
	* `10 not in [1,2,3,4,5]` = `True`
	* `'cat' in 'my pet cat'` = `True`. Also be careful, because the word `cat` is in `catatonic`
	* `'cat' not in 'my pet cat'` = `False`