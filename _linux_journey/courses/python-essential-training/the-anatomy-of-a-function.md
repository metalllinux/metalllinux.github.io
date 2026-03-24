---
title: "This takes in two numbers and an operation (either string sum or string multiply) and returns a result"
category: "python-essential-training"
tags: ["python-essential-training", "anatomy", "function"]
---

* It is not just a linear set of instructions the program has to follow.
	* They must also think of systems, tasks, objects and interacting components.
* The basic unit of a program is not an instruction, but a function.
* Functions have a name and some parameters, as indicated by the `def` statement.
```
# This takes in two numbers and an operation (either string sum or string multiply) and returns a result
def performOperation(num1, num2, operation):
    if operation == 'sum':
	       return num1 + num2
		 if operation == 'multiply':
		     return num1 * num2

performOperation(2, 3, 'sum')
```
* The output would be `5`
* What if we want to add the parameters together, but we don't wan tto write `sum` all the time.
	* A default value can be provided, which is called `name parameters` or `keyword arguments`. An example would be:
```
# This takes in two numbers and an operation (either string sum or string multiply) and returns a result
def performOperation(num1, num2, operation='sum'):
    if operation == 'sum':
	       return num1 + num2
		 if operation == 'multiply':
		     return num1 * num2

performOperation(2, 3)
```
* We still get the same output of `5`
* We can provide our own value with:
```
# This takes in two numbers and an operation (either string sum or string multiply) and returns a result
def performOperation(num1, num2, operation='sum'):
    if operation == 'sum':
	       return num1 + num2
		 if operation == 'multiply':
		     return num1 * num2

performOperation(2, 3, operation='multiply')
```
* The `multiply` above override the `sum` and produces the output of `6`.
* Can also just pass in as the third parameter with:
```
# This takes in two numbers and an operation (either string sum or string multiply) and returns a result
def performOperation(num1, num2, operation='sum'):
    if operation == 'sum':
	       return num1 + num2
		 if operation == 'multiply':
		     return num1 * num2

performOperation(2, 3, 'multiply')
```
* However it is easier and more readable to do:
`operation='multiply'`
* Can also do:
```
# This takes in two numbers and an operation (either string sum or string multiply) and returns a result
def performOperation(num1, num2, operation='sum', message='Default message'):
    print(message)
    if operation == 'sum':
	       return num1 + num2
		 if operation == 'multiply':
		     return num1 * num2

performOperation(2, 3, message='A new message!', operation='multiply')
```
* In the above, we can call `message` before or after the `operation`.
* One rule is that `keyword arguments` must come after positional arguments.
	* Afterwards, keyword arguments can be in any order.
		* Anticipate however all the variatbles the user might be passing in.
* Using `*args`
```
def performOperation(*args):
    print(args)

performOperation(1,2,3)
```
* The above will output:
```
(1, 2, 3)
```
* The `*` at the beginning of `args` tells Python that the `args` is just a reference and has to take input that is passed in.
	* Don't necessarily have to use `args` as the variable name, but it is the Python standard however.
* When it is called, as shown in the output, it is a `Tuple`.
	* It only works for positional arguments, not keyword arguments.
* To handle keyword arguments, we use `**kwargs`.
```
def performOperation(*args, **kwargs):
    print(args)
	  print(kwargs)
performOperation(1,2,3, operation='sum')
```
* This then provides you the output shown below:
```
(1, 2, 3)
{'operation': 'sum'}
```
* keyword arguments are a `dictionary` instead of a `tuple`.
	* This makes sense, because keyword arguments can have keys and values that can be passed in any order and that requires a dictionary to reference them.
* To improve the `performOperation` function further, we use the `math` library.
```
import math
string sum or string multiply) and returns a result
def performOperation(*args, operation='sum'):
    if operation == 'sum':
	       return sum(args)
		 if operation == 'multiply':
		     return math.prod(args)

performOperation(1,2,3, operation='sum')
```
* We get `6` as the output of the above.