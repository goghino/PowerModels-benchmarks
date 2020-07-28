#!/bin/sh

#SBATCH --job-name=SCOPF_case3_oltc_pst
#SBATCH -p slim
#SBATCH -n 1
#SBATCH --time=10:20:59
#SBATCH --mem=64148
#SBATCH --exclusive
#SBATCH -o ./out/slurm_case3_oltc_pst-%j.out
#SBATCH -e ./err/slurm_case3_oltc_pst-%j.err
julia run_powermodel.jl cases/case3_oltc_pst.m
