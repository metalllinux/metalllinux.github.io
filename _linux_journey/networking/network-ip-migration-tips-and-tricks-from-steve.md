---
title: "Network Ip Migration Tips And Tricks From Steve"
category: "networking"
tags: ["networking", "network", "migration", "tips", "tricks"]
---

* Set expectations for customers that network unavailability will happen and when it will happen.
* Give regular status updates at certain times during the window of downtime.
	* "Home Assistant is back up" for example.
* Set a time window for the client and stick to it.
	* Regardless of the situation, if you don't complete it within a certain time, pull the ripcord and rollback the changes.
		* What is your rollback plan.
* Know ahead of time what you are going to test and have multiple test cases.
	* Laptop can connect, but desktop is not able to connect to the network for example.
* Be prepared for any aftermath.
	* Changes cause unanticipated problems down the line.
* Set aside time for the "oops" moments.
* Communication path only with stakeholders, to avoid other parties blaming the changes made.
* Check firewall rules after the network changes are made.
	* Firewalls very quickly see the new changes and can tell if changing from a /24 to a /21 IP scheme.