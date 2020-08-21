import pandas as pd 
from os import listdir
from os.path import isfile, join
import sys


def mergeInfo(option,formulation,type_case):
    if(option=="-i"):
        df = pd.DataFrame(columns=["case","iterations"])
    elif(option=="-t"):
        df = pd.DataFrame(columns=["case","time"])
        
    for csv_file in out_files:
        arr=csv_file.split("_")
        if(arr[1]==type_case):
            if(arr[3]==formulation+".csv"):
                data = pd.read_csv(mypath+"/"+csv_file) 
                if(option=="-i"):
                    # print(data[['case','iterations']])
                    if(df.empty):
                        df=data[['case','iterations']]
                    else:
                        df = df.merge(data[['case','iterations']], left_on='case', right_on='case', suffixes=('_ipopt', '_knitro'))
                elif(option=="-t"):
                    # print(data[['case','time']])
                    if(df.empty):
                        df=data[['case','time']]
                    else:
                        df= df.merge(data[['case','time']], left_on='case', right_on='case',suffixes=('_ipopt', '_knitro'))

    print(df)
    df.to_csv("csv_formulations/results_"+type_case+"_"+formulation+option+".csv", index=False)
    

mypath="csv_results"
type_case=sys.argv[1]
out_files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
# option = sys.argv[1]
# formulation=sys.argv[2]
option = ["-i","-t"]
formulation = ["ACP","ACR","ACT"]


for opt in option:
    for form in formulation:
        mergeInfo(opt,form,type_case)
