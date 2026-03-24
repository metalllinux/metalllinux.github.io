---
title: "Kustomize Output"
category: "cka-certification"
tags: ["cka-certification", "kustomize", "output"]
---

# Kustomise Output

* How do we apply these configs with `kustomize build`.

* To actually apply the commands, have to use this command here:
```
kustomize build k8s/ | kubectl apply -f -
```

* Can also apply the configurations another way using this command:
```
kubectl apply -k k8s/
```

* You can also delete the resources using this command:
```
kustomize build k8s/ | kubectl delete -f -
```

* To do this natively with `kubectl`, run `kubectl delete -k k8s/`

    * The `-k` flag means `kustomize`.
