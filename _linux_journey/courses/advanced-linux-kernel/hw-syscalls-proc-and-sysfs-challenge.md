---
title: "Hw Syscalls Proc And Sysfs Challenge"
category: "advanced-linux-kernel"
tags: ["advanced-linux-kernel", "syscalls", "proc", "sysfs", "challenge"]
---

* `uname` stands for Unix Name.
* What is the size of the Kernel file that corresponds to the Kernel you are running.
	* Kernel file is in the `/boot` directory.
	* `ls -l /boot`
	* As an example:
```
lrwxrwxrwx 1 root root        26  3月 19 11:40 vmlinuz -> vmlinuz-5.15.0-101-generic
```
* How much RAM is available to your running Kernel?
	* Swap memory is used by the Kernel itself.
	* Can also get information from a `proc` file, with `/proc/meminfo` looks like this:
```
howard@explosion:~$ head /proc/meminfo
MemTotal:       16299920 kB
MemFree:        11054764 kB
MemAvailable:   13460144 kB
Buffers:          152728 kB
Cached:          2577384 kB
SwapCached:            0 kB
Active:          3745828 kB
Inactive:         989372 kB
Active(anon):    2115004 kB
Inactive(anon):    21308 kB
```
* Use the `man` command to show the output of `strace` with a summary and count of the number of times a process uses each system call.
	* What system call is called the most, via the command date.
	* `strace -c date` will output the following:
```
2024年  3月 25日 月曜日 16:10:13 JST
% time     seconds  usecs/call     calls    errors syscall
------ ----------- ----------- --------- --------- ----------------
 43.88    0.000165         165         1           execve
 16.76    0.000063           7         9           mmap
  7.18    0.000027           6         4           mprotect
  6.12    0.000023           5         4           openat
  4.79    0.000018           3         6           newfstatat
  3.46    0.000013           2         6           close
  3.46    0.000013          13         1           munmap
  2.39    0.000009           3         3           brk
  2.39    0.000009           2         4           pread64
  2.13    0.000008           2         3           read
  1.86    0.000007           7         1           write
  1.06    0.000004           4         1         1 access
  1.06    0.000004           2         2         1 arch_prctl
  0.80    0.000003           3         1           getrandom
  0.53    0.000002           2         1           lseek
  0.53    0.000002           2         1           set_tid_address
  0.53    0.000002           2         1           set_robust_list
  0.53    0.000002           2         1           prlimit64
  0.53    0.000002           2         1           rseq
------ ----------- ----------- --------- --------- ----------------
100.00    0.000376           7        51         2 total
```
* By default, it is sorted by `% time`. One of the system calls that took the most time was `mmap`. `mmap` stands for memory map.
	* `mmap` system call is used in a process to map a particular file. It gets a pointer to the file and then can treat the file like a chunk of memory.
	* Most libraries that programs use are standard libraries.
* Running `strace date` without the `-c` will display all of the calls that it made.
* `strace` prints its output to `standard error`.
* The `|` symbol only grabs `standard out`
* In `Bash`, if you do `|&`, that makes `standard out` and `standard error` go into the pipe symbol.
	* Thus, doing `strace date |& read` will show all of the system calls of `read`.
* Can you determine using `strace`, which system call is used to change the directory?
	* If we use `cd`, there is a system call for that.
	* `cd` itselfl is not a command. If you do `which cd`, no output will be displayed.
	* When we run a regular command like `date`, the Shell starts a new process.
	* The `cd` command however is meant to change the state of the current process.
		* The Shell itself, has to do the `cd`. The shell itself it going to call the system call, to perform the `cd`.
	* We can write a shell script with `cd` and then `strace` that.
```
#!/bin/bash
cd "$@"
```
* The `$@` passes any arguments that we have.
* Can then run the script with `./cd /etc` as an example.
* Can then `strace` the script with `strace ./cd /etc` and then you receive some output.
* If we check the `man` page for `chdir` (`cd`), in the top left-hand corner you will see a `2` and this means it is a `system call`:
```
CHDIR(2)                                                                     
```
* Question 6, determine how many system calls are defined in your Kernel Source.
	* `grep "define __NR" unistd.h | wc -l`
	* This can be found in `/usr/src/linux-5.3.0/include/uapi/asm-generic`
	* Then `view unistd.h`
	* Can perform a lazy search by running `/__NR.*read`
	* An example on my system is at `/usr/src/linux-headers-5.15.0-100/include/uapi/asm-generic/unistd.h`
	* Searching there, we can find `#define __NR_readlinkat 78`. The number is an approximation, depending on the architecture.
	* For the `syscalls`, checking the following observes this amount:
