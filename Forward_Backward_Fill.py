import pandas as pd 
data=pd.read_excel("pandas_practice_data.xlsx")
print(data.fillna(method="ffill"))
print(data.fillna(method="bfill"))
