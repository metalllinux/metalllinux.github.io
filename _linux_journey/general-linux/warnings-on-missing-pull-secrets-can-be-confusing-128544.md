---
title: "Warnings on missing pull secrets can be confusing #128544"
category: "general-linux"
tags: ["warnings", "missing", "pull", "secrets", "confusing"]
---

# Warnings on missing pull secrets can be confusing #128544

THESE CAN BE IGNORED IN KUBERNETES

https://github.com/kubernetes/kubernetes/issues/128544

Jamstah
opened on Nov 5, 2024 · edited by Jamstah
What happened?
A previous enhancement has added a warning event when a pull secret is missing: #117927

If the image has pulled successfully because either another pull secret did the job, or the image doesn't need auth, the warning is distracting.

As an example, this pod is running perfectly fine and has no problems, and yet when described, has had 11k warning events emitted over the last 9 days.

  Warning  FailedToRetrieveImagePullSecret  114s (x11399 over 9d)  kubelet  Unable to retrieve some image pull secrets (sa-integration); attempting to pull the image may not succeed.
We have been including multiple pull secrets in our pulls because it's more flexible to point to a few that may exist than to have to very exactly map each pod to a pull secret. This change means we will get warnings even when everything is working exactly as we wanted it to.

What did you expect to happen?
No warnings if an image is pulled successfully.

How can we reproduce it (as minimally and precisely as possible)?
Create a pod or service account that references a missing pull secret that is not required to pull the image.

Anything else we need to know?
My suggestion would be to only emit that warning if the image cannot be pulled (for example, reaches ImagePullBackOff), or to include the detail about the missing secret in the existing image pull failure events.

Kubernetes version
Details
Cloud provider
Details
OS version
Details
Install tools
Details
Container runtime (CRI) and version (if applicable)
Details
Related plugins (CNI, CSI, ...) and versions (if applicable)
Details
Activity

Jamstah
added 
kind/bug
Categorizes issue or PR as related to a bug.
 on Nov 5, 2024

k8s-ci-robot
added 
needs-sig
Indicates an issue or PR lacks a `sig/foo` label and requires one.
 
needs-triage
Indicates an issue or PR lacks a `triage/foo` label and requires one.
 on Nov 5, 2024
Jamstah
Jamstah commented on Nov 5, 2024
Jamstah
on Nov 5, 2024
Author
/sig node


k8s-ci-robot
added 
sig/node
Categorizes an issue or PR as relevant to SIG Node.
 and removed 
needs-sig
Indicates an issue or PR lacks a `sig/foo` label and requires one.
 on Nov 5, 2024

github-project-automation
added this to  SIG Node Bugson Nov 5, 2024

github-project-automation
moved this to Triage in  SIG Node Bugson Nov 5, 2024
Jamstah
Jamstah commented on Nov 5, 2024
Jamstah
on Nov 5, 2024
Author
FYI @kaisoz as the PR creator, and @seh and @kannon92 as the reviewers of the original PR that introduces the warning.

seh
seh commented on Nov 5, 2024
seh
on Nov 5, 2024
Contributor
I got involved with the aforementioned #117927 innocently, offering copyediting suggestions for the English language messages it emitted. Reading it again today, the patch looks sound, in the sense that it warns someone that the controller was not able to do what the pod author asked it to do: Namely, fetch these Secrets. If the pod author had misspelled a Secret name, or forgot to create the Secret, it's helpful to learn about that mismatch and dangling reference.

What you're asking for here changes the meaning of image pull secrets, treating them lazily as advice that may not turn out to be necessary: Try to pull this image, and if you can't, try again with any of these credentials that might be available.

That's what the kubelet is doing today, given that it proceeds even if it can't pull all the nominated Secrets, but the warning indicates that it's operating in a degraded mode. I take it that you'd prefer to think of this lack of Secrets being available as possibly intentional, and you don't want to hear about that lack until and unless it turns out to matter.

Jamstah
Jamstah commented on Nov 5, 2024
Jamstah
on Nov 5, 2024
Author
I don't think I'm asking to change the meaning, they are already lazy. The fact that you can specify multiple is a good indicator of that - why would you need multiple is you just expect the one specified pull secret to work?

Otherwise, spot on - a missing pull secret could very well be intentional (as designed) and not something we want to be warned about unnecessarily.

seh
seh commented on Nov 5, 2024
seh
on Nov 5, 2024
Contributor
I haven't thought through this carefully, but would you consider predicating this behaviour on a new annotation on the containing Pod?

