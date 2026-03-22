import pandas as pd 
import numpy as np 
data=pd.read_csv("expense3.csv")
print(data.replace(0,23))

data["Product"]=data['Product'].replace(0,"Lappy")
print(data)
