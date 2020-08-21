import pandas as pd 
from os import listdir
from os.path import isfile, join
import sys

# Compare compare iteration and solution time of convex modedel with the exact models
# 1) logs folder --> wrapperIPOT.py --> 2) csv_results/ .csv --> mergeInfoObj.py --> csv_formulations/objectives/ .csv iteration and time results

def mergeInfo(option,formulation,type_case,optimizer):
    if(option=="-i"):
        df = pd.DataFrame(columns=["case","iterations"])
    elif(option=="-t"):
        df = pd.DataFrame(columns=["case","time"])
        
    for csv_file in out_files:
        arr=csv_file.split("_")
        if(arr[1]==type_case and arr[2]==optimizer):
            if(arr[3]==formulation[0]+".csv" or arr[3]==formulation[1]+".csv"):
                data = pd.read_csv(mypath+"/"+csv_file) 
                # print(csv_file)
                if(option=="-i"):
                    # print(data[['case','iterations']])
                    if(df.empty):
                        df=data[['case','iterations']]
                    else:
                        df = df.merge(data[['case','iterations']], left_on='case', right_on='case', suffixes=('_CONVEX','_EXACT'))
                elif(option=="-t"):
                    # print(data[['case','time']])
                    if(df.empty):
                        df=data[['case','time']]
                    else:
                        df= df.merge(data[['case','time']], left_on='case', right_on='case',suffixes=('_CONVEX','_EXACT'))

    print(df)
    df.to_csv("csv_formulations/objectives/results_"+type_case+"_"+optimizer+option+".csv", index=False)
    

mypath="csv_results"
type_case=sys.argv[1]
out_files = [f for f in listdir(mypath) if isfile(join(mypath, f))]


optimizer="ipopt"
formulation = ["ACP","DCP"]
option = ["-i","-t"]


for opt in option:
    mergeInfo(opt,formulation,type_case,optimizer)
