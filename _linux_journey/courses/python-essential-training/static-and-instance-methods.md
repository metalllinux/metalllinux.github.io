---
title: "The split function splits text by space and transforms it into a list"
category: "python-essential-training"
tags: ["python-essential-training", "static", "instance", "methods"]
---

* This is `String Parsing`.
```
class WordSet:
    def __init__(self):
	      self.words = set()
		  
		 def addText(self, text):
		 		 text = self.cleanText(text)
				  # The split function splits text by space and transforms it into a list
				  for word in text.split():
				  		  self.words.add(word)

     # replace is a useful function to replace characters in strings
	   # cleanText has the self instance passed in, however this never actually is used
		 def cleanText(self, text):
		      # The below is called `Chaining Functions`
		 		  text = text.replace('!', '').replace('.', '').replace(',', '').replace('\'', '')
				   # This makes everything lowercase
				   return text.lower()
		  
wordSet = WordSet()

wordSet.addText('Hi, I\'m Howard! Here is a sentence I want to add!')
wordSet.addText('Here is another sentence I want to add.')

print(wordSet.words)
```
* This will output something like this:
```
{'a', 'add', 'another', 'is', 'to'} and so on
```
* If you remove `self` from `def addText(self, text):`, you will receive a `takes 1 positional argument but 2 were given` error. We are still passing the `self` instance into the method, however it only takes one parameter now.
* If you remove `self` from `text = self.cleanText(text)`, this will cause another error, it does not know where it is defined and will produce an error.
	* To fix that, we can use `	text = WordSet.cleanText(text)`
* For `cleanText`, this is what is known as a static method:
```
def cleanText(text):
		 		  text = text.replace('!', '').replace('.', '').replace(',', '').replace('\'', '')
				   return text.lower()
```
* Programmers call these static methods, in the sense that they are unchanging.
	* Traditionally, static methods are used to hold constants, unchanging variables, fundamental business logic and so on.
* Methods such as `addText` are `Instance Methods`.
	* They are methods that belong to a particular instance of a class.
* So you haved `Static Methods` like `def cleanText(text):` and `Instance Methods` such as `addText`
* In addition to static methods, there are also Static Attributes. The `legs` attribute on the dog class for example.
	* It is part of the Class Definition, as opposed to being associated with a particular class instance. To example:
```
class WordSet:
    # This will control which punctuation is replaced
    replacePuncs = ['!', '.', ',', '\']
    def __init__(self):
	      self.words = set()
		  
		 def addText(self, text):
		 		 text = self.cleanText(text)
				  # The split function splits text by space and transforms it into a list
				  for word in text.split():
				  		  self.words.add(word)

     # replace is a useful function to replace characters in strings
	   # cleanText has the self instance passed in, however this never actually is used
		 def cleanText(self, text):
		      # The below is called `Chaining Functions`
		 		  text = text.replace('!', '').replace('.', '').replace(',', '').replace('\'', '')
				   # This makes everything lowercase
				   return text.lower()
		  
wordSet = WordSet()

wordSet.addText('Hi, I\'m Howard! Here is a sentence I want to add!')
wordSet.addText('Here is another sentence I want to add.')

print(wordSet.words)
```
* A different version an be done here:
```
class WordSet:
    # This will control which punctuation is replaced
    replacePuncs = ['!', '.', ',', '\']
    def __init__(self):
	      self.words = set()
		  
		 def addText(self, text):
		 		 text = self.cleanText(text)
				  # The split function splits text by space and transforms it into a list
				  for word in text.split():
				  		  self.words.add(word)

     # replace is a useful function to replace characters in strings
	   # cleanText has the self instance passed in, however this never actually is used
		 def cleanText(self, text):
		       # The below is called `Chaining Functions`
						for punc in WordSet.replacePuncs:
								 text = text.replace(punc, '')
					 # This makes everything lowercase
				   return text.lower()
		  
wordSet = WordSet()

wordSet.addText('Hi, I\'m Howard! Here is a sentence I want to add!')
wordSet.addText('Here is another sentence I want to add.')

print(wordSet.words)
```
* With Static Variables, we have the option to use `WordSet` or `self` just under where it says `def cleanText`
* Decorators - annotations or descriptions of your function definitions.
	* They define special attributes about the function, so that Python knows how to handle the function.
```
class WordSet:
    # This will control which punctuation is replaced
    replacePuncs = ['!', '.', ',', '\']
    def __init__(self):
	      self.words = set()
		  
		 def addText(self, text):
		      # Now that we have used the decorator below, we can set text to equal `text = self.~~~~` 
		 		 text = self.cleanText(text)
				  # The split function splits text by space and transforms it into a list
				  for word in text.split():
				  		  self.words.add(word)

     # Below is an example of a decorator. We have explicitly told Python here that cleanText is a static method and that `self` should not be passed in as an argument
	   @staticmethod
		 def cleanText(self, text):
		       # The below is called `Chaining Functions`
						for punc in WordSet.replacePuncs:
								 text = text.replace(punc, '')
					 # This makes everything lowercase
				   return text.lower()
		  
wordSet = WordSet()

wordSet.addText('Hi, I\'m Howard! Here is a sentence I want to add!')
wordSet.addText('Here is another sentence I want to add.')

print(wordSet.words)
```
* For writing code in Python, it is good to have your own style.