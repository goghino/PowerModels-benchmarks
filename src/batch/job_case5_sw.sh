#!/bin/sh

#SBATCH --job-name=SCOPF_case5_sw
#SBATCH -p slim
#SBATCH -n 1
#SBATCH --time=10:20:59
#SBATCH --mem=64148
#SBATCH --exclusive
#SBATCH -o ./out/slurm_case5_sw-%j.out
#SBATCH -e ./err/slurm_case5_sw-%j.err
julia run_powermodel.jl cases/case5_sw.m
