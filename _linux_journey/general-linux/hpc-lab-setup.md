---
title: "Hpc Lab Setup"
category: "general-linux"
tags: ["hpc", "lab", "setup"]
---

The HPC Lab is a persistent deployment in Vultr to allow the SA team to prototype solutions in a shared environment.
Goals

    A testing site for our Ansible automation, Warewulf, and IQube deployments.

    Environment to troubleshoot Warewulf issues. 

    Easy button to deploy Warewulf Slurm demo environemnt. 

Prerequisites

Access to Vultr

Mountain access key that has access to Classic HPC Infrastructure 8 subscription 

Access to Bitbucket repos

    Ansible installed on your laptop

    Terraform

API Access to Vultr

Authorise your IP address to use the Vultr API. (This can change frequently, depending on your ISP.)
![205f205a292e464faf7733a996926a9f.png](../_resources/205f205a292e464faf7733a996926a9f-1.png)
Deploy a Slurm HPC Lab Environment on Vultr
Deploying the Environment

The following section walks though how to deploy a Slurm HPC cluster of CPU instances on Vultr where: 

    Slurm components (controller, and database) are installed using packages from OpenHPC

    Warewulf is installed through Mountain using subscription warewulf-rocky-8

    Slurm compute node Warewulf image is imported using Mountain subscription warewulf-node-images

    Warewulf overlays are configured using Ansible templates/files. 

    Warewulf nodes and node profiles are managed using an Ansible fact and rendered using a Jinja template

    Pull down classic-hpc repository

git clone git@bitbucket.org:ciqinc/classic-hpc.git && cd classic-hpc

    Set up Ansible dynamic inventory. 

        Populate inventory.vultr.yml with your Vultr API key in field api_keyand update the filter with your user name for the owner Vultr tag. For example owner:bphan. When provisioning the HPC lab environment, your instances will be tagged with owner:<username>. 

        Inventory groups are set based on instance tags: warewulf_servers, scheduler, and database.

    Create a copy of configs/warewulf-slurm-vultr-demo.yml called cluster.config.yml

cp config/warewulf-slurm-vultr-demo.yml configs/cluster.config.yml 

    Run the playbook to stand up the HPC lab

ansible-playbook -u root -i inventory.vultr.yml \
  --extra-vars "bitbucket_ssh_private_key=/path/to/private/key" \
  --extra-vars "vultr_api_key=[redacted]" \
  --extra-vars "vultr_ssh_public_key=/path/to/public/key" \
  --extra-vars "ciq_mountain_access_key=[redacted]" \
  playbooks/setup-hpc-lab.yml

 
Run example hello world job. 

    Log in via SSH to hpc-lab-control0. 

        You can easily find the public IP of this host using command ansible-inventory -i inventory.vultr.yml --list

    Switch to your test user - su - test

    Allocate resources for your job. The following command will allocate a single node and 4 cores: 

        salloc -N 1 -n 4 

    Compile an example MPI hello world job

        mpicc -O3 /opt/ohpc/pub/examples/mpi/hello.c

    Run the compiled program

        prun ./a.out

You should see this following output: 
[test@hpc-lab-control0 ~]$ prun ./a.out 
[prun] Master compute host = hpc-lab-control0
[prun] Resource manager = slurm
[prun] Launch cmd = mpirun ./a.out (family=openmpi4)

 Hello, world (4 procs total)
    --> Process #   0 of   4 is alive. -> bphan-hpc-lab-compute0
    --> Process #   2 of   4 is alive. -> bphan-hpc-lab-compute0
    --> Process #   3 of   4 is alive. -> bphan-hpc-lab-compute0
    --> Process #   1 of   4 is alive. -> bphan-hpc-lab-compute0

If you have successfully run the test job, your environment should be set up to run the following demo: 
Tearing down the HPC lab

When you have finished testing or doing a demo you can tear down the provisioned environment by running the playbook destroy-hpc-lab.yml. 
ansible-playbook -u root -i inventory.vultr.yml \
  --extra-vars "vultr_api_key=[redacted]" \
  --extra-vars "vultr_ssh_public_key=/path/to/public/key" \
  playbooks/destroy-hpc-lab.yml
Deployment FAQ

Q: I have submitted a job or requested compute resources in Slurm, but my job is stuck in a pending state or the scheduler is taking a long time to assign my user compute resources. How do I debug this? 

A: First check the status of your nodes using command sinfo.  For example, the output below shows node bphan-hpc-lab-compute0 is in a down state, which prevent cluster users from using the compute resource. 
[root@hpc-lab-control0 ~]# sinfo
PARTITION AVAIL  TIMELIMIT  NODES  STATE NODELIST
normal*      up 1-00:00:00      1   down bphan-hpc-lab-compute0

If there is an asterisk beside the state (ex. down*), this mean that the Slurm controller cannot reach the Slurm client (slurmd) on the compute node. This typically indicates the service had issues starting up during the boot process. 

To put the compute node back into state idle, run the following command as root on the node the Slurm controller is running on: 
scontrol update nodename=bphan-hpc-lab-compute0 state=idle

After running the command above, we can run sinfo again to confirm the node is back in and idle state. 
[root@hpc-lab-control0 ~]# sinfo
PARTITION AVAIL  TIMELIMIT  NODES  STATE NODELIST
normal*      up 1-00:00:00      1   idle bphan-hpc-lab-compute0

If your job was previously queued, it should being running once the compute node is put back into an idle state. If there is a job running on the node, you should see the node in state alloc. 
Warewulf Demo FAQ

Q: How is a Warewulf node image container differ from a Docker container I would create which runs, for example, an Apache server?

A: Warewulf node image container have a kernel installed in the container. When a Warewulf managed node is PXE booting, it will use the kernel within the node image to boot the bare metal node. 

Q: Can I manage a VM running in VMWare with Warewulf?

A: Yes.

Q: Can Warewulf manage a login node in addition to my compute nodes?

A: Yes, Warewulf can manage a login node. We would recommend setting up a new node profile for a login node. This new profile will have an additional network interface configured which allows users to SSH into the login node.  

Q: How do you tell Warewulf which interface to provision over?

A: That’s meant to be the “primary” interface. But, ultimately, it depends on the BIOS / firmware on the compute node and which interface it attempts to PXE boot over first.
Deploy a IQube Lab Environment

TODO
Configuration

    https://bitbucket.org/ciqinc/hpc-lab/

    https://bitbucket.org/ciqinc/classic-hpc/

    https://bitbucket.org/ciqinc/iqube-ansible/