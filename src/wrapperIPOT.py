from os import listdir
import numpy as np
from os.path import isfile, join
import os
import pandas as pd 
import sys

# create a csv file with the time solution and iterations of each case
#-i    iterations info
#-t    time solve info
#-a    all info
# option = sys.argv[1]
option = "-a"

mypath=sys.argv[1]
out_files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
name_logs=""
file=""
#find type case
for log_file in out_files:
    f = open(mypath+"/"+log_file, "r")
    case= f.readline()
    case=case.replace("\n","")
    arr =case.split('/')
    print(arr)
    f.close()
    if(len(arr)>1):
        file=log_file
        name_logs=arr[1]
        break
#find optimizer formulation
f = open(mypath+"/"+file, "r")
f.readline()
optimizer= f.readline()
optimizer=optimizer.replace("\n","")
formulation= f.readline()
formulation=formulation.replace("\n","")
print("Case set: "+ name_logs+" Optimizer: "+ optimizer +" Formulation: "+ formulation)
f.close()


df = pd.DataFrame(columns=["case","iterations","time"])
#fill the dataframe with the output of each OPF simulation
for log_file in out_files:
    f = open(mypath+"/"+log_file, "r")
    case= log_file.replace('.out','')
    case= case.replace('log_','')
    # print(case)
    it=np.nan
    time_sim=np.nan
    for line in f:
        if(optimizer=="knitro"):
            if "# of iterations" in line:
                it=line.replace("# of iterations","")
                it=it.replace("=","")
                it=it.replace("\n","")
                it=it.strip()
                it=int(it)
                # print(line)
        elif(optimizer=="ipopt"):
            if "Number of Iterations....:" in line:
                it=line.replace("Number of Iterations....: ","")
                it=int(it)
        
        if "Time to Solution........:" in line:
            time_sim=line.replace("Time to Solution........:","")
            time_sim=float(time_sim)
            # print(line)
    df=df.append({"case":case,"iterations":it,"time":time_sim}, ignore_index=True)
    f.close()
    
if(option=="-a"):
    print(df)
    # Export to csv file
    df.to_csv("csv_results/results_"+name_logs+"_"+optimizer+"_"+formulation+".csv", index=False)
elif(option=="-i"):
    print(df[['case','iterations']])
elif(option=="-t"):
    print(df[['case','time']])
    
