import os
from os import listdir
from os.path import isfile, join
import sys

partition = "slim"
mypath=sys.argv[1]
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

print(onlyfiles)
# JOB - ARRAY STRATEGY
def runBench():
    batch_file="runBench_array.sh"
    os.popen("rm -rf out").read()
    os.popen("rm -rf err").read()
    os.popen("mkdir out").read()
    os.popen("mkdir err").read()
    f = open(batch_file, "w+")
    f.write("#!/bin/sh\n\n")
    f.write("#SBATCH -p %s\n" %partition)
    f.write("#SBATCH -n 1\n")
    f.write("#SBATCH --time=10:20:59\n")
    f.write("#SBATCH --mem=64148\n")
    f.write("#SBATCH --exclusive\n")
    f.write("#SBATCH -o ./out/slurm-%A_%a.out\n")
    f.write("#SBATCH -e ./err/slurm-%A_%a.err\n")
    f.write("#SBATCH --array=0-{}%5".format(len(onlyfiles)-1))
    f.write("\n")
    f.write("# -----   inputs parameters ------- \n")
    # ----  write parameters inside job array  ---
    f.write("parameters=(")
    for rd in onlyfiles:
        f.write("\"")
        f.write("%s\"\n" % (mypath+str(rd)))
    f.write(")")
    f.write("\n")
    # ----------------------------------------------
    f.write("julia run_powermodel.jl ${parameters[$SLURM_ARRAY_TASK_ID]}\n")
    f.close()
    job = os.popen("sbatch " + batch_file).read()
    print(job)
 
if (__name__ == '__main__'):
    runBench()
