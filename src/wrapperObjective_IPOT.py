from os import listdir
import numpy as np
from os.path import isfile, join
import os
import pandas as pd 
import sys

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


df = pd.DataFrame(columns=["case","objective_val"])
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
            if "Final objective value " in line:
                it=line.replace("Final objective value","")
                it=it.replace("=","")
                it=it.replace("\n","")
                it=it.strip()
                it=float(it)
                # print(line)
        elif(optimizer=="ipopt"):
            if "Objective...............:" in line:
                arr=line.split(" ")
                it=arr[7].replace("\n","")
                it=float(it)
            # print(line)
    df=df.append({"case":case,"objective_val":it}, ignore_index=True)
    f.close()
    

print(df)
# # Export to csv file
df.to_csv("csv_results/objectives/OBJresults_"+name_logs+"_"+optimizer+"_"+formulation+".csv", index=False)

    
