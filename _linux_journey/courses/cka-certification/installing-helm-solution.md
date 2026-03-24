---
title: "Installing Helm - Solution"
category: "cka-certification"
tags: ["cka-certification", "installing", "helm", "solution"]
---

# Installing Helm - Solution

* One method of installing the Helm package:
```
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
chmod 700 get_helm.sh
./get_helm.sh
```

* Identify the version of `helm` with:
```
helm version
```

* Which environment variable can help show if `helm` is running in `debug` mode?
```
helm --help
```
* Check under `Environment variables`.
* The answer is:
```
$HELM_DEBUG                        | indicate whether or not Helm is running in Debug mode
```

* A command line flag that enables verbose output is `--debug`.

* How to check valid commands with `helm get`, use `helm get --help` 
* These are the available commands:
```
Available Commands:
  all         download all information for a named release
  hooks       download all hooks for a named release
  manifest    download the manifest for a named release
  metadata    This command fetches metadata for a given release
  notes       download the notes for a named release
  values      download the values file for a named release
```
