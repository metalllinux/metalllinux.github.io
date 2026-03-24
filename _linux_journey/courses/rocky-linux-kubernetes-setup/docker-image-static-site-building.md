---
title: "Docker Image Static Site Builder"
category: "rocky-linux-kubernetes-setup"
tags: ["rocky-linux-kubernetes-setup", "docker", "image", "static", "site"]
---

# Docker Image Static Site Builder

* Create the website building directory, `src` and `html` directories:

```
mkdir -p ~/metalinux_docs/src/html
```

* Make the `index.html` file:

```
cat <<EOF | tee ~/metalinux_docs/src/html/index.html
<!DOCTYPE html>
<html>

<body>
    <h1>Hello!</h1>
    <img src="metalinux-1.png" />
    <h1>Test</h1> 
    <img src="metalinux-1.png" />
    <p>Test</p>
</body>

</html>
EOF
```

* Add pictures of your choice into `~/metalinux_docs/src/html/`

* Create the `Dockerfile`:

```
cat <<EOF | tee ~/metalinux_docs/Dockerfile
FROM nginx:1.29.1-alpine
COPY src/html /usr/share/nginx/html
EXPOSE 80/tcp

# Documentation
# CMD ["nginx", "-g", "daemon off;"]
EOF
```

* Change directory into the `~/metalinux_docs/src/html/` directory:

```
cd ~/metalinux_docs/
```

* Build the Docker Image:

```
docker build -t metalinux-docs .
```

* Check the image was build:

```
docker images
```

* Check that the image can be ran as a container:

```
docker run -d -p 80:80 <image_id> 
```

* Go to `localhost` in the browser.

* Create the `.dockerignore` file:

```
cat <<EOF | tee ~/metalinux_docs/.dockerignore
**/file_name
EOF
```

* Login to Docker:

```
docker login
```

* Push the image to DockerHub:

```
docker tag metalinux-docs:latest metalllinux/metalinux-docs:latest
docker push metalllinux/metalinux-docs:latest
```

* Install `docker` on the Master Node.

* On the Master Node, log into `docker`:

```
docker login
```

* Copy the credential into Kubernetes:

```
kubectl create secret generic regcred \
    --from-file=.dockerconfigjson=~/.docker/config.json \
    --type=kubernetes.io/dockerconfigjson
```

* Create a manifests directory if there is not one already:

```
mkdir -p ~/manifests
```

* Declaratively it can be done like so:

