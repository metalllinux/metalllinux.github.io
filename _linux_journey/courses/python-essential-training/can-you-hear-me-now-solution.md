---
title: "Can You Hear Me Now Solution"
category: "python-essential-training"
tags: ["python-essential-training", "you", "hear", "now", "solution"]
---

* Write a wrapper function called `getWithRetry`, that attempts to get the output of all of the functions below:  def getData50(), def getData25() and def getData10()
* Sometimes the services are just down and you don't want th function to retry forever.
* The retries are not also free and can take a while for you to have another chance.
* 
* If there is a `none` response, try again.
	* If you receive a string, then `return` the string.
* 
* The `random` function returns a float between zero and 1.
```
    import random,
    import time
    servicesAreUp = True,
    
    def getData50():
        if servicesAreUp and random.random() < 0.5:
            return 'You got the data! That only happens 50% of the time!'
    
    def getData25():
        if servicesAreUp and random.random() < 0.25:
            return 'You got the data! That only happens 25% of the time!'    
    
    def getData10():
        if servicesAreUp and random.random() < 0.1:
            return 'You got the data! That only happens 10% of the time!'

# Your code here!,
def getWithRetry(dataFunc):
＃ Only a maximum amount of 20 retries
    maxRetries = 20
# The for loop loops through from 0 to the maximum retries of 20. An underscore is used as the variable name here. In Python, this is often done to indicate that the variable isn't being used. Instead of defining a variable that we will not use, the underscore just stands in for that variable.
    for _ in range(0, maxRetries):
			  # Then we receive the response
        response = dataFunc()
		    # We check if it is valid
        if response:
		    # Then we return the response after that
            return response

```
* Another way to do it is via `recursion`
```
    def getWithRetry(dataFunc, retries=20):
        if retries == 0:
            return 'THE SERVICE IS DOWN!'
			   # If dataFunc returns a non-string, it is going to return it and it won't evaluate the other side with getWithRetry. That is the power of the "or" statement. dataFunc() evalues to None, it does the other side of the "or" statement. Then goes back up the block to try again.
        return dataFunc() or getWithRetry(dataFunc, retries-1)

# Should return 'You got the data! That only happens 50% of the time!'
getWithRetry(getData50)

# Should return 'You got the data! That only happens 25% of the time!'
getWithRetry(getData25)

# Should return 'You got the data! That only happens 10% of the time!'
getWithRetry(getData10)


```
