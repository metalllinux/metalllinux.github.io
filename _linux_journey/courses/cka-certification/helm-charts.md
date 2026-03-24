---
title: "Helm Charts"
category: "cka-certification"
tags: ["cka-certification", "helm", "charts"]
---

# Helm Charts

* Helm goes through all of the required steps, without bothering the user for the details.

* How does Helm know how to achieve the goal of `helm install`.

    * `Charts` are like an instruction manual for packages.

* In the `values.yaml` file, find parameters which are passed to the Chart.

* Apart from the `values.yaml` file, every chart has a `Chart.yaml` file:
```
apiVersion: v2
appVersion: "1.16.0"
name: hello-world
description: A web application

type: application
```

* The chart `apiVersion` can either be `v1` or `v2`.

* The `appVersion` defines the version of the application.

* When `helm 2` existed, the `apiVersion` part did not exist.

* Helm 3 needed a way to differentiate charts built in the past with `Helm 2`, with what is needed in Helo 3.

    * `apiVersion` now allows Helm 3.
    
    * Helm 2 ignores the above field.
    
    * If the `apiVersion` field doesn't exist, then this is definitely a `Helm 2` chart.
    
* `appVersion` refers to the version of the application.

    * The field is only for informational purposes - it doesn't do anything else apart from that.
    
* `version` version of the chart itself. Every chart must have its own version - helps in making changes to the chart itself.

* There are two types of charts: `application` and `library`.

    * `application` is the default type for a chart.
    * `library` is a utility that helps in building charts.
    
* The `wordpress` application is a two tiered approach.

* `dependencies` - in the above example, no need to merge the charts from the MariaDB, it pulls in the dependencies.

* `home` and `icon` doesn't mattter.

* The chart structure consists of the following:
```
hello-world-chart
    templates
    values.yaml
    Chart.yaml
    LICENSE
    README.md
    charts (directory and contains charts that the main chart depends on)
```
