---
title: "Experiment With The Go Playground"
category: "learning-go"
tags: ["learning-go", "experiment", "playground"]
---

* https://golang.org has everything you need to get started, including packages, binaries and the Go Playground.
	* Can run your code in the Go Playground.
* There is also a full screen version of the Go Playground, at https://play.golang.org
	* `Multiple files` has to place all of the code files into one.
	* Other examples include `Display image`, `Sleep` and `Clear`
* On the homepage, there are multiple samples. If you click `Share`, you can see the full version in The Go Playground.
* Via the Go Playground, you can easily share code by pasting it there and clicking the `Share` button.
* The Go Playground uses a backend server to compile the application and return the results.
	* The applications running in the Go playground, do not have access to the outside world.
		* Can't make requests to external hosts on the web and cannot host your own web services.
* Local host address is 127.0.0.1 works for many examples, won't be able to get a host outside of that environment.
	* The Playground also fakes the filesystem and simulates read and write operations. You write the files and then read them during the same applications run. Changes are not persistent.
	* Always the same date and time in the Go Playground - November 10th, 2009 11pm. This particular date and time, was when Go was first announced.
		* It also helps to make the results `determinative`.
* The Go Playground is completely free with no limitations.
	* No limitations on the number of source code files to work with.
	* No limitations on the number of times you can run the code.