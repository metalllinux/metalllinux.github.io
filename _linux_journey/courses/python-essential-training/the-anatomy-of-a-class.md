---
title: "This has two instance attributes: 'name' and 'legs'. They are called instance attributes, because they are attributres of each instance that a dog class has"
category: "python-essential-training"
tags: ["python-essential-training", "anatomy", "class"]
---

* Guido van Rossum (creator of Python)
* Previous class that was made:
```
class Dog:
    def __init__(self):
				# This has two instance attributes: 'name' and 'legs'. They are called instance attributes, because they are attributres of each instance that a dog class has
        self.name = 'Rover'
		     self.legs = 4
		
		def speak(self):
		    print(self.name + ' says: Bark!')
			
# To make a new instance, we can use:
myDog = Dog('Rover')
print(myDog.name)
print(myDog.legs)
```
* The above will output:
```
Rover
4
```
* We are unable to see the value for example: `self.legs = 4`
* If you call `Dog.legs`, that will cause a error.
* We can make `legs` an attribute of the class itself:
```
class Dog:
		 # This is called a `Static Attribute` or `Static Variable`
	   legs = 4
		# We can make `legs` a class, by moving it outside of the initialisation function (or constructor) as it is known
    def __init__(self):
				# This has two instance attributes: 'name' and 'legs'. They are called instance attributes, because they are attributres of each instance that a dog class has
        self.name = 'Rover'
		
		def speak(self):
		    print(self.name + ' says: Bark!')
			
# To make a new instance, we can use:
myDog = Dog('Rover')
print(myDog.name)
print(myDog.legs)
```
* You will then receive the same output as below:
```
Rover
4
```
* However, if you then call:
```
Dog.legs
```
* The output for that will be `4`.
* Traditionally, static variables are used to hold constants and fundamental business logic.
	* Be careful however, because just like any variable, this can be reset on the class, for example `Dog.legs = 3`
* If we then make a new dog:
```
Dog.legs = 3
myDog = Dog('Rover')
print(myDog.name)
print(myDog.legs)
```
* You will then receive the output of:
```
Rover
3
```
* The convention to make sure the variable is not changed, is to add an `underscore` before the variable name.
```
_egs = 4
```
*  is an indicator/warning - mess with this at your own risk, because you can break things accidentally.
* Another connotation is that the user should rely on or use the values directly.
	* These private variables are implementation details - subject to change without notice.
		* In that case, we can use a `getter function`:
```
class Dog:
	   _legs = 4
    def __init__(self):
        self.name = 'Rover'
		# The below is a `getter method`. They always start with get
		def getLegs(self):
				 return self._legs
		
		def speak(self):
		    print(self.name + ' says: Bark!')
			
myDog = Dog('Rover')
print(myDog.name)
print(myDog.getLegs())
```
* Output will be:
```
Rover
4
```
* We don't necessariily have to pass the `self` attribute into the `getter` function.
	* `self` is an object instance that we are calling the function on.
		* `self` is `myDog` --> Same value.
* `_legs` however is a static variable in the class. We can rewrite `getLegs` as the following:
```
class Dog:
	   _egs = 4
    def __init__(self):
        self.name = 'Rover'
		# The below is a `getter method`. They always start with get
		def getLegs():
				 return Dog._legs
		
		def speak(self):
		    print(self.name + ' says: Bark!')
			
myDog = Dog('Rover')
print(myDog.name)
print(myDog.getLegs())
```
* The above will cause an error, because when we call a method on a class instance, such as `myDog.getLegs()`, the class instance `myDog` gets passed in as the first value. The error will be `takes 0 positional arguments but 1 was given`, because `def getLegs()` is empty.
* The best way to run the program, is like so:
```
class Dog:
	   _egs = 4
    def __init__(self):
        self.name = 'Rover'
		# The below is a `getter method`. They always start with get
		def getLegs(self):
				 return self._legs
		
		def speak(self):
		    print(self.name + ' says: Bark!')
			
myDog = Dog('Rover')
print(myDog.name)
print(myDog.getLegs())
```
* We can also do something like this:
```
myDog = Dog('Rover')
myDog._legs = 3
print(myDog.name)
print(myDog.getLegs())
print(Dog._legs)
```
* We are changing the instance variable, but not the class variable, which remains the same.