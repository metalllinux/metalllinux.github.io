---
title: "Get Input From The Console"
category: "learning-go"
tags: ["learning-go", "input", "console"]
---

* To get input, you require a package called `bufio`.
* Need another package called `os`.
* Comments with how to get input from the console:
```
package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	// Stdin is standard input (what the user types on the command line)
	reader := bufio.NewReader(os.Stdin)
	// Displaying a prompt to the user. We are not using Println, as we do not want a line feed at the end of the string
	fmt.Print("Enter text: ")
	// We need the application to pause and let the user type something in. We need two variables, the first being a string and what the user types. This is called "input", the second variable is an error object.
	// If you want to ignore a variable, we need to use the underscore character.
	// Both variables are initialised with reader.ReadString. The ReadString function requires a single byte (one character). This is called a delimeter. Tells the ReadString fuction when to start accepting input.
	// Characters are wrapped in single quotes, whilst fulll srings are wrapped in double quotes
	input, _ := reader.ReadString('\n')
	fmt.Println("You entered:", input)
}
```