I can't think of any precedent for controlling the telemetry about an object like this, but while I'd prefer to add a "disposition" to each entry in the "ImagePullSecrets" field, we can't do so, since those are LocalObjectReferences containing only a name.

Jamstah
Jamstah commented on Nov 5, 2024
Jamstah
on Nov 5, 2024
Author
I would consider it, but I'm not sure it's the right pattern.

Also, thinking about it, the other reason for multiple pull secrets is that you can have multiple containers in a pod, and multiple pods sharing a service account. I still think it makes them lazy, but perhaps with different intentions.

Either way, the new warning changes behaviour we previously relied on, and is making our customers jumpy.


Jamstah
mentioned this on Nov 11, 2024
Only warn about missing pull secrets if image pull fails #128732
Jamstah
Jamstah commented on Nov 11, 2024
Jamstah
on Nov 11, 2024 · edited by Jamstah
Author
I've raised #128732 for this one which stops the warning from being emitted unless the image pull also fails.

sftim
sftim commented on Nov 12, 2024
sftim
on Nov 12, 2024
Contributor
I'm not sure we should accept this. Other people may be relying on the existing pattern of event emission.

Jamstah
Jamstah commented on Nov 12, 2024
Jamstah
on Nov 12, 2024 · edited by Jamstah
Author
We were relying on missing pull secrets being silently ignored for a long time (before the existing warning was added), so that could be argued both ways :)

This change still reports the missing pull secret when image pull fails, which is when it could be helpful. If image pull hasn't failed, the warning is likely false, and distracting. Our clusters currently have hundreds of warnings being emitted when everything is working perfectly.

kaisoz
kaisoz commented on Nov 13, 2024
kaisoz
on Nov 13, 2024
Contributor
@Jamstah, sorry for this late reply! I've thought about your proposal, and I think it makes sense. One could argue whether a pod should really reference secrets that it won't use, but on the other hand, I agree that the current warning feels too generic. I like the idea of emitting it only if there is an error. 👍🏻

Jamstah
Jamstah commented on Nov 13, 2024
Jamstah
on Nov 13, 2024
Author
Thanks, I'm glad it still meets your needs :)

Jamstah
Jamstah commented on Nov 14, 2024
Jamstah
on Nov 14, 2024 · edited by Jamstah
Author
As an example of the issue, this pod is running perfectly fine and has no problems, and yet when described, has had 11k warning events emitted over the last 9 days.

jammy@mac007470 ~ % oc describe pod ace-dashboard-dash-6df758874d-z5tb5
Name:             ace-dashboard-dash-6df758874d-z5tb5
Namespace:        integration
Priority:         0
Service Account:  ace-dashboard-dash
...
Status:           Running
...
Conditions:
  Type                        Status
  PodReadyToStartContainers   True 
  Initialised                 True 
  Ready                       True 
  ContainersReady             True 
  PodScheduled                True 
...
Events:
  Type     Reason                           Age                    From     Message
  ----     ------                           ----                   ----     -------
  Warning  FailedToRetrieveImagePullSecret  114s (x11399 over 9d)  kubelet  Unable to retrieve some image pull secrets (sa-integration); attempting to pull the image may not succeed.
Jamstah
Jamstah commented on Nov 14, 2024
Jamstah
on Nov 14, 2024
Author
Also see: kubernetes/website#48718

kannon92
kannon92 commented on Dec 21, 2024
kannon92
on Dec 21, 2024
Contributor
Given there is a PR up,

/triage accepted
/priority important-soon


k8s-ci-robot
added 
triage/accepted
Indicates an issue or PR is ready to be actively worked on.
 
priority/important-soon
Must be staffed and worked on either currently, or very soon, ideally in time for the next release.
 and removed 
needs-triage
Indicates an issue or PR lacks a `triage/foo` label and requires one.
 on Dec 21, 2024

kannon92
moved this from Triage to Triaged in  SIG Node Bugson Dec 21, 2024
SergeyKanzhelev
SergeyKanzhelev commented on Mar 13, 2025
SergeyKanzhelev
on Mar 13, 2025
Member
/remove-priority important-soon

/priority backlog


k8s-ci-robot
added 
priority/backlog
Higher priority than priority/awaiting-more-evidence.
 and removed 
priority/important-soon
Must be staffed and worked on either currently, or very soon, ideally in time for the next release.
 on Mar 13, 2025
Jamstah
Jamstah commented on Mar 31, 2025
Jamstah
on Mar 31, 2025
Author
@SergeyKanzhelev this PR is now back in a ready to go state (since 2 weeks ago), but hasn't seen any reviewers yet.

Would putting the priority back help? I'm not really familiar with the workflow of the project :/
