---
title: "Functions"
category: "python-essential-training"
tags: ["python-essential-training", "functions"]
---

* `print` is a function.
	* Parenthesis are where you place your `arguments` inside of them.
	* Have to start with a lowercase letter, cannot start with a number.
* `def` is for definition.
```
def multiplyByThree(val):
    return 3 * val

multiplyByThree(4)
```
* keyword here is `return`
	* In the above, we are returning 3 times the value that we passed into the function.
	* Can call the function by running `multipleByThree(4)`. The output is:
`12`
* Can change this and make a function with two arguments:
```
def multiply(val1, val2):
    return val1 * val2
multiply(3, 4)
```
The returned value from above is `12`.
* Functions don't always have to return something.
	* Can make a function that mutates or changes a value.
```
a = [1,2,3]

def appendFour(myList)
    myList.append(4)
	
appendFour(a)
print(a)
```
* Running the above function then outputs:
[1, 2, 3, 4]
* Bread going into the toaster and leaving it there for someone to collect later.
* To print the back the returned value of the print function:
```
print(print('Hello, World!'))
```
* This would output:
```
Hello, World!
None
```
* `None` is a special Python keyword like `Null` it represents the absense of value. It has its own type, called `NoneType`.
	* Be careful using none.
* `None + 1` does not work.