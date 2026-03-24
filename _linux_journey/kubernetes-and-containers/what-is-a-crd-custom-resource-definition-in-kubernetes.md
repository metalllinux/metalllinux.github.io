---
title: "What is a CRD Custom Resource Definition in Kubernetes?"
category: "kubernetes-and-containers"
tags: ["kubernetes-and-containers", "crd", "custom", "resource", "definition"]
---

# What is a CRD Custom Resource Definition in Kubernetes?

The user is asking about CRDs (Custom Resource Definitions). This is a fundamental Kubernetes concept that's important for understanding how Kubernetes can be extended. I should provide a clear, comprehensive explanation.

## CRD - Custom Resource Definition

A **CRD (Custom Resource Definition)** is a powerful Kubernetes feature that allows you to extend the Kubernetes API by creating your own custom resources. Think of it as a way to teach Kubernetes about new types of objects that it doesn't know about by default.

### Key Concepts

**1. Standard vs Custom Resources**
- **Standard Resources**: Built-in Kubernetes objects like Pods, Services, Deployments, ConfigMaps
- **Custom Resources**: User-defined objects that you create using CRDs

**2. What CRDs Enable**
- Add new object types to your cluster
- Store and retrieve structured data
- Use kubectl with your custom objects just like native Kubernetes resources
- Leverage Kubernetes features like RBAC, API versioning, and namespace scoping

### Real-World Example

Let's say you want to manage databases in Kubernetes. Instead of just using StatefulSets and Services, you could create a CRD for a "Database" resource:

```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: databases.example.com
spec:
  group: example.com
  versions:
  - name: v1
    served: true
    storage: true
    schema:
      openAPIV3Schema:
        type: object
        properties:
          spec:
            type: object
            properties:
              engine:
                type: string
                enum: ["mysql", "postgres", "mongodb"]
              version:
                type: string
              storage:
                type: string
  scope: Namespaced
  names:
    plural: databases
    singular: database
    kind: Database
```

After creating this CRD, you can now create Database objects:

```yaml
apiVersion: example.com/v1
kind: Database  # Your custom resource!
metadata:
  name: my-app-db
spec:
  engine: postgres
  version: "14"
  storage: "100Gi"
```

### Common Use Cases for CRDs

1. **Operators**: Tools like Prometheus Operator, MySQL Operator use CRDs to manage complex applications
2. **Service Mesh**: Istio uses CRDs for VirtualService, DestinationRule, etc.
3. **CI/CD**: Tekton uses CRDs for Pipeline, Task, PipelineRun
4. **Gateway API**: Uses CRDs for Gateway, HTTPRoute, GatewayClass (like in your exercise!)
5. **Backup/Restore**: Velero uses CRDs for Backup, Restore, Schedule resources

### How CRDs Work

```
1. Define CRD → 2. Apply to Cluster → 3. Kubernetes API Extended → 4. Create Custom Resources
```

Once a CRD is installed:
- The Kubernetes API server recognizes the new resource type
- You can use `kubectl` commands with it:
  ```bash
  kubectl get databases
  kubectl describe database my-app-db
  kubectl delete database my-app-db
  ```
- It's stored in etcd like any other Kubernetes resource
- You can watch for changes, set up controllers, apply RBAC rules

### Gateway API Example (From Your Exercise)

In your Gateway API migration exercise, these are CRDs:
- `GatewayClass` 
- `Gateway`
- `HTTPRoute`

They're not native Kubernetes resources - they were added by installing the Gateway API CRDs:

```bash
# This command installs the CRDs
kubectl apply -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.0.0/standard-install.yaml

# After installation, you can see them
kubectl get crd | grep gateway
```

### CRD vs ConfigMap/Secret

**Why not just use ConfigMap?**
- ConfigMaps store unstructured data (key-value pairs)
- CRDs create actual API resources with:
  - Schema validation
  - Versioning
  - Status subresources
  - OpenAPI schema
  - Admission webhooks
  - Field selectors

### Benefits of CRDs

✅ **Native Integration**: Works with kubectl, client libraries, and Kubernetes tooling  
✅ **Declarative**: Follows Kubernetes declarative model  
✅ **Validation**: Built-in OpenAPI schema validation  
✅ **RBAC**: Fine-grained access control  
✅ **Versioning**: Support multiple versions with conversion  
✅ **Ecosystem**: Many tools and operators use CRDs  

### CRD Controllers

CRDs are often paired with **Controllers** (software that watches for changes to custom resources and takes action):

```
CRD defines the "what" → Controller implements the "how"
```

For example:
- **CRD**: Defines a "Database" resource
- **Controller**: Watches for Database resources and actually creates StatefulSets, Services, PVCs, etc.

This pattern is called the **Operator Pattern** and is fundamental to extending Kubernetes functionality.

In summary, CRDs are Kubernetes' way of allowing you to extend its API with your own custom resource types, making Kubernetes adaptable to almost any workload or operational pattern you need!

