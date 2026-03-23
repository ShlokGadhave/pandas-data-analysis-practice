import pandas as pd 
data=pd.read_excel("pandas_practice_data.xlsx")
print(data['Quantity'].duplicated().sum())

print(data.drop_duplicates("Quantity")) 

#drop duplicates must be used when unque id required 