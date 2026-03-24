---
title: "Cockpit and Timeout Reasons Whilst Doing Training"
category: "general-linux"
tags: ["cockpit", "timeouts", "when", "deploying", "environment"]
---

# Cockpit and Timeout Reasons Whilst Doing Training

Hey y’all. I think Jonathan figured out why we have been having so many issues with cockpit and timeouts with the training. It has to do with using the same ip for two instances of an application. Cookies are scoped per domain and not per port so there are collisions and the cockpit instances get confused. As an alternative I think we should test and potentially move to

https://vmhost.208.167.236.84.nip.io:9090/
And

https://warewulf.208.167.236.84.nip.io:9091/
As an example. This would scope those cookies correctly and potentially fix our problems

