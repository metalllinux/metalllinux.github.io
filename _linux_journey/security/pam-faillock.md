---
title: "pam_faillock"
category: "security"
tags: ["security", "pam", "faillock"]
---

# pam_faillock

pam_faillock(8) - Linux man page

https://linux.die.net/man/8/pam_faillock

pam_faillock(8) - Linux man page
Name

pam_faillock - Module counting authentication failures during a specified interval
Synopsis

auth ... pam_faillock.so {preauth|authfail|authsucc} [dir=/path/to/tally-directory] [even_deny_root] [deny=n] [fail_interval=n] [unlock_time=n] [root_unlock_time=n] [audit] [silent] [no_log_info]

account ... pam_faillock.so [dir=/path/to/tally-directory] [no_log_info]

Description

This module maintains a list of failed authentication attempts per user during a specified interval and locks the account in case there were more than deny consecutive failed authentications.

Normally, failed attempts to authenticate root will not cause the root account to become blocked, to prevent denial-of-service: if your users aren't given shell accounts and root may only login via su or at the machine console (not telnet/rsh, etc), this is safe.
Options

{preauth|authfail|authsucc}

    This argument must be set accordingly to the position of this module instance in the PAM stack.

    The preauth argument must be used when the module is called before the modules which ask for the user credentials such as the password. The module just examines whether the user should be blocked from accessing the service in case there were anomalous number of failed consecutive authentication attempts recently. This call is optional if authsucc is used.

    The authfail argument must be used when the module is called after the modules which determine the authentication outcome, failed. Unless the user is already blocked due to previous authentication failures, the module will record the failure into the appropriate user tally file.

    The authsucc argument must be used when the module is called after the modules which determine the authentication outcome, succeded. Unless the user is already blocked due to previous authentication failures, the module will then clear the record of the failures in the respective user tally file. Otherwise it will return authentication error. If this call is not done, the pam_faillock will not distinguish between consecutive and non-consecutive failed authentication attempts. The preauth call must be used in such case. Due to complications in the way the PAM stack can be configured it is also possible to call pam_faillock as an account module. In such configuration the module must be also called in the preauth stage. 
dir=/path/to/tally-directory
    The directory where the user files with the failure records are kept. The default is /var/run/faillock. 
audit
    Will log the user name into the system log if the user is not found. 
silent
    Don't print informative messages. This option is implicite in the authfail and authsucc functions. 
no_log_info
    Don't log informative messages via syslog(3). 
deny=n
    Deny access if the number of consecutive authentication failures for this user during the recent interval exceeds n. The default is 3. 
fail_interval=n
    The length of the interval during which the consecutive authentication failures must happen for the user account lock out is n seconds. The default is 900 (15 minutes). 
unlock_time=n
    The access will be reenabled after n seconds after the lock out. The default is 600 (10 minutes). 
even_deny_root
    Root account can become locked as well as regular accounts. 
root_unlock_time=n
    This option implies even_deny_root option. Allow access after n seconds to root account after the account is locked. In case the option is not specified the value is the same as of the unlock_time option. 

Module Types Provided

The auth and account module types are provided.
Return Values

PAM_AUTH_ERR

    A invalid option was given, the module was not able to retrieve the user name, no valid counter file was found, or too many failed logins. 
PAM_SUCCESS
    Everything was successful. 
PAM_IGNORE
    User not present in passwd database. 

Notes

pam_faillock setup in the PAM stack is different from the pam_tally2 module setup.

The individual files with the failure records are created as owned by the user. This allows pam_faillock.so module to work correctly when it is called from a screensaver.

Note that using the module in preauth without the silent option or with requisite control field leaks an information about existence or non-existence of an user account in the system because the failures are not recorded for the unknown users. The message about the user account being locked is never displayed for nonexisting user accounts allowing the adversary to infer that a particular account is not existing on a system.
Examples

Here are two possible configuration examples for /etc/pam.d/login. They make pam_faillock to lock the account after 4 consecutive failed logins during the default interval of 15 minutes. Root account will be locked as well. The accounts will be automatically unlocked after 20 minutes.

In the first example the module is called only in the auth phase and the module does not print any information about the account blocking by pam_faillock. The preauth call can be added to tell the user that his login is blocked by the module and also to abort the authentication without even asking for password in such case.

    auth     required       pam_securetty.so
    auth     required       pam_env.so
    auth     required       pam_nologin.so
    # optionally call: auth requisite pam_faillock.so preauth deny=4 even_deny_root unlock_time=1200
    # to display the message about account being locked
    auth     [success=1 default=bad] pam_unix.so
    auth     [default=die]  pam_faillock.so authfail deny=4 even_deny_root unlock_time=1200
    auth     sufficient     pam_faillock.so authsucc deny=4 even_deny_root unlock_time=1200
    auth     required       pam_deny.so
    account  required       pam_unix.so
    password required       pam_unix.so shadow
    session  required       pam_selinux.so close
    session  required       pam_loginuid.so
    session  required       pam_unix.so
    session  required       pam_selinux.so open

In the second example the module is called both in the auth and account phases and the module gives the authenticating user message when the account is locked

    auth     required       pam_securetty.so
    auth     required       pam_env.so
    auth     required       pam_nologin.so
    auth     required       pam_faillock.so preauth silent deny=4 even_deny_root unlock_time=1200
    # optionally use requisite above if you do not want to prompt for the password
    # on locked accounts, possibly with removing the silent option as well
    auth     sufficient     pam_unix.so
    auth     [default=die]  pam_faillock.so authfail deny=4 even_deny_root unlock_time=1200
    auth     required       pam_deny.so
    account  required       pam_faillock.so
    # if you drop the above call to pam_faillock.so the lock will be done also
    # on non-consecutive authentication failures
    account  required       pam_unix.so
    password required       pam_unix.so shadow
    session  required       pam_selinux.so close
    session  required       pam_loginuid.so
    session  required       pam_unix.so
    session  required       pam_selinux.so open

Files

/var/run/faillock/*

    the files logging the authentication failures for users 

See Also

faillock(8), pam.conf(5), pam.d(5), pam(8)
Author

pam_faillock was written by Tomas Mraz. 
