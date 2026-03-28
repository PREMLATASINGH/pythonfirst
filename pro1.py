import pandas as pd
df=pd.read_csv('E-commerce .csv')
print(df)
print(df.head())
print(df.tail())
print(df.describe())
print(df.info())
print(df.isnull().sum())
print(df.fillna(0))
print(type(df))
df['total_sales']=df['Price']*df['Qantity']
print(df['total_sales'])