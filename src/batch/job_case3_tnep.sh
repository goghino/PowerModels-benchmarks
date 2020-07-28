#!/bin/sh

#SBATCH --job-name=SCOPF_case3_tnep
#SBATCH -p slim
#SBATCH -n 1
#SBATCH --time=10:20:59
#SBATCH --mem=64148
#SBATCH --exclusive
#SBATCH -o ./out/slurm_case3_tnep-%j.out
#SBATCH -e ./err/slurm_case3_tnep-%j.err
julia run_powermodel.jl cases/case3_tnep.m
