---
title: "Useful Advice On Oom Killers"
category: "general-linux"
tags: ["useful", "advice", "oom", "killers"]
---

Maybe they should check the database logs to see why the OOM killer was forced to stop the process. There will be access logs that log requests, which will likely highlight the real cause. The database itself will also have server logs that may contain crucial information. Monitoring the K8s node but not the DB inside isn't providing anything useful. It seems a lot like these guys have zero understanding of how to monitor a database. I'm sure Oracle offers a service to help them. Be careful here. Their expectations from the call, imo, are completely removed from reality. From my experience, running a DB inside K8s is more trouble than its worth. Not something I've ever seen in the wild, esp. in prod.