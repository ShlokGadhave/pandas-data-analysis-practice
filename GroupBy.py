import pandas as pd 
data=pd.read_excel("ESD.xlsx")

gp=data.groupby(["Department","Gender"]).agg({"EEID":"count"})
print(gp)

gp=data.groupby("Department").agg({"Annual Salary":"max"})
print(gp)