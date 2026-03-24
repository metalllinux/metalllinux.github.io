---
title: "Pull an Image from a Private Registry"
category: "kubernetes-and-containers"
tags: ["kubernetes-and-containers", "pull", "image", "private", "registry"]
---

# Pull an Image from a Private Registry

This page shows how to create a Pod that uses a [Secret](https://kubernetes.io/docs/concepts/configuration/secret/) to pull an image from a private container image registry or repository. There are many private registries in use. This task uses [Docker Hub](https://www.docker.com/products/docker-hub) as an example registry.

## Before you begin

-   You need to have a Kubernetes cluster, and the kubectl command-line tool must be configured to communicate with your cluster. It is recommended to run this tutorial on a cluster with at least two nodes that are not acting as control plane hosts. If you do not already have a cluster, you can create one by using [minikube](https://minikube.sigs.k8s.io/docs/tutorials/multi_node/) or you can use one of these Kubernetes playgrounds:
    
    -   [iximiuz Labs](https://labs.iximiuz.com/playgrounds?category=kubernetes&filter=all)
    -   [Killercoda](https://killercoda.com/playgrounds/scenario/kubernetes)
    -   [KodeKloud](https://kodekloud.com/public-playgrounds)
    -   [Play with Kubernetes](https://labs.play-with-k8s.com/)
-   To do this exercise, you need the `docker` command line tool, and a [Docker ID](https://docs.docker.com/docker-id/) for which you know the password.
    
-   If you are using a different private container registry, you need the command line tool for that registry and any login information for the registry.
    

## Log in to Docker Hub

On your laptop, you must authenticate with a registry in order to pull a private image.

Use the `docker` tool to log in to Docker Hub. See the _log in_ section of [Docker ID accounts](https://docs.docker.com/docker-id/#log-in) for more information.

When prompted, enter your Docker ID, and then the credential you want to use (access token, or the password for your Docker ID).

The login process creates or updates a `config.json` file that holds an authorisation token. Review [how Kubernetes interprets this file](https://kubernetes.io/docs/concepts/containers/images/#config-json).

View the `config.json` file:

```
cat ~/.docker/config.json
```

The output contains a section similar to this:

```
{
    "auths": {
        "https://index.docker.io/v1/": {
            "auth": "c3R...zE2"
        }
    }
}
```

## Create a Secret based on existing credentials

A Kubernetes cluster uses the Secret of `kubernetes.io/dockerconfigjson` type to authenticate with a container registry to pull a private image.

If you already ran `docker login`, you can copy that credential into Kubernetes:

```
kubectl create secret generic regcred \
    --from-file=.dockerconfigjson=<path/to/.docker/config.json> \
    --type=kubernetes.io/dockerconfigjson
```

If you need more control (for example, to set a namespace or a label on the new secret) then you can customise the Secret before storing it. Be sure to:

-   set the name of the data item to `.dockerconfigjson`
-   base64 encode the Docker configuration file and then paste that string, unbroken as the value for field `data[".dockerconfigjson"]`
-   set `type` to `kubernetes.io/dockerconfigjson`

Example:

```
apiVersion: v1
kind: Secret
metadata:
  name: myregistrykey
  namespace: awesomeapps
data:
  .dockerconfigjson: UmVhbGx5IHJlYWxseSByZWVlZWVlZWVlZWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGxsbGx5eXl5eXl5eXl5eXl5eXl5eXl5eSBsbGxsbGxsbGxsbGxsbG9vb29vb29vb29vb29vb29vb29vb29vb29vb25ubm5ubm5ubm5ubm5ubm5ubm5ubm5ubmdnZ2dnZ2dnZ2dnZ2dnZ2dnZ2cgYXV0aCBrZXlzCg==
type: kubernetes.io/dockerconfigjson
```

If you get the error message `error: no objects passed to create`, it may mean the base64 encoded string is invalid. If you get an error message like `Secret "myregistrykey" is invalid: data[.dockerconfigjson]: invalid value ...`, it means the base64 encoded string in the data was successfully decoded, but could not be parsed as a `.docker/config.json` file.

## Create a Secret by providing credentials on the command line

Create this Secret, naming it `regcred`:

```
kubectl create secret docker-registry regcred --docker-server=<your-registry-server> --docker-username=<your-name> --docker-password=<your-pword> --docker-email=<your-email>
```

where:

-   `<your-registry-server>` is your Private Docker Registry FQDN. Use `https://index.docker.io/v1/` for DockerHub.
-   `<your-name>` is your Docker username.
-   `<your-pword>` is your Docker password.
-   `<your-email>` is your Docker email.

You have successfully set your Docker credentials in the cluster as a Secret called `regcred`.

## Inspecting the Secret `regcred`

To understand the contents of the `regcred` Secret you created, start by viewing the Secret in YAML format:

```
kubectl get secret regcred --output=yaml
```

The output is similar to this:

```
apiVersion: v1
kind: Secret
metadata:
  ...
  name: regcred
  ...
data:
  .dockerconfigjson: eyJodHRwczovL2luZGV4L ... J0QUl6RTIifX0=
type: kubernetes.io/dockerconfigjson
```

The value of the `.dockerconfigjson` field is a base64 representation of your Docker credentials.

To understand what is in the `.dockerconfigjson` field, convert the secret data to a readable format:

```
kubectl get secret regcred --output="jsonpath={.data.\.dockerconfigjson}" | base64 --decode
```

The output is similar to this:

```
{"auths":{"your.private.registry.example.com":{"username":"janedoe","password":"xxxxxxxxxxx","email":"jdoe@example.com","auth":"c3R...zE2"}}}
```

To understand what is in the `auth` field, convert the base64-encoded data to a readable format:

```
echo "c3R...zE2" | base64 --decode
```

The output, username and password concatenated with a `:`, is similar to this:

```
janedoe:xxxxxxxxxxx
```

Notice that the Secret data contains the authorisation token similar to your local `~/.docker/config.json` file.

You have successfully set your Docker credentials as a Secret called `regcred` in the cluster.

## Create a Pod that uses your Secret

Here is a manifest for an example Pod that needs access to your Docker credentials in `regcred`:

```
apiVersion: v1
kind: Pod
metadata:
  name: private-reg
spec:
  containers:
  - name: private-reg-container
    image: <your-private-image>
  imagePullSecrets:
  - name: regcred

```

Download the above file onto your computer:

```
curl -L -o my-private-reg-pod.yaml https://k8s.io/examples/pods/private-reg-pod.yaml
```

In file `my-private-reg-pod.yaml`, replace `<your-private-image>` with the path to an image in a private registry such as:

```
your.private.registry.example.com/janedoe/jdoe-private:v1
```

To pull the image from the private registry, Kubernetes needs credentials. The `imagePullSecrets` field in the configuration file specifies that Kubernetes should get the credentials from a Secret named `regcred`.

Create a Pod that uses your Secret, and verify that the Pod is running:

```
kubectl apply -f my-private-reg-pod.yaml
kubectl get pod private-reg
```

Also, in case the Pod fails to start with the status `ImagePullBackOff`, view the Pod events:

```
kubectl describe pod private-reg
```

If you then see an event with the reason set to `FailedToRetrieveImagePullSecret`, Kubernetes can't find a Secret with name (`regcred`, in this example).

Make sure that the Secret you have specified exists, and that its name is spelled properly.

```
Events:
  ...  Reason                           ...  Message
       ------                                -------
  ...  FailedToRetrieveImagePullSecret  ...  Unable to retrieve some image pull secrets (<regcred>); attempting to pull the image may not succeed.
```

## Using images from multiple registries

A pod can have multiple containers, each container image can be from a different registry. You can use multiple `imagePullSecrets` with one pod, and each can contain multiple credentials.

The image pull will be attempted using each credential that matches the registry. If no credentials match the registry, the image pull will be attempted without authorisation or using custom runtime specific configuration.

## What's next

-   Learn more about [Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)
    -   or read the API reference for [Secret](https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/secret-v1/)
-   Learn more about [using a private registry](https://kubernetes.io/docs/concepts/containers/images/#using-a-private-registry).
-   Learn more about [adding image pull secrets to a service account](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#add-imagepullsecrets-to-a-service-account).
-   See [kubectl create secret docker-registry](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands/#-em-secret-docker-registry-em-).
-   See the `imagePullSecrets` field within the [container definitions](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#containers) of a Pod

Items on this page refer to third party products or projects that provide functionality required by Kubernetes. The Kubernetes project authors aren't responsible for those third-party products or projects. See the [CNCF website guidelines](https://github.com/cncf/foundation/blob/master/website-guidelines.md) for more details.

You should read the [content guide](https://kubernetes.io/docs/contribute/style/content-guide/#third-party-content) before proposing a change that adds an extra third-party link.
