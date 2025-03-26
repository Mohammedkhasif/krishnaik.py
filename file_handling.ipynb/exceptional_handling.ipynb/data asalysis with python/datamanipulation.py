print("hello")
"""
import pandas as pd
df = pd.read_csv('data.csv') 
df.head(5)
df.tail(5)
df.discribe()
df.dtype()
HANDLING MISSING VALUES
df.isnull()
false- no MISSING VALUES
true- MISSING VALUES
df.isnull().any()
df.isnull().any(axis=1)
df.isnull().sum()


FILLING ANY MISSING VALUES
df.fillna(0)
THE MISISNG VALUES CAN BE FILLED WITH ANY VALUE


FILLING MISSING VALUES WITH THE MEAN OF THE COLUMN
df['sales_fillNA'] = df['sales].fillna(df['sales'].mean())

RENAMING COLUMNS

df.rename(column = {'sales':'total_sales'}, inplace = True)



CHANGE DATA TYPE
df['total_sales'] = df['total_sales'].astype('float') 




TO APPLY ANY FUNCTION TO ANY ONE COLUMN
WEE CAN USE LAMBDA FUNCTION
df['total_sales'] = df['total_sales'].apply(lambda x: x*2)

 



DATA AGGREGATION
grouped_mean = df.groupby('Product')['total_sales'].mean()
print(grouped_mean)

grouped_sum = df.groupby(['Product','Region'])['total_sales'].sum()
print(grouped_sum)



AGGREGATION MULTIPLE FUNCTIONS
grouped = df.groupby('Product')['total_sales'].agg(['mean','sum', count])
print(grouped)



MERGING AND JOINING DATAFRAMES

df1 = pd.DataFrame({'key': ['A', 'B', 'C', 'D'], value1 : [1,2,3,4]})
df2 = pd.DataFrame({'key': ['A', 'B', 'C', 'D'], value2 : [5,6,7,8]})
df1
df2

(key is common in both the dataframes)

pd.merge(df1,df2, on = 'key', how = 'inner')

pd.merge(df1,df2, on = 'key', how = 'outer')


pd.merge(df1,df2, on = 'key', how = 'left')







"""