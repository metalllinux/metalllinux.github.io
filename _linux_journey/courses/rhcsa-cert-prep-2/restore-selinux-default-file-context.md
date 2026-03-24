---
title: "Restore Selinux Default File Context"
category: "rhcsa-cert-prep-2"
tags: ["rhcsa-cert-prep-2", "restore", "selinux", "default", "file"]
---

- With standard Linux permissions, these are stored with the file.
    - With SELinux, the security context is also stored with the file.
        - In the `extended attributes` section.
- Default Security Context Settings are also in the SELinux Security Policy as well.
    - For example, these settings ensure that all the files in `/home` have a certain type.
        - If you perform `ls -lZ /home`, the default Security Context is `user_home_t` for the files.
            - We can also change the Security Context of a file.
                - No need to elevate privileges when doing this for your own files.
                    - If you want to change another user's files' Security Context, then you need to elevate privileges.
                        - `chcon -t etc_t newfile`
                            - The `etc_t` is the type it is being changed to.
                                - You will see that `user_home_t` has been changed to `etc_t`
                                    - The Security Context database can also make changes, in this case changing back the Security Context to `user_home_t`
                                        - `restorecon newfile.txt`
                                            - If you want to reset the Security Label of every file, you need to relabel the drive.
                                                - SELinux would restore and relabel the Security Context of each file back to what it was before.
                                                    - To perform this, we create a file in the `/` directory called `.autorelabel` and then reboot the machine.
                                                        - `sudo touch /.autorelabel`
                                                            - The next time you reboot, the Security Context of all files in the operating system will be set back to their defaults.
                                                                - Once all relabelling is done, the hidden \`autorelabel\` file that was created is then deleted.
                                                                    - If you want the file in your home directory to have a different security context.
                                                                        - And don't want a \`restorecon\` or \`autolabel\` to reset it, you can change the policy database.
                                                                            - \`sudo semanage fcontext -a -t etc\_t /home/user1/newfile.txt\`
                                                                                - \`fcontext\` is used for files.
                                                                                    - Can verify the change was added to the policy, by listing all file contexts.
                                                                                        - \`sudo semanage fcontext -l | grep newfile.txt
                                                                                            - Then restore the security context back with \`restorecon newfile.txt\`.