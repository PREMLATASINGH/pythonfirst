import pandas as pd

data = {"name": ["A", "B"], "age": [20, 30]}
df = pd.DataFrame(data)
print(df)
print(type(df))
print(df.shape)