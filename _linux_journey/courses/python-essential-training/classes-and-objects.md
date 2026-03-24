---
title: "Classes And Objects"
category: "python-essential-training"
tags: ["python-essential-training", "classes", "objects"]
---

* Similar to having a whole kitchen, toaster, microwave, dish washer, all with different nodes.
* What if we want two separate kitchens with separate appliances.
	* The class deals with this.
* Class names use uppercase letters.
* In the indented line, we define all the functions and attributes that a dog has.
* `__init__` is for initialisation. The function is called, whenever an instance of the class `Dog` is created.
* Two underscores on either side are specially defined by Python.
	* Makes sure the computer recognises `__init__` as the initialisation function.
* `self` is the specific instance of the `Dog` class after it has been initialised.
* `self` is passed to the `speak` function.
	* Then provides you access to any of the attributes or functions under the `def __init__(self)` class.
* `self.name` concatenates the Dogs name with the `' says: Bark!'` string.
* `my_dog = Dog()` , the `my_dog` is equal to a newly created instance of the class `Dog`.
	* When the above is ran, the `__init__` function get called and an instance of the `Dog` class is returned. 
* Remember, variables and functions are lowercase and classes start with an uppercase character.
* Running `my_dog.speak()` will output `Rover says: Bark!`
```
class Dog:
    def __init__(self):
        self.name = 'Rover'
		     self.legs = 4
		
		def speak(self):
		    print(self.name + ' says: Bark!')

my_dog = Dog()
another_dog = Dog()

my_dog.speak()
```
* How to give dogs difference names and provide a name when we initialise the dog.
```
class Dog:
    def __init__(self, name):
        self.name = name
		     self.legs = 4
		
		def speak(self):
		    print(self.name + ' says: Bark!')

my_dog = Dog('Rover')
another_dog = Dog('Fluffy')

my_dog.speak()
```
* Running `my_dog = Dog('Rover')` will output `Rover says: Bark!`
* Running `another_dog = Dog('Fluffy')` will output `Fluffy says: Bark!`
* If use .function syntax such as `.speak()` the class instance of `my_dog` is passed in as a variable.
* Class Instances are also called Objects, hence "Object Oriented Programming".
* Variables inside the classes such as `self.name = name` are called Attributes.
* The functions inside such the below are called Methods (or Class Methods).
```
		def speak(self):
		    print(self.name + ' says: Bark!')
```
* The `Dog` object has the Method `Speak`.