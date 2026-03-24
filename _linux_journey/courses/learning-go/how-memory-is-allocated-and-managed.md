---
title: "How Memory Is Allocated And Managed"
category: "learning-go"
tags: ["learning-go", "memory", "allocated", "managed"]
---

* Go runtime is statically linked to an application.
* When you compile and build a binary Go application, the runtime is included.
* Your application depends on the runtime, which operators in the background in dedicated threads.
* Memory is allocated and de-allocated automatically.
* Collections of `complex` types such as `maps` (key value pairs), you have to initialise them correctly.
* Two built-in functions to be aware of are `make()` and `new()` to initialise `maps`, `slices` and `channels`.
	* You'll use these to initialise the objects.
* **The new() function**
	* Allocates, but does not initialise memory.
	* When you allocate an object using the `new()` function, you'll get back a memory address indicating the location of the map, the map object itself as zero memory storage. If a key-value pair is added to the map, this will cause an error.
* **The make() function**
	* This allocates and initialises memory.
	* Allocates non-zeroed storage and returns a memory address.
	* The storage is non-zero and is ready to accept values.
* Using `new()` instead of `make()` can cause a crash:
```
// Here the keys are strings and the associated values are integers. The new() function declares that
m := new(map[string]int)
m["theAnswer"] = 42
fmt.Println(m)
```
* The app will then crash like the following:
```
// invalid operation: m["theAnswer"]
// (type *map[string]int does not support indexing)
```
* The error is informing us that it is dealing with a map with zero memory storage and there is no place to put the data. Therefore the application panics and crashes.
* To fix this, use `make()` to allocate and initialise memory.
```
// Here, again we are saying that it contains strings as keys and ints as values. This time however, we are initialising the make() function
m := make(map[string]int)
m["theAnswer"] = 42
fmt.Println(m)
```
* When we try to initialise an entry, it will succeed. When it is output, we receive:
```
map[theAnswer:42]
```
* Whenever you use complex options, it is critical to wrap these in the `make()` function.
	* If your intent is to immediately add data to the object.
* Memory is de-allocated by the garbage collector (GC).
	* This runs in the background and each time it kicks in, it will look for Objects that are out of scope or set to **nil**.
	* That means it can clean out the memory and return that memory to the memory pool.
* GC was rebuilt in Go 1.5 for low latency.
	* This reduces the pauses, when we are running our Go applications.
* For more information on Garbage Collection, we can check out the following links:
	* https://golang.org/pkg/runtime
	* Can find further details in the development documentation and in the runtime package.