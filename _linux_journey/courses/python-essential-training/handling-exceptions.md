---
title: "Handling Exceptions"
category: "python-essential-training"
tags: ["python-essential-training", "handling", "exceptions"]
---

* If we do not care about the specific instance of an exception
```
def causeError():

try:
	  1/0

except Exception:
		print('There was some error here.')
		
causeError()
```
* If there is an error, it will print out  "There was some error here."
* Using `finally`
```
def causeError():

		try:
			  1/0

		except Exception:
				print('There was some error here.')
		finally:
				print('This will always execute!')

causeError()
```
* That will print out:
```
There was some error here.
This will always execute!
```
* `finally` statements will execute regardless of what happens in the `try` block.
* `except` statements are also not needed.
* `finally` statements are useful for timing how long a function takes to execute.
* We would need to import the `time` class:
```
import time

def causeError():
		# This is done in "seconds"
		start = time.time()
		try:
				# Pauses execution for x number of seconds
				time.sleep(0.5)
			  1/0
		except Exception:
				print('There was some error here.')
		finally:
				print(f'Function took {time.time() - start} seconds to execute')

causeError()
```
* Running the above will then show `Function took X seconds to execute`
* The `try` and `finally` statement patterns help keep the code clean and compact.
* Catching Exceptions by Type:
```
def causeError():

		try:
			  return 1/0
		except ZeroDivisionError:
				print('There was a zero division error!')
		except Exception:
				print('There was some error here.')

causeError()
```
* The above would print out:
	* `There was a zero division error!`
```
def causeError():

		try:
				# This would cause a type error
			  return 1 + 'a'
		except TypeError:
				print('There was a type error!')
		except ZeroDivisionError:
				print('There was a zero division error!')
		except Exception:
				print('There was some error here.')

causeError()
```
* The order of the `except` statements does matter.
	* If Python matches the first one, it will then not bother with the others.
	* You want the more general exceptions lower down. and the more specific sections higher up.
		* This type of error checking is useful for HTTP request response handling. 
* To make the above code easier, you can place it into a single function and use a customer decorator.
* Customer decorators:
```
def handleException(func):
		 # Need to pass the variable `args` to the function
		 def wrapper(*args):
		 		 try:
				 		  func()	
		except TypeError:
				print('There was a type error!')
		except ZeroDivisionError:
				print('There was a zero division error!')
		except Exception:
				print('There was some error here.')
		return wrapper
		
#handleException
def causeError():
		return 1/0
		
causeError()
```
* The about will output:
```
There was a zero division error!
```
* Raising Exceptions:
```
#handleException
def raiseError():
		 raise Exception()

raiseError()
```
* The `raise` statement `raises` or `throws` the new exception that is created once reached. 
* As an example, we can turn it into any function that excepts the number zero:
```
#handleException
def raiseError(n):
		 if n == 0:
		 		 raise Exception()
			print(n)

# We get an error if the argument below is `0`, otherwise it just prints out the value presented
raiseError(1)
```
* No `else` statement is needed in the above example, because once you get to the `raise` statement, the program is halted and the `print` statement is never reached.
* 