```
cat <<EOF | tee ~/manifests/metalinux_docs-secret.yaml
apiVersion: v1
kind: Secret
metadata:
  name: dockerhub-secret
  namespace: metalinux-docs
data:
  .dockerconfigjson: ewoJImF1dGhzIjogewoJCSJodHRwczovL2luZGV4LmRvY2tlci5pby92MS8iOiB7CgkJCSJhdXRoIjogImJXVjBZV3hzYkdsdWRYZzZaR05yY2w5d1lYUmZTRVpCVnpjelYyWkhaRXRzZG1WV0xXNXRUM2gxTjBwdVVYQloiCgkJfSwKCQkiaHR0cHM6Ly9pbmRleC5kb2NrZXIuaW8vdjEvYWNjZXNzLXRva2VuIjogewoJCQkiYXV0aCI6ICJiV1YwWVd4c2JHbHVkWGc2WlhsS2FHSkhZMmxQYVVwVFZYcEpNVTVwU1hOSmJsSTFZME5KTmtscmNGaFdRMGx6U1cxMGNGcERTVFpKYm1oWllUTkNRMlJFVG5sV00wMTVVbmt4TVZscWJITmpSWEJ1WTFOS09TNWxlVXB2WkVoU2QyTjZiM1pNTW1neFdXazFhMkl5VG5KYVdFbDFXVEk1ZEVscWNEZEpiVlowV1Zkc2MwbHFiMmxoUnpreldWaEthMHh0UlhWa2JVWjFXa2RXZVdReVJuTlJTRUo1WWpOU2RtSnRNV2hoVjNkMVdUSTVkRWxwZDJsak1sWjZZekpzZG1Kc09YQmFRMGsyU1dwT2FVMXRXWGxQVkUxNVRGUmthVTF0U1hST1JHUnNUV2t3TlU1SFZtcE1WRUV4VDBSc2FWcEVSbTFQVkd4b1dXbEpjMGx1VG5aa1dFcHFXbE5KTmtsdFJqRmtSMmQzU1dsM2FXUllUbXhqYlRWb1lsZFZhVTlwU25SYVdGSm9Za2Q0YzJGWE5URmxRMGx6U1c1V01XRlhVV2xQYVVwcFQxUkdhRTlFWXpOTlV6QXdXbGRWTUV4VVVYcE9SRkYwV1cxU2JVMXBNV3hhYWsxNlRWZFpkMWxxV1hkWmJWbHBabE4zYVdGWVRucEphbTlwWVVoU01HTklUVFpNZVRsellqSmtjR0pwTld0aU1rNXlXbGhKZFZreU9YUk1lVWx6U1c1T01WbHBTVFpKYlVZeFpFZG5kMlpIU1RWTlYwVTBUbnBqZUV4VVVteGFWRkYwVGtSTk1FNURNV2xhUjFsNVRGZFdiVTE2VFhoYWFrSnBUbXBDYVZwcFNYTkpiVVl4V2tOSk5sZDVTbTlrU0ZKM1kzcHZka3d5YURGWmFUVnJZakpPY2xwWVNYVlpNamwwU1dsM2FXRklVakJqU0UwMlRIazVhMkl5VG5KYVdFbDBZMGhLZGxwRE5URmplVFZvWkZoU2IwMUROV3BpTWpCMlpGaE9iR050YkhWYWJUaHBXRk4zYVdGWFJqQkphbTk0VG5wVk1VMXFXWGxOZWxVd1RFTktiR1ZJUVdsUGFrVXpUbFJWZVU1cVZUVk9WRkZ6U1c1T2FtSXpRbXhKYW05cFlqTkNiR0p0Ykd0SlJ6bHRXbTE0Y0dKdFZtWlpWMDVxV2xoT2VrbHBkMmxaV0hCM1NXcHZhVlJFVWpKTlIxSjBZa1UxUTJOR2JGWmhhMlJJV1ZkSmQxRjZTa3RrUjJSVldqRm9lVTFXUmpaT1IxRnBabEV1VW10UGRURmpSMFJEYWxKQlRubFhhMGhaT0dwRFlWQk1VV3hNY2tkSmJtTnhkVVpFVDI4MmIzTTRSRlpmZWxKaWMyWjFVbmxwYWxseFkyaDJURmxQVFZWTFJrZEpUekU0UkVjelZEaGZaRXd5ZW5oS2VHUlJaazFZWmpSTlpsQjNXa0ZDV2tnMk9HRkNRbm8wYm0xUmIyZDNOVGxuUkRCQlIyZ3pNbWhDWjFaVVRHNDVPSEY1Ym5CblVrMVpRVlJmYXpRdFdHZDVkakpuVGxsS1FqRjRNRGgxUTNGZlRtOXlla1pUVVdkV05ERk9jMFYwTTFGYVNtZFhlbTlET1ZsaWMzZHJZbWRRVlROWVUyRlJNMEp2WWw5d2JqQnhaa1J5VDFCQ2NsWmxhRlY0TlVacE5DMXNkblJYWkZOT1YycE5UVU4wVXpGNlMwWnJVbWhIUjJ0Mk9FMXVRelpzTlV4dGJIQTRVRmxRUXpGSmNHWkJSbXRSYlZwR2RVeDFORko0ZUcxVGJrMVRSR3h5UVZKRU1rcHJiVW96YmpWNFMyMURlSFJ2T1dkT1JHMDFPR3hUVjFkdGRXdDBUVGxaY0RSbU9WRTNSbmRCIgoJCX0sCgkJImh0dHBzOi8vaW5kZXguZG9ja2VyLmlvL3YxL3JlZnJlc2gtdG9rZW4iOiB7CgkJCSJhdXRoIjogImJXVjBZV3hzYkdsdWRYZzZkakV1VFZGbVQwVnhkVkV4YjBaNFkweDVkbmw1Y21kUVFrbGtVRk5UVUc1U05VMVJkMmhhUWxOcVpEUnZTbVpXWm1kZmVXUmpibUpmWWxCak9HRm1UbUZyYUdvd1VtaHBjemhLTFV0WVpXNHpTbGh5YTFaSlVtcFZMaTVNTkhZd1pHMXNUa0p3V1ZWcVIwZGhZakJETWtwMFoxUm5XSEl4VVhvMFpBPT0iCgkJfQoJfQp9   
type: kubernetes.io/dockerconfigjson
EOF
```

* The `.docker/config.json` file has to be base64 encoded:

```
cat ~/.docker/config.json | base64 | tr -d '\n'
```

* Apply the manifest:

