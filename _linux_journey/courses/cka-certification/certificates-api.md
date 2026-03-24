---
title: "Certificates Api"
category: "cka-certification"
tags: ["cka-certification", "certificates", "api"]
---

* Certificate Workflow and API.
* The admin will have their own certificate and key.
* What if there is another admin added?
	* We need to get them a certificate and keypair.
	* They generate a certificate signing request.
	* The request is then sent to the current admin.
	* The admin then sends that signing request to the Certificate Authority server, has it signed using the CA server's private key and root certificate.
	* The certificate is then sent back.
	* The certificate has a validity period. When the certificate expires, the previous setup is ran.
* Whoever has access to the CA's private key and root certificate can generate as many certs as they like, with any privileges they want.
* The environment then needs to be secured.
* The Master Node can also act as a Certificate Authority.
* `kubeadm` creates a pair of CA files (private key and root certificate).
* Kubernetes has a Certificates API.
	* The certificate request is sent directly to Kubernetes through an API call.
	* In this case, when the current admin receives a Certificate Signing Request, they do the following:
1. Create a CertificateSigningRequest Object.
2. Review Requests.
3. Approve Requests.
4. Share certs to users.
The above can be done easily using `kubectl` commands.
* How is the above done?
* The user first generates a key:
```
openssl genrsa -out jane.key 2048

jane.key
```
```
openssl req -new -key jane.key -subj "/CN=jane" -out jane.csr

certificate request
```
* Then a certificate signing request object is created:
```
jane-csr.yaml
apiVersion: certificates.k8s.io/v1
kind: CertificateSigningRequest
metadata:
  name: jane
spec:
  expirationSeconds: 600
  usages:
  - digital signature
  - key encipherment
  - server auth
  request:
     <base64_encoded_version_of_the_certificate_request_file_goes_here>
```
* The `request:` field is where you specify the signing request sent by the user.
* The Certificate Request must be encoded in `base64` like so:
```
cat jane.csr | base64 
```
* All Certificate Signing Request can be seen by Administrators by running the `kubectl get csr` command.
* Approve any requests by running:
```
kubectl certificate approve jane
```
* The certificate can then be extracted and shared with the user.
* To view the certificate in a `yaml` format:
```
kubectl get csr jane -o yaml
```
* The generated certificate under `certificate:` is part of the output.
* This will be in a `base64` encoded format.
* To decode it and get the proper certificate, place the certificate into an `echo` command and then decode it:
```
echo "<cert_here>" | base64 --decode
```
* In the Control Plane, you have the following:
```
kube-api server, scheduler, controller-manager, etcd-server
```
* All certificate-related operations are carried out by the Controller Manager.
* Inside the Controller Manager are the following components:
* CSR-APPROVING
* CSR-SIGNING
* These are responsible for acrrying out the tasks.
* To find the Kube Controller Manager's settings, go to `/etc/kubernetes/manifests/kube-controller-manager.yaml`
	* You can specify the Certificate Authority's root certificate location and private key location:
```
--cluster-signing-cert-file=/etc/kubernetes/pki/ca.crt
--cluster-signing-key-file=/etc/kubernetes/pki/ca.key
```
