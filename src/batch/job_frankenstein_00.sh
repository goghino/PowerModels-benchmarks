#!/bin/sh

#SBATCH --job-name=SCOPF_frankenstein_00
#SBATCH -p slim
#SBATCH -n 1
#SBATCH --time=10:20:59
#SBATCH --mem=64148
#SBATCH --exclusive
#SBATCH -o ./out/slurm_frankenstein_00-%j.out
#SBATCH -e ./err/slurm_frankenstein_00-%j.err
julia run_powermodel.jl cases/frankenstein_00.m
