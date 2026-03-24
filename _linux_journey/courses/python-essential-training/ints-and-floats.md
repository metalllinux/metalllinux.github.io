---
title: "Ints And Floats"
category: "python-essential-training"
tags: ["python-essential-training", "ints", "floats"]
---

* How to convert between them and the pitfalls to look out for.
* Math with ints --> `20 / 4` = `5.0` and we get a float back.
	* Always returns a float from a division, because there is the potential for non-whole numbers to come back.
* If we add/multiply a float with an int, we get back a float --> `4 + 4.0` = `8.0` or `4 * 4.0` = `16.0`
	* Exponents as well --> `4 ** 4.0` = `256.0`
* To convert a float into an int, we use `int(4 ** 4.0)` = `256`
	* The above is an `int` class and not function. This is a built-in class in Python.
		* `str`, `float`, `list` etc, these are all classes.
* To convert from a float to an int, this process is called `casting`.
	* Casting from the Int 256 in the above example to the Float 256.
* When you cast from a float to an int, Python does not round the numbers, for example `int(8.9)` = `8` or `int(14/3)` = `5`.
* Can also use the `round` function for this, for example `round(14/3)` = `5`.
* We can also specify the number of decimal places we want to round to, for example `round(14/3, 2)` = `4.67`.
* If you do `1.2 - 1.0`, you receive `0.1999999996`
	* Floats are approximations. Only a finite amount of memory to store them.
		* Pythons uses some tricks in approximations and sometimes you see strange rounding errors, such as `14/3` = `4.666666666667`.
			* Good to use `round` here, such as `round(1.2 - 1.0, 2)` = `0.2`