#!/bin/sh

#SBATCH --job-name=SCOPF_case7_tplgy
#SBATCH -p slim
#SBATCH -n 1
#SBATCH --time=10:20:59
#SBATCH --mem=64148
#SBATCH --exclusive
#SBATCH -o ./out/slurm_case7_tplgy-%j.out
#SBATCH -e ./err/slurm_case7_tplgy-%j.err
julia run_powermodel.jl cases/case7_tplgy.m
