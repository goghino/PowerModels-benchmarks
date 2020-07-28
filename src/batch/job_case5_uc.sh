#!/bin/sh

#SBATCH --job-name=SCOPF_case5_uc
#SBATCH -p slim
#SBATCH -n 1
#SBATCH --time=10:20:59
#SBATCH --mem=64148
#SBATCH --exclusive
#SBATCH -o ./out/slurm_case5_uc-%j.out
#SBATCH -e ./err/slurm_case5_uc-%j.err
julia run_powermodel.jl matpower/case5_uc.m