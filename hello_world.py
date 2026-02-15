print("hello world")
print(" I am premlata singh")
import pandas as pd
print("pandas version:", pd.__version__)
import numpy as np
print("numpy version:", np.__version__)
arr=np.array([1, 2, 3, 4, 5])
print("numpy array:", arr)
arr1=arr*2
print("array multiplied by 2:", arr1)
arr1=arr1+5
print("array after adding 5:", arr1)
arr2=arr1+arr
print("array after adding original array:", arr2)   
arr3=np.sqrt(arr2)
print("square root of the array:", arr3)
arr4=np.log(arr2)
print("logarithm of the array:", arr4)