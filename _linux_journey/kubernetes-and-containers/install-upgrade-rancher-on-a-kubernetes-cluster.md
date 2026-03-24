---
title: "Install Upgrade Rancher On A Kubernetes Cluster"
category: "kubernetes-and-containers"
tags: ["kubernetes-and-containers", "install", "upgrade", "rancher", "kubernetes"]
---

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![logo](https://ranchermanager.docs.rancher.com/img/rancher-logo-horiz-colour.svg)](https://ranchermanager.docs.rancher.com/)

[Latest](https://ranchermanager.docs.rancher.com/)

[English](#)

[Quick Links](#)

[More from SUSE](#)

- [What is Rancher?](https://ranchermanager.docs.rancher.com/)
- [Getting Started](#)
    
    - [Overview](https://ranchermanager.docs.rancher.com/getting-started/overview)
    - [Quick Start Guides](https://ranchermanager.docs.rancher.com/getting-started/quick-start-guides)
        
    - [Installation and Upgrade](https://ranchermanager.docs.rancher.com/getting-started/installation-and-upgrade)
        
        - [Installation Requirements](https://ranchermanager.docs.rancher.com/getting-started/installation-and-upgrade/installation-requirements)
            
        - [Installation References](https://ranchermanager.docs.rancher.com/getting-started/installation-and-upgrade/installation-references)
            
        - [Install/Upgrade on a Kubernetes Cluster](https://ranchermanager.docs.rancher.com/getting-started/installation-and-upgrade/install-upgrade-on-a-kubernetes-cluster)
            
            - [Rollbacks](https://ranchermanager.docs.rancher.com/getting-started/installation-and-upgrade/install-upgrade-on-a-kubernetes-cluster/rollbacks)
            - [Upgrades](https://ranchermanager.docs.rancher.com/getting-started/installation-and-upgrade/install-upgrade-on-a-kubernetes-cluster/upgrades)
            - [Upgrading in an Air-Gapped Environment](https://ranchermanager.docs.rancher.com/getting-started/installation-and-upgrade/install-upgrade-on-a-kubernetes-cluster/air-gapped-upgrades)
            - [Installing Rancher on Amazon EKS](https://ranchermanager.docs.rancher.com/getting-started/installation-and-upgrade/install-upgrade-on-a-kubernetes-cluster/rancher-on-amazon-eks)
            - [Installing Rancher on Azure Kubernetes Service](https://ranchermanager.docs.rancher.com/getting-started/installation-and-upgrade/install-upgrade-on-a-kubernetes-cluster/rancher-on-aks)
            - [Installing Rancher on a Google Kubernetes Engine Cluster](https://ranchermanager.docs.rancher.com/getting-started/installation-and-upgrade/install-upgrade-on-a-kubernetes-cluster/rancher-on-gke)
            - [Upgrading a Hardened Custom/Imported Cluster to Kubernetes v1.25](https://ranchermanager.docs.rancher.com/getting-started/installation-and-upgrade/install-upgrade-on-a-kubernetes-cluster/upgrade-a-hardened-cluster-to-k8s-v1-25)
            - [Troubleshooting the Rancher Server Kubernetes Cluster](https://ranchermanager.docs.rancher.com/getting-started/installation-and-upgrade/install-upgrade-on-a-kubernetes-cluster/troubleshooting)
        - [Other Installation Methods](https://ranchermanager.docs.rancher.com/getting-started/installation-and-upgrade/other-installation-methods)
            
        - [Resources](https://ranchermanager.docs.rancher.com/getting-started/installation-and-upgrade/resources)
            
        - [Upgrading and Rolling Back Kubernetes](https://ranchermanager.docs.rancher.com/getting-started/installation-and-upgrade/upgrade-and-roll-back-kubernetes)
https://ranchermanager.docs.rancher.com/getting-started/installation-and-upgrade/install-upgrade-on-a-kubernetes-cluster
# Install/Upgrade Rancher on a Kubernetes Cluster

In this section, you'll learn how to deploy Rancher on a Kubernetes cluster using the Helm CLI.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

- [Kubernetes Cluster](#kubernetes-cluster)
- [Ingress Controller](#ingress-controller)
- [CLI Tools](#cli-tools)

### Kubernetes Cluster[​](#kubernetes-cluster "Direct link to Kubernetes Cluster")

Set up the Rancher server's local Kubernetes cluster.

Rancher can be installed on any Kubernetes cluster. This cluster can use upstream Kubernetes, or it can use one of Rancher's Kubernetes distributions, or it can be a managed Kubernetes cluster from a provider such as Amazon EKS.

For help setting up a Kubernetes cluster, we provide these tutorials:

- **RKE:** For the tutorial to install an RKE Kubernetes cluster, refer to [this page.](https://ranchermanager.docs.rancher.com/how-to-guides/new-user-guides/kubernetes-cluster-setup/rke1-for-rancher) For help setting up the infrastructure for a high-availability RKE cluster, refer to [this page.](https://ranchermanager.docs.rancher.com/how-to-guides/new-user-guides/infrastructure-setup/ha-rke1-kubernetes-cluster)
- **K3s:** For the tutorial to install a K3s Kubernetes cluster, refer to [this page.](https://ranchermanager.docs.rancher.com/how-to-guides/new-user-guides/kubernetes-cluster-setup/k3s-for-rancher) For help setting up the infrastructure for a high-availability K3s cluster, refer to [this page.](https://ranchermanager.docs.rancher.com/how-to-guides/new-user-guides/infrastructure-setup/ha-k3s-kubernetes-cluster)
- **RKE2:** For the tutorial to install an RKE2 Kubernetes cluster, refer to [this page.](https://ranchermanager.docs.rancher.com/how-to-guides/new-user-guides/kubernetes-cluster-setup/rke2-for-rancher) For help setting up the infrastructure for a high-availability RKE2 cluster, refer to [this page.](https://ranchermanager.docs.rancher.com/how-to-guides/new-user-guides/infrastructure-setup/ha-rke2-kubernetes-cluster)
- **Amazon EKS:** For details on how to install Rancher on Amazon EKS, including how to install an Ingress controller so that the Rancher server can be accessed, refer to [this page.](https://ranchermanager.docs.rancher.com/getting-started/installation-and-upgrade/install-upgrade-on-a-kubernetes-cluster/rancher-on-amazon-eks)
- **AKS:** For details on how to install Rancher with Azure Kubernetes Service, including how to install an Ingress controller so that the Rancher server can be accessed, refer to [this page.](https://ranchermanager.docs.rancher.com/getting-started/installation-and-upgrade/install-upgrade-on-a-kubernetes-cluster/rancher-on-aks)
- **GKE:** For details on how to install Rancher with Google Kubernetes Engine, including how to install an Ingress controller so that the Rancher server can be accessed, refer to [this page.](https://ranchermanager.docs.rancher.com/getting-started/installation-and-upgrade/install-upgrade-on-a-kubernetes-cluster/rancher-on-gke) GKE has two modes of operation when creating a Kubernetes cluster, Autopilot and Standard mode. The cluster configuration for Autopilot mode has restrictions on editing the kube-system namespace. However, Rancher needs to create resources in the kube-system namespace during installation. As a result, you will not be able to install Rancher on a GKE cluster created in Autopilot mode.

### Ingress Controller[​](#ingress-controller "Direct link to Ingress Controller")

The Rancher UI and API are exposed through an Ingress. This means the Kubernetes cluster that you install Rancher in must contain an Ingress controller.

For RKE, RKE2, and K3s installations, you don't have to install the Ingress controller manually because one is installed by default.

For distributions that do not include an Ingress Controller by default, like a hosted Kubernetes cluster such as EKS, GKE, or AKS, you have to deploy an Ingress controller first. Note that the Rancher Helm chart does not set an `ingressClassName` on the ingress by default. Because of this, you have to configure the Ingress controller to also watch ingresses without an `ingressClassName`.

Examples are included in the **Amazon EKS**, **AKS**, and **GKE** tutorials above.

### CLI Tools[​](#cli-tools "Direct link to CLI Tools")

The following CLI tools are required for setting up the Kubernetes cluster. Please make sure these tools are installed and available in your `$PATH`.

- [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-kubectl) - Kubernetes command-line tool.
- [helm](https://docs.helm.sh/using_helm/#installing-helm) - Package management for Kubernetes. Refer to the [Helm version requirements](https://ranchermanager.docs.rancher.com/getting-started/installation-and-upgrade/resources/helm-version-requirements) to choose a version of Helm to install Rancher. Refer to the [instructions provided by the Helm project](https://helm.sh/docs/intro/install/) for your specific platform.

## Install the Rancher Helm Chart[​](#install-the-rancher-helm-chart "Direct link to Install the Rancher Helm Chart")

Rancher is installed using the [Helm](https://helm.sh/) package manager for Kubernetes. Helm charts provide templating syntax for Kubernetes YAML manifest documents. With Helm, we can create configurable deployments instead of just using static files.

For systems without direct internet access, see [Air Gap: Kubernetes install](https://ranchermanager.docs.rancher.com/getting-started/installation-and-upgrade/other-installation-methods/air-gapped-helm-cli-install/install-rancher-ha).

To choose a Rancher version to install, refer to [Choosing a Rancher Version.](https://ranchermanager.docs.rancher.com/getting-started/installation-and-upgrade/resources/choose-a-rancher-version)

To choose a version of Helm to install Rancher with, refer to the [Helm version requirements](https://ranchermanager.docs.rancher.com/getting-started/installation-and-upgrade/resources/helm-version-requirements)

note

The installation instructions assume you are using Helm 3.

To set up Rancher,

1.  [Add the Helm chart repository](#1-add-the-helm-chart-repository)
2.  [Create a namespace for Rancher](#2-create-a-namespace-for-rancher)
3.  [Choose your SSL configuration](#3-choose-your-ssl-configuration)
4.  [Install cert-manager](#4-install-cert-manager) (unless you are bringing your own certificates, or TLS will be terminated on a load balancer)
5.  [Install Rancher with Helm and your chosen certificate option](#5-install-rancher-with-helm-and-your-chosen-certificate-option)
6.  [Verify that the Rancher server is successfully deployed](#6-verify-that-the-rancher-server-is-successfully-deployed)
7.  [Save your options](#7-save-your-options)

### 1\. Add the Helm Chart Repository[​](#1-add-the-helm-chart-repository "Direct link to 1. Add the Helm Chart Repository")

Use `helm repo add` command to add the Helm chart repository that contains charts to install Rancher. For more information about the repository choices and which is best for your use case, see [Choosing a Rancher Version](https://ranchermanager.docs.rancher.com/getting-started/installation-and-upgrade/resources/choose-a-rancher-version).

- Latest: Recommended for trying out the newest features
    
    ```text
    helm repo add rancher-latest https://releases.rancher.com/server-charts/latest
    ```
    
- Stable: Recommended for production environments
    
    ```text
    helm repo add rancher-stable https://releases.rancher.com/server-charts/stable
    ```
    
- Alpha: Experimental preview of upcoming releases.
    
    ```text
    helm repo add rancher-alpha https://releases.rancher.com/server-charts/alpha
    ```
    
    Note: Upgrades are not supported to, from, or between Alphas.

### 2\. Create a Namespace for Rancher[​](#2-create-a-namespace-for-rancher "Direct link to 2. Create a Namespace for Rancher")

We'll need to define a Kubernetes namespace where the resources created by the Chart should be installed. This should always be `cattle-system`:

```text
kubectl create namespace cattle-system
```

### 3\. Choose your SSL Configuration[​](#3-choose-your-ssl-configuration "Direct link to 3. Choose your SSL Configuration")

The Rancher management server is designed to be secure by default and requires SSL/TLS configuration.

note

If you want to externally terminate SSL/TLS, see [TLS termination on an External Load Balancer](https://ranchermanager.docs.rancher.com/getting-started/installation-and-upgrade/installation-references/helm-chart-options#external-tls-termination). As outlined on that page, this option does have additional requirements for TLS verification.

There are three recommended options for the source of the certificate used for TLS termination at the Rancher server:

- **Rancher-generated TLS certificate:** In this case, you will need to install `cert-manager` into the cluster. Rancher utilizes `cert-manager` to issue and maintain its certificates. Rancher will generate a CA certificate of its own, and sign a cert using that CA. `cert-manager` is then responsible for managing that certificate. No extra action is needed when `agent-tls-mode` is set to strict. More information can be found on this setting in [Agent TLS Enforcement](https://ranchermanager.docs.rancher.com/getting-started/installation-and-upgrade/installation-references/tls-settings#agent-tls-enforcement).
- **Let's Encrypt:** The Let's Encrypt option also uses `cert-manager`. However, in this case, cert-manager is combined with a special Issuer for Let's Encrypt that performs all actions (including request and validation) necessary for getting a Let's Encrypt issued cert. This configuration uses HTTP validation (`HTTP-01`), so the load balancer must have a public DNS record and be accessible from the internet. When setting `agent-tls-mode` to `strict`, you must also specify `--privateCA=true` and upload the Let's Encrypt CA as described in [Adding TLS Secrets](https://ranchermanager.docs.rancher.com/getting-started/installation-and-upgrade/resources/add-tls-secrets). More information can be found on this setting in [Agent TLS Enforcement](https://ranchermanager.docs.rancher.com/getting-started/installation-and-upgrade/installation-references/tls-settings#agent-tls-enforcement).
- **Bring your own certificate:** This option allows you to bring your own public- or private-CA signed certificate. Rancher will use that certificate to secure websocket and HTTPS traffic. In this case, you must upload this certificate (and associated key) as PEM-encoded files with the name `tls.crt` and `tls.key`. If you are using a private CA, you must also upload that certificate. This is due to the fact that this private CA may not be trusted by your nodes. Rancher will take that CA certificate, and generate a checksum from it, which the various Rancher components will use to validate their connection to Rancher. If `agent-tls-mode` is set to `strict`, the CA must be uploaded, so that downstream clusters can successfully connect. More information can be found on this setting in [Agent TLS Enforcement](https://ranchermanager.docs.rancher.com/getting-started/installation-and-upgrade/installation-references/tls-settings#agent-tls-enforcement).

| Configuration | Helm Chart Option | Requires cert-manager |
| --- | --- | --- |
| Rancher Generated Certificates (Default) | `ingress.tls.source=rancher` | [yes](#4-install-cert-manager) |
| Let’s Encrypt | `ingress.tls.source=letsEncrypt` | [yes](#4-install-cert-manager) |
| Certificates from Files | `ingress.tls.source=secret` | no  |

### 4\. Install cert-manager[​](#4-install-cert-manager "Direct link to 4. Install cert-manager")

> You should skip this step if you are bringing your own certificate files (option `ingress.tls.source=secret`), or if you use [TLS termination on an external load balancer](https://ranchermanager.docs.rancher.com/getting-started/installation-and-upgrade/installation-references/helm-chart-options#external-tls-termination).

This step is only required to use certificates issued by Rancher's generated CA (`ingress.tls.source=rancher`) or to request Let's Encrypt issued certificates (`ingress.tls.source=letsEncrypt`).

Click to Expand

### 5\. Install Rancher with Helm and Your Chosen Certificate Option[​](#5-install-rancher-with-helm-and-your-chosen-certificate-option "Direct link to 5. Install Rancher with Helm and Your Chosen Certificate Option")

The exact command to install Rancher differs depending on the certificate configuration.

However, irrespective of the certificate configuration, the name of the Rancher installation in the `cattle-system` namespace should always be `rancher`.

Testing and Development:

This final command to install Rancher requires a domain name that forwards traffic to Rancher. If you are using the Helm CLI to set up a proof-of-concept, you can use a fake domain name when passing the `hostname` option. An example of a fake domain name would be `<IP_OF_LINUX_NODE>.sslip.io`, which would expose Rancher on an IP where it is running. Production installs would require a real domain name.

- Rancher-generated Certificates
- Let's Encrypt
- Certificates from Files

The default is for Rancher to generate a CA and uses `cert-manager` to issue the certificate for access to the Rancher server interface.

Because `rancher` is the default option for `ingress.tls.source`, we are not specifying `ingress.tls.source` when running the `helm install` command.

- Set the `hostname` to the DNS name you pointed at your load balancer.
- Set the `bootstrapPassword` to something unique for the `admin` user.
- To install a specific Rancher version, use the `--version` flag, example: `--version 2.7.0`
- For Kubernetes v1.25 or later, set `global.cattle.psp.enabled` to `false` when using Rancher v2.7.2-v2.7.4. This is not necessary for Rancher v2.7.5 and above, but you can still manually set the option if you choose.

```text
helm install rancher rancher-<CHART_REPO>/rancher \
  --namespace cattle-system \
  --set hostname=rancher.my.org \
  --set bootstrapPassword=admin
```

If you are installing an alpha version, Helm requires adding the `--devel` option to the install command:

```text
helm install rancher rancher-alpha/rancher --devel
```

Wait for Rancher to be rolled out:

```text
kubectl -n cattle-system rollout status deploy/rancher
Waiting for deployment "rancher" rollout to finish: 0 of 3 updated replicas are available...
deployment "rancher" successfully rolled out
```

The Rancher chart configuration has many options for customising the installation to suit your specific environment. Here are some common advanced scenarios.

- [HTTP Proxy](https://ranchermanager.docs.rancher.com/getting-started/installation-and-upgrade/installation-references/helm-chart-options#http-proxy)
- [Private Container Image Registry](https://ranchermanager.docs.rancher.com/getting-started/installation-and-upgrade/installation-references/helm-chart-options#private-registry-and-air-gap-installs)
- [TLS Termination on an External Load Balancer](https://ranchermanager.docs.rancher.com/getting-started/installation-and-upgrade/installation-references/helm-chart-options#external-tls-termination)

See the [Chart Options](https://ranchermanager.docs.rancher.com/getting-started/installation-and-upgrade/installation-references/helm-chart-options) for the full list of options.

### 6\. Verify that the Rancher Server is Successfully Deployed[​](#6-verify-that-the-rancher-server-is-successfully-deployed "Direct link to 6. Verify that the Rancher Server is Successfully Deployed")

After adding the secrets, check if Rancher was rolled out successfully:

```text
kubectl -n cattle-system rollout status deploy/rancher
Waiting for deployment "rancher" rollout to finish: 0 of 3 updated replicas are available...
deployment "rancher" successfully rolled out
```

If you see the following error: `error: deployment "rancher" exceeded its progress deadline`, you can check the status of the deployment by running the following command:

```text
kubectl -n cattle-system get deploy rancher
NAME      DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
rancher   3         3         3            3           3m
```

It should show the same count for `DESIRED` and `AVAILABLE`.

### 7\. Save Your Options[​](#7-save-your-options "Direct link to 7. Save Your Options")

Make sure you save the `--set` options you used. You will need to use the same options when you upgrade Rancher to new versions with Helm.

### Finishing Up[​](#finishing-up "Direct link to Finishing Up")

That's it. You should have a functional Rancher server.

In a web browser, go to the DNS name that forwards traffic to your load balancer. Then you should be greeted by the colorful login page.

Doesn't work? Take a look at the [Troubleshooting](https://ranchermanager.docs.rancher.com/getting-started/installation-and-upgrade/install-upgrade-on-a-kubernetes-cluster/troubleshooting) Page

[Edit this page](https://github.com/rancher/rancher-docs/edit/main/docs/getting-started/installation-and-upgrade/install-upgrade-on-a-kubernetes-cluster/install-upgrade-on-a-kubernetes-cluster.md)

Last updated on **Aug 19, 2024**

[Previous<br>Feature Flags](https://ranchermanager.docs.rancher.com/getting-started/installation-and-upgrade/installation-references/feature-flags)[Next<br>Rollbacks](https://ranchermanager.docs.rancher.com/getting-started/installation-and-upgrade/install-upgrade-on-a-kubernetes-cluster/rollbacks)

- [Prerequisites](#prerequisites)
    - [Kubernetes Cluster](#kubernetes-cluster)
    - [Ingress Controller](#ingress-controller)
    - [CLI Tools](#cli-tools)
- [Install the Rancher Helm Chart](#install-the-rancher-helm-chart)
    - [1\. Add the Helm Chart Repository](#1-add-the-helm-chart-repository)
    - [2\. Create a Namespace for Rancher](#2-create-a-namespace-for-rancher)
    - [3\. Choose your SSL Configuration](#3-choose-your-ssl-configuration)
    - [4\. Install cert-manager](#4-install-cert-manager)
    - [5\. Install Rancher with Helm and Your Chosen Certificate Option](#5-install-rancher-with-helm-and-your-chosen-certificate-option)
    - [6\. Verify that the Rancher Server is Successfully Deployed](#6-verify-that-the-rancher-server-is-successfully-deployed)
    - [7\. Save Your Options](#7-save-your-options)
    - [Finishing Up](#finishing-up)

Copyright © 2024 SUSE Rancher. All Rights Reserved.