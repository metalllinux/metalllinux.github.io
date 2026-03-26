---
title: "Slurm Setup on Rocky Linux 8.10 with One Controller Node and One Compute Node"
category: "rocky-linux"
tags: ["rocky-linux", "slurm", "setup", "rocky", "linux"]
---

# Slurm Setup on Rocky Linux 8.10 with One Controller Node and One Compute Node

* Add the following to `/etc/hosts` on both the Controller and Compute Nodes:

```
sudo tee -a /etc/hosts << EOF
192.168.1.120 rocky-linux8-slurm-controller-node
192.168.1.121 rocky-linux8-slurm-compute-node
EOF
```

* Create `ssh` keys without passwords for the `root` user on both nodes:

```
ssh-keygen -t rsa -b 4096
```

* Perform `ssh-copy-id` for the `root` user on each node:

```
ssh-copy-id root@192.168.1.120
ssh-copy-id root@192.168.1.121
```

* Pull down the `slurm`

* Install the following packages on both Nodes:

```
dnf install -y autofs munge openmpi openmpi-devel nfs-utils rpcbind 
```

* Enable these services on the Controller Node:

```
systemctl enable --now nfs-server 
systemctl enable --now rpcbind
```

* Add the IP address from the Compute Node:

```
firewall-cmd --add-rich-rule='rule family="ipv4" source address="192.168.1.121" accept' --permanent
firewall-cmd --reload
```

* Create the NFS directory on the Controller Node for the `root` user:

```
mkdir ~/nfs
```

* Configure the `exports` file on the Controller Node:

```
cat << "EOF" | sudo tee /etc/exports
/root/nfs 192.168.1.121(rw,sync,no_subtree_check,no_root_squash)
EOF
```

* Add the IP address of the Controller Node to the Compute Node's Firewall:

```
firewall-cmd --add-rich-rule='rule family="ipv4" source address="192.168.1.120" accept' --permanent
firewall-cmd --reload
```

* Edit `/etc/auto.master` on the Compute Node:

```
cat << "EOF" | tee -a /etc/auto.master
/root/nfs /etc/auto.nfs 
EOF
```

* Create the `nfs` directory for the `myuser` user on the Compute Node:

```
mkdir ~/nfs
```

* Then we create the `/etc/auto.nfs` file on the Compute Node:

```
cat << "EOF" | tee -a /etc/auto.nfs
rocky-linux810-slurm-controller-node:/root/nfs
EOF
```

* Restart the `autofs` and `rpcbind` services on the Compute Node:

```
systemctl restart autofs
systemctl restart rpcbind
```

* On the Controller Node, go into the `nfs` directory in the `myuser` user. Create the following test MPI C program:

```
cat << "EOF" | tee ~/nfs/test.c
# include <stdio.h>
# include <mpi.h>

int main(int argc, char *argv[]){
        int rank, size;
        MPI_Init(&argc,&argv); /* Starts MPI */
        MPI_Comm_rank(MPI_COMM_WORLD, &rank); /* get current process id */
        MPI_Comm_size(MPI_COMM_WORLD, &size); /* get number of processes */
        
        printf("Hello World from %d of %d!\n",rank,size);
        
        MPI_Finalize(); /* End of MPI */
        
        return 0;
}
EOF
```

* Add the following to the `myuser` user's `bashrc` on the Controller and the Compute Nodes:

```
cat << "EOF" | tee -a ~/.bashrc
PATH=$PATH:/usr/lib64/openmpi/bin
# LD_LIBRARY_PATH=/usr/lib64/openmpi/lib
EOF
```

* Source `.bashrc` afterwards:

```
source ~/.bashrc
```

* Then compile the `test.c` program for the `myuser` user:

```
mpicc ~/nfs/test.c
```

* Then run the program:

```
~/a.out
```

* Any errors such as the following can be safely ignored:

