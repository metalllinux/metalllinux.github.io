---
title: "Worker Node Failure"
category: "cka-certification"
tags: ["cka-certification", "worker", "node", "failure"]
---

# Worker Node Failure

* Check the status of the Nodes. Are they reported as `Ready` or `Not Ready`:

```
kubectl get nodes
```

* If reported as `Not Ready`, run the `kubectl describe node <node_name>` command. This can help point towards why a node fails.

    * Depending on the status of the `kubectl describe` command, it is either set to `True`, `False` or `Unknown`.
    
    * When a node is out of disk space, the `OutOfDisk` flag is set to true.
    
    * When a node is out of memory, the `MemoryPressure` flag is set to true.
    
    * When disk capacity is low, the `DiskPressure` flag is set to true.
    
    * When there are too many processes, the `PIDPressure` flag is set to true.
    
    * If the node as a whole is healthy, the `Ready` flag is set to true.
    
    * When a worker node stops communicating with the Master Node, either due to a crash or other reason, the above statuses are set to `Unknown`

            * Can indicate possible loss of a node. Check the `LastHeartbeatTime` field, for the time the node may have crashed.
            
                * Check if the worker node is online at all or if it has crashed.
                
                    * If it is crashed, bring it back up.
                    
                        * Check for CPU, memory and disk issues with tools like `top` and `df -h`.
                        
                        * Check the status of the `kubelet`. Check the `kubelet` logs for possible issues, using commands such as `service kubelet status` and `sudo journalctl -u kubelet`.
                        
                        * Check the `kubelet` certificates and ensure they are not expired. 
                        
                            * Check that the certificates are part of the right group and that the certificates are part of the right CA.
                            
                                `openssl x509 -in /var/lib/kubelet/worker-1.crt -text`
                                
                                    * Check the `Validity` section and `Issuer`.
