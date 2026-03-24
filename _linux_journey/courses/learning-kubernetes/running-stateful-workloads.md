---
title: "Running Stateful Workloads"
category: "learning-kubernetes"
tags: ["learning-kubernetes", "running", "stateful", "workloads"]
---

* Earlier in the course, a sample application was deployed and this is `stateless`. This does not communicate with the database.
* How is data storage handled in Kubernetes.
	* Option 1 --> Connect the application to a database that is running outside of the cluster.
		* For example, an application that uses Postgres for data persistence. Can either build and maintain a SQL database on a server that is separate from the cluster OR use a manged database service such as Azure SQL, Amazon RDS or Google Cloud SQL and configure that to communicate with Kubernetes.
	* Option 2 --> Use a Kubernetes Persistent Volume. They are a type of data storage that exists in your cluster. They remain, even after a Pod is destroyed.
		* Can use a Kubernetes Object called a Stateful Set. It makes sure the updated application can communicate with the same volume as the previous pod.