```
kubectl apply -f ~/manifests/metalinux_docs-secret.yaml
```

* Output the secret with this command:

```
kubectl get secret dockerhub-secret -n metalinux-docs --output="jsonpath={.data.\.dockerconfigjson}" | base64 --decode
```

* Create the pod that uses my secret:

```
cat <<EOF | tee ~/manifests/metalinux_docs-pod.yaml
apiVersion: v1
kind: Pod
metadata:
  name: metalinux-docs
  namespace: metalinux-docs
spec:
  replicas: 2
  selector:
    matchLabels:
      app: metalinux-docs
spec:
  containers:
  - name: metalinux-docs-container
    image: metalllinux/metalinux-docs:latest
    ports: 
    - containerPort: 80
  imagePullSecrets:
  - name: dockerhub-secret
EOF
```

* Create the service for the `metalinux-docs` pod:

```
cat <<EOF | tee ~/manifests/metalinux_docs-service.yaml
apiVersion: v1
kind: Service
metadata:
  name: metalinux-docs-service
  namespace: metalinux-docs
spec:
  type: LoadBalancer
  selector:
    app: metalinux-docs
  ports:
  - port: 80
    targetPort: 80
EOF
```

* Apply the service manifest:

```
kubectl apply -f ~/manifests/metalinux_docs-service.yaml 
```

* Follow Cloudflare's instructions until you generate the tunnel token: https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/deployment-guides/kubernetes/

* Convert the token into base64:

```
cat token | base64 -w 0
```

* Create the tunnel token manifest for Cloudflare:

```
cat <<EOF | tee ~/manifests/metalinux_docs-cloudflare-tunnel-secret.yaml
apiVersion: v1
data:
    token: ZXlKaElqb2lNVEF6WVRJMU9UZGpNVGhsTnpWaU1URTNPVEpqWXpFNU1qUTNPV1U0TnpRaUxDSjBJam9pTkRFME1XRXpOV1V0TVRRME5pMDBNVEl3TFdFeE5XRXROVE01T1dVd016RXpZMlZtSWl3aWN5STZJazVVWnpWWmFrcHFUWHBaZEU1VVNYcFplVEF3V1hwSmVVeFVaM2RPYW1OMFdWUnJlazVFUVRWT1ZGVjZUV3BKTVNKOQo=
kind: Secret
metadata:
    name: cloudflare-tunnel-secret
    namespace: metalinux-docs
type: Opaque
EOF
```

* Generate the secret:

```
kubectl apply -f ~/manifests/metalinux_docs-cloudflare-tunnel-secret.yaml
```

* Make the Cloudflare Tunnel Pod:

```
cat <<EOF | tee ~/manifests/metalinux_docs-cloudflare-tunnel-pod.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cloudflared-deployment
  namespace: metalinux-docs
spec:
  replicas: 2
  selector:
    matchLabels:
      pod: cloudflared
  template:
    metadata:
      labels:
        pod: cloudflared
    spec:
      securityContext:
        sysctls:
        # Allows ICMP traffic (ping, traceroute) to resources behind cloudflared.
          - name: net.ipv4.ping_group_range
            value: "65532 65532"
      containers:
        - image: cloudflare/cloudflared:latest
          name: cloudflared
          env:
            # Defines an environment variable for the tunnel token.
            - name: TUNNEL_TOKEN
              valueFrom:
                secretKeyRef:
                  name: cloudflare-tunnel-secret
                  key: token
          command:
            # Configures tunnel run parameters
            - cloudflared
            - tunnel
            - --no-autoupdate
            - --loglevel
            - debug
            - --metrics
            - 0.0.0.0:2000
            - run
          livenessProbe:
            httpGet:
              # Cloudflared has a /ready endpoint which returns 200 if and only if
              # it has an active connection to Cloudflare's network.
              path: /ready
              port: 2000
            failureThreshold: 1
            initialDelaySeconds: 10
            periodSeconds: 10
EOF
```

* Create the Cloudflare Tunnel Pod:

```
kubectl apply -f ~/manifests/metalinux_docs-cloudflare-tunnel-pod.yaml
```

* Add a tunnel route. Go to the `Zero Trust Home` --> `Networks` --> `Tunnels`. Press the hamburger menu and select `Configure`. Then navigate to `Public hostnames` and then click `Add a public hostname`.

* For `Domain`, I put `howards-linux-journey-notes.wiki `

* For `Service`, I put `metalinux-docs-service` and set the `Type` to `HTTPS`

* Go to Cloudflare's main page and add your nameserver. 
