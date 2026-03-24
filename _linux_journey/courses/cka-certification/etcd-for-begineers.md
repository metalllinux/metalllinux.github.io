---
title: "Etcd For Begineers"
category: "cka-certification"
tags: ["cka-certification", "etcd", "begineers"]
---

* ETCD is a distributed, reliable key-value store that is Simple, Secure & Fast.
* Traditionally, databases are in a tabular format - sql / relational databases.
	* These stores information in rows and colums.
	* Adding an additional colum impacts the entire table and all of the individual parts within them.
	* Every time new information is added, the entire table is affected.
	* It leads to a lot of empty cells.
![screenshot.png](../../_resources/screenshot-2.png)
* A key value store stores information in documents / pages - all information about an individual is stored within the file.
* These files can be in any format or structure and changing one file does not affect others.
![screenshot.png](../../_resources/screenshot.png)
* To Install ETCD, we run:
	* Download Binaries
	* Extract
	* Run ETCD Service
![screenshot.png](../../_resources/screenshot-1.png)
* When you run ETCD, it starts a service on port `2379` by default.
* You can then attach any client to the ETCD service, to store and retrive information.
* A default client that comes with `etc` is the `etcdctl` client.
	* This is a command line client for `etcd`.
* Stores and retrieves key value pairs.
	* `./etcdctl set key1 value1`
	* Creates an entry in the database with the information.
* To retrieve the stored data, run the `./etcdctl get key1` command and in this example, this returns `value1`.
* To view more options, run the `./etcdctl` command without any arguments.
* Important to understand `etcd` releases.
* v0.1 --> August 2013
* v0.5 --> December 2014
* v2.0 --> February 2015
	* Raft consensus algorithm was redesigned.
	* Supported more than 10,000 writes per second.
* v3.1 --> January 2017
	* More optimisations and improvements.
* CNCF Incubation --> November 2018
* Important to note the changes between v2.0 and v3.1
	* API versions changed between versions 2.0 and 3.1.
		* That means the `etcdctl` commands changed as well.
* These commands are for v2.0:
	* `etcdctl set key1 value1`
	* `etcdctl get key1`
	* `etcdctl`
* `etcdctl` is configured to work with v2.0 and v3.1 at the same time.
* Run `etcdctl --version` to see what version and API version is in use.
	* `etcdctl` version and the API version are two different things.
* With the release of v3.4, the default API version is set to 3.
* To change `etcdctl` to work with v3.1, add the following before each command like so:
	* `ETCDCTL_API=3 ./etcdctl version`
	* Or you can export it as an environment variable like this:
		* `export ETCDCTL_API=3`
			* `etcdctl version`
* With v3.1, the `version` command is just `etcdctl version`. In v2.0, this is `etcdctl --version`.
* Running just `etcdctl` by itself also just shows the version and API as well.
* To set a value is `etcdctl put key1 value1` with the output of `OK`
* To get a value, this is `etcdctl get key1` and it will show
```
key1
value1
```