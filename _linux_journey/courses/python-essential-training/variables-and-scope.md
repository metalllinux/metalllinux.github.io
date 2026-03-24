---
title: "Variables And Scope"
category: "python-essential-training"
tags: ["python-essential-training", "variables", "scope"]
---

* There is another way to get all of the variables without using `*args` or `*kwargs` at all.
	* We can do that using the `locals()` function.
* For example:
```
def performOperation(num1, num2, operation='sum'):
		 print(locals())
performOperation(1, 2, operation='multiply')
```
* The output will be a dictionary of all of the variables that have been passed in, doesn't matter if they are positional arguments or keyword arguments:
```
{'num1': 1, 'num2': 2, 'operation': 'multiply'}
```
* The fuction is called `locals`, because the variable names are available inside the function.
* In Python, we usually talk about 'local variables' (things that are assigned within the function).
* Global variables - things that are assigned outside of the function in the main body of the code.
	* There is a built-in Python function called `globals` which provides these variables.
* Example of the `globals()` function is below:
```
# Shows all the globally available variables in the program
globals()
```
* When you're talking about which variables that you have access to in a particular line of code, that is called `the scope`.
	* Terminology is `global variable scope` ,  `local variable scope` or the scope of variables within a function.
* To check how global and local variables interact each other, we can use the following function:
```
message = 'Some global data'

# Each functions has its own variable scope
# They also have access to the global variables as well
def function1(varA, varB):
     print(message)
     print(locals())
	 
def function2(varC, varB):
     print(message)
		 print(locals())
		 
function1(1, 2)
function2(3, 4)
```
* What if `varA` is defined in the global scope.
```
message = 'Some global data'
varA = 2
# Each functions has its own variable scope
# They also have access to the global variables as well
def function1(varA, varB):
     print(varA)
	   print(message)
     print(locals())
	 
def function2(varC, varB):
     print(varA)
	   print(message)
		 print(locals())
		 
function1(1, 2)
function2(3, 4)
```
* You will receive an output of:
```
1
Some global data
{'varA': 1, 'varB': 2}
2
Some global data
{'varC': 3, 'varB': 4}
```
* When Python goe sto look up the data associated with the variable name, it checks the `local scope` first and then if that is not defined, go to the `global scope`
* Can also redefine the message, so that the first function gets its own value for message.
```
message = 'Some global data'
varA = 2
# Each functions has its own variable scope
# They also have access to the global variables as well
def function1(varA, varB):
     # This was added here
		 message = 'Some local data'
     print(varA)
	   print(message)
     print(locals())
	 
def function2(varC, varB):
     print(varA)
	   print(message)
		 print(locals())
		 
function1(1, 2)
function2(3, 4)
```
* We can also declare a function within another function:
```
def function1(varA, varB):
     # This was added here
		 message = 'Some local data'
     print(varA)
	   def inner_function(varA, varB):
	   			print(f'innner_function local scope: {locals()}')
		 
		 inner_function(123, 456)
		 
function(1, 2)
```
* Will output:
```
1
inner_function local scope: {'varA': 123, 'varB': 456}
```
* In the above, we cannot call `inner_function` outside of `function1`.
* Another thing we can do is:
```
def function1(varA, varB):
     # This was added here
		 message = 'Some local data'
     print(varA)
	   def inner_function(varA, varB):
	   			print(f'innner_function local scope: {locals()}')
		 
		 print(locals())
		 inner_function(123, 456)
		 
function(1, 2)
```
* `inner_function` is defined as a variable.