---
title: "Errors And Exceptions"
category: "python-essential-training"
tags: ["python-essential-training", "errors", "exceptions"]
---

* Dividing something by zero, for example `1/0` will provide the output `division by zero`.
* Errors and Exceptions are the same thing.
	* All of these errors and exceptions extend a class called the `base exception`.
		* For example the `division by zero` error extends the arithmetic error, which extends the exception, which extends the base exception. The `base` exceptions gives us useful and powerful properties of exceptions.
			* It halts the execution of the code and provides you reasons on why it was halted.
* In an error, the error will point to the line number with an arrow, for example:  `----> 1 1/0`.
	* The entire error output that you see is called a `stack trace`.
		* These are nested operations and provide ways to debug the program.
* Useful stack trace example:
```
def causeError():
		 return 1/0
		 
def callCauseError():
		 return causeError()
		 
callCauseError()
```
* A useful way to catch an exception is via a `try/except` statement.
```
try:
	  1/0
# We are catching the exception here
except Exception as e:
		print(type(e))

causeError()
```
* This will output:
```
<class 'ZeroDivisionError'>
```
* We see from the above that the exception has been caught and is not being raised anymore.
	* It is just a class, has attributes and can even be returned.
* Exceptions when used correctly are like a secondary layer of code.