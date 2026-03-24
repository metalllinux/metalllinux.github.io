---
title: "To Allow Ssh Logins When Installing Rocky Linux 9."
category: "rocky-linux"
tags: ["rocky-linux", "allow", "ssh", "logins", "when"]
---

* Add the following to the end of the `rootpw` line in the kickstart file:
```
--allow-ssh
```
The --allow-ssh option is only available from 9.1 onwards. Any version below 9.1, you need to add the following section in the kickstart file (the --allow-ssh option does not exist in <9.1 ):
```
%post
echo "PermitRootLogin yes" > /etc/ssh/sshd_config.d/01-permitrootlogin.conf
%end
```

note that, that %post config for < 9.1 won't work on > 9.1, because RH ships a 99 or 98-redhat which would change it back to no