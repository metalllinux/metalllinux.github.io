---
title: "Checking Logs Of A Linux System"
category: "general-linux"
tags: ["checking", "logs", "linux", "system"]
---

* Two services that handle syslog messages:
	* `systemd-journald` daemon.
	* `Rsyslog` service.
* `systemd-journald` collects messages from various services and then forwards them to `Rsyslog` for further processing.
* `systemd-journald` will collect messages from the following sources:
	* Kernel
	* Early stages of the boot process.
	* Standard and error output of daemons as they start up and when they run.
	* `Syslog`
* `Rsyslog` sorts `syslog` by *type* and *priority* and writes them to the `/var/log` directory. 
* Sub-directories storing `syslog` messages.
	* `/var/log/messages` - has all messages except the following:
		* `/var/log/secure` - Security and Authentication-related Messages and Errors.
		* `/var/log/maillog` - Mail server-related messages and errors.
		* `/var/log/cron` - Log files related to periodically executed tasks.
		* `/var/log/boot.log` - Log files related to system startup.
* It is possible to inspect logs via the web-console like so:
![viewing-logs.png](../_resources/viewing-logs.png)
* To see all boot looks using `journalctl`, we can use `journalctl -b`
* Uses of `journalctl` include:
	* `journalctl FILEPATH`
		* For example `journalctl /dev/sda` - shows all logs for a particular drive.
	* `journalctl -b`
		* Shows logs for the current boot state.
	* `journalctl -k -b -1`
		* Shows kernel logs for the current boot.
	* `journalctl -b _SYSTEMD_UNIT=<name.service> _PID=<number>`
		* Shows matches for the `systemd-units` that match `<name.service>` and the PID number.
	* `journalctl -b _SYSTEMD_UNIT=<name.service> _PID=<number> + _SYSTEMD_UNIT=<name2.service>` - the plus is a local `or` here, so it shows all messages from the `<name.service>` with the specific `PID` and all messages from the `<name2.service>`
	* Can make it more general with this version: `journalctl -b _SYSTEMD_UNIT=<name.service> _SYSTEMD_UNIT=<name2.service>` - shows all entries matching either service.
* To show a list of boots, you can do `journalctl --list-boots` - Shows a tabular list of boot numbers and timestamps of the first and last messages for the boot. 
	* To get more information, need to to use: `journalctl --boot=ID _SYSTEMD_UNIT=<name.service>`
