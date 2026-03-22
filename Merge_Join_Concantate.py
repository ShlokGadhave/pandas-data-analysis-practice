import pandas as pd 
data1={"Employee Id":["EM01",'EM02',"EM03"],"Salary":[20000,3000,40000]}
data2={"Employee Id":["EM04",'EM05',"EM06"],"Gender":["F","M","F"]}
df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)
print(df1)
print(df2)
print(pd.merge(df1,df1,on="Employee Id")) # data merged on the basis of the employee id 
print(pd.merge(df1,df2,on="Employee Id",how="right")) # data merge on the basis on right 
print(pd.merge(df1,df2,on="Employee Id",how="left"))

print(pd.concat([df1,df2]))