```
rocky-linux810-slurm-controller-node:pid31626.a.out: Failed to get enp1s0 (unit 0) cpu set
rocky-linux810-slurm-controller-node:pid31626: PSM3 can't open nic unit: 0 (err=23)
rocky-linux810-slurm-controller-node:pid31626.a.out: Failed to get enp1s0 (unit 0) cpu set
rocky-linux810-slurm-controller-node:pid31626: PSM3 can't open nic unit: 0 (err=23)
rocky-linux810-slurm-controller-node:pid31626.a.out: Failed to get enp1s0 (unit 0) cpu set
rocky-linux810-slurm-controller-node:pid31626: PSM3 can't open nic unit: 0 (err=23)
rocky-linux810-slurm-controller-node:pid31626.a.out: Failed to get enp1s0 (unit 0) cpu set
rocky-linux810-slurm-controller-node:pid31626: PSM3 can't open nic unit: 0 (err=23)
--------------------------------------------------------------------------
Open MPI failed an OFI Libfabric library call (fi_endpoint).  This is highly
unusual; your job may behave unpredictably (and/or abort) after this.

  Local host: rocky-linux810-slurm-controller-node
  Location: mtl_ofi_component.c:513
  Error: Invalid argument (22)
--------------------------------------------------------------------------
```

* Then attempt to run the `test.c` program in parallel:

```
mpirun -n 2 ~/a.out
```

* `-n <integer>` can choose how many processes to run in paralle (up to the amount of CPUs that you have available)

* Create a `machinefile` in the `myuser` user's `~/nfs` directory and add the Compute Node:

```
cat << "EOF" | tee ~/nfs/machinefile
rocky-linux810-slurm-compute-node
EOF
```

* Test the same program using a `machinefile`:

```
mpirun -n 6 --machinefile machinefile ~/a.out
```

* On the Controller Node, install `mariadb`:

```
dnf install -y mariadb mariadb-server
```

* On the Controller Node, tell `mariadb` to start on boot:

```
systemctl enable --now mariadb
```

* Run the `mysql_secure_installation` script:

```
sudo mysql_secure_installation
```

* Set a `root` password.

* Answer Yes to all other questions.

* Access MariaDB as the `root` user:

```
mysql -u root -p 
```

* Show the default databases:

```
SHOW DATABASES;
```

* Check user information:

```
SELECT host,user,password FROM mysql.user;
```

* Create a new database:

```
CREATE DATABASE opencentral;
```

* Create an admin user:

```
GRANT ALL PRIVILEGES On opencentral.* TO 'admin'@'localhost' IDENTIFIED BY 'openCentr@l';
```

* flush privileges:

```
FLUSH PRIVILEGES;
```

* Then exit with `\q`

* Then log in again as the `admin` user. The password is `openCentr@l`

```
mysql -u admin -p 
```

* Then type `SHOW DATABASES;`

* Use the `opencentral` DB:

```
USE opencentral;
```

* Create a test table:

```
CREATE TABLE test (sl_no integer, name varchar(45), dob date);
```

* Insert sample data into the table:

```
INSERT INTO test VALUES (1,'ABC','1785.01.04');
INSERT INTO test VALUES (2,'DEF','1985.06.07');
INSERT INTO test VALUES (3,'GHI','2020.03.25');
```

* Check the data:

```
SELECT * FROM test;
```

* Exit out with `\q`

* Enable the `devel` repository for access to `munge-devel`:

```
dnf config-manager --set-enabled devel
```

* Install the required packages to build `slurm` on the Controller Node:

```
dnf install -y autoconf automake make mariadb-devel munge-devel pam-devel perl-ExtUtils-MakeMaker perl-devel python3 readline-devel rpm-build
```

* Pull down the `slurm 25.05` tarball on to the Controller Node:

```
wget https://download.schedmd.com/slurm/slurm-25.05.5.tar.bz2
```

* Build the `slurm 25.05` RPM:

