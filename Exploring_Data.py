import pandas as pd 
data=pd.read_excel("Data-for-Practice.xlsx")
print(data)
print(data.head(10)) #Give us first 10 rows that is from the it gives us first 10 rows form each column 
print(data.tail(10)) #Give us first 10 rows from downwards 

# default value of head and tail is 5
