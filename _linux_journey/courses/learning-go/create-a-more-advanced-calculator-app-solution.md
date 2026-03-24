---
title: "Create A More Advanced Calculator App Solution"
category: "learning-go"
tags: ["learning-go", "create", "more", "advanced", "calculator"]
---

* Code structured like the following:
```
package main

import {
		 "fmt"
		 "strings"
		 "strconv"
}

func calculate(input1 string, input2 string, operation string) float64 {
			var result float64
			value1 := convertInputToValue(input1)
			value2 := convertInputToValue(input2)
			
			// The switch statement has 4 cases, one for each mathematical operation 
			switch operation {
			// In the case of the operation being the "+" character, it means we need to add values
			case "+":
					result = addValues(value1, value2)
			}
			case "-":
					result = subtractValues(value1, value2)
			case "*":
					result = multiplyValues(value1, value2)
			case "/": 
					result = divideValues(value1, value2)
			// If it is not valid, a "panic" is then thrown
			default:
					panic("Invalid Operation")
			}
			// Once we get to this line, we have a valid result and it is returned 
			return result
}

// Calculate returns the sum of the two parameters
// This is the function that parses the value AND an error condition. If the error is not "nil", that means there was a problem
// If that happens, then a message is created saying that the value has to be a number

// This parses the values or throws an error

func convertInputToValue(input string) float64 {
		value, err := strconv.ParseFloat(strings.TrimSpace(input), 64)
		if err != nil {
				message := fmt.Sprintf("%v must be a number", input)
				panic(message)
		}
		return value
}

// Each function has two parameters and returns a float64 as well
func addValues(value1, value2 float64) float64 {
			return value1 + value2
}

func subtractValues(value1, value2 float64) float64 {
			return value1 - value2
}

func multiplyValues(value1, value2 float64) float64 {
			return value1 * value2
}

func divideValues(value1, value2 float64) float64 {
			return value1 * value2
}


```