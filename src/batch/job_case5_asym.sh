#!/bin/sh

#SBATCH --job-name=SCOPF_case5_asym
#SBATCH -p slim
#SBATCH -n 1
#SBATCH --time=10:20:59
#SBATCH --mem=64148
#SBATCH --exclusive
#SBATCH -o ./out/slurm_case5_asym-%j.out
#SBATCH -e ./err/slurm_case5_asym-%j.err
julia run_powermodel.jl cases/case5_asym.m
