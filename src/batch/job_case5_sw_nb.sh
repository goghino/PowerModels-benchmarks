#!/bin/sh

#SBATCH --job-name=SCOPF_case5_sw_nb
#SBATCH -p slim
#SBATCH -n 1
#SBATCH --time=10:20:59
#SBATCH --mem=64148
#SBATCH --exclusive
#SBATCH -o ./out/slurm_case5_sw_nb-%j.out
#SBATCH -e ./err/slurm_case5_sw_nb-%j.err
julia run_powermodel.jl matpower/case5_sw_nb.m