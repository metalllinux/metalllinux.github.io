---
title: "The Difference Between kubectl create and kubectl apply"
category: "kubernetes-and-containers"
tags: ["kubernetes-and-containers", "difference", "between", "kubectl", "create"]
---

# The Difference Between kubectl create and kubectl apply

The user is asking about the difference between two kubectl commands: `kubectl create -f` and `kubectl apply -f`. This is a technical Kubernetes question that I can answer based on my knowledge without needing any tools.

The key differences are:
1. `kubectl create -f` creates new resources and will fail if the resource already exists
2. `kubectl apply -f` creates new resources OR updates existing ones (declarative approach)
3. `apply` maintains configuration history and supports more sophisticated update strategies
4. `create` is imperative, `apply` is declarative

Let me provide a clear explanation of these differences.

The main differences between `kubectl create -f` and `kubectl apply -f` relate to how they handle resource creation and updates:

## **kubectl create -f**
- **Imperative command** that creates new resources only
- **Fails if the resource already exists** - you'll get an error like "Error from server (AlreadyExists)"
- Creates resources exactly as specified in the file
- Cannot update existing resources - you'd need to delete and recreate
- Simpler and straightforward for initial resource creation
- No configuration tracking

## **kubectl apply -f**
- **Declarative command** that creates OR updates resources
- **Idempotent** - can run multiple times safely without errors
- Creates new resources if they don't exist, updates them if they do
- Maintains the last-applied-configuration annotation on resources
- Supports more sophisticated update strategies (3-way merge)
- Tracks configuration changes for better management
- Preferred for GitOps and CI/CD workflows

## **When to use each:**

**Use `create`** when:
- You're certain the resource doesn't exist
- You want the operation to fail if it already exists
- You're doing quick, one-time resource creation
- You need simple, imperative operations

**Use `apply`** when:
- Managing resources in production
- Working with version-controlled manifests
- Need to repeatedly update configurations
- Following declarative infrastructure-as-code practices
- Implementing GitOps workflows

## **Example scenario:**
```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx
spec:
  replicas: 3
  ...
```

- First run: Both commands would create the deployment
- Second run: `create -f` would fail with "AlreadyExists", while `apply -f` would check for changes and update if needed
- If you change replicas to 5: Only `apply -f` can update the existing deployment

In practice, `kubectl apply -f` is generally preferred for most use cases because of its flexibility and idempotent nature, making it ideal for automation and repeated deployments.

