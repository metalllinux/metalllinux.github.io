---
title: "Reading And Writing Yaml"
category: "learning-kubernetes"
tags: ["learning-kubernetes", "reading", "writing", "yaml"]
---

* Infrastructure as Code (IaC)
* GitOps
* Both of the above terms are highly used and usually paired with Kubernetes.
* You deploy the IaC changes via a GitOps workflow.
* For the source files, the most commonly used ones are YAML manifests.
* YAML stands for "YAML Ain't Markup Language"
	* Data serialisation languages like YAML, allow interoperability between devices, programming languages and so on.
		*  Other examples are JSON and XML.
		*  Allows to make your data portable.
		*  Designed to be read and understood by humans.
*  Knowing YAML helps you work with Kubernetes manifests and objects.
*  Example YAML file:
```
---
# An instructor record
name: Metalinux
courses:
  - Learning Kubernetes
  - Kubernetes Package Management with Help
jobs:
  DigitalOcean: 1.25
  Fairwinds: 2.75
  Galvanize: 3
  titles:
    - Director of Instruction
		- Web Development Instructor
		- Instructional Designer
```
* In YAML, `---` on its own, signifies the beginning of a document.
	* You can have multiple documents within one file.
* A line that begins with a `#` sign is a comment.
* YAML stores key value pairs with a colon in between them.
	* For example, `field` is `name` and the value is `Metalinux`.
* In YAML, a list or an array of items is called a `sequence`.
	* Each item is preceded by a `-` and has its own line.
* You can use YAML to create a map of nested key-value pairs.
* YAML files can either have the `.yml` or `.yaml` extension.
	* Both are fine.
* Regarding indentation, run the files through a validator, for example [yamlcheck.com](yamlchecker.com)
* 