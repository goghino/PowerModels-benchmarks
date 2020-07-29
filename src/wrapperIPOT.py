from os import listdir
from os.path import isfile, join
import os
import pandas as pd 
import sys

#-i    iterations info
#-t    time solve info
#-a    all info
option = sys.argv[1]

mypath="logs"
out_files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
df = pd.DataFrame(columns=["case","iterations","time"])

for log_file in out_files:
    f = open(mypath+"/"+log_file, "r")
    case= f.readline()
    case=case.replace("\n","")
    # print(case)
    it="0"
    time_sim="0"
    for line in f:
       
        if "Number of Iterations....:" in line:
            it=line.replace("Number of Iterations....: ","")
            # print(line)
        elif "Time to Solution........:" in line:
            time_sim=line.replace("Time to Solution........:","")
            # print(line)
    df=df.append({"case":case,"iterations":int(it),"time":float(time_sim)}, ignore_index=True)
    f.close()
    
if(option=="-a"):
    print(df)
elif(option=="-i"):
    print(df[['case','iterations']])
elif(option=="-t"):
    print(df[['case','time']])