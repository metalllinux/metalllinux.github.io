---
title: "Write And Read Local Text Files"
category: "learning-go"
tags: ["learning-go", "write", "read", "local", "text"]
---

* There are high level extractions of the low level operations required to create text files.
* Here is a simple approach to reading and writing to text files:
```
package main

import {
		// We need to add three more declarations here:
    "fmt"
		"io"
		"io/ioutil"
		"os"
}

func main() {
		 content := "Hello from Go!"
		 // Below we create a file reference
		 // We'll also be calling something that returns an error and thus I'll be setting an object 
		 // We pass in the name and location of the file into os.Create()
		 // ./ is the same directory as the application
		 file, err := os.Create("./fromString.txt")
		 // We use this function to make sure that everything is okay and we can continue
		 // If there is a problem, it will crash the application
		 checkError(err)
		 // Now we can write to the file
		 // The WriteString function requires a writer object and a string
		 length, err := io.WriteString(file, content)
		 checkError(err)
		 // If we get to this stage, we know the file is created
		 // The length variable will be returned by write string. That will be the number of characters written to the file
		 fmt.Printf("Wrote a file with %v characters\n", length)
		 // Now we need to close the file and a new keyword is introduced --> defer --> meaning wait until everything else is done and then execute this command \
		 // When you work with files, it is important to close them once finished
		 defer file.Close()
}

// We need a function for error checking:
// It receives an error (err) object
// We then examine the err object with "error"
func checkError(err error){
		if err != nil
				// It then panics and displays the error message
				 panic(err)
}
```
* Once the application is ran, we see a message like the following:
```
Wrote a file with 14 characters
```
* Next we have the `readFile` function:
```
package main

import {
		// We need to add three more declarations here:
    "fmt"
		"io"
		"io/ioutil"
		"os"
}

func main() {
		 content := "Hello from Go!"
		 file, err := os.Create("./fromString.txt")
		 checkError(err)
		 length, err := io.WriteString(file, content)
		 checkError(err)
		 fmt.Printf("Wrote a file with %v characters\n", length)
		 defer file.Close()
		 // We pass in the name of the file we are reading
		 defer readFile("./fromString.txt")
}

// When you read a file, it also comes as an array of bytes
// In this case, those bytes (returned value) is just called data
func readFile(fileName String) {
		// Here we have to check for an error
		data, err := ioutil.ReadFile(fileName)
		// Checks for an error and if so, crashes the application
		checkError(err) 
		fmt.Println("Text read from file:", string(data))
} 

func checkError(err error){
		if err != nil
}
```
* Once we run the code, we see the text is being successfully read from the file.
```
Text read from file: Hello from Go!
```
* Important to use `defer`, if you work with anything that might not run automatically.
* You want to make sure that the file is completely closed before you attempt to read it.