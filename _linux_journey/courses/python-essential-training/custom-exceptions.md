---
title: "Nothing needs to be defined for this class. This is because it inherits the constructor of the `Exception` class that it is extending."
category: "python-essential-training"
tags: ["python-essential-training", "custom", "exceptions"]
---

```
class customException(Exception):
    # Nothing needs to be defined for this class. This is because it inherits the constructor of the `Exception` class that it is extending.
		 pass
```
* We can write a function that raises the new custom exception:
```
class customException(Exception):
		 pass

def causeError():
		raise CustomException('You called the causeError function!')
		
causeError()
```
* Custom exceptions are usually lighweight classes, with very little special attributes, methods and so on.
* An example of writing an HTTP exception with a static staus code:
```
class httpException(Exception):
		 statusCode = None
		 messages = None
		 # We overrite the parent constructor below:
		 def __init__(self):
		 		 super().__init__(f'Status code: {self.statusCode} and message is: {self.message}')
				 
# Then we need a few child classes that extend the HTTP exception:
class NotFound(HttpException): 
	  statusCode = 404
	  message = 'Resource not found'

class ServerError(HttpException):
		statusCode = 500
		message = 'Server is down'
		
def raiseServerError():
		raise ServerError()

raiseServerError()
```
* These custom exceptions help keep code organised, are great at documenting issues and what caused them. 
* They help separate common excepted error from issues that require a developer's attention.
* 