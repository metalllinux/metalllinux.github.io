---
title: "Advanced Kubectl Commands"
category: "cka-certification"
tags: ["cka-certification", "advanced", "kubectl", "commands"]
---

# Advanced Kubectl Commands

* How to use JSON PATH with `kubectl` in Kubernetes.

* Good to practice with JSON PATH on a Kubernetes dataset.

* Why do we use JSON PATH

    * Useful for large datasets in Kubernetes and for big Production environments - need to see information about 100s of nodes and 1000s of PODs, Deployments and ReplicaSets
    
        * Will have requirements of printing summary of states of different resources, want to view different fields about resources.
        
            * `kubectl` supports JSON PATH to make filtering data across large datasets much easier.
            
* How does the `kubectl` utility work? It is the Kubernetes CLI and allows us to interact with Kubernetes Objects.

* When running the following:

```
kubectl get nodes
```

* That is directly connecting to the `kube-apiserver`.

    * The `kube-apiserver` speaks the JSON language and therefore returns things in a JSON format.
    
    * The output of the `kubectl get nodes` command is actually shortened from the JSON PATH output.
    
        * To print additoinal details, can use `kubectl get nodes -o wide`

* A good use of JSON PATH and `kubectl` - to show nodes and their CPU counts in a tabular format:

    * Also print a list of pods and the images they use.
    
        * None of the built-in commands can output exactly these.
        
* JSON PATH queries allow you to filter the output of a command as you like.

* How to get started in JSON PATH in `kubectl`?

    * Identify the `kubectl` command (kubectl get nodes, kubectl get pods etc)
    
    * Familiarise with the JSON format - printing the output in JSON - `kubectl get nodes -o json` / `kubectl get pods -o json`.
    
    * Look through the structure of the JSON document and form the JSON PATH query.
    
        * An example is using `.items[0].spec.containers[0].image`
        
    * Then use the query you developed with the same `kubectl` command. Using the above example:
    
        ```
        kubectl get pods -o=jsonpath='{.items[0].spec.containers[0].image}'
        ```
* Good to use a JSON PATH evaluator like https://jsonpath.com/

* Play around with it until you have the best JSON PATH query and then add that to the `kubectl` command.

* A good example JSON PATH command to provide the names of the nodes:

```
kubectl get nodes -o=jsonpath='{.items[*].metadata.name}'
```

    * The output would be `master node01`

* A good example of returning the hardware architecture of the nodes:

```
kubectl get nodes -o=jsonpath='{.items[*]}.status.nodeInfo.architecture}'
```

* The output would be:

```
amd64 amd64
```

* A good command on returning the CPU count of a node:

```
kubectl get nodes -o=jsonpath='{.items[*].status.capacity.cpu}'
```

* The output here would be:

```
4 4
```

* Can merge the queries together to get multiple output, like so:

```
kubectl get nodes -o=jsonpath='{.items[*].status.capacity.cpu}{.items[*]}.status.nodeInfo.architecture}' 
```

* The output would be:

```
master node01 4 4
```

* You can make the above output much more pretty though:

```
{"\n"} - new line
{"\t"} - tab
```

* An example is below:

```
kubectl get nodes -o=jsonpath='{.items[*].status.capacity.cpu}{"\n"}{.items[*]}.status.nodeInfo.architecture}' 
```

```
master node01 
4       4
```

* You can also use `loops` with `range`.

    * We iterate through items in the list and create properties of each item. 

* To get the format we want below:

```
master 4
node01 4
```

* We need to do this pseudocode:

```
FOR EACH NODE

  PRINT NODE NAME \t PRINT CPU COUNT \n
  
END FOR
```

* To specify the `FOR EACH` statement, we need the `range` keyword:

```
'{range.items[*]}'
```

    * The `*` means for each item.
    
* To print the node name and cpu, use the same line from earlier:

```
kubectl get nodes -o=jsonpath='{range.items[*]{.metadata.name} {"\t"} {.status.capacity.cpu} {"\n"}{end}'
```

* Can also use JSON PATH when printing custom columns:

```
kubectl get nodes -o=custom-columns=<COLUMN NAME>:<JSON_PATH>
```

* An example of using columns is below:

```
kubectl get nodes -o=custom-columns=NODE:.metadata.name ,CPU:.status.capacity.cpu
```

* This looks liks this:

```
NODE CPU
master 4
node01 4
```

* You can also sort the output based on a property from each item.

* Examples are below:

```
kubectl get nodes --sort-by=.metadata.name
kubectl get node s--sort-by=.status.capacity.cpu
```
