import numpy as np
import pandas as pd
df=pd.read_csv('sales2017_raw.csv')
print(df)
print(df.head())
print(df.tail())
print(df.describe())
print(df.isnull().sum())