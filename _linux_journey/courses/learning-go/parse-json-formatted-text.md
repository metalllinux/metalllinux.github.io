---
title: "Parse Json Formatted Text"
category: "learning-go"
tags: ["learning-go", "parse", "json", "formatted", "text"]
---

* Go has a JSON package that allows you to easily parse and read the text.
```
package main

import {
		"fmt"
		"io/ioutil"
		"net/http"
		"encoding/json"
		"strings"
}

const url = "http://services.explorecalifornia.org/json/tours.php"

func main() {
			resp, err := http.Get(url)
			if err != nil {
					panic(err)
			}
		 fmt.Printf("Response type: %T\n", resp)
		 defer resp.Body.Close()
		 		 
		 bytes, err := ioutil.ReadAll(resp.Body) 
		 if err != nil {
			  	panic(err)
			}
			
			content := string(bytes)
			
			// The below is commented out.
			fmt.Printf(content)
			
			tours := toursFromHoward
			for _, tour := range tours{
							for.Println(tour.Name) 
			}
	}

// This is the JSON formatted string taken from the website
// We return the values as structured data - specifically a slice containing instances of the Tour object
func toursFromJson (content string) []Tour {
		 // We now create the slice of the Tour objects
		 // We set an initial size of 0 and initial capacity at 20
		 // Not sure how many tours will get, so set initial values at that
		 tours := make([]Tour, 0, 20)

			// We then create a decode object
			// We need to read the value that is passed in
			// We call the "strings" package and the NewReader function
			// decoder now has a link to the content
			decoder := json.NewDecoder(strings.NewReader(content))

			// We now check and make sure we do not have any errors
			// We are calling a function called token from the decoder object
			_, err := decoder.Token()
			if err != nil {
					// We panic and exit the application
					panic(err)
			}
			
			// We now transform the JSON formatted text into the Tour slice objects
			// We declare a variable of "tour" and set it as type "Tour"
			var tour Tour
			// We call a function called "More" from "decoder"
			// The function reads the next available object from the JSON content
			// If it finds some, it will return true and if not, in will return false
			// This will then feed i the data
			for decoder.More() {
					err := decoder.Decode(&tour)
					if err != nil {
							panic(err)
					}
					tours = append(tours,tour)
			}
			// We also need the tour object
			return tours
			
			
			tours = append(tours, tour)
}


// This will be a new custom type
type Tour struct {
		// Because the two fields have the same type, then can be declared on the same line
		// Uppercase character has been provided to them, so they are labelled as public
		Name, Price string
}
```
* Example of the JSON file being decoded:
![Screenshot from 2024-05-04 20-19-27.png](../../_resources/Screenshot%20from%202024-05-04%2020-19-27.png)
* The output would look like a list of all the tour names.
![Screenshot from 2024-05-04 22-43-11.png](../../_resources/Screenshot%20from%202024-05-04%2022-43-11.png)
* Go uses restful web services, that return data in JSON format.
