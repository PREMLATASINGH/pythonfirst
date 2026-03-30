import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data={"name": ["A", "B","C","D","E","F","G","H"], "age": [20, 30,40,50,43,54,43,23]}

df=pd.DataFrame(data)
print(df)
print(df.head())
print(df.tail())
print(df.isnull().sum())
print(df.shape)
print(df.fillna(0))
print(df.describe())
plt.hist(df)
plt.show()
print(df.info())
