---
title: "Work With Dates And Times"
category: "learning-go"
tags: ["learning-go", "work", "dates", "times"]
---

* Dates and Times are managed in Go with the Time Package.
```
package main

import (
		  "fmt"
)

func main() {
		
		 n := time.Now()
		 fmt.Println("I recorded this video at ", n)
		
    fmt.Println("Dates and times")

}
```
* A variable declared with the `time` type, encapsulates maths operations, timezone management and more.
* When we run the above code, we receive the following:
```
:!'go' 'run' '/home/howard/learning-go-2875237/go_learning/work_with_dates_and_times/main.go'  2>&1| tee /tmp/nvim.howard/OA5SJz/1                                                                                                      
I recorded this video at  2024-04-17 14:29:24.296399799 +0900 JST m=+0.000008168
Dates and times
```
* We can also create more explicit time values:
```
package main

import (
	"fmt"
	"time"
)

func main() {

	n := time.Now()
	fmt.Println("I recorded this video at ", n)

	fmt.Println("Dates and times")
	// The day is "10", the hour value is "23". Zeroes are used for the minutes, seconds and milliseconds. For the location, constant of time.UTC
	t := time.Date(2009, time.November, 10, 23, 0, 0, 0, time.UTC)
	// We then output the above with
	fmt.Println("Go launched at ", t)
	// For a formatted version of the date/time value.
	// t.Format is available via the time object itself. We need a layout string, which is a representation of the formatted time value
	fmt.Println(t.Format(time.ANSIC))
}
```
* There are other standard formats included in the documentation.
* Another configuration method is with:
```
package main

import (
	"fmt"
	"time"
)

func main() {

	n := time.Now()
	fmt.Println("I recorded this video at ", n)

	fmt.Println("Dates and times")
	// The day is "10", the hour value is "23". Zeroes are used for the minutes, seconds and milliseconds. For the location, constant of time.UTC
	t := time.Date(2009, time.November, 10, 23, 0, 0, 0, time.UTC)
	// We then output the above with
	fmt.Println("Go launched at ", t)
	// For a formatted version of the date/time value.
	// t.Format is available via the time object itself. We need a layout string, which is a representation of the formatted time value
	fmt.Println(t.Format(time.ANSIC))
}
```