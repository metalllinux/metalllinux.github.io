---
title: "Docker Vs. Containerd"
category: "cka-certification"
tags: ["cka-certification", "docker", "containerd"]
---

* Differences between them are the following.
* CLI Tools.
	* `docker` - `ctr`
	* `containerd` - `crictl`
	* `nerdctl`
* In the beginning there was `docker` (`rkt` was also available).
	* `docker` made containers super simple.
	* `kubernetes` only used to work with `docker` only.
* `kubernetes` users needed `kubernetes` to run with other runtimes aside from `docker`.
* There, `kubernetes` introduced an interface called `Container Runtime Interface (CRI)`
	* `CRI` allow any vendor to work as a container runtime.
	* As long as the vendor adheres to the OCIstands (Open Container Initiative) --> imagespec and runtimespec
		* `imagespec` - specifications on how an image should be built.
		* `runtimespec` - defines the standards on how a container runtime should be developed.
	* This then allowed `rkt` to be supported via CRI.
* `docker` was not initially built to support he `CRI` standards.
	* `kubernetes` introduced `dockershim` - allowed the support of `docker` outside of the `CRI`.
* `docker` consists of the following `CLI`, `API`, `BUILD`, `VOLUMES`, `AUTH`, `SECURITY` and `containerd`.
	* The Container Runtime for `docker` was `runc`. What managed `runc` was `containerd`.
		* `containerd` is CRI compatible and can work with Kubernetes like all other runtimes.
		* `containerd` can be used as a runtime on its own, separate from `docker`.
* `kubernetes` kept supporting `docker`, but having to support `dockershim` added unnessary effort.
	* `dockershim` was removed in v1.24 of `kubernetes`.
		* All images built before `docker` was removed, continued to work due to `docker` following the OCI standard.
			* These images continued to work with `containerd`.
* Specifically looking at `containerd`.
	* Part of `docker`, but is a separate project in its own right. It is a member of the CNCF. Can install `containerd` without requiring `docker` itself.
		* Typically we run containers with the `docker run` command, but how do we do that if `docker` is not available?
			* The tool that comes with containerD is `ctr` - used from debugging `containerD`. Aside from that, interaction with `containerD` is done through API calls.
				* The `nerdctl` command provides a stable and friendly experience.
* To pull an image using the `ctr` command, you would do `ctr images pull docker.io/library/redis:alpine`
* To run a container, we use `ctr run docker.io/library/redis:alpine redis`.
* The better alternative is `nerdctl`
	* Provides a `docker`-like CLI for 	`containerD`.
	* Supports `docker compose`.
	* Supports encrypted container images.
	* Lazy pulling.
	* P2P image distribution.
	* Image signing and verifying.
	* Namespaces in Kubernetes.
		* None of the above are available in Docker.
* Just replace the `docker` command with `nerdctl`. Can run all `docker` commands like this.
	* For example `docker run --name redis redis:alp`, with `nerdctl` this would be with `nerdctl run --name redis redis:alpine`
	* Another example is `docker run --name webserver -p 80:80 -d nginx` in `nerdctl` is `nerdctl run --name webserver -p 80:80 -d nginx`
	* `nerdctl` specifically created for `containerD`
* CLI - crictl
	* `crictl provides a CLI for CRI compatible container runtimes` - it connect them as a single interface.
	* Installed separately.
	* Used to inspect and debug container runtimes.
		* Not to create containers ideally.
			* That is the job of `docker` or `nerdctl`.
	* Works across different runtimes.
	* Developed and maintained by the Kubernetes community.
	* It works alongside the kubelet.
	* The kubelet is responsible for ensuring a specific number of containers or pods are available on a node at at time.
		* If you create containers with the CRI utility, `kubelet` will eventually remove them.  The `kubelet` is unaware of those containers and pods that have been created. Anything it sees, it will go and delete.
			* CRI Control Utility is oinly for debugging purposes.
* `crictl` command line examples.
	* `crictl` is helpful for basic container-related activities such as pulling images.
		* `crictl pull busybox`
	* Or listing existing images, listing containers.
		* `crictl images`
		* `crictl ps -a`
			* To exec a command in a container, run `crictl exec -i -t <container_id> ls`
* Find logs with `crictl logs <container_name>`
* `crictl pods` - `crictl` command is aware of pods, which `docker` and `nerdctl` are not.
* `docker` commands are useful to troubleshoot containers and view logs - especially on Worker Nodes.
* The below chart lists the comparisons between `docker` and the `CRI Control` tool
![Screenshot_select-area_20240808215328.png](../../_resources/Screenshot_select-area_20240808215328.png)
![Screenshot_select-area_20240808215640.png](../../_resources/Screenshot_select-area_20240808215640.png)
* Prior to version 1.24, the CRI tool connected to runtime endpoints. 
![Screenshot_select-area_20240808215755.png](../../_resources/Screenshot_select-area_20240808215755.png)
* Post Kubernetes 1.24, a significant change was made. 
![Screenshot_select-area_20240808215916.png](../../_resources/Screenshot_select-area_20240808215916.png)
* Updated default endpoints were changed.
* `crictl --runtime-endpoint`
* `export CONTAINER_RUNTIME_ENDPOINT`
	* Users are encouraged to manually set the endpoint.
		* Changes are documented in the Kubernetes CRI Tools GitHub Repo.
* https://github.com/kubernetes-sigs/cri-tools/issues/868
* https://github.com/kubernetes-sigs/cri-tools/pull/869
* Summary:
![Screenshot_select-area_20240808220517.png](../../_resources/Screenshot_select-area_20240808220517.png)