```
rpmbuild -ta slurm-25.05.5.tar.bz2
```

* Once the packages are built, install the following on the Controller Node:

```
dnf localinstall -y ~/rpmbuild/RPMS/x86_64/slurm-25.05.5-1.el8.x86_64.rpm
dnf localinstall -y ~/rpmbuild/RPMS/x86_64/slurm-perlapi-25.05.5-1.el8.x86_64.rpm
dnf localinstall -y ~/rpmbuild/RPMS/x86_64/slurm-slurmctld-25.05.5-1.el8.x86_64.rpm
```

* After the packages are installed, transfer the following over to the Compute Node:

```
rsync -AvP ~/rpmbuild/RPMS/x86_64/slurm-25.05.5-1.el8.x86_64.rpm <user>@<ip>:~/
rsync -AvP ~/rpmbuild/RPMS/x86_64/slurm-perlapi-25.05.5-1.el8.x86_64.rpm <user>@<ip>:~/
rsync -AvP ~/rpmbuild/RPMS/x86_64/slurm-slurmd-25.05.5-1.el8.x86_64.rpm <user>@<ip>:~/
```

* Install the `slurm`, `slurm-perlapi` and `slurm-slurmd` packages on the Compute Node:

```
dnf localinstall -y ~/slurm-25.05.5-1.el8.x86_64.rpm
dnf localinstall -y ~/slurm-perlapi-25.05.5-1.el8.x86_64.rpm
dnf localinstall -y ~/slurm-slurmd-25.05.5-1.el8.x86_64.rpm
```

* Make sure both the Controller Node and Compute Node have synchronised clocks.

* On the Controller Node, as `root`, `cd` into the `munge` directory:

```
cd /etc/munge
```

* Create the `munge` key (the /usr/sbin/mungekey command is only available on munge version 5.14+):

```
dd if=/dev/urandom bs=1 count=1024 > /etc/munge/munge.key
chown munge:munge /etc/munge/munge.key
chmod 400 /etc/munge/munge.key
```

* `rsync` the `munge` key to the Compute Node:

```
rsync -AvP /etc/munge/munge.key root@<ip>:/etc/munge/munge.key
```

* On the Compute Node, ensure the right permissions are set on the `munge.key`:

```
chown munge:munge /etc/munge/munge.key
chmod 400 /etc/munge/munge.key
```

* Create the `slurm.conf` file using this tool: https://slurm.schedmd.com/configurator.html on both the Controller Node and the Compute Node:

* An example used is below:

