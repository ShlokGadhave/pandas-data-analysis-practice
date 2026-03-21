import pandas as pd 
data={"Name":["Shlok","Tommy","Jonny"],"Roll No.":[25,13,45],"Salary":[2000,4500,3000]}
df=pd.DataFrame(data)
print(df)

# to read file use pd.read_csv("path")
# to read excel file use pd.read_excel("path")