```
#define __NR_syscalls 449
```
	* There will be some `syscalls` however that are unassigned.
* Question 7, Run a `sleep 100` with `&` and put in in the background.
	* For example, running `sleep 100 &` will run the command in the background and provide us our prompt back. The process ID is also provided below as an example:
```
howard@explosion:~$ sleep 100 &
[1] 7028
```
* We then run `cd fd` and then `ls -l` and we see:
```
lrwx------ 1 howard howard 64  3月 26 18:06 0 -> /dev/pts/1
lrwx------ 1 howard howard 64  3月 26 18:06 1 -> /dev/pts/1
lrwx------ 1 howard howard 64  3月 26 18:06 2 -> /dev/pts/1
lrwx------ 1 howard howard 64  3月 26 18:06 74 -> 'socket:[22516]'
lrwx------ 1 howard howard 64  3月 26 18:06 78 -> 'socket:[22518]'
```
* We can see that the `sleep` command was running on the window `/dev/pts/1`:
```
howard@explosion:/proc/7028/fd$ tty
/dev/pts/1
[1]+  Done                    sleep 100  (wd: ~)
(wd now: /proc/7028/fd)

```
* The `sleep` command has stin, stdout and stderr, corresponding from numbers `0 ~ 2` above.
* Does your system have a PCI Ethernet Device?
	* Good way to get output for Ethernet devices is with `lspci | grep -i ethernet`
* Question 9 is, is the Kernel variable ip_forward?
	* This is under `/proc/sys`.
	* Good way is to use the `find` command.
	* In `/proc/sys`, run the following: `find . | grep ip_forward`. Example output is:
```
howard@explosion:/proc/sys$ find . | grep ip_forward
./net/ipv4/ip_forward
./net/ipv4/ip_forward_update_priority
./net/ipv4/ip_forward_use_pmtu
```
* Then we change directory to `cd /net/ipv4`. We `cat ip_forward`. In my example, I see:
```
howard@explosion:/proc/sys$ cat ./net/ipv4/ip_forward
0
```
* Because it is set to `0`, that means it is not forwarding packets between interfaces.
* Another way to check items under `/proc/sys` is via the `sysctl` command:
	* `sysctl -a`
		* That will output all of the system call commands that are available.
		* Need to be `root` and can `sudo` the Shell with `sudo bash`. Will then look like the following:
```
howard@explosion:/proc/sys$ sudo bash
[sudo] password for howard: 
root@explosion:/proc/sys# sysctl -a | grep ip_forward
net.ipv4.ip_forward = 0
net.ipv4.ip_forward_update_priority = 1
net.ipv4.ip_forward_use_pmtu = 0
```
* It leaves off the `/proc/sys` part and replaces the `/` for `.` instead.
* Can then report the value with `sysctl net.ipv4.ip_forward` and it outputs the following:
```
root@explosion:/proc/sys# sysctl net.ipv4.ip_forward
net.ipv4.ip_forward = 0
```
* We can change these values with:
```
sysctl net.ipv4.ip_forward=1
```
* Checking the value again, it will then say:
```
root@explosion:/proc/sys# sysctl net.ipv4.ip_forward
net.ipv4.ip_forward = 1
```
* Can set a config file, so whenever the system is booted, `ip_forward` is set to `number`.
* Question 10, according to sysblock, do you have an sda device and if so, do you have device files for partitions of sda. Does the command `fdisk -l` open any files under `/sys/dev/block`
	* We can check `/sys/block`. It will show the following:
