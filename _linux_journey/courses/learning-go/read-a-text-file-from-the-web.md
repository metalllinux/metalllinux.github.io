---
title: "Read A Text File From The Web"
category: "learning-go"
tags: ["learning-go", "read", "text", "file", "web"]
---

```
package main

import {
		 "fmt"
}
// The goal is to download the JSON content
const url = "http://services.explorecalifornia.org/json/tours.php"
// Am able to create an HTTP server with Go
func main() {
			// Once we call this function, we receive a response object. That is the object called "resp". Also a function that could return an error, hence why "err" is added
			resp, err := http.Get(url)
			if err != nil {
					// Then we panic and pass in the err object
					panic(err)
			}
			// An uppercase T is used for the type. Then we pass in the "resp" object
		 fmt.Printf("Response type: %T\n", resp)
}
```
* Once we run the above, we receive a pointer to an object named "response":
```
// This is a member of the HTTP package. The "response" object has a public field called "body". The body represents everything, in particular the json packet
Response type: *http.Response
```
* We now need code to close the body:
```
package main

import {
		 "fmt"
}
const url = "http://services.explorecalifornia.org/json/tours.php"
func main() {
			resp, err := http.Get(url)
			if err != nil {
					panic(err)
			}
		 fmt.Printf("Response type: %T\n", resp)
		 // We are deferring the call and therefore everything else will happen, once this has finished
		 defer resp.Body.Close()
		 
		 // We will receive an array called byte array. Its name is "bytes"
		 
		 bytes, err := ioutil.ReadAll(resp.Body) 
		 if err != nil {
			  	panic(err)
			}
			
			// We are starting with an array of bytes and therefore needs to start with a string
			// content's value is set to "bytes", wrapped in the "string" function
			content := string(bytes)
			fmt.Printf(content)
}
```
* We would then receive all of the data from the particular web page.