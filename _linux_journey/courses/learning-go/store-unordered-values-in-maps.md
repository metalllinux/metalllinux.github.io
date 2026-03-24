---
title: "Store Unordered Values In Maps"
category: "learning-go"
tags: ["learning-go", "store", "unordered", "values", "maps"]
---

* A map is an unordered collection of key-value pairs.
	* i.e. a hash table.
* Allows you to store collections of data and then arbitrarily find items in the collection, based on their keys.
* A map's keys can be any type that can be compared to each other, for the purposes of sorting.
* Pretty common to use strings for keys or any other type.
* An example of this is:
```
package main

import (
		 "fmt"
)

func main() {
			// This is initialised with the make() function
			// The key type is wrapped in brackets and is set to "string". The associated value type is also set to "string".
	   states := make(map[string]string)
	   // Output the value of the map:
	   fmt.Println(states)
}
```
* The output will show that the map is empty:
```
map[]
```
* Then to add items to the map, we do:
```
package main

import (
		 "fmt"
)

func main() {
			// This is initialised with the make() function
			// The key type is wrapped in brackets and is set to "string". The associated value type is also set to "string".
	   states := make(map[string]string)
	   // Output the value of the map:
	   fmt.Println(states)
	   // Items are added here:
	   // The string-based key is "WA"
	   states["WA"] = "Washington"
	   states["OR"] = "Oregon"
	   states["CA"] = "California"
	   fmt.Println(states)
}
```
* Thus the results of the above look like:
```
map[CA:California OR:Oregon WA:Washington]
```
* The contained key-value pairs are shown separated with spaces. Each pair has a `:`.
* To retrieve an item based on its key, we do:
```
package main

import (
		 "fmt"
)

func main() {
			// This is initialised with the make() function
			// The key type is wrapped in brackets and is set to "string". The associated value type is also set to "string".
	   states := make(map[string]string)
	   // Output the value of the map:
	   fmt.Println(states)
	   // Items are added here:
	   // The string-based key is "WA"
	   states["WA"] = "Washington"
	   states["OR"] = "Oregon"
	   states["CA"] = "California"
	   fmt.Println(states)
	   
	   // Retrieving an item based on its key.
	   // The syntax value is "states"
	   california := states["CA"]
	   fmt.Println(california)
}
```
* The result would then be:
```
California
```
* To remove it, we can use a built-in function called "delete":
```
package main

import (
		 "fmt"
)

func main() {
			// This is initialised with the make() function
			// The key type is wrapped in brackets and is set to "string". The associated value type is also set to "string".
	   states := make(map[string]string)
	   // Output the value of the map:
	   fmt.Println(states)
	   // Items are added here:
	   // The string-based key is "WA"
	   states["WA"] = "Washington"
	   states["OR"] = "Oregon"
	   states["CA"] = "California"
	   fmt.Println(states)
	   
	   // Retrieving an item based on its key.
	   // The syntax value is "states"
	   california := states["CA"]
	   fmt.Println(california)

     // Removing an item:
     delete(states, "OR") 
	 	fmt.Println(california)
}
```
* After the delete operation has concluded, `Oregon` will be gone:
```
California
map[CA:California WA:Washington]
```
* New items can be added like the following:
```
package main

import (
		 "fmt"
)

func main() {
			// This is initialised with the make() function
			// The key type is wrapped in brackets and is set to "string". The associated value type is also set to "string".
	   states := make(map[string]string)
	   // Output the value of the map:
	   fmt.Println(states)
	   // Items are added here:
	   // The string-based key is "WA"
	   states["WA"] = "Washington"
	   states["OR"] = "Oregon"
	   states["CA"] = "California"
	   fmt.Println(states)
	   
	   // Retrieving an item based on its key.
	   // The syntax value is "states"
	   california := states["CA"]
	   fmt.Println(california)

     // Removing an item:
     delete(states, "OR") 
	 	fmt.Println(california)
		
		// Adding an item:
		states["NY"] = "New York"
}
```
* Therefore, the output of that would be:
```
map[CA:California NY:New York WA:Washington]
```
* This is an unordered collection, so it will not be the same every time.
* To iterate or loop through a `map`, we can use a `for` statement:
```
package main

import (
		 "fmt"
)

func main() {
			// This is initialised with the make() function
			// The key type is wrapped in brackets and is set to "string". The associated value type is also set to "string".
	   states := make(map[string]string)
	   // Output the value of the map:
	   fmt.Println(states)
	   // Items are added here:
	   // The string-based key is "WA"
	   states["WA"] = "Washington"
	   states["OR"] = "Oregon"
	   states["CA"] = "California"
	   fmt.Println(states)
	   
	   // Retrieving an item based on its key.
	   // The syntax value is "states"
	   california := states["CA"]
	   fmt.Println(california)

     // Removing an item:
     delete(states, "OR") 
	 	fmt.Println(california)
		
		// Adding an item:
		states["NY"] = "New York"
		
		// Iteration through maps can be done with a for loop:
		// "k" stands for "key" and "v" stands for "value"
		// We want to loop through the "states" map
		// Each time through the loop, "k" will be one of the "keys" and "v" is one of the values
		for k, v := range states {
		// %v is used for both the key and the value here
				 fmt.Printf("%v: %v\n", k, v)
		}
}
```
* Running the above will loop through and output each item in the array:
```
WA: Washington
NY: New York
CA: California
```
* The order of iteration is not guaranteed here. 
* If you want to guarantee the order, you have to manage it yourself.
	* For example, to list the States in alphabetical order.
	* To do that, we extract the keys from the map, as a slice of the string's array.
