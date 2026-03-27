import pandas as pd

data = {"name": ["A", "B","C","D"], "age": [20, 30,40,50]}
df = pd.DataFrame(data)
print(df)
print(type(df))
print(df.shape)
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.fillna(0))
print(df)