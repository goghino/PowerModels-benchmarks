#!/bin/sh

#SBATCH -p slim
#SBATCH -n 1
#SBATCH --time=10:20:59
#SBATCH --mem=64148
#SBATCH --exclusive
#SBATCH -o ./out/slurm-%A_%a.out
#SBATCH -e ./err/slurm-%A_%a.err
#SBATCH --array=0-24%10
# -----   inputs parameters ------- 
parameters=("case2736sp.m"
"case3012wp.m"
"case13659pegase.m"
"case42k.m"
"case6495rte.m"
"case3375wp.m"
"case1951rte.m"
"case6515rte.m"
"case2383wp.m"
"case2868rte.m"
"case6470rte.m"
"case2746wp.m"
"case6468rte.m"
"case3120sp.m"
"case2746wop.m"
"case193k.m"
"case99k.m"
"case_ACTIVSg10k.m"
"case2869pegase.m"
"case2737sop.m"
"case_ACTIVSg2000.m"
"case_ACTIVSg70k.m"
"case9241pegase.m"
"case21k.m"
"case_ACTIVSg25k.m"
)
julia run_powermodel.jl ${parameters[$SLURM_ARRAY_TASK_ID]}