```
lrwxrwxrwx 1 root root 0  3月 27 08:55 loop7 -> ../devices/virtual/block/loop7
lrwxrwxrwx 1 root root 0  3月 27 08:55 sda -> ../devices/pci0000:00/0000:00:1f.2/ata2/host1/target1:0:0/1:0:0:0/block/sda
```
* Confirmed there is a block device called `sda`.
* To check for device files for `sda`, we can do:
```
howard@explosion:/sys/block$ ls -l /dev/sda*
brw-rw---- 1 root disk 8, 0  3月 27 08:55 /dev/sda
brw-rw---- 1 root disk 8, 1  3月 27 08:55 /dev/sda1
brw-rw---- 1 root disk 8, 2  3月 27 08:55 /dev/sda2
brw-rw---- 1 root disk 8, 3  3月 27 08:55 /dev/sda3
brw-rw---- 1 root disk 8, 4  3月 27 08:55 /dev/sda4
```
* All of the above have `major` number `8` and they have `minor` numbers of `0~4`.
* `0` is the whole disk.
* `1` is the first partition on the first controller.
* To then check with `strace`, we do (we need |& because `fdisk` outputs to stderr):
```
strace fdisk -l |&
```
* To check how many things it opened, we can use `strace fdisk -l |& grep sys/dev/block | grpe open | wc -l`.
* In my case, we get `28`:
```
root@explosion:/sys/block# strace fdisk -l |& grep sys/dev/block | grep open | wc -l
28
```
* Question 11. Using `dmesg` and `grep`, do you see the Kernel reporting the Kernel Command Line?
	* `dmesg | grep -i command` will show:
```
[    0.034807] Kernel command line: BOOT_IMAGE=/boot/vmlinuz-6.5.0-26-generic root=UUID=ca2eb2d6-2fc2-4c9e-8001-11190efd85ee ro quiet splash radeon.cik_support=0 radeon.si_support=0 amdgpu.cik_support=1 amdgpu.si_support=1 amdgpu.dc=1 vt.handoff=7
[    0.034970] Unknown kernel command line parameters "splash BOOT_IMAGE=/boot/vmlinuz-6.5.0-26-generic", will be passed to user space.

```
* Then check `/var/log` and then check with:
	* `grep -rl BOOT_IMAGE .`
		* The `l` will list out the file if there is a match. `r` of course is for `recursive`. That outputs something similar to:
```
howard@explosion:/var/log$ sudo grep -rl BOOT_IMAGE .
./dmesg.0
./syslog.1
./installer/syslog
./kern.log.1
./dmesg
./syslog
./kern.log
./journal/fa438c9af4094b8980d0c8694143cbdc/user-1000.journal
./journal/fa438c9af4094b8980d0c8694143cbdc/system.journal
./journal/fa438c9af4094b8980d0c8694143cbdc/system@440d5f7bd82b4e53aed6f76fd54a620b-0000000000000001-0006135d07519475.journal
./Xorg.0.log
./auth.log
./Xorg.0.log.old
```
* There are a bunch of files where Kernel messages could get saved.
	* It is distribution dependent on how this works.
* What other devices are character devices and share the same major number with `/dev/null`?
	* In the `/dev/` directory, we have the following:
```
howard@explosion:/dev$ ls -l null
crw-rw-rw- 1 root root 1, 3  3月 27 21:40 null
```
* Major is `1` and Minor is `3`
* We can check this in `/dev` with:
```
ls -l | grep "^c" | grep " 1,"
```
* The `^` will match lines that start with a `c` (character device file)
* The `grep " 1,"` will show lines where the major is number `1`. That will then output:
```
howard@explosion:/dev$ ls -l | grep "^c" | grep " 1,"
crw-rw-rw-  1 root   root      1,   7  3月 27 21:40 full
crw-r--r--  1 root   root      1,  11  3月 27 21:40 kmsg
crw-r-----  1 root   kmem      1,   1  3月 27 21:40 mem
crw-rw-rw-  1 root   root      1,   3  3月 27 21:40 null
crw-r-----  1 root   kmem      1,   4  3月 27 21:40 port
crw-rw-rw-  1 root   root      1,   8  3月 27 21:40 random
crw-rw-rw-  1 root   root      1,   9  3月 27 21:40 urandom
crw-rw-rw-  1 root   root      1,   5  3月 27 21:40 zero
```
* What happens if we have a device file with Major `1` and Minor `2`.
* We can make a device file with the `mknod` command.
	* `cd /tmp`
	* `mknod <name> c 1 2`
	* That then creates a character device file with a Major numbe of `1` and a Minor number of `2`.
	* If you then try to `cat` the file, the Kernel will not recognise it.
```
howard@explosion:/tmp$ sudo mknod try_me c 1 2
howard@explosion:/tmp$ cat try_me
cat: try_me: No such device or address
```
* There is nothing that corresponds to a device file with `1, 2`
* Just because you have a device file, does not mean you have a device.