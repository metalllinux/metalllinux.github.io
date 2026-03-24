---
title: "Returns the square of `num`"
category: "python-essential-training"
tags: ["python-essential-training", "multithreading"]
---

* Need to import the `threading` and `time` modules.
* Example --> Create a function that calculates the square of a number, but takes a long time to do it:
```
import threading
import time

def longSquare(num):
		 time.sleep(1)
		 # Returns the square of `num`
		 return num**2

[longSquare(n) for n in range(0, 5)]
```
* The above would output:
```
[0, 1, 4, 9, 16]
```
* Another example is waiting to fetch data back from a remote server.
```
import threading
import time

def longSquare(num):
		 time.sleep(1)
		 # Returns the square of `num`
		 return num**2

[longSquare(n) for n in range(0, 5)]

# The word `target` is used to describe the target function. `args` are the arguments we pass to the function
# A `,` is placed after the 1 and 2, to show Python it is a Tuple and not a random variable with parenthesis around it. If you only have one value in the tuple, sometimes that is necessary
t1 = threading.Thread(target=longSquare, args=(1,))
t2 = threading.Thread(target=longSquare, args=(2,))

# Both of the threads now need to be started with the following functions:
t1.start()
t2.start()

# They are both joined together with `join`. The join function checks to see if the thread has completed execution yet. It then pauses until execution is completed. 
t1.join()
t2.join()

# The return value of the function is not available in the threads.

```
* To better receive the output, we can do:
```
import threading
import time

def longSquare(num):
		 time.sleep(1)
		 # This adds the result to the dictionary
		 results[num] = num**2

[longSquare(n) for n in range(0, 5)]

# We need a dictionary to handle the output:

results = {}
t1 = threading.Thread(target=longSquare, args=(1,results))
t2 = threading.Thread(target=longSquare, args=(2,results))

t1.start()
t2.start()

t1.join()
t2.join()

# The return value of the function is not available in the threads.

print(results)
```
* You will then see the output of:
```
{2: 4, 1: 1}
```
* Threads share memory and can modify the same object.
* A common pattern is to place all above thread configuration into a list.
```
def longSquare(num):
		 time.sleep(1)
		 # This adds the result to the dictionary
		 results[num] = num**2
		 
results = {}
# Runs the command on X amount of threads (in this case 10)
threads = [threading.Thread(target=longSquare, args=(n, results)) for n in range(0, 10)]
[t.start() for t in threads]
[t.join() for t in threads]
print(results)
```