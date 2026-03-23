import pandas as pd 
data=pd.read_excel("ESD.xlsx")
data["Bonus"]=(data['Annual Salary']/100)*2 #makes column from the original column 
print(data)

