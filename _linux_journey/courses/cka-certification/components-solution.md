---
title: "Components Solutions"
category: "cka-certification"
tags: ["cka-certification", "components", "solution"]
---

# Components Solutions



* What components are enabled in the Community Overview

```
bases:
  - ../../base

components:
  - ../../components/auth
```

* In the above case, only the `auth` component is included.

* What components are enabled in the `dev` overlay?

  * Check the `kustomization.yaml` file:
  
```
components:
  - ../../components/auth
  - ../../components/db
  - ../../components/logging
```

* How many environment variables does the `db` component add to the `api-deployment`?

```
Navigate to the /root/code/project_mercury/components directory.

The db component includes a patch file named api-patch.yaml, which modifies the api-deployment by adding two environment variables:

    DB_CONNECTION
    DB_PASSWORD

These variables are injected into the api container to enable connectivity with the database.

Below is the relevant configuration from the patch file:

apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-deployment
spec:
  template:
    spec:
      containers:
        - name: api
          env:
            - name: DB_CONNECTION
              value: postgres-service
            - name: DB_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: db-creds
                  key: password

Correct Answer : 2
```

* What is the name of the `secret generator` created in the `db` component:

```
Within the db component, the kustomization.yaml file defines a secretGenerator named db-creds. This generator creates a Kubernetes Secret with a key-value pair for the database password.

Below is the relevant configuration:

secretGenerator:
  - name: db-creds
    literals:
      - password=password1

File Location: components/db/kustomization.yaml

This secret is referenced in other configurations (e.g., the api-patch.yaml) to inject credentials securely into the application.

Correct Answer: The secret generator is named db-creds.
```

* Add the logging component to the community overlay?

```
To include the logging functionality in the community edition of the application, update the kustomization.yaml file under the community overlay by adding the logging component path.

Update File:
code/project_mercury/overlays/community/kustomization.yaml

components:
  - ../../components/auth
  - ../../components/logging

    Ensure that ../../components/logging is listed under components along with any existing components like auth.

How to apply?

kubectl apply -k /root/code/project_mercury/overlays/community
```

* A new caching component needs to be created for the application.

There is already a directory located at:
project_mercury/components/caching/

This directory contains the following files:

    redis-depl.yaml
    redis-service.yaml

Finish setting up this component by creating a kustomisation.yaml file in the same directory and importing the above Redis configuration files.

```
Create a kustomization.yaml file inside the components/caching/ directory with the following content:

apiVersion: kustomize.config.k8s.io/v1alpha1
kind: Component

resources:
  - redis-depl.yaml
  - redis-service.yaml

This defines the caching component using Kustomize and includes the required Redis resources for deployment.
```

* With the database setup for the caching component complete, we now need to update the api-deployment so that it can connect to the Redis instance.

Create a Strategic Merge Patch to add the following environment variable to the container in the deployment:

    Name: REDIS_CONNECTION
    Value: redis-service


Note:

    The patch file must be created at:
    project_mercury/components/caching/ with name api-patch.yaml

    After creating the patch file, you must also update the kustomisation.yaml file in the same directory (components/caching/) to include this patch under the patches field.

This step is essential — without updating kustomisation.yaml, the patch will not be applied when the component is used in an overlay.

```
Navigate to the /root/code/project_mercury/ directory.

1. Create the patch file
Location: components/caching/api-patch.yaml

apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-deployment
spec:
  template:
    spec:
      containers:
        - name: api
          env:
            - name: REDIS_CONNECTION
              value: redis-service

This patch ensures that the api container can access Redis using the specified environment variable.

2. Update the component's kustomization.yaml
Location: components/caching/kustomization.yaml

    Ensure that the kustomization.yaml file includes the api-patch.yaml under the patches field

apiVersion: kustomize.config.k8s.io/v1alpha1
kind: Component

resources:
  - redis-depl.yaml
  - redis-service.yaml

patches:
  - path: api-patch.yaml

Note:

    If you want to apply this component independently (e.g., using kubectl apply -k components/caching/), you will need to include ../../base/ in the resources field so that Kustomize can locate the original api-deployment for patching.

    However, when this component is used within an overlay like overlays/enterprise/, the base is already included at a higher level. Adding ../../base/ again inside the component will cause a duplicate resource error during kubectl apply -k overlays/enterprise/.

```

* Finally, let's add the caching component to the Enterprise edition of the application.

You need to update the kustomisation.yaml file located in the code/project_mercury/overlays/enterprise/ directory to include the caching component.

Once done, apply the updated configuration using:

kubectl apply -k /root/code/project_mercury/overlays/enterprise

```
Navigate to the /root/code/project_mercury/ directory.

Update the following file:
overlays/enterprise/kustomization.yaml

Ensure the components section includes the caching component:

components:
  - ../../components/auth
  - ../../components/db
  - ../../components/caching

This change ensures that the Enterprise edition of the application now includes the Redis-based caching functionality provided by the caching component.

    How to apply ?

kubectl apply -k overlays/enterprise/
```
