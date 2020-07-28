#!/bin/sh

#SBATCH --job-name=SCOPF_case5_uc_strg
#SBATCH -p slim
#SBATCH -n 1
#SBATCH --time=10:20:59
#SBATCH --mem=64148
#SBATCH --exclusive
#SBATCH -o ./out/slurm_case5_uc_strg-%j.out
#SBATCH -e ./err/slurm_case5_uc_strg-%j.err
julia run_powermodel.jl cases/case5_uc_strg.m
