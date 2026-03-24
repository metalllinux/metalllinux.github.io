---
title: "How to Install and Use an Azure Connected Registry"
category: "general-linux"
tags: ["install", "azure", "connected", "registry"]
---

[](https://www.codit.eu/en/)

I'm looking for something

[Case Studies](https://www.codit.eu/en/clients/)[Expertise](https://www.codit.eu/en/expertise/)[Industries](https://www.codit.eu/en/industries/)[Blog](https://www.codit.eu/en/blog/)[Events](https://www.codit.eu/en/events/)[Careers](https://www.codit.eu/en/jobs/)[About](https://www.codit.eu/en/about/)[Contact](https://www.codit.eu/en/contact/)

# How to Install and Use an Azure Connected Registry

In 2021, Microsoft released a feature of Azure Container Registry called 'connected registry' in public preview. A connected registry allows you to install a container registry on-prem, which synchronizes or mirrors an Azure Container Registry in the cloud. This allows you to have your container images nearby, which is beneficial in scenarios where you have an occasional or limited connection with the cloud. At the moment that you need to pull a container image, the image doesn't need to be pulled from Azure but is already present where you need it. In this blog post, I'll dive a bit deeper into the technicalities of how to deploy a connected registry.

Frederik Gheysels

28 July 2022

[In another blog post](https://www.codit.eu/blog/how-acrs-connected-registry-feature-helps-us-shipping-containers/), I explained how we can use a connected registry to bring containers onboard vessels.

In this article, I’ll dive a bit deeper and show you how you can deploy a connected Azure Container Registry, and how it must be configured so that images can be pulled.  Scripting is great, as it allows you to automate your deployments.

Let’s dive right into this!

### Installing a connected registry

Before we can pull images from a connected registry, we need to install one. This consists of 2 parts:

- Create a connected registry instance in Azure.
- Deploy the required connected registry components on the machine that will actually host the connected registry.

## Define a connected registry instance in Azure

When you want to make use of an on-prem connected registry, you first need to define a ‘connected registry’ resource in Azure.

This can be done by using the `az acr connected-registry` [command](https://docs.microsoft.com/en-us/cli/azure/acr/connected-registry?view=azure-cli-latest). When creating a connected registry, you need to specify which repositories from the parent Azure Container Registry must be synced or mirrored.  This is explained in great detail [here](https://docs.microsoft.com/en-us/azure/container-registry/overview-connected-registry-access).

## Specify the repositories that must be synced

If you don’t have a fixed list of repositories that must be synced with your connected registries, but want to sync all repositories that exist in a certain namespace, it can be quite cumbersome to manually list them all. Instead, you can list all the repositories that you want to sync via scripting. For instance:

|     |     |
| --- | --- |
|     | $azureContainerRegistry \= "mycontainerregistry" |
|     |     |
|     | # Get a list of all repositories that exist in the container registry. |
|     | # We'll use this list to retrieve the repositories that we want to sync |
|     | $existingRepositories \= az acr repository list \--name $azureContainerRegistry \| ConvertFrom-Json |
|     |     |
|     | # In this example, we'll specify that we will sync all repositories that are defined in the 'somenamespace' namespace |
|     | $repositoriesToSync \= $existingRepositories \| Where-Object {$_ \-Like "somenamespace/\*"} |
|     |     |
|     | # When specifying the repositories that must be synced, each repository must be enclosed in double quotes and separated with a space |
|     | $repositoriesToSyncString \= $repositoriesToSync \| % {"""$_"""} \| Join-String \-Separator " " |

[view raw](https://gist.github.com/fgheysels/d51b837f79381a80b7a4947f3fa88975/raw/630442797ed1667b0b8a41b2545d12c3066f7e26/specify-cacr-repos.ps1) [specify-cacr-repos.ps1](https://gist.github.com/fgheysels/d51b837f79381a80b7a4947f3fa88975#file-specify-cacr-repos-ps1) hosted with ❤ by [GitHub](https://github.com)

## Create the Connected Registry Azure resource

Once we have all the required information, the connected registry resource in Azure can be created.

|     |     |
| --- | --- |
|     | # Create the connected registry instance. Use the invoke-expression command, because the $repositoriesToSyncString variable otherwise gives some issues |
|     | $connectedRegistryName \= "myconnectedregistry" |
|     |     |
|     | Invoke-Expression "az acr connected-registry create --name $connectedRegistryName --registry $azureContainerRegistry --mode ReadOnly --sync-schedule '30 \* \* \* \*' --sync-window PT1H --repository $repositoriesToSyncString" |

[view raw](https://gist.github.com/fgheysels/b984a57c434c1095279f823bfd538f88/raw/62000aeff4f52baa4038bfc3853939849c3fba74/create-cacr.ps1) [create-cacr.ps1](https://gist.github.com/fgheysels/b984a57c434c1095279f823bfd538f88#file-create-cacr-ps1) hosted with ❤ by [GitHub](https://github.com)

With the above command, we specify that the connected registry must sync all repositories that are listed in the `$repositoriesToSyncString`.

The connected registry can only read from the parent ACR since the mode is set to `ReadOnly`.

Syncing happens every hour at 30 minutes and the sync window is set to 1 hour.

## Deploy the connected registry on-prem components

Now that we have created the necessary Azure resources for the connected registry, it is time to deploy the on-prem components.

In this article, we’ll focus on deploying a connected registry in a Kubernetes cluster.  If you want to deploy a connected registry in IoT Edge, please see [this](https://docs.microsoft.com/en-us/azure/container-registry/quickstart-deploy-connected-registry-iot-edge-cli) article.

## Get the connection-string of the connected registry

Before we can deploy the connected registry components, we need to get hold of the connection-string of the connected registry resource that exists in Azure.

We will need this information when deploying the on-prem components, so let’s just quickly retrieve the required information.

|     |     |
| --- | --- |
|     | $credentials \= az acr connected\-registry get-settings \` |
|     | \--name $connectedRegistryName \` |
|     | \--registry $azureContainerRegistry \` |
|     | \--parent\-protocol https |
|     | \--generate 1 \` |
|     | \--yes \| ConvertFrom-Json |

[view raw](https://gist.github.com/fgheysels/230d4ed42929ef8e355afb9c87218aee/raw/fec0507de997a3e9af9648490cbc8ecf7853bf8d/cacr-get-connectionstring.ps1) [cacr-get-connectionstring.ps1](https://gist.github.com/fgheysels/230d4ed42929ef8e355afb9c87218aee#file-cacr-get-connectionstring-ps1) hosted with ❤ by [GitHub](https://github.com)

With the above command, we generate a password and retrieve the credentials with one single command.

The `$credentials` object contains a connection-string that we’ll use in the next step.

## Deploying connected registry service

When you want to pull container images from a connected registry in a Kubernetes cluster, you will need to deploy the connected registry components inside your Kubernetes container. This can easily be done by installing a Helm chart provided by Microsoft.

I like to deploy these components in a dedicated Kubernetes namespace.  Execute the command below to create a Kubernetes namespace in an idempotent way.  This means that, when the namespace already exists, no error will be given:

|     |     |
| --- | --- |
|     | $azureContainerRegistry \= "mycontainerregistry" |
|     |     |
|     | # Get a list of all repositories that exist in the container registry. |
|     | # We'll use this list to retrieve the repositories that we want to sync |
|     | $existingRepositories \= az acr repository list \--name $azureContainerRegistry \| ConvertFrom-Json |
|     |     |
|     | # In this example, we'll specify that we will sync all repositories that are defined in the 'somenamespace' namespace |
|     | $repositoriesToSync \= $existingRepositories \| Where-Object {$_ \-Like "somenamespace/\*"} |
|     |     |
|     | # When specifying the repositories that must be synced, each repository must be enclosed in double quotes and separated with a space |
|     | $repositoriesToSyncString \= $repositoriesToSync \| % {"""$_"""} \| Join-String \-Separator " " |

[view raw](https://gist.github.com/fgheysels/d51b837f79381a80b7a4947f3fa88975/raw/630442797ed1667b0b8a41b2545d12c3066f7e26/specify-cacr-repos.ps1) [specify-cacr-repos.ps1](https://gist.github.com/fgheysels/d51b837f79381a80b7a4947f3fa88975#file-specify-cacr-repos-ps1) hosted with ❤ by [GitHub](https://github.com)

## Create the Connected Registry Azure resource

Once we have all the required information, the connected registry resource in Azure can be created.

|     |     |
| --- | --- |
|     | # Create the connected registry instance. Use the invoke-expression command, because the $repositoriesToSyncString variable otherwise gives some issues |
|     | $connectedRegistryName \= "myconnectedregistry" |
|     |     |
|     | Invoke-Expression "az acr connected-registry create --name $connectedRegistryName --registry $azureContainerRegistry --mode ReadOnly --sync-schedule '30 \* \* \* \*' --sync-window PT1H --repository $repositoriesToSyncString" |

[view raw](https://gist.github.com/fgheysels/b984a57c434c1095279f823bfd538f88/raw/62000aeff4f52baa4038bfc3853939849c3fba74/create-cacr.ps1) [create-cacr.ps1](https://gist.github.com/fgheysels/b984a57c434c1095279f823bfd538f88#file-create-cacr-ps1) hosted with ❤ by [GitHub](https://github.com)

With the above command, we specify that the connected registry must sync all repositories that are listed in the `$repositoriesToSyncString`.

The connected registry can only read from the parent ACR since the mode is set to `ReadOnly`.

Syncing happens every hour at minute 30 and the sync window is set to 1 hour.

## Deploy the connected registry on-prem components

Now that we have created the necessary Azure resources for the connected registry, it is time to deploy the on-prem components.

In this article, we’ll focus on deploying a connected registry in a Kubernetes cluster.  If you want to deploy a connected registry in IoT Edge, please see [this](https://docs.microsoft.com/en-us/azure/container-registry/quickstart-deploy-connected-registry-iot-edge-cli) article.

## Get the connection-string of the connected registry

Before we can deploy the connected registry components, we need to get hold of the connection-string of the connected registry resource that exists in Azure.

We will need this information when deploying the on-prem components, so let’s just quickly retrieve the required information.

|     |     |
| --- | --- |
|     | $credentials \= az acr connected\-registry get-settings \` |
|     | \--name $connectedRegistryName \` |
|     | \--registry $azureContainerRegistry \` |
|     | \--parent\-protocol https |
|     | \--generate 1 \` |
|     | \--yes \| ConvertFrom-Json |

[view raw](https://gist.github.com/fgheysels/230d4ed42929ef8e355afb9c87218aee/raw/fec0507de997a3e9af9648490cbc8ecf7853bf8d/cacr-get-connectionstring.ps1) [cacr-get-connectionstring.ps1](https://gist.github.com/fgheysels/230d4ed42929ef8e355afb9c87218aee#file-cacr-get-connectionstring-ps1) hosted with ❤ by [GitHub](https://github.com)

With the above command, we generate a password and retrieve the credentials with one single command.

The `$credentials` object contains a connection-string that we’ll use in the next step.

## Deploying connected registry service

When you want to pull container images from a connected registry in a Kubernetes cluster, you will need to deploy the connected registry components inside your Kubernetes container. This can easily be done by installing a Helm chart provided by Microsoft.

I like to deploy these components in a dedicated Kubernetes namespace.  Execute the command below to create a Kubernetes namespace in an idempotent way.  This means that, when the namespace already exists, no error will be given:

|     |     |
| --- | --- |
|     | kubectl create namespace connected\-registry \--dry\-run\=client \-o yaml \| kubectl apply \-f \- |

[view raw](https://gist.github.com/fgheysels/4d91071faf56895e27203d9540558842/raw/43ff59f711675f7a8e3342da36ffceaa461df401/cacr-create-ns.ps1) [cacr-create-ns.ps1](https://gist.github.com/fgheysels/4d91071faf56895e27203d9540558842#file-cacr-create-ns-ps1) hosted with ❤ by [GitHub](https://github.com)

Getting the Helm chart that is provided by Microsoft is done by executing these commands:

|     |     |
| --- | --- |
|     | helm chart pull mcr.microsoft.com/acr/connected\-registry/chart:0.2.0 |
|     | helm chart export mcr.microsoft.com/acr/connected\-registry/chart:0.2.0 \--destination $home |

[view raw](https://gist.github.com/fgheysels/3c07737531fbfab42b341c809a495007/raw/31d7a1839533cfc726093fb740f0f48e62187f77/cacr-deploy-helm.ps1) [cacr-deploy-helm.ps1](https://gist.github.com/fgheysels/3c07737531fbfab42b341c809a495007#file-cacr-deploy-helm-ps1) hosted with ❤ by [GitHub](https://github.com)

Verify if everything is running correctly by executing `kubectl get pods -n connected-registry`.

As you can see, with the above command we specify the connection-string to the connected-registry resource that is defined in Azure.  
We also specify that we want to be able to pull images from a private registry using http instead of being required to pull images using https (`httpEnabled=true`).

With the `sync.chunkSizeInMb` parameter you can specify the size of the chunks in which container layers must be downloaded. If you’re running on a slow or unstable connection, it is advised to set this parameter quite low.

The `pvc.storageClassName` specifies that we want to store the container images on local storage of the node. The values that you can specify for this parameter vary per Kubernetes flavor. The `local-path` value is a setting that is specific for [Rancher’s K3s](https://rancher.com/docs/k3s/latest/en/).

## Configure pulling from a private registry

When you want to pull from a private registry using http instead of https, you need to configure that the connected-registry is a private registry.

How this is done again depends on your Kubernetes version.  For K3s, this is done by editing the `/etc/rancher/k3s/registries.yaml` file.  More information on this can be found [here](https://rancher.com/docs/k3s/latest/en/installation/private-registry/).

To configure this, you’ll need the IP address at which the connected registry is reachable. The command below can be used to retrieve the IP address of the connected registry service that is running in Kubernetes:

|     |     |
| --- | --- |
|     | $connectedRegistryIp \= kubectl get service $connectedRegistryName \-o\=jsonpath\='{@.spec.clusterIP}' \-n connected\-registry |

[view raw](https://gist.github.com/fgheysels/a1c21bd53c2c51b0f3ad68fcb859c4af/raw/faeba81df7fb9c348ff6ecd49ca5638b6f8c370c/cacr-getservice-ip.ps1) [cacr-getservice-ip.ps1](https://gist.github.com/fgheysels/a1c21bd53c2c51b0f3ad68fcb859c4af#file-cacr-getservice-ip-ps1) hosted with ❤ by [GitHub](https://github.com)

Modify the `/etc/rancher/k3s/registries.yaml` file so that it looks like the sample below. Of course, you need to use the IP address that you’ve acquired (`$connectedRegistryIp`) instead of the sample address `10.1.1.1`

|     |     |
| --- | --- |
|     | mirrors: |
|     | "10.1.1.1:80": |
|     | endpoint: |
|     | \- "http://10.1.1.1:80" |
|     |     |
|     | configs: |
|     | "10.1.1.1:80": |
|     | tls: |
|     | \- insecure_skip_verify: true |

[view raw](https://gist.github.com/fgheysels/49fd60afdf1fbb2f054214f96d2d50bb/raw/73ea8fca8fe9a042126d39c810ccc2c88098b918/cacr-registries.yaml) [cacr-registries.yaml](https://gist.github.com/fgheysels/49fd60afdf1fbb2f054214f96d2d50bb#file-cacr-registries-yaml) hosted with ❤ by [GitHub](https://github.com)

Modifying this file can also be automated using your favourite scripting language. Using Powershell, you can for instance use the `powershell-yaml` module to do that. You can find this module [here](https://github.com/cloudbase/powershell-yaml).

Here is the code to do that:

|     |     |
| --- | --- |
|     | Install-Module \-Name powershell\-yaml \-Force |
|     | Import-Module powershell\-yaml \-Force |
|     |     |
|     | $mirror \= @{ endpoint \= @("http://$($connectedRegistryIp):80")} |
|     | $config \= @{ tls \= @{ insecure_skip_verify \= $true }} |
|     |     |
|     | $contents \= @{} |
|     |     |
|     | if ($True \-eq (Test-Path /etc/rancher/k3s/registries.yaml) ) |
|     | {   |
|     | $contents \= Get-Content \-Path /etc/rancher/k3s/registries.yaml \| ConvertFrom-Yaml |
|     | }   |
|     | else |
|     | {   |
|     | # If the file does not exist, create it. This is necessary to avoid errors |
|     | # later in the script where we'll (temporarly) modify the access rights on that file. |
|     | sudo touch /etc/rancher/k3s/registries.yaml |
|     | }   |
|     |     |
|     | #\# Add entries for the connected ACR |
|     | if( $null \-eq $contents\["mirrors"\] ) |
|     | {   |
|     | $contents\["mirrors"\] \= @{} |
|     | }   |
|     | $contents\["mirrors"\]\["""$($connectedRegistryIp):80"""\] \= $mirror |
|     |     |
|     | if( $null \-eq $contents\["configs"\] ) |
|     | {   |
|     | $contents\["configs"\] \= @{} |
|     | }   |
|     | $contents\["configs"\]\["""$($connectedRegistryIp):80"""\] \= $config |
|     |     |
|     | sudo \-E chmod a+w /etc/rancher/k3s/registries.yaml \| true |
|     |     |
|     | $yamlContent \= $contents \| ConvertTo-Yaml |
|     | #\# It seems that there's a bug in ConvertTo-Yaml: quotes are escaped with an additional single quote |
|     | $yamlContent \= $yamlContent \-Replace "'""", '"' \-Replace """'", '"' |
|     | Set-Content \-Path /etc/rancher/k3s/registries.yaml \-Value $yamlContent |
|     |     |
|     | sudo \-E chmod 644 /etc/rancher/k3s/registries.yaml \| true |

[view raw](https://gist.github.com/fgheysels/fb69478b174bd86e9508c2c741d2376d/raw/98b47b1a278c85cee7c9339d58da817e55ba0bce/cacr-configure-registries.ps1) [cacr-configure-registries.ps1](https://gist.github.com/fgheysels/fb69478b174bd86e9508c2c741d2376d#file-cacr-configure-registries-ps1) hosted with ❤ by [GitHub](https://github.com)

After the `registries.yaml` file has been modified, K3s must be restarted for the changes to have effect:

|     |     |
| --- | --- |
|     | sudo -E systemctl restart k3s |

[view raw](https://gist.github.com/fgheysels/697404551b2b5a5a3de0c4db0dcd8ab9/raw/f1f99b43e6133cf6102402715029feeca1b73758/cacr-restart-k3s.sh) [cacr-restart-k3s.sh](https://gist.github.com/fgheysels/697404551b2b5a5a3de0c4db0dcd8ab9#file-cacr-restart-k3s-sh) hosted with ❤ by [GitHub](https://github.com)

The connected registry is now in place and will start pulling container images from its’ parent Azure Container Registry.

## Pulling images from a connected registry

Now that the connected registry components are up and running, we need to configure it so that images can be pulled from the connected registry.

## Configure Client Token

Before images can be pulled from the connected registry, a client token must be configured.  As explained [here](https://docs.microsoft.com/en-us/azure/container-registry/overview-connected-registry-access#client-tokens), the client token specifies from which repository images can be pulled.

A token is created using a [scope map](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-repository-scoped-permissions).  In the scope map, we specify the repositories from which images can be pulled. We can use the `$existingRepositories` that we have declared and initialised earlier for this. We can extract the repositories that the client is allowed to pull. Again, let us specify that images can be pulled if they belong to a repository that is in a certain namespace:

|     |     |
| --- | --- |
|     | $allowedRepositories \= $existingRepositories \| Where-Object {$_ \-Like "somenamespace/\*"} |

[view raw](https://gist.github.com/fgheysels/e9f36710762b696175b3e81f6ac2485c/raw/cd919f2b7ca4f363f215fa9c540d199502c692f0/cacr-specify-repositories-for-pulling.ps1) [cacr-specify-repositories-for-pulling.ps1](https://gist.github.com/fgheysels/e9f36710762b696175b3e81f6ac2485c#file-cacr-specify-repositories-for-pulling-ps1) hosted with ❤ by [GitHub](https://github.com)

As can be read from the [documentation](https://docs.microsoft.com/en-us/cli/azure/acr/scope-map?view=azure-cli-latest#az-acr-scope-map-create) of the `az acr scope-map create` command, each repository must be prefixed with `--repository` and must be suffixed with the actions that are allowed for that repository.

The following command does that:

|     |     |
| --- | --- |
|     | $allowedRepositoriesString \= $allowedRepositories \| % { "\--repository $_ content/read" } \| Join-String \-Separator " " |

[view raw](https://gist.github.com/fgheysels/4b7c7c4431091538924e269b72e59dbe/raw/b09ab4227a8222a050577877a720f01dd5816c3d/cacr-pull-repos-argumentstring.ps1) [cacr-pull-repos-argumentstring.ps1](https://gist.github.com/fgheysels/4b7c7c4431091538924e269b72e59dbe#file-cacr-pull-repos-argumentstring-ps1) hosted with ❤ by [GitHub](https://github.com)

Now we have everything to create scope map.  Again, we use the `Invoke-Expression` command to avoid problems with the quotes in the `$allowedRepositoriesString` variable:

|     |     |
| --- | --- |
|     | $scopemapName \= "myscopemap" |
|     |     |
|     | Invoke-Expression "az acr scope-map create -n $scopemapName -r $azureContainerRegistryName --description 'Scope map for connected registry client token' $allowedRepositoriesString" |

[view raw](https://gist.github.com/fgheysels/3cb00f4d705899e3c6130bbae5d59c0e/raw/204f463981d3dedc7587cd2ed7876065c36304fa/cacr-clienttoken-scopemap.ps1) [cacr-clienttoken-scopemap.ps1](https://gist.github.com/fgheysels/3cb00f4d705899e3c6130bbae5d59c0e#file-cacr-clienttoken-scopemap-ps1) hosted with ❤ by [GitHub](https://github.com)

Now, we can use the scope map to generate a client access token and add that token to our connected registry:

|     |     |
| --- | --- |
|     | $tokenName \= "myclienttoken" |
|     |     |
|     | $token \= az acr token create \-n $tokenName \-r $azureContainerRegistryName \--scope\-map $scopemapName \| ConvertFrom-Json |
|     |     |
|     | az acr connected\-registry update \--registry $azureContainerRegistryName \--name $connectedRegistryName \--add-client\-tokens $tokenName |

[view raw](https://gist.github.com/fgheysels/80f4d07b1a9427f607895b79b0e1ad9d/raw/dcf0c29ba1f802e5d097d1838a887758122152ca/cacr-clientaccesstoken.ps1) [cacr-clientaccesstoken.ps1](https://gist.github.com/fgheysels/80f4d07b1a9427f607895b79b0e1ad9d#file-cacr-clientaccesstoken-ps1) hosted with ❤ by [GitHub](https://github.com)

*Note that it is a good idea to often roll the client access token. This can be done by simply executing the above commands again.*

## Create a Pull Secret for the Connected Registry

When you want to pull images in Kubernetes, you need a pull secret. The `$token` that we have just generated can be used to create a pull secret for the connected registry:

|     |     |
| --- | --- |
|     | $pullSecretUserName \= $token.credentials.username |
|     | $pullSecretPassword \= $token.credentials.passwords\[0\].value |
|     |     |
|     | # Retrieve IP address of connected-registry service that is running in k3s |
|     | $connectedRegistryIpAddress \= kubectl get service $connectedRegistryName \-o\=jsonpath\='{@.spec.clusterIP}' \-n connected\-registry |
|     |     |
|     | $connectedRegistryUrl \= "http://$($connectedRegistryIpAddress):80" |
|     |     |
|     | kubectl delete secret mypullsecretname \--ignore\-not\-found \-n mynamespace |
|     | kubectl create secret docker\-registry mypullsecretname \--docker\-server\=$connectedRegistryUrl \--docker\-username\=$pullSecretUserName \--docker\-password\=$pullSecretPassword \-n mynamespace |

[view raw](https://gist.github.com/fgheysels/f20aded8908460610a28f304702090f1/raw/ba13d3e7cfea01fee8002fdf73c51ceda7ee07ac/cacr-create-pullsecret.ps1) [cacr-create-pullsecret.ps1](https://gist.github.com/fgheysels/f20aded8908460610a28f304702090f1#file-cacr-create-pullsecret-ps1) hosted with ❤ by [GitHub](https://github.com)

Now you can use this pull secret in your Kubernetes deployments to pull container images from your Connected Registry! Just don’t forget to specify the pull secret in your Kubernetes deployment.yaml manifest.

I hope this article helps you in setting up an Azure Connected Registry!

Frederik

## Related articles

[How ACR's Connected Registry Feature Helps to Connect Vessels](https://www.codit.eu/blog/how-acrs-connected-registry-feature-helps-us-shipping-containers/)

[Euronav is the largest independent crude oil tanker company in the world and some time ago, they asked Codit to partner up in building a solution that could help them optimise their fuel consumption. Codit then helped them to build an application that runs both in the cloud and on…](https://www.codit.eu/blog/how-acrs-connected-registry-feature-helps-us-shipping-containers/)

[Logic Apps anywhere Comeback : welcome Logic Apps Hybrid](https://www.codit.eu/blog/logic-apps-anywhere-comeback-welcome-logic-apps-hybrid/)

[Three years ago, we explored using Azure Arc-enabled Kubernetes for hybrid integration in strict, low-latency environments. After a pause, the containerised Logic Apps deployment model is back—refreshed and powered by Azure Container Apps. Let’s dive into what’s new!](https://www.codit.eu/blog/logic-apps-anywhere-comeback-welcome-logic-apps-hybrid/)

[Key Takeaways from VisugXL 2024](https://www.codit.eu/blog/key-takeaways-from-visugxl-2024/)

[Last week, a group of Coditers attended VisugXL, an incredible event for .NET and Azure enthusiasts. The sessions covered a broad spectrum of topics, from sharpening performance skills to tackling real-world challenges in microservices architecture. Here are their key takeaways from this experience.](https://www.codit.eu/blog/key-takeaways-from-visugxl-2024/)

## Talk to the author

### Contact Frederik

Architect

Click here to get in touch

## Share this

Stay in Touch - Subscribe to Our Newsletter

Keep up to date with industry trends, events and the latest customer stories

[](https://www.facebook.com/Coditcompany/)[](https://www.linkedin.com/company/codit/)[](https://twitter.com/CoditCompany)[](https://www.instagram.com/codit.eu/)

Country

<a id="select2-country-wr-container"></a>Belgium

Language

<a id="select2-language-ch-container"></a>English

[Privacy Policy](https://www.codit.eu/en/privacy-policy/)[Terms & Conditions](https://www.codit.eu/en/general-terms-conditions-be/)