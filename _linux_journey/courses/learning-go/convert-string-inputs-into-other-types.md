---
title: "Convert String Inputs Into Other Types"
category: "learning-go"
tags: ["learning-go", "convert", "string", "inputs", "into"]
---

* The following continues on from:
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
* Those values always come to you as strings.
	* You may need to convert them to other types.
* Final file with comments and an example output when building and running the file as well:
```
package main

import (
	"bufio"
	"fmt"
	"os"

	// We need strconv which is part of the Go Core library. strconv stands for string conversion
	"strconv"
	// This particular package contains all sorts of functions for manipulating strings
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter text: ")
	input, _ := reader.ReadString('\n')
	fmt.Println("You entered:", input)

	fmt.Print("Enter a number: ")
	numInput, _ := reader.ReadString('\n')
	// We ignore the error object using the underscore character
	// We will now convert the above string, into a number
	// This time, we do care about the error object, because the user can easily pass in a number
	// ParseFloat requires two parameters. The second value is the bit size. This can be 32 or 64, depending on the OS
	// If the user typed space characters at the beginning or end of the string, it will not parse correctly
	// TrimSpace removes any leading or trailing white space
	aFloat, err := strconv.ParseFloat(strings.TrimSpace(numInput), 64)
	// We now need to evaluate if the object comes back correctly, this is done via nil or non-nil. We need additional code for this.
	// err is the error object
	if err != nil {
		fmt.Println(err)
	} else {
		// We assume the user typed in something here
		fmt.Println("Value of number:", aFloat)
	}
}
```
```
[myuser@rocky-linux-9-1 convert_string_inputs_to_other_types]$ ./main_2 
Enter text: test
You entered: test

Enter a number: 42.2
Value of number: 42.2
[myuser@rocky-linux-9-1 convert_string_inputs_to_other_types]$ ./main_2 
Enter text: temp
You entered: temp

Enter a number: test
strconv.ParseFloat: parsing "sfdsd": invalid syntax
```