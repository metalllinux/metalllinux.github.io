---
title: "Convert A Slice Of Strings To A Map Solution"
category: "learning-go"
tags: ["learning-go", "convert", "slice", "strings", "map"]
---

* A map object is a collection of key value pairs.
* The keys will be strings and the associated float values will be `float64`s.
* The challenge asks that all of the associated values add up to 100.
```
package main

// Converts a slice of strings to an object map
func convertToMap(items []string) map[string]float64 {

	// Create a map object
	// Created from the "make" function. The "map" signature is passed in, the key is a "string" and the associated value is a "float64"
	result := make(map[string]float64)
	
	// Next, a value is assigned to each item in the map
	// We get that value, from dividing by 100
	// "len" is being wrapped in the "float64" function. This is due to "len" returning an integer and the "map" object requires float64 values
	elementValue := 100 / float64(len(items))
	
	// Regarding the "for" loop. Each iteration of the for loop provides us with the index and the value of the slice
	// In this case, we are not interested in the index, so we use an underscore for the variable name. For the value however, we are using that as the key in the map
	// Within the for loop, the map value is assigned to the object. This sets both the key and the element value. After the loop is done, the result is returned
	for _, fruit := range items {
			result[fruit] = elementValue
	} 
	return result
}
```