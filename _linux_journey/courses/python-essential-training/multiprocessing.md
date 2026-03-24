---
title: "Multiprocessing"
category: "python-essential-training"
tags: ["python-essential-training", "multiprocessing"]
---

* How do we write a program to start, stop and manage running multiple programs in unison.
* We have to use the module `multiprocessing`.
```
from multiprocessing import Process
```
* To keep in mind about using the official Python multiprocessing module. On some OS', you can't use this to start a new process that runs a function, if that function is defined in the same file, as opposed to being imported at the top, for example at the top of the program with `import myFunction`
	* To solve that issue, there is a third party module called `multiprocess`, which can be installed with `pip install multiprocess`
		* `multiprocess` has all of the same functions and can be used in the same way as `multiprocessing`, however it does not care where the function is defined. 
```
from multiprocess import Process
import time
```
* Very simlar to the previously used `thread` class. We have copied the following and changed to `Process` instead.
```
from multiprocess import Process
import time

def longSquare(num):
		 time.sleep(1)
		 return[num] = num**2

results = {}
p1 = Process(target=longSquare, args=(1,))
p2 = Process(target=longSquare, args=(2,))

p1.start()
p2.start()

p1.join()
p2.join()

print(results)
```
* If you run the above, it will produce `{}` and there will be no results.
	* Processes do not share memory. They get a copy of the directory in their own separate memory space. We cannot access it.
		* They can only access it if it is recorded somewhere like a file or database.
			* We can also print the computed value from within the function itself.
				* We then run this version instead:
```
def longSquare(num):
		 time.sleep(1)
		 print(num**2)
		 print('Finished computing!')

results = {}
p1 = Process(target=longSquare, args=(1,))
p2 = Process(target=longSquare, args=(2,))

p1.start()
p2.start()

p1.join()
p2.join()

print(results)
```
* If we run this again with the `print(num**2)`, we receive the output of `14`.
* What if we expand this further to 10 processes:
 ```
from multiprocess import Process
import time
 
def longSquare(num):
		 time.sleep(1)
		 print(num**2)
		 print('Finished computing!')

results = {}
processes = [Process(target=longSquare, args=(n,results)) for n in range(0, 10)]
[p.start() for p in processes]
[p.join() for p in processes]

print(results)
```
* You would receive an output similar to:
```
01
4
9
Finished computer! Finished computing!16
etc
```
* To better tidy this up:
```
from multiprocess import Process
import time
import threading

def longSquare(num):
		 time.sleep(1)
		 print(num**2)
		 print('Finished computing!')

results = {}
p1 = Process(target=longSquare, args=(1,))
p2 = Process(target=longSquare, args=(2,))

p1.start()
p2.start()

p1.join()
p2.join()

print(results)

results = {}

threads = [threading.Thread(target=longSquare, args=(n, results)) for n in range(0, 10)]
[t.start() for t in threads]
[t.join() for t in threads]

print(results)
```
* The output would look much cleaner, for example:
```
91634534534
Finished computing!
14

Finished computing!

Finished computing!
```
* Threads and processes are usually about computing things in parallel.
	* With processors, you are wanting to run multiple processes in parallel.
* With Threads however, the same processor will execute a statement from `thread A`, `thread B`, `thread C` and `thread A` again.
	* These are picked up in a round-robin fashion.
		* The processor will go to a different thread, if one is waiting for whatever reason.
			* `time.sleep` would be a good reason.
* Threading emulates parallel computing.
	* Useful when your programs have periods of downtime.
* 