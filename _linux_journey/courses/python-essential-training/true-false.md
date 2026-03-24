---
title: "True False"
category: "python-essential-training"
tags: ["python-essential-training", "true", "false"]
---

* True / False
	* Further aspects are available.
* Casting Booleans
	* Python casts integers to Booleans nicely.
	* `bool(1)` = `True`
	* `bool(0)` = `False`
		* Anything except `0` is cast as `True`, for example `bool(-1)` = `True`
	* Imaginary 1, such as `bool(1j)` = `True`
		* `0` and `float zero` are both false.
			* `bool(0.0` and `bool(0j)`
	* For strings:
		* `bool('True')` = `True`
		* `bool('False')` = `True`
			* An empty string is the only `False` string:
				* `bool('')` = `False`
			* For spaces, these are also `True`, for example `bool(' ')` = `True`
	* For Data Structures, `bool([])` = `False`.
		* If anything is placed inside a Data Structure, this equates to `True`, for example `bool([1,2])`
	* An empty Dictionary is `False` --> `book({})` = `False`
	* For the `None` value that is returned from Functions if you do not provide an explicit return value.
		* `bool(None)` = `False`
	* Why is it important to learn about how booleans are cast in Python? 
		* Booleans aren't usually used directly.
		* Usually checking the Boolean values inside an if statement or a for loop.
			* A common situation for booleans is:
```
myList = [1,2]
if myList:
     print('myList has some values in it!')
```
			* We are casting the value of `myList` to a boolean.
* You can also do this:
```
a = 5
b = 5
if a - b:
    print('a and b are not equal!')
a == b
```
* The above will not print. A has to equal to B.
* Boolean Logic
	* Evaluating a situation as to whether or not to go for a walk:
```
weatherIsNice = False
haveUmbrella = True

if not haveUmbrella or weatherIsNice:
    print('Stay inside')
else:
    print('Go for a walk')
```
* The above outputs `Go for a walk`.
* Python evaluates Booleans left to right.
* To do the same Boolean logic as above, we can do the following:
```
weatherIsNice = True
haveUmbrella = False

if not haveUmbrella and not weatherIsNice:
    print('Stay inside')
else:
    print('Go for a walk')
```
* Can also place parenthesis around lines for readability.
```
weatherIsNice = True
haveUmbrella = False

if (not haveUmbrella) and (not weatherIsNice):
    print('Stay inside')
else:
    print('Go for a walk')
```
* Can also flip the order of statement for readability.
```
weatherIsNice = True
haveUmbrella = False

if haveUmbrella or weatherIsNice):
    print('Go for a walk')
else:
    print('Stay inside')
```