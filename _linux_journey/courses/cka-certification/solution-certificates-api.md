---
title: "Solution Certificates Api"
category: "cka-certification"
tags: ["cka-certification", "solution", "certificates", "api"]
---

* Create a CertificateSigningRequest object with the name `akshay`, contents of `akshay.csr`. The API is `certificates.k8s.io/v1`. Add an additional field called`signerName`. For client authentication, use`kubernetes.io/kube-apiserver-client`
* Solution to the above:
* Create the `base64` encoded format:
```
cat akshay.csr | base64 -w 0
```
* Save this into a file:
```
---
apiVersion: certificates.k8s.io/v1
kind: CertificateSigningRequest
metadata:
  name: akshay
spec:
  groups:
  - system:authenticated
  request: <Paste the base64 encoded value of the CSR file>
  signerName: kubernetes.io/kube-apiserver-client
  usages:
  - client auth
```
* Apply the `yaml` file:
```
kubectl apply -f akshay-csr.yaml
```
* Find the condition of a Certificate Signing Record with:
```
kubectl get csr
```
* Can also use the above command to check the amount of `csr` requests on the cluster.
* How to check the group a CSR is coming from:
```
kubectl get csr agent-smith -o yaml | grep system
```
* How to deny a request:
```
kubectl certificate deny agent-smith
```
* How to delete a request:
```
kubectl delete csr agent-smith
```

* Generally don't want to give `system:masters` powers to a regular user.