```
package main

import (
		 "fmt"
)

func main() {
			// This is initialised with the make() function
			// The key type is wrapped in brackets and is set to "string". The associated value type is also set to "string".
	   states := make(map[string]string)
	   // Output the value of the map:
	   fmt.Println(states)
	   // Items are added here:
	   // The string-based key is "WA"
	   states["WA"] = "Washington"
	   states["OR"] = "Oregon"
	   states["CA"] = "California"
	   fmt.Println(states)
	   
	   // Retrieving an item based on its key.
	   // The syntax value is "states"
	   california := states["CA"]
	   fmt.Println(california)

     // Removing an item:
     delete(states, "OR") 
	 	fmt.Println(california)
		
		// Adding an item:
		states["NY"] = "New York"
		
		// Iteration through maps can be done with a for loop:
		// "k" stands for "key" and "v" stands for "value"
		// We want to loop through the "states" map
		// Each time through the loop, "k" will be one of the "keys" and "v" is one of the values
		for k, v := range states {
		// %v is used for both the key and the value here
				 fmt.Printf("%v: %v\n", k, v)
		}
		
		// To make it more ordered, we can do the following:
		// We are making this a slice of string values
		// The initial value is the length of the state's variable
		keys := make([]string, len(states))
		// Then we add each key from the map to the slice:
		i := 0
		for k:= range states {
				 keys[i] = k
				 i++
		}
		fmt.Println(keys) 
}
```
* The following is then output:
```
package main

import (
		 "fmt"
		 "sort"
)

func main() {
			// This is initialised with the make() function
			// The key type is wrapped in brackets and is set to "string". The associated value type is also set to "string".
	   states := make(map[string]string)
	   // Output the value of the map:
	   fmt.Println(states)
	   // Items are added here:
	   // The string-based key is "WA"
	   states["WA"] = "Washington"
	   states["OR"] = "Oregon"
	   states["CA"] = "California"
	   fmt.Println(states)
	   
	   // Retrieving an item based on its key.
	   // The syntax value is "states"
	   california := states["CA"]
	   fmt.Println(california)

     // Removing an item:
     delete(states, "OR") 
	 	fmt.Println(california)
		
		// Adding an item:
		states["NY"] = "New York"
		
		// Iteration through maps can be done with a for loop:
		// "k" stands for "key" and "v" stands for "value"
		// We want to loop through the "states" map
		// Each time through the loop, "k" will be one of the "keys" and "v" is one of the values
		for k, v := range states {
		// %v is used for both the key and the value here
				 fmt.Printf("%v: %v\n", k, v)
		}
		
		// To make it more ordered, we can do the following:
		// We are making this a slice of string values
		// The initial value is the length of the state's variable
		keys := make([]string, len(states))
		// Then we add each key from the map to the slice:
		i := 0
		for k:= range states {
				 keys[i] = k
				 i++
		}
		fmt.Println(keys) 
		
		// To then sort it, we do
		sort.Strings(keys)
		fmt.Println(keys) 
}
```
* That result looks like:
```
[WA NY CA]
[CA NY WA]
```
* To further sort this, we can do:
```
package main

import (
		 "fmt"
		 "sort"
)

func main() {
			// This is initialised with the make() function
			// The key type is wrapped in brackets and is set to "string". The associated value type is also set to "string".
	   states := make(map[string]string)
	   // Output the value of the map:
	   fmt.Println(states)
	   // Items are added here:
	   // The string-based key is "WA"
	   states["WA"] = "Washington"
	   states["OR"] = "Oregon"
	   states["CA"] = "California"
	   fmt.Println(states)
	   
	   // Retrieving an item based on its key.
	   // The syntax value is "states"
	   california := states["CA"]
	   fmt.Println(california)

     // Removing an item:
     delete(states, "OR") 
	 	fmt.Println(california)
		
		// Adding an item:
		states["NY"] = "New York"
		
		// Iteration through maps can be done with a for loop:
		// "k" stands for "key" and "v" stands for "value"
		// We want to loop through the "states" map
		// Each time through the loop, "k" will be one of the "keys" and "v" is one of the values
		for k, v := range states {
		// %v is used for both the key and the value here
				 fmt.Printf("%v: %v\n", k, v)
		}
		
		// To make it more ordered, we can do the following:
		// We are making this a slice of string values
		// The initial value is the length of the state's variable
		keys := make([]string, len(states))
		// Then we add each key from the map to the slice:
		i := 0
		for k:= range states {
				 keys[i] = k
				 i++
		}
		fmt.Println(keys) 
		
		// To then sort it, we do
		sort.Strings(keys)
		fmt.Println(keys) 
}
		// This is now an iterative loop with an index number
		for i := range keys {
			  fmt.Println(states[keys[i]])
		}
```
* The result is then we output the state values in Alphabetical order:
```
California
New York
Washington
```
* By using slices and maps together, we can process that data in whichever order is needed.
* 