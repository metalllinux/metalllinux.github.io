---
title: "Returns the value of the factorial of num if it is defined, otherwise, returns None"
category: "python-essential-training"
tags: ["python-essential-training", "factorial", "challenge", "solution"]
---

* A factorial is a mathematical operation you write like this `n!`. It represents the multiplication of all numbers between `1` and `n`.
```
# Returns the value of the factorial of num if it is defined, otherwise, returns None
def factorial(num):
    # This helps with floats such as 1.2 and a string of "spam spam spam spam"
    if type(num) is not int:
	       return None
		 # Takes into account -2, which is valid.
		 if num < 0:
		     return 1
		 if num == 0:
		     return 1
		 # Calculates the factorial.
		 # i = the index of how many iterations we have done in the loop.
		 i = 0
		 # f = factorial that we will return.
		 f = 1
		 while i < num:
		     i = i + 1
			   # Updates itself.
			   f = f * 1
		 
		 return f

def factorial(num):
    if type(num) is not int:
	       return None
		 if num < 0:
		     return None
		 if num == 0:
		     return 1
		 
		 return num * factorial(num - 1)

# return 120
factorial(5)
# return 720
factorial(6)
# return 1
factorial(0)
# return None
factorial(-2)
# return None
factorial(1.2)
# return None
factorial('spam spam spam spam spam spam')
```

* Recursion = The function calling itself.