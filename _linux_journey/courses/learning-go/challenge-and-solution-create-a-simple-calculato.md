---
title: "Challenge And Solution Create A Simple Calculato"
category: "learning-go"
tags: ["learning-go", "challenge", "solution", "create", "simple"]
---

* Explanation of the code is provided in the comments:
```
package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)

	fmt.Print("Value 1: ")
	input1, _ := reader.ReadString('\n')
	// Both values were parsed using ParseFloat, which is a member of the strconv package
	// The TrimSpace function is also used, to make sure any space around the packages is taken away
	// The value of 64 is also used
	float1, err := strconv.ParseFloat(strings.TrimSpace(input1), 64)
	// If the error is not equal to `nil`, that means there was no error
	// If there is an error, the error is then printed and we run the `panic` function and that stops the application completely
	if err != nil {
		fmt.Println(err)
		panic("Value 1 must be a number")
	}

  // All of the above is then done for the second value
	fmt.Print("Value 2: ")
	input2, _ := reader.ReadString('\n')
	float2, err := strconv.ParseFloat(strings.TrimSpace(input2), 64)
	if err != nil {
		fmt.Println(err)
		panic("Value 2 must be a number")
	}

  // The sum of the two values is then returned
	sum := float1 + float2
	sum = math.Round(sum*100) / 100
	fmt.Printf("The sum of %v and %v is %v\n\n", float1, float2, sum)

}
```
* The two values are then passed into a function called `calculate`. 15.5 is the sum of the two values.
* 