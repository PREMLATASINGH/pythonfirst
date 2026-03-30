import numpy as np
import pandas as pd
data={"name": ["A", "B","C","D","E","F"], "age": [20, 30,40,50,43,54]}

df=pd.DataFrame(data)
print(df)
print(df.head())
print(df.tail())