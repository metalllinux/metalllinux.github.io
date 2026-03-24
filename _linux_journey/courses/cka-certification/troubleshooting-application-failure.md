---
title: "Troubleshooting - Application Failure"
category: "cka-certification"
tags: ["cka-certification", "troubleshooting", "application", "failure"]
---

# Troubleshooting - Application Failure

* Database pod hosts a database application and serves the web servers via an application.

    * The web server is hosted on a web pod and serves users.
    
* Its good to write down and map out how the application is configured before starting.

    * For example --> `DB` --> `DB-Service` --> `WEB` --> `WEB-Service` --> User
    
        * For troubleshooting, check every object and link in this map to find the root cause of the issue.
        
* For example, we have users whom are having difficulties in accessing the application.

    * If it is a web application, check that the IP port is available by the user using `curl`:
    
```
curl http://web-service-ip:node-port
```

    * Next, check the web service - has it discovered endpoints for the `WEB` pod?
    
        * You can use `kubectl describe serice web-service`.
        
    * Compare the `Selector` configured on the service (output from the above `kubectl describe` command) to the ones on the pod.
    
        * Make sure the Selectors match what is in the YAML object.
        
* Check the pod itself and make sure it is in a `running` state. The amount of restarts is good to check if the application itself is restarting or not.

* Can also check the following:

```
kubectl get pod

kubectl describe pod web

kubectl logs web
```

* However, one thing to keep in mind is the current version of the pod's logs, may not match the previous fail state.

    * You can watch the logs with the `-f` options using `kubectl logs web -f` or use the `--previous` option to view the logs of a previous pod like so:
    
```
kubectl logs web -f --previous
```

* Check the status of the DB Service.

* Check the logs of the DB pod.
