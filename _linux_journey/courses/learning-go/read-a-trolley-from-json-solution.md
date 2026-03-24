---
title: "Read A Trolley From Json Solution"
category: "learning-go"
tags: ["learning-go", "read", "trolley", "json", "solution"]
---

* There are 3 instances of a struct named `cart item`.
	* The price is a float and the quantity is an integer.
	* When the string is passed into `getCartFromJson`, we receive back a slice of cart item objects.
* Test Code
```
jsonString := 
`[{"name":"apple","price":2.99,"quantity":3},
{"name":"orange","price":1.50,"quantity":8},
{"name":"banana","price":0.49,"quantity":12}]
`

result := getCartFromJson(jsonString)
```
* Answer Code
```
package main

import (
			"encoding/json"
)

// In order to get the fields of the struct for the package, the fields have to be public.
// That is why they are capitalised here. It makes them directly accessible. The values can then be written to
// The fields then need to be matched up with the values in the JSON string
// To match what text in the JSON file, we match the field with json

type cartItem struct {
		Name string `json:"name"`
		Price float64 `json:"price"`
		Quantity int `json:"quantity"`
}


//getCartFromJson() returns a slight containing cartItem objects.
func getCartFromJson(jsonString string) []cartItem {
		var cart []cartItem
		// We pass in a byte slice, this is wrapped around the "jsonString". The value is then returned to the cart object with &cart
		err := json.Unmarshal([]byte(jsonString), &cart)
		if err != nil {
				panic("Error reading json string")
		}
		return cart 
}
