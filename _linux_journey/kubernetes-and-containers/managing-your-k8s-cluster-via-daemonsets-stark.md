---
title: "Managing Your K8S Cluster Via Daemonsets Stark &"
category: "kubernetes-and-containers"
tags: ["kubernetes-and-containers", "managing", "your", "k8s", "cluster"]
---

[](https://starkandwayne.com/blog/managing-your-kubernetes-cluster-with-daemonsets/../../index.html)

- [Services](https://starkandwayne.com/blog/managing-your-kubernetes-cluster-with-daemonsets/index.html#)
    - [Consulting](https://starkandwayne.com/blog/managing-your-kubernetes-cluster-with-daemonsets/../../services-consulting/index.html)
    - [Google KF Migration](https://starkandwayne.com/blog/managing-your-kubernetes-cluster-with-daemonsets/../../google-kf-migration/index.html)
    - [Kubernetes Services](https://starkandwayne.com/blog/managing-your-kubernetes-cluster-with-daemonsets/../../services-kubernetes/index.html)
    - [Cloud Foundry Services](https://starkandwayne.com/blog/managing-your-kubernetes-cluster-with-daemonsets/../../services-cloud-foundry/index.html)
    - [Open Source](https://starkandwayne.com/blog/managing-your-kubernetes-cluster-with-daemonsets/../../services-open-source/index.html)
- [Resource centre](https://starkandwayne.com/blog/managing-your-kubernetes-cluster-with-daemonsets/index.html#)
    - [Case Studies](https://starkandwayne.com/blog/managing-your-kubernetes-cluster-with-daemonsets/../../case-studies/index.html)
    - [Concourse Tutorial](https://concoursetutorial.com/)
    - [Silly Kubectl Tricks](https://starkandwayne.com/blog/managing-your-kubernetes-cluster-with-daemonsets/../../silly-kubectl-tricks/index.html)
    - [Ultimate Guide to BOSH](https://ultimateguidetobosh.com/)
- [Blog](https://starkandwayne.com/blog/managing-your-kubernetes-cluster-with-daemonsets/../index.html)
- [About Us](https://starkandwayne.com/blog/managing-your-kubernetes-cluster-with-daemonsets/index.html#)
    - [About S&W](https://starkandwayne.com/blog/managing-your-kubernetes-cluster-with-daemonsets/../../about-us/index.html)
    - [Qarik + S&W](https://starkandwayne.com/blog/managing-your-kubernetes-cluster-with-daemonsets/../../qarik-acquires-stark-and-wayne/index.html)
    - [Careers](https://starkandwayne.com/blog/managing-your-kubernetes-cluster-with-daemonsets/../../careers/index.html)
- [Contact Us](https://www.starkandwayne.com/contact-us/)

# Managing Your k8s Cluster via DaemonSets

March 20, 2020

By [Ashley Gerwitz](https://starkandwayne.com/blog/managing-your-kubernetes-cluster-with-daemonsets/../author/agerwitz/index.html "Posts by Ashley Gerwitz")

This one goes out to all the cluster operators.

It really isn’t fair. All those application folks get to play with cool stuff like automatic traffic routing based on label matches, process resurrection, and more. All services provided by *the clusters **we run**.* We’re still on the hook for figuring out how to [spin those clusters](https://kubernetes.io/docs/setup/production-environment/tools/kops/), [configure them](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm/), [patch them](https://github.com/jhunt/k8s-boshrelease/), etc, but we don’t get to use Kubernetes for that.

Or, do we?

I’m here to tell you that you ***can*** use Kubernetes to manage parts of Kubernetes itself.

No, I’m not talking about [static pods for the control plane](https://kubernetes.io/docs/tasks/configure-pod-container/static-pod/), although that is a great strategy. I’m talking about applying all those other layers of software, systems, and configurations that invariably accompany running ***anything*** in production.

We’re going to use **DaemonSets**.

There’s a ton of stuff we can do with the ability to run a single pod on each node in our cluster. To keep this blog post from approaching book-length, I’m going to focus in on three tasks I want to accomplish:

1.  Provision a named admin account for SSH access & troubleshooting
2.  Modify some kernel tuning parameters via `sysctl` and friends
3.  Run **ClamAV** for scanning nodes for unsavory files

## Provisioning SSH Access to Nodes

This one works especially well on managed Kubernetes offerings like [Linode Kubernetes Engine (LKE)](https://www.linode.com/products/kubernetes/), Amazon’s EKS, etc.

```
---apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: cluster-admin
spec:
  selector:
    matchLabels:
      aikido: cluster-admin
  template:
    metadata:
      labels:
        aikido: cluster-admin
    spec:
      volumes:
        - name: hostfs
          hostPath:
            path: /
      initContainers:
        - name: init
          image: alpine
          command:
            - /bin/sh
            - -xc
            - |
              chroot /host getent passwd jhunt || chroot /host useradd -m jhunt \
              && chroot /host chsh -s /bin/bash jhunt \
              && echo "jhunt ALL=(ALL:ALL) NOPASSWD:ALL" > /host/etc/sudoers.d/jhunt \
              && mkdir -p /host/home/jhunt/.ssh \
              && chmod 0700 /host/home/jhunt/.ssh \
              && chroot /host chown -R jhunt:jhunt /home/jhunt \
              && echo "ssh-PUBLIC-KEY-HERE" > /host/home/jhunt/.ssh/authorized_keys \
              && echo done
          volumeMounts:
            - name: hostfs
              mountPath: /host
      containers:
        - name: sleep
          image: filefrog/k8s-hacks:pause
```

That’s a lot. Let’s take it bit by bit.

We’re setting up a **DaemonSet**, which means we’ll get exactly one pod on each cluster node (kubelet) that we have. That holds true now, and in the future as we scale the cluster up or down. New nodes will automatically gain one of these `cluster-admin` pods.

The pods themselves consist of two containers: an *init container* that does all of the work, and a regular container that just sleeps, to make Kubernetes happy. We have a volume, called `hostfs` that represents the *node filesystem* (note the `path: /` under the volume’s `hostPath` configuration.

The init container mounts this volume, and it does so in **read-write** mode. This is risky, so if and when you do this for real, *audit the images you are running!*

The init container (an alpine base image) does most of its stuff via an explicit command. You can also do this via a ConfigMap, if you want. That command is a rough translation of this shell script:

```
# add `jhunt` to /etc/passwd, /etc/shadow,
# et al, if the account doesn't already exist
#
if ! chroot /host getent passwd jhunt; then
  chroot /host useradd -m jhunt
fi
# he'll use bash thank you very much.
chroot /host chsh -s /bin/bash jhunt
# jhunt needs full sudo access...
echo "jhunt ALL=(ALL:ALL) NOPASSWD:ALL" > /host/etc/sudoers.d/jhunt
# set up for SSH key-based authentication.
mkdir -p /host/home/jhunt/.ssh
chmod 0700 /host/home/jhunt/.ssh
chroot /host chown -R jhunt:jhunt /home/jhunt
echo "ssh-PUBLIC-KEY-HERE" > /host/home/jhunt/.ssh/authorized_keys
```

Once the init container has done its thing, I should be able to access any cluster node via SSH, using my private key. Once on-box, I’ll be comfortably at home in bash, with full root access to the box via sudo.

Most of the trickier parts of this configuration rely on knowing when to `chroot` into the `/host` mountpoint, which you’ll recall is the actual root filesystem of each Kubernetes node. For example, when checking for the existence of the “jhunt” account, we have to `chroot /host getent ...`, otherwise we’ll be looking at the *init container’s* user database.

After the init container winds down, Kubernetes is left with nothing to execute but the `filefrog/k8s-hacks:pause` image. You can find the full code for that over at its GitHub repo, https://github.com/jhunt/k8s-hacks/tree/master/pause.

## Tuning Node Kernel Parameters

We recently ran into a particularly nasty bug involving unbearable and inexplicable network slowdowns between Linux hosts. I won’t bore you with the details in this blog post – although I ***do*** reserve the right to devote an entire, other blog post to that very subject – but at the end of the day, the culprit was `net.ipv4.tcp_tw_recycle` having been enabled.

Unless [you know precisely what you are doing](https://vincent.bernat.ch/en/blog/2014-tcp-time-wait-state-linux), it’s best to just turn it off.

We can use our **DaemonSet** pattern to do just that, on all nodes, for all time.

```
---
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: sysctl
spec:
  selector:
    matchLabels:
      aikido: sysctl
  template:
    metadata:
      labels:
        aikido: sysctl
    spec:
      hostNetwork: yes
      initContainers:
        - name: init
          image: alpine
          command:
            - /bin/sh
            - -c
            - sysctl net.ipv4.tcp_tw_recycle=0
          securityContext:
            privileged: true
      containers:
        - name: sleep
          image: filefrog/k8s-hacks:pause
```

There’s a few things to note about this example.

First and foremost, there is no `hostPath` mount. We don’t need one in this case, since we have access to `/proc`, and all we are doing is running `sysctl` to change kernel parameters.

Secondly, this is a more-privileged-than-normal configuration. The entire pod exists in the *host* network namespace (`hostNetwork: yes`). It must, because we want to interact with the tuning parameters for the host’s network interfaces (i.e., the real `eth0`). The init container is also `privileged: yes`, since it needs real root permission to change settings in the kernel.

A really great thing about this setup is that now, no matter what the underlying AMI, golden disk image, or BOSH stemcell, is doing, as soon as a node is put into this cluster, it won’t be recycling TCP `TIME_WAIT` states.

## Running ClamAV Against Nodes

Finally, we’re going to use a **DaemonSet** to install a cluster-wide, per-node software addon: ClamAV antivirus.

The particulars of the *actual implementation* of ClamAV in OCI images is a bit beyond the scope of this blog post. I’ve packaged up the image in an upstream git repository, available at https://github.com/filefrog/clamav.

Here’s a cut-down version of the Kubernetes YAML spec for this little hack, edited for brevity and clarity. [The full version can be found here](https://gist.github.com/jhunt/21190d872fced7f45ac2b7adc83c67c3).

```
---
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: clamd
spec:
  selector:
    matchLabels:
      aikido: clamd
  template:
    metadata:
      labels:
        aikido: clamd
    spec:
      volumes:
        - name: host
          hostPath:
            path: /
      containers:
        - name: clamd
          image: filefrog/clamav
          volumeMounts:
            - name: host
              mountPath: /host
              readOnly: yes
```

There’s a lot more to this [in the real gist](https://gist.github.com/jhunt/21190d872fced7f45ac2b7adc83c67c3). It includes a second container for regularly updating the virus definitions database, properly initializes those databases via an init container, and provides some additional configuration to make scanning more resilient.

The easiest way to apply this to your cluster is via URL:

```
$ kubectl apply -f https://bit.ly/2vSOxwm
configmap/clamav created
daemonset.apps/clamd created
$ kubectl get pods
NAME           READY   STATUS    RESTARTS   AGE
clamd-swgkb    2/2     Running   0          63s
```

*(**Note**: you should see one container per cluster node; my demo environment is a single-node cluster, so I only have the one pod.)*

Don’t worry if it seems like it’s taking forever to come up – `clamd` has a lot of virus definitions to read in. Once both containers are in the Ready state, you’ll be ready to start interacting with ClamAV.

The DaemonSet doesn’t have any Service instances in front of it. While `clamd` is listening on TCP/3310, on all interfaces, it is *not* in the `hostNetwork` namespace, so the only way to reach it is via either ***port-forwarding*** or `kubectl exec`.

*(We explicitly **do not** expose the TCP/3310 port via a ClusterIP, NodePort, or LoadBalancer Service because ClamAV doesn’t perform any authentication against clients connecting to it. This means anyone who can open a connection can ask clamd to scan whatever they want. This is a gaping security hole, and a very low-risk amplificaiton attack / denial of service. [You can read more here](https://blog.clamav.net/2016/06/regarding-use-of-clamav-daemons-tcp.html).)*

First, we’ll try port-forwarding and running telnet locally.

```
$ kubectl port-forward clamd-swgkb 3310:3310
Forwarding from 127.0.0.1:3310 -> 3310
Forwarding from [::1]:3310 -> 3310
$ telnet 127.0.0.1 3310
Trying ::1...
Connected to localhost.
Escape character is '^]'.
```

The image we’re using to run ClamAV has a copy of the [EICAR test file](https://en.wikipedia.org/wiki/EICAR_test_file), a benign payload that is explicitly recognised by most antivirus solutions (including ClamAV) and categorised as a positive payload match.

We can use the `SCAN` command to test this out:

```
$ telnet 127.0.0.1 3310
Trying ::1...
Connected to localhost.
Escape character is '^]'.
SCAN /var/lib/eicar/eicar.com
/var/lib/eicar/eicar.com: Win.Test.EICAR_HDB-1 FOUND
Connection closed by foreign host.
```

Next, we’ll try to just exec clamdscan inside the container:

```
$ kubectl exec -it clamd-swgkb -c clamd \
  -- clamdscan /var/lib/eicar/eicar.com
/var/lib/eicar/eicar.com: Win.Test.EICAR_HDB-1 FOUND
----------- SCAN SUMMARY -----------
Infected files: 1
Time: 0.022 sec (0 m 0 s)
command terminated with exit code 1
```

Now that we’re satisfied that ClamAV is in fact running, and can detect malware and other unsavory and dangerous payloads, we can scan the whole `/host` mount, looking for dangerous things on the *cluster nodes themselves*.

```
$ kubectl exec -it clamd-swgkb -c clamd \
  -- clamdscan /host
/host: OK
----------- SCAN SUMMARY -----------
Infected files: 0
Time: 291.040 sec (4 m 51 s)
```

## Go Forth and Manage!

We can do a lot ***with Kubernetes*** to ***manage Kubernetes***. If you can find or build an OCI image to package up the software, you can use namespaces, extra capabilities, and host filesystem mounts (if your Pod Security Policies allow it) to do all the things you normally resort to configuration management and other platform automation tools for.

<img width="64" height="64" src="../_resources/3785cb89435a42400395d8d3cc65e689_faeaae06932c47f5a.jpg"/>

Written by:  
**Ashley Gerwitz**

Marketing Manager at Stark & Wayne and Qarik

Spread the word

![twitter icon](../_resources/twitter-b_91a7015545e54760b1978f8e2aa25796.svg) ![facebook icon](../_resources/facebook-b_7c82763f29ec4cf785ac73451194f07d.svg)![linkedin icon](../_resources/linkedin-b_03d4b15075cf40e185c31213f3cd5a4a.svg)

![Stark & Wayne Logo Footer](../_resources/S_W-Horizontal-logo-White-Lime-G_d6dbe60f2a834f0c8.png)

Stark & Wayne is the premier Kubernetes, Cloud Foundry, Cloud Native, Serverless platform consulting firm.

[Contact us](https://www.qarik.com/contact) today to help build out, secure, and systematically update your cloud platform.

### Services

- [Consulting](https://starkandwayne.com/blog/managing-your-kubernetes-cluster-with-daemonsets/../../services-consulting/index.html)
- [Google KF Migration](https://starkandwayne.com/blog/managing-your-kubernetes-cluster-with-daemonsets/../../google-kf-migration/index.html)
- [Kubernetes Services](https://starkandwayne.com/blog/managing-your-kubernetes-cluster-with-daemonsets/../../services-kubernetes/index.html)
- [Cloud Foundry Services](https://starkandwayne.com/blog/managing-your-kubernetes-cluster-with-daemonsets/../../services-cloud-foundry/index.html)
- [Open Source](https://starkandwayne.com/blog/managing-your-kubernetes-cluster-with-daemonsets/../../services-open-source/index.html)

### Resource centre

- [Case Studies](https://starkandwayne.com/blog/managing-your-kubernetes-cluster-with-daemonsets/../../case-studies/index.html)
- [Concourse Tutorial](https://concoursetutorial.com/)
- [Silly Kubectl Tricks](https://starkandwayne.com/blog/managing-your-kubernetes-cluster-with-daemonsets/../../silly-kubectl-tricks/index.html)
- [Ultimate Guide to BOSH](https://ultimateguidetobosh.com/)

### Reference

- [About Us](https://starkandwayne.com/blog/managing-your-kubernetes-cluster-with-daemonsets/../../about-us/index.html)
- [Blog](https://starkandwayne.com/blog/managing-your-kubernetes-cluster-with-daemonsets/../index.html)
- [Careers](https://starkandwayne.com/blog/managing-your-kubernetes-cluster-with-daemonsets/../../careers/index.html)
- [Contact Us](https://www.starkandwayne.com/contact-us/)
- [About Qarik](https://www.qarik.com)

Copyright © 2024, Stark & Wayne

<a id="facebook"></a>[![facebook icon](../_resources/facebook_91c8f30710ba4380b7ea58e13e218dbe.svg)](https://www.facebook.com/starkandwayne) <a id="twitter"></a>[![twitter icon](../_resources/twitter_661dfc883f9743729d59d2ab9f8d653d.svg)](https://twitter.com/starkandwayne)<a id="linked in"></a>[![linkedin icon](../_resources/linkedin_a6711e6466224f69a567b550c0687fd5.svg)](https://www.linkedin.com/company/qarik)<a id="youtube"></a>[![youtube icon](../_resources/youtube_71bce2046e8a48d6a88cd5f3c3802c09.svg)](https://www.youtube.com/user/StarkAndWayne)<a id="github"></a>[![github icon](../_resources/github_a963b96c971d4518a88ad9a8207a534d.svg)](https://github.com/starkandwayne)