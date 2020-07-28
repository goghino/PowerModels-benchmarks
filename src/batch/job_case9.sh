#!/bin/sh

#SBATCH --job-name=SCOPF_case9
#SBATCH -p slim
#SBATCH -n 1
#SBATCH --time=10:20:59
#SBATCH --mem=64148
#SBATCH --exclusive
#SBATCH -o ./out/slurm_case9-%j.out
#SBATCH -e ./err/slurm_case9-%j.err
julia run_powermodel.jl cases/case9.m
