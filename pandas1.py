import pandas as pd

data = {"name": ["A", "B","c"], "age": [20, 30,40]}
df = pd.DataFrame(data)
print(df)
print(type(df))
print(df.shape)
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.fillna(0))
print(df)