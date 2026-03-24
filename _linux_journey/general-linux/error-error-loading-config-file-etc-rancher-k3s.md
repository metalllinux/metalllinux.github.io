---
title: "Error Error Loading Config File Etc Rancher K3S"
category: "general-linux"
tags: ["error", "error", "loading", "config", "file"]
---

[Skip to main content](#content)

[](#)

1.  [](https://devops.stackexchange.com/help "Help centre and other resources")
2.  [](https://stackexchange.com "A list of all 183 Stack Exchange sites")

5.  [Log in](https://devops.stackexchange.com/users/login?ssrc=head&returnurl=https%3a%2f%2fdevops.stackexchange.com%2fquestions%2f16043%2ferror-error-loading-config-file-etc-rancher-k3s-k3s-yaml-open-etc-rancher)
6.  [Sign up](https://devops.stackexchange.com/users/signup?ssrc=head&returnurl=https%3a%2f%2fdevops.stackexchange.com%2fquestions%2f16043%2ferror-error-loading-config-file-etc-rancher-k3s-k3s-yaml-open-etc-rancher)

[DevOps](https://devops.stackexchange.com)

1.  1.  [Home](https://devops.stackexchange.com/)
    2.  <a id="nav-questions"></a>[Questions](https://devops.stackexchange.com/questions)
    3.  [Tags](https://devops.stackexchange.com/tags)
    
    5.  <a id="nav-users"></a>[Users](https://devops.stackexchange.com/users)
    6.  <a id="nav-labs-jobs"></a>[Jobs](https://devops.stackexchange.com/jobs?source=so-left-nav)
    7.  <a id="nav-companies"></a>[Companies](https://stackoverflow.com/jobs/companies?so_medium=devops&so_source=SiteNav)
    8.  <a id="nav-unanswered"></a>[Unanswered](https://devops.stackexchange.com/unanswered)
2.  Teams
    
    <img width="140" height="24" src="../_resources/teams-promo_6b654156b09143109880a08114cc921e.htm"/>
    
    Ask questions, find answers and collaborate at work with Stack Overflow for Teams.
    
https://devops.stackexchange.com/questions/16043/error-error-loading-config-file-etc-rancher-k3s-k3s-yaml-open-etc-rancher
[](https://devops.stackexchange.com/posts/16043/timeline)

When I run commands under `k3s kubectl`, I get

```
$ k3s kubectl version
WARN[0000] Unable to read /etc/rancher/k3s/k3s.yaml, please start server with --write-kubeconfig-mode to modify kube config permissions 
error: error loading config file "/etc/rancher/k3s/k3s.yaml" : open /etc/rancher/k3s/k3s.yaml: permission denied
```

How should I resolve this? Should I change the permissions of `/etc/rancher/k3s/k3s.yaml`

- [rancher](https://devops.stackexchange.com/questions/tagged/rancher "show questions tagged 'rancher'")
- [k3s](https://devops.stackexchange.com/questions/tagged/k3s "show questions tagged 'k3s'")

[Share](https://devops.stackexchange.com/q/16043 "Short permalink to this question")

[Improve this question](https://devops.stackexchange.com/posts/16043/edit)

asked May 31, 2022 at 19:53

<img width="32" height="32" src="../_resources/605442f85418d858e2ce1e1aea2092bb_397f4b32295443bd9.png"/>](https://devops.stackexchange.com/users/18965/evan-carroll)

[Evan Carroll](https://devops.stackexchange.com/users/18965/evan-carroll)

2,611

66 gold badges

3333 silver badges

8181 bronze badges

[Add a comment](# "Use comments to ask for more information or suggest improvements. Avoid answering questions in comments.")

<a id="tab-top"></a>

## 2 Answers

Sorted by:

<a id="16044"></a>

32

[](https://devops.stackexchange.com/posts/16044/timeline)

# No, do not change permissions of `/etc/rancher/k3s/k3s.yaml`

First set up your an environmental variable for `KUBECONFIG=~/.kube/config`.

```
export KUBECONFIG=~/.kube/config
```

Then let's generate the file at that location. [Your `k3s.yaml` file should **NOT** be world readable.](https://github.com/k3s-io/k3s/issues/389). This is by-design. It should be owned by root and set to `0600`. Instead copy the config locally as [described here](https://devops.stackexchange.com/a/16014/18965),

```
mkdir ~/.kube 2> /dev/null
sudo k3s kubectl config view --raw > "$KUBECONFIG"
chmod 600 "$KUBECONFIG"
```

You can add `export KUBECONFIG=~/.kube/config` to your `~/.profile` or `~/.bashrc` to make it persist on reboot.

[Share](https://devops.stackexchange.com/a/16044 "Short permalink to this answer")

[Improve this answer](https://devops.stackexchange.com/posts/16044/edit)

[edited Nov 29 at 18:45](https://devops.stackexchange.com/posts/16044/revisions "show all edits to this post")

<img width="32" height="32" src="../_resources/j5pNC_2afb9ccb2b6340d9b6f03d5df2157982.htm"/>](https://devops.stackexchange.com/users/44615/emil-carpenter)

[Emil Carpenter](https://devops.stackexchange.com/users/44615/emil-carpenter)

103

33 bronze badges

answered May 31, 2022 at 19:53

<img width="32" height="32" src="../_resources/605442f85418d858e2ce1e1aea2092bb_397f4b32295443bd9.png"/>](https://devops.stackexchange.com/users/18965/evan-carroll)

[Evan Carroll](https://devops.stackexchange.com/users/18965/evan-carroll)

2,611

66 gold badges

3333 silver badges

8181 bronze badges

- If the "sudo k3s kubectl ..." line is giving an error stating "sudo: k3s: command not found", then you can try by adding `/usr/local/bin/` in front of "k3s". Which would make that line as this: `sudo /usr/local/bin/k3s kubectl config view --raw > "$KUBECONFIG"`
    
    – [UNOPARATOR](https://devops.stackexchange.com/users/36269/unoparator "101 reputation")
    
    [Commented Aug 1, 2022 at 7:30](#comment17001_16044)
    
- @UNOPARATOR the only way that could make a difference is if `/usr/local/bin` is not in your `$PATH` which would be pretty awkward anyway.
    
    – [Evan Carroll](https://devops.stackexchange.com/users/18965/evan-carroll "2,611 reputation")
    
    [Commented Aug 1, 2022 at 15:34](#comment17002_16044)
    
- In my case with a CentOS 8 Stream server, after the k3s installation that line wasn't working. There was no mention of adding that to `$PATH` but it might be considered common practice and not mentioned because of that. I'm no linux expert of any kind, just commented in case someone like me encounters the same issue.
    
    – [UNOPARATOR](https://devops.stackexchange.com/users/36269/unoparator "101 reputation")
    
    [Commented Aug 2, 2022 at 5:06](#comment17003_16044)
    
- When you run `echo $PATH` you should see `/usr/local/bin` in your path. Almost certainly CentOS does that. (also, CentOS is dead, everyone went to Rocky).
    
    – [Evan Carroll](https://devops.stackexchange.com/users/18965/evan-carroll "2,611 reputation")
    
    [Commented Aug 2, 2022 at 14:47](#comment17009_16044)
    
- 1
    
    @UNOPARATOR, the problem is that on CentOS by default `sudo` will use a PATH value different from your own PATH. This other value does not include `/usr/local/bin`, which is why it couldn't find the `k3s` command. One way to resolve this is to add `/usr/local/bin` to the `secure_path` option in `/etc/sudoers`. See [superuser.com/questions/927512/…](https://superuser.com/questions/927512/how-to-set-path-for-sudo-commands "how to set path for sudo commands") for details. Ubuntu and Debian do not have this issue (`secure_path` includes `/usr/local/bin`).
    
    – [Stanley Yu](https://devops.stackexchange.com/users/42962/stanley-yu "101 reputation")
    
    [Commented Dec 28, 2023 at 20:55](#comment18245_16044)
    

[Show **3** more comments](# "Expand to show all comments on this post")

<a id="19325"></a>

0

[](https://devops.stackexchange.com/posts/19325/timeline)

Prefix you command with sudo.

Run:

`sudo k3s kubectl version`

[Share](https://devops.stackexchange.com/a/19325 "Short permalink to this answer")

[Improve this answer](https://devops.stackexchange.com/posts/19325/edit)

answered May 22 at 21:43

<img width="32" height="32" src="../_resources/2ad6269ed22259975de37dd1c488b9cd_4cc7a97e11f4447eb.png"/>](https://devops.stackexchange.com/users/45321/user10339671)

[user10339671](https://devops.stackexchange.com/users/45321/user10339671)

1

[Add a comment](# "Use comments to ask for more information or suggest improvements. Avoid comments like “+1” or “thanks”.")

<a id="new-answer"></a>

## Your Answer

### Sign up or <a id="login-link"></a>[log in](https://devops.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fdevops.stackexchange.com%2fquestions%2f16043%2ferror-error-loading-config-file-etc-rancher-k3s-k3s-yaml-open-etc-rancher%23new-answer)

Sign up using Google

Sign up using Email and Password

### Post as a guest

Name

Email

Required, but never shown

By clicking “Post Your Answer”, you agree to our <a id="tos"></a>[terms of service](https://stackoverflow.com/legal/terms-of-service/public) and acknowledge you have read our <a id="privacy"></a>[privacy policy](https://stackoverflow.com/legal/privacy-policy).

## 

Not the answer you're looking for? Browse other questions tagged

- [rancher](https://devops.stackexchange.com/questions/tagged/rancher "show questions tagged 'rancher'")
- [k3s](https://devops.stackexchange.com/questions/tagged/k3s "show questions tagged 'k3s'")

or [ask your own question](https://devops.stackexchange.com/questions/ask).

- The Overflow Blog
- [Legal advice from an AI is illegal](https://stackoverflow.blog/2024/12/17/legal-advice-from-an-ai-is-illegal/?cb=1)
    
- Featured on Meta
- [The December 2024 Community Asks Sprint has been moved to March 2025 (and...](https://meta.stackexchange.com/questions/404724/the-december-2024-community-asks-sprint-has-been-moved-to-march-2025-and-length?cb=1 "The December 2024 Community Asks Sprint has been moved to March 2025 (and lengthened to 2 weeks to compensate)")
    
- [Stack Overflow Jobs is expanding to more countries](https://meta.stackexchange.com/questions/404909/stack-overflow-jobs-is-expanding-to-more-countries?cb=1)
    

#### Linked

[6](https://devops.stackexchange.com/q/16013?lq=1 "Question score (upvotes - downvotes)")[k3s: The connection to the server localhost:8080 was refused - did you specify the right host or port?](https://devops.stackexchange.com/questions/16013/k3s-the-connection-to-the-server-localhost8080-was-refused-did-you-specify-t?noredirect=1&lq=1)

[1](https://devops.stackexchange.com/q/17257?lq=1 "Question score (upvotes - downvotes)")[With kubectl, I'm getting Unable to connect to the server: x509: certificate signed by unknown authority](https://devops.stackexchange.com/questions/17257/with-kubectl-im-getting-unable-to-connect-to-the-server-x509-certificate-sig?noredirect=1&lq=1)

[\-1](https://devops.stackexchange.com/q/16108?lq=1 "Question score (upvotes - downvotes)")[How can I get an installation of k3s working with KubeApps?](https://devops.stackexchange.com/questions/16108/how-can-i-get-an-installation-of-k3s-working-with-kubeapps?noredirect=1&lq=1)

#### Related

[0](https://devops.stackexchange.com/q/16152?rq=1 "Question score (upvotes - downvotes)")[Does /etc/rancher/k3s/registries.yaml affect \`k3s ctr\` and \`k3s crictl\`?](https://devops.stackexchange.com/questions/16152/does-etc-rancher-k3s-registries-yaml-affect-k3s-ctr-and-k3s-crictl?rq=1)

#### [Hot Network Questions](https://stackexchange.com/questions?tab=hot)

- [adduser allows weak password - how to prevent?](https://unix.stackexchange.com/questions/788334/adduser-allows-weak-password-how-to-prevent)
- [Is SQL Injection possible if we're using only the IN keyword (no equals = operator) and we handle the single quote](https://security.stackexchange.com/questions/279871/is-sql-injection-possible-if-were-using-only-the-in-keyword-no-equals-operat)
- [Understanding the phrase halacha l'Moshe mi'Sinai](https://judaism.stackexchange.com/questions/146520/understanding-the-phrase-halacha-lmoshe-misinai)
- [Energy stored in EM fields are non-retrievable?](https://physics.stackexchange.com/questions/837506/energy-stored-in-em-fields-are-non-retrievable)
- [Do accidentals have other meanings, or is their usage in this hymn all wrong?](https://music.stackexchange.com/questions/138333/do-accidentals-have-other-meanings-or-is-their-usage-in-this-hymn-all-wrong)
- [Joining two lists by matching elements of the two](https://mathematica.stackexchange.com/questions/309454/joining-two-lists-by-matching-elements-of-the-two)
- [Why do some installers insist on not doing a full frame window replacement?](https://diy.stackexchange.com/questions/311795/why-do-some-installers-insist-on-not-doing-a-full-frame-window-replacement)
- [Does fringe biology inspire fringe philosophy?](https://philosophy.stackexchange.com/questions/120492/does-fringe-biology-inspire-fringe-philosophy)
- [Why does David Copperfield say he is born on a Friday rather than a Saturday?](https://literature.stackexchange.com/questions/28371/why-does-david-copperfield-say-he-is-born-on-a-friday-rather-than-a-saturday)
- [Is there a way I can enforce verification of an EC signature at design-time rather than implementation-time?](https://crypto.stackexchange.com/questions/113793/is-there-a-way-i-can-enforce-verification-of-an-ec-signature-at-design-time-rath)
- [Snowshoe design for satyrs and fauns](https://worldbuilding.stackexchange.com/questions/263577/snowshoe-design-for-satyrs-and-fauns)
- [Finding corners where multiple polygons meet in QGIS](https://gis.stackexchange.com/questions/488840/finding-corners-where-multiple-polygons-meet-in-qgis)
- [Horror Film about a streamer convention set at a hotel where a tragedy had taken place](https://scifi.stackexchange.com/questions/293670/horror-film-about-a-streamer-convention-set-at-a-hotel-where-a-tragedy-had-taken)
- [Which accents \*don't\* merge FIRE and HIRE? What about RITE and RIDE?](https://linguistics.stackexchange.com/questions/49602/which-accents-dont-merge-fire-and-hire-what-about-rite-and-ride)
- [How to deal with academic loneliness?](https://academia.stackexchange.com/questions/215587/how-to-deal-with-academic-loneliness)
- [Is it normal for cabinet nominees to meet with senators before hearings?](https://politics.stackexchange.com/questions/90095/is-it-normal-for-cabinet-nominees-to-meet-with-senators-before-hearings)
- [Iterating through a set of sublists to find some desired sublists](https://mathematica.stackexchange.com/questions/309514/iterating-through-a-set-of-sublists-to-find-some-desired-sublists)
- [Why are there no no-attribution licences other than "public domain"?](https://opensource.stackexchange.com/questions/15258/why-are-there-no-no-attribution-licences-other-than-public-domain)
- [Handling a customer that is contacting my subordinates on LinkedIn demanding a refund (already given)?](https://workplace.stackexchange.com/questions/199856/handling-a-customer-that-is-contacting-my-subordinates-on-linkedin-demanding-a-r)
- [World split into pocket dimensions; protagonist escapes from windowless room, later lives in abandoned city and raids a supermarket](https://scifi.stackexchange.com/questions/293666/world-split-into-pocket-dimensions-protagonist-escapes-from-windowless-room-la)
- [What can I do about a Schengen visa refusal from Greece that mentions a prior refusal from Sweden as the reason?](https://travel.stackexchange.com/questions/192672/what-can-i-do-about-a-schengen-visa-refusal-from-greece-that-mentions-a-prior-re)
- [centre text in a cell](https://tex.stackexchange.com/questions/733096/centre-text-in-a-cell)
- [Why is Young's modulus represented as a single value in DFT calculations?](https://mattermodeling.stackexchange.com/questions/13841/why-is-youngs-modulus-represented-as-a-single-value-in-dft-calculations)
- [How to Mitigate Risks Before Delivering a Project with Limited Testing?](https://softwareengineering.stackexchange.com/questions/456067/how-to-mitigate-risks-before-delivering-a-project-with-limited-testing)

[Question feed](https://devops.stackexchange.com/feeds/question/16043 "Feed of this question and its answers")

##### [DevOps](https://devops.stackexchange.com/)

- [Tour](https://devops.stackexchange.com/tour)
- [Help](https://devops.stackexchange.com/help)
- [Chat](https://chat.stackexchange.com?tab=site&host=devops.stackexchange.com)
- [Contact](https://devops.stackexchange.com/contact)
- [Feedback](https://devops.meta.stackexchange.com)

##### [Company](https://stackoverflow.co/)

- [Stack Overflow](https://stackoverflow.com)
- [Teams](https://stackoverflow.co/teams/)
- [Advertising](https://stackoverflow.co/advertising/)
- [Talent](https://stackoverflow.co/advertising/employer-branding/)
- [About](https://stackoverflow.co/)
- [Press](https://stackoverflow.co/company/press/)
- [Legal](https://stackoverflow.com/legal)
- [Privacy Policy](https://stackoverflow.com/legal/privacy-policy)
- [Terms of Service](https://stackoverflow.com/legal/terms-of-service/public)

- [Cookie Policy](https://stackoverflow.com/legal/cookie-policy)

##### [Stack Exchange Network](https://stackexchange.com)

- [Technology](https://stackexchange.com/sites#technology)
- [Culture & recreation](https://stackexchange.com/sites#culturerecreation)
- [Life & arts](https://stackexchange.com/sites#lifearts)
- [Science](https://stackexchange.com/sites#science)
- [Professional](https://stackexchange.com/sites#professional)
- [Business](https://stackexchange.com/sites#business)
- [API](https://api.stackexchange.com/)
- [Data](https://data.stackexchange.com/)

- [Blog](https://stackoverflow.blog?blb=1)
- [Facebook](https://www.facebook.com/officialstackoverflow/)
- [Twitter](https://twitter.com/stackoverflow)
- [LinkedIn](https://linkedin.com/company/stack-overflow)
- [Instagram](https://www.instagram.com/thestackoverflow)

Site design / logo © 2024 Stack Exchange Inc; user contributions licensed under [CC BY-SA](https://stackoverflow.com/help/licensing) . <a id="svnrev"></a>rev 2024.12.18.20664