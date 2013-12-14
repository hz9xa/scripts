#!/bin/sh
############################################################
# PBS script for submmitting jobs in to queue on ITC cluster
############################################################

#PBS -l select=1:ncpus=1:mem=64GB
#PBS -l walltime=100:00:00
#PBS -o output.o
#PBS -j oe
#PBS -m bea
#PBS -M hz9xa@virginia.edu
#PBS -V

cd $PBS_O_WORKDIR
python err_prof_sfu.py isfu_err.txt

