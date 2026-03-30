import numpy as np
import pandas as pd
data={"product":["laptop","phone","chair","table","laptop",'airpot','table'],
    "category":["tech","tech","furniture","furniture","tech",'tech',"furniture"],
    "quantity":[1,2,3,1,2,7,4],
    "price":[1200,800,150,300,1200,500,675],
    "sales":[900,500,100,200,900,700,800],
    "region":["east","west","east","south","west","east","west"],
    "date":['2024-01-01','2024-01-02','2024-01-03','2024-01-04','2024-01-01','2024-01-05','2024-01-06']
}
df=pd.DataFrame(data)
print(df)
df = df.drop(columns=['date'])
print(df)
print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.describe())
print(df.isnull().sum())
total_sales = df['sales'].sum()
print(total_sales)
sale_by_cateogry=df.groupby('category')['sales'].sum()
print(sale_by_cateogry)
sale_by_region=df.groupby('region')['sales'].sum()
print(sale_by_region)
sale_by_quantity=df.groupby('quantity')['sales'].sum()
print(sale_by_quantity)
sale_by_product=df.groupby('product')['sales'].sum()
print(sale_by_product)
print(df['product'],df['price'])
print(df["price"]>700)
print(df["price"]>800)
print(df["product"].unique)
print(df['price'].unique)
print(df['region'].unique)
print(df["product"].value_counts())
print(df["price"].value_counts())
print(df["region"].value_counts())
print(df["category"].value_counts())
print(df["quantity"].value_counts())
df1=df[df['product']=='laptop']
print(df1)
df2=df[(df["price"]>800)&(df["region"]=='east')]
print(df2)
df3=df[(df["sales"].sum())&df["quantity"]>2]
print(df3)