```
cat << "EOF" | sudo tee /etc/slurm/slurm.conf
# slurm.conf file generated by configurator.html.
# Put this file on all nodes of your cluster.
# See the slurm.conf man page for more information.
#
ClusterName=rocky-linux810
SlurmctldHost=rocky-linux810-slurm-controller-node
#SlurmctldHost=
#
#DisableRootJobs=NO
#EnforcePartLimits=NO
#Epilog=
#EpilogSlurmctld=
#FirstJobId=1
#MaxJobId=67043328
#GresTypes=
#GroupUpdateForce=0
#GroupUpdateTime=600
#JobFileAppend=0
#JobRequeue=1
#JobSubmitPlugins=lua
#KillOnBadExit=0
#LaunchType=launch/slurm
#Licenses=foo*4,bar
#MailProg=/bin/mail
#MaxJobCount=10000
#MaxStepCount=40000
#MaxTasksPerNode=512
#MpiDefault=
#MpiParams=ports=#-#
#PluginDir=
#PlugStackConfig=
#PrivateData=jobs
ProctrackType=proctrack/cgroup
#Prolog=
#PrologFlags=
#PrologSlurmctld=
#PropagatePrioProcess=0
#PropagateResourceLimits=
#PropagateResourceLimitsExcept=
#RebootProgram=
ReturnToService=1
SlurmctldPidFile=/var/run/slurmctld.pid
SlurmctldPort=6817
SlurmdPidFile=/var/run/slurmd.pid
SlurmdPort=6818
SlurmdSpoolDir=/var/spool/slurmd
SlurmUser=slurm
#SlurmdUser=root
#SrunEpilog=
#SrunProlog=
StateSaveLocation=/var/spool/slurmctld
#SwitchType=
#TaskEpilog=
TaskPlugin=task/affinity,task/cgroup
#TaskProlog=
#TopologyPlugin=topology/tree
#TmpFS=/tmp
#TrackWCKey=no
#TreeWidth=
#UnkillableStepProgram=
#UsePAM=0
#
#
# TIMERS
#BatchStartTimeout=10
#CompleteWait=0
#EpilogMsgTime=2000
#GetEnvTimeout=2
#HealthCheckInterval=0
#HealthCheckProgram=
InactiveLimit=0
KillWait=30
#MessageTimeout=10
#ResvOverRun=0
MinJobAge=300
#OverTimeLimit=0
SlurmctldTimeout=120
SlurmdTimeout=300
#UnkillableStepTimeout=60
#VSizeFactor=0
Waittime=0
#
#
# SCHEDULING
#DefMemPerCPU=0
#MaxMemPerCPU=0
#SchedulerTimeSlice=30
SchedulerType=sched/backfill
SelectType=select/cons_tres
#
#
# JOB PRIORITY
#PriorityFlags=
#PriorityType=priority/multifactor
#PriorityDecayHalfLife=
#PriorityCalcPeriod=
#PriorityFavorSmall=
#PriorityMaxAge=
#PriorityUsageResetPeriod=
#PriorityWeightAge=
#PriorityWeightFairshare=
#PriorityWeightJobSize=
#PriorityWeightPartition=
#PriorityWeightQOS=
#
#
# LOGGING AND ACCOUNTING
#AccountingStorageEnforce=0
#AccountingStorageHost=
#AccountingStoragePort=
#AccountingStorageType=
#AccountingStoreFlags=
#JobCompHost=
#JobCompLoc=
#JobCompParams=
#JobCompPass=
#JobCompPort=
JobCompType=jobcomp/none
#JobCompUser=
#JobContainerType=
JobAcctGatherFrequency=30
#JobAcctGatherType=
SlurmctldDebug=info
SlurmctldLogFile=/var/log/slurmctld.log
SlurmdDebug=info
SlurmdLogFile=/var/log/slurmd.log
#SlurmSchedLogFile=
#SlurmSchedLogLevel=
#DebugFlags=
#
#
# POWER SAVE SUPPORT FOR IDLE NODES (optional)
#SuspendProgram=
#ResumeProgram=
#SuspendTimeout=
#ResumeTimeout=
#ResumeRate=
#SuspendExcNodes=
#SuspendExcParts=
#SuspendRate=
#SuspendTime=
#
#
# COMPUTE NODES
NodeName=rocky-linux810-slurm-compute-node NodeAddr=192.168.1.121 State=UNKNOWN
PartitionName=debug Nodes=ALL Default=YES MaxTime=INFINITE State=UP
EOF
```

* On the Controller and Compute Nodes, set up `munge` and `slurm` users:

```
export MUNGEUSER=2001
sudo groupadd -g $MUNGEUSER munge
sudo useradd -m -c "MUNGE Uid 'N' Gid Emporium" -d /var/lib/munge -u $MUNGEUSER -g munge -s /sbin/nologin munge
export SLURMUSER=2002
sudo groupadd -g $SLURMUSER slurm
sudo useradd -m -c "SLURM Workload Manager" -d /var/lib/slurm -u $SLURMUSER -g slurm -s /bin/bash slurm
```

* Create the directories and permissions for `munge` and `slurm` on the Controller and Compute Nodes (permission of `755` needed for `/run/munge`, due to `munge` version 5.13):

