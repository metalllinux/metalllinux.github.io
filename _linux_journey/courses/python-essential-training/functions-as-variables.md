---
title: "In the case of the function, this information is about required parameters (if any)"
category: "python-essential-training"
tags: ["python-essential-training", "functions", "variables"]
---

* Variables have a name and data associated with them.
* `x = 5`
* Functions have a function name and data associated with them:
```
# In the case of the function, this information is about required parameters (if any)
def x():
    # And the line of the instruction that has to be executed
    return
```
* Functions in Python are represented as objects.
* We can see this with the `__code__` attribute of Python function objects.
* As an example. we can do:
```
print(x.__code__.co_varnames)
print(x.__code__.co_code)
```
* This prints out:
```
# This is the variable name (in this case nothing is given in the above function)
()
# This is a Python byte object of all of the lines of code in the function
b'd\x01S\x00'
```
* You won't especially need this.
* Functions are not anything special in Python - just variables associated with some data.
* To demonstrate this, we can do:
```
    def lowercase(text):
	      # Makes the text all lowercase
        return text.lower()
    
    def removePunctuation(text):
	      # This removes any punctuation
        punctuations = ['.', '-', ',', '*']
        for punctuation in punctuations:
            text = text.replace(punctuation, '')
        return text
    
    def removeNewlines(text):
	      # Removes any newline characters
        text = text.replace('\', ' ')
        return text
    
    def removeShortWords(text):
	      # Removes words if the word length is 3 or less
        return ' '.join([word for word in text.split() if len(word) > 3])
    
    def removeLongWords(text):
	      # Removes any long words as well
        return ' '.join([word for word in text.split() if len(word) < 6])

```
* We can mix and match the functions, by calling them in a list.
```
processingFunctions = [lowercase, removePunctuation, removeNewlines]

for fun in processingFunctions:
    text = func(text)
	
print(text)
```
* The above allows us to go through the text and remove characters using any of the above functions.
* The final processing function you will encounter is the `Lambda Function`.
	* Not every piece of data needs a variable name.
	* You can do the same with functions as well and they are called `Lambda Functions`.
		* From the Greek letter Lambda.
* To define a small function without a variable name, use:
```
(lambda x: x + 3)(5)
```
* The output will be: `8`
* No multiline functions with Lambda functions.
* Don't need to type `return`, as this is automatically assumed.
	* `implied return` as it is known as.
		* Comes in handy for Python functions that take in a list of arguments.
* For example, sorting a list of values.
```
myList = [5,4,3,2]
sorted(myList)
```
* Will output the following:
```
[2, 3, 4, 5]
```
* Can also pass in a function into the list (for things that don't have an obvious numeric value) and returns the value we should see.
```
myList = [{'num: 3'}, {'num': 2}, {'num': 1}]
sorted(myList, key=lambda x: x['num'])
```
* This will output:
```
[{'num': 1}. {'num': 2}. {'num': 3}]
```
* Convenient and concise way to write mini functions as values (lambda).