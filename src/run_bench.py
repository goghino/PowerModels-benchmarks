import os
from os import listdir
from os.path import isfile, join
import sys

partition = "slim"
mypath=sys.argv[1]
cases_files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

def chunkIt(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return out

# print(cases_files)
# JOB - POOL STRATEGY
def runBench():
    max_job_limit=10
    bin_chunks= chunkIt(cases_files,max_job_limit)
    print(bin_chunks)
    os.popen("rm -rf batch").read()
    os.popen("rm -rf out").read()
    os.popen("rm -rf err").read()
    os.popen("mkdir out").read()
    os.popen("mkdir err").read()
    os.popen("mkdir batch").read()
    count=0
    for chunk in bin_chunks:
        job_name="SCOPF_"+str(count)
        batch_file="batch/job_"+job_name+".sh"
        f =open(batch_file,"w+")
        f.write("#!/bin/sh\n\n")
        f.write("#SBATCH --job-name="+job_name+"\n")
        f.write("#SBATCH -p %s\n" %partition)
        f.write("#SBATCH -n 1\n")
        f.write("#SBATCH --time=10:20:59\n")
        f.write("#SBATCH --mem=64148\n")
        f.write("#SBATCH --exclusive\n")
        f.write("#SBATCH -o ./out/slurm_"+job_name+"-%j.out\n")
        f.write("#SBATCH -e ./err/slurm_"+job_name+"-%j.err\n")
        # ----------------------------------------------
        for rd in chunk:
            case_name=rd.replace('.m','')
            f.write("julia run_powermodel.jl "+mypath+rd+" >> logs/log_"+case_name+".out\n")
        f.close()
       	# job = os.popen("sbatch " + batch_file).read()
        # print(job)
        count+=1
 
if (__name__ == '__main__'):
    runBench()