```
sudo mkdir /run/munge /etc/slurm /run/slurm/ /var/lib/slurm /var/log/slurm /var/spool/slurm /var/spool/slurmctld 
sudo chown -R munge: /etc/munge/ /var/log/munge/ /var/lib/munge/ /run/munge/
sudo chmod 0755 /etc/munge/ /var/log/munge/ /var/lib/munge/ /run/munge/
sudo chown -R slurm: /etc/slurm/ /var/log/slurm/ /var/lib/slurm/ /run/slurm/ /var/spool/slurm/ /var/spool/slurmctld
sudo chmod 0755 /etc/slurm/ /var/log/slurm/ /var/lib/slurm/ /run/slurm/ /var/spool/slurm/ /var/spool/slurmctld
```
* Drop back to a regular user and start the `munge` service on both Nodes:

```
systemctl enable --now munge
```

* Set up the `slurm` database via the following commands on the Controller Node:

```
mysql -u root -p
CREATE DATABASE slurm_acct_db;
GRANT ALL ON slurm_acct_db.* TO 'slurm'@'localhost' IDENTIFIED BY 'slurm@1234' WITH GRANT OPTION;
FLUSH PRIVILEGES;
EXIT;
```

* Enable the `slurmctld` service on the Controller Node:

```
systemctl enable --now slurmctld
```

* Enable the `slurmd` service on the Compute Node:

```
systemctl enable --now slurmd
```

* Run the `sinfo` command  on the Controller Node to ensure the Compute Nodes can be found:

```
sinfo
PARTITION AVAIL  TIMELIMIT  NODES  STATE NODELIST
debug*       up   infinite      1   idle rocky-linux810-slurm-compute-node

sinfo -l
Thu Jan 01 16:44:59 2026
PARTITION AVAIL  TIMELIMIT   JOB_SIZE ROOT OVERSUBS     GROUPS  NODES       STATE RESERVATION NODELIST
debug*       up   infinite 1-infinite   no       NO        all      1        idle             rocky-linux810-slurm-compute-node

sinfo -Nl
Thu Jan 01 16:45:14 2026
NODELIST                           NODES PARTITION       STATE CPUS    S:C:T MEMORY TMP_DISK WEIGHT AVAIL_FE REASON              
rocky-linux810-slurm-compute-node      1    debug*        idle 1       1:1:1      1        0      1   (null) none

scontrol show node
NodeName=rocky-linux810-slurm-compute-node Arch=x86_64 CoresPerSocket=1 
   CPUAlloc=0 CPUEfctv=1 CPUTot=1 CPULoad=0.00
   AvailableFeatures=(null)
   ActiveFeatures=(null)
   Gres=(null)
   NodeAddr=192.168.1.121 NodeHostName=rocky-linux810-slurm-compute-node Version=25.05.5
   OS=Linux 4.18.0-553.89.1.el8_10.x86_64 #1 SMP Fri Dec 12 10:42:53 UTC 2025 
   RealMemory=1 AllocMem=0 FreeMem=6804 Sockets=1 Boards=1
   State=IDLE ThreadsPerCore=1 TmpDisk=0 Weight=1 Owner=N/A MCS_label=N/A
   Partitions=debug 
   BootTime=2026-01-01T14:22:23 SlurmdStartTime=2026-01-01T16:43:20
   LastBusyTime=2026-01-01T16:43:20 ResumeAfterTime=None
   CfgTRES=cpu=1,mem=1M,billing=1
   AllocTRES=
   CurrentWatts=0 AveWatts=0
   
scontrol ping
Slurmctld(primary) at rocky-linux810-slurm-controller-node is UP
```

* Execute a test job from the Controller Node:

```
srun -c 1 -n 1 -J crunchy "/bin/hostname"
rocky-linux810-slurm-compute-node
```

* Execute a test job using the test.c program file like the following:

```
srun -c 1 -n 1 -J crunchy "/home/myuser/nfs/a.out"
```
