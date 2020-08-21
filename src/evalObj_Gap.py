import pandas as pd 
from os import listdir
from os.path import isfile, join
import sys


def mergeInfo(formulation,type_case,optimizer):
    df = pd.DataFrame(columns=["case","objective_val"])
    
    for csv_file in out_files:
        arr=csv_file.split("_")
        if(arr[1]==type_case and arr[2]==optimizer):
            if(arr[3]==formulation[0]+".csv" or arr[3]==formulation[1]+".csv"):
                data = pd.read_csv(mypath+"/"+csv_file) 
                # print(csv_file)
                if(df.empty):
                    df=data[['case','objective_val']]
                else:
                    df = df.merge(data[['case','objective_val']], left_on='case', right_on='case', suffixes=('_CONVEX','_EXACT'))
               
    return df
    
    

mypath="csv_results/objectives"
type_case=sys.argv[1]
out_files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

optimizer="ipopt"
formulation = ["ACP","DCP"]
df = mergeInfo(formulation,type_case,optimizer)  
# print(df)

df= df.assign(GAP=((df["objective_val_EXACT"]-df["objective_val_CONVEX"])/df["objective_val_EXACT"] )*100)

    
print(df)
df.to_csv("csv_results/objectives/GAPs/GAPresults_"+type_case+"_"+optimizer+".csv", index=False)

