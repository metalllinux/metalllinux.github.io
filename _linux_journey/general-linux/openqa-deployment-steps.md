---
title: "Openqa Deployment Steps"
category: "general-linux"
tags: ["openqa", "deployment", "steps"]
---

```
podman run --name openqa --device /dev/kvm -p 1080:80 -p 1443:443 --detach \
  registry.opensuse.org/devel/openqa/containers/openqa-single-instance
```
```
podman exec openqa openqa-clone-job https://openqa.fedoraproject.org/tests/3336535
```
```
podman exec -it openqa openqa-cli monitor
```
```
wget -q0 scenario-definitions.yaml \
› https://raw.githubusercontent.com/os-autoinst/os-autoinst-distri-example/main/ scenario-definitions.yaml
```
```
podman cp scenario-definitions.yaml openqa:scenario-definitions.yaml
```
```
podman exec -it openqa openqa-cli schedule --monitor --param-file SCENARIO_DEFINITIONS_YAML=scenario-definitions.yaml DISTRI=example VERSION=0 FLAVOR=DVD ARCH=x86_64 TEST=simple_boot _GROUP_ID=0 BUILD=test https://github.com/os-autoinst/os-autoinst-distri-example.git NEEDLES_DIR=%%CASEDIR%%/needles
```
* Exec into the container with:
```
podman exec -ti openqa /bin/bash
```