#!/bin/sh

#SBATCH -p slim
#SBATCH -n 1
#SBATCH --time=10:20:59
#SBATCH --mem=64148
#SBATCH --exclusive
#SBATCH -o ./out/slurm-%A_%a.out
#SBATCH -e ./err/slurm-%A_%a.err
#SBATCH --array=0-25%5
# -----   inputs parameters ------- 
parameters=("../cases/case14.m"
"../cases/case2.m"
"../cases/case24.m"
"../cases/case3.m"
"../cases/case30.m"
"../cases/case3_oltc_pst.m"
"../cases/case3_tnep.m"
"../cases/case5.m"
"../cases/case5_asym.m"
"../cases/case5_clm.m"
"../cases/case5_db.m"
"../cases/case5_dc.m"
"../cases/case5_ext.m"
"../cases/case5_gap.m"
"../cases/case5_npg.m"
"../cases/case5_pwlc.m"
"../cases/case5_strg.m"
"../cases/case5_sw.m"
"../cases/case5_sw_nb.m"
"../cases/case5_tnep.m"
"../cases/case5_uc.m"
"../cases/case5_uc_strg.m"
"../cases/case6.m"
"../cases/case7_tplgy.m"
"../cases/case9.m"
"../cases/frankenstein_00.m"
)
julia run_powermodel.jl ${parameters[$SLURM_ARRAY_TASK_ID]}
