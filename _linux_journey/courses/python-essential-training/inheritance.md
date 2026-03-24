---
title: "Inheritance"
category: "python-essential-training"
tags: ["python-essential-training", "inheritance"]
---

* A class can extend another class.
* The original class is called the `parent` class and the class extending it is called the `child` class.
	* The `child` class inherits all of the `parent` classes' methods and attributes.
* Inheritance happens automatically when the child class is created.
```
class Dog:
	   _legs = 4
    def __init__(self, name):
        self.name = name
		
		def speak(self):
		    print(self.name + ' says: Bark!')

		def getLegs(self):
				 return self._legs
				 
# The parenthesis are used after the class name, to indicate the parent dog class is being extended
class Chihuahua(Dog):
```
* Use the above to make a chihuahua class. Then if we want to test this:
```
dog = Chihuahua('Bob')
dog.speak()
```
* This will then output:
```
Roxy says: Bark!
```
* To add further changes, we can do:
```
class Dog:
	   _legs = 4
    def __init__(self, name):
        self.name = name
		
		def speak(self):
		    print(self.name + ' says: Bark!')

		def getLegs(self):
				 return self._legs
				 
class Chihuahua(Dog):
		def speak(self):
				 print(f'{self.name} says: Yap yap yap!')
```
* This will then output instead:
```
Roxy says: Yap yap yap!
```
* If the `child` class `Chihuahua`  defines any attributes or methods that conflict with the `parent` class, the `parent` class' are overwritten and the `child`'s are used instead.
* To further add, we can do:
```
myDog = Dog('Rover')
myDog.speak()
```
* The output will still be:
```
Roxy says: Bark!
```
* We can also add additional methods to the `child` class.
* We can do this:
```
class Dog:
	   _legs = 4
    def __init__(self, name):
        self.name = name
		
		def speak(self):
		    print(self.name + ' says: Bark!')

		def getLegs(self):
				 return self._legs
				 
class Chihuahua(Dog):
		def speak(self):
				 print(f'{self.name} says: Yap yap yap!')

		def wagTail(self):
			  print('Vigorous wagging!')
```
* Then we do:
```
myDog = Dog('Rover')
myDog.speak()
dog.wagTail()
```
* Extending built-in classes in Python:
* You can instantiate a new list by calling it like:
```
# In this case, `list()` is an actual class
myList = list()
```
* If we want to make a list, that guarantees that all items appended to it are unique, we do:
	* We can extend the `list()` class and make our own unique list class:
```
# The below overrides the append function
class UniqueList(list):
		 def append(self, item): 
		     if item in self:
			       return
				  self.append(item)
```
* If we just run `self.append(item)` in the above, this will cause `infinite recursion` or a never ending loop. We need to call `append` in the `parent` class (the original list class).
* In that case, we can use a function called `super`, which gets the underlying instance of the `parent` class:
```
# The below overrides the append function
class UniqueList(list):
		 def append(self, item): 
		     if item in self:
			       return
				  super().append(item)

# Here we are creating a list
uniqueList = UniqueList()
uniqueList.append(1)
uniqueList.append(1)
uniqueList.append(2)

print(uniqueList)
```
* This will output:
```
[1, 2]
```
* The `super` function is also used in a constructor.
* For example to add an attirbute to the `child` class instance, we use:
```
# The below overrides the append function
class UniqueList(list):
		 
		 # We are overwritting the constructor in the parent class. We can solve this by using super again. Make sure that the parent constructor gets called first and then we can add the new property
		 def __init__(self):
		      super().__init__()
		 			self.someProperty = 'Unique List!'
		 
		 def append(self, item): 
		     if item in self:
			       return
				  super().append(item)

# Here we are creating a list
uniqueList = UniqueList()
uniqueList.append(1)
uniqueList.append(1)
uniqueList.append(2)

print(uniqueList.someProperty)
```
* This will output:
```
Unique List!
```