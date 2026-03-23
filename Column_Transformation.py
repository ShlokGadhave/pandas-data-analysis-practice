import pandas as pd 
data=pd.read_excel("ESD.xlsx")
#print(data)
data.loc[(data[ "Bonus %"])==0 ,"GetBonus"]="No Bonus"
data.loc[(data["Bonus %"])>0,"GetBonus"]=" Bonus" #useful for making colums from any existing columns 
print(data.head(10))

import pandas as pd 
data=pd.read_excel("ESD.xlsx")
data["Title"]=data["Full Name"]+" "+data["Job Title"]
print(data)