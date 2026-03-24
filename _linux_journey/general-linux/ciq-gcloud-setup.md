---
title: "Ciq Gcloud Setup"
category: "general-linux"
tags: ["ciq", "gcloud", "setup"]
---

Overview

Only those who have been granted access will be able to access CIQ’s gcloud.  For now, the only use case is to pull down IQube images.  The current CI pushes the latest build to a GCP artifacts repository.
gcloud CLI
To get started, you will need to install the glcoud CLI.  The instructions can be found here: 

https://cloud.google.com/sdk/docs/install#rpm

Authentication Setup

The next step is to setup the authentication.  You should pay attention to the instructions for using gcloud and docker.  We do not need to use a service account. We will want to use us-west1 for the region.

The specific instructions can be found here:

https://cloud.google.com/container-registry/docs/advanced-authentication#gcloud-helper

Using Apptainer

Once you have the credentials from the prior step, you can use Apptainer to pull down the SIF images from GCP.

You will need to configure Apptainer by editing the ~/.apptainer/docker-config.json and add a section for credential helpers to use gcloud for authenticating.

```
{
        "auths": {
        },
        "credHelpers": {
                "us-west1-docker.pkg.dev": "gcloud",
                "gcr.io": "gcloud",
                "us.gcr.io": "gcloud",
                "eu.gcr.io": "gcloud",
                "asia.gcr.io": "gcloud",
                "staging-k8s.gcr.io": "gcloud",
                "marketplace.gcr.io": "gcloud"
        }
}
```