import pandas as pd 
data={"Fruits":["Mango","Papya","Orange","Apple"],"Price":[20,400,500,600],"Quantiy":[15,20,30,35]}
df1=pd.DataFrame(data)
print(df1)

df2=df1.copy()
print(df2)
df2.loc[0,"Price"]=20
df2.loc[1,"Price"]=500
df2.loc[2,"Price"]=600
df2.loc[3,"Price"]=8000
print(df2)
print(df1.compare(df2))