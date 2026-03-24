---
title: "Other Types Of Numbers"
category: "python-essential-training"
tags: ["python-essential-training", "other", "types", "numbers"]
---

* Useful things you can do with the `int` class in Python.
* If you pass in a number as a string, it will be converted, for example --> `int('100')` = `100`
	* We are casting the string of `100` to the integer of `100`.
* If you pass a second argument as a number, such as `int('100', 2)`, it takes the second argument as the base that the number should be converted from. In this case, the answer is `4`. `100` in base `2` is `4` in base `10`.
	* The first argument has to be a string as well. `int(100, 2)` will throw an error.
		* When converting from one base to base 10, you might have things in the string that aren't numbers.
			* `int('1ab', 16)` is valid in base 16. = `427`
* Floats have a Floating Point Error. For example if you do `1.2 - 1.0` = `0.19999999996`, which is not the expected `0.2`.
	* In the above cases, we use the Decimal Module.
* **All imports stay at the top of your Python code.**
	* `from decimal import Decimal, getcontext`
		* We import the Class `Decimal` and the Function `getcontext`.
		* If you run the function `getcontext()`, it runs the function with a bunch of attributes inside of it.
			* These are the global settings that get applied to your usage of the Decimal class.
			* Can change any of the settings, by running `getcontext().prec=4`
* Can instantiate a Decimal Class with a number value.
	* `Decimal(1) / Decimal(3)` = `Decimal('0.3333')` to 4 places of precision. Running then `getcontext().prec=2` will do `Decimal('0.33')`
		* If a float is passed to the decimal, like `Decimal(3.14)` = `Decimal('3.140002342342')`
			* It is trying to provide the exact float output from above.
				* In that situation, we can do `Decimal('3.14')` as a string.
					* Be wary of small numbers or very large numbers.