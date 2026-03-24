---
title: "How to Run Benchmarking for PingPong and allreduce on a Rocky Linux image:"
category: "rocky-linux"
tags: ["rocky-linux", "run", "mpi", "benchmarking", "pingpong"]
---

# How to Run Benchmarking for PingPong and allreduce on a Rocky Linux image:

PingPong
/usr/mpi/gcc/openmpi-4.1.7rc1/bin/mpirun -n 2 -N 1 -hostfile hostlist.txt -x UCX_NET_DEVICES=mlx5_0:1 /usr/mpi/gcc/openmpi-4.1.7rc1/tests/imb/IMB-MPI1 -msglog 27:28 pingpong

Allreduce (We are using 36 cores/node to match the number of cores used in the Oracle implementation)
/usr/mpi/gcc/openmpi-4.1.7rc1/bin/mpirun -n 72 -N 36 -hostfile hostlist.txt -x UCX_NET_DEVICES=mlx5_0:1 /usr/mpi/gcc/openmpi-4.1.7rc1/tests/imb/IMB-MPI1 -npmin 72 allreduce
