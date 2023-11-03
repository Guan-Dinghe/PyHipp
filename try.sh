#!/bin/bash

# Submit this script with: sbatch <this-filename>

#SBATCH --time=24:00:00   # walltime
#SBATCH --ntasks=1   # number of processor cores (i.e. tasks)
#SBATCH --nodes=1   # number of nodes
#SBATCH --cpus-per-task=5	# number of processors per task
#SBATCH -J "try"   # job name

## /SBATCH -p general # partition (queue1)
#SBATCH -o try-slurm.%N.%j.out # STDOUT
#SBATCH -e try-slurm.%N.%j.err # STDERR

# LOAD MODULES, INSERT CODE, AND RUN YOUR PROGRAMS HERE
sleep 30
aws sns publish --topic-arn arn:aws:sns:ap-southeast-1:171322778133:awsnotify --message "RPLS4aJobDone"
