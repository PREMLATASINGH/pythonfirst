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
arr5=np.max(arr2)
print("maximum value in the array:", arr5)
arr6=np.min(arr2)
print("minimum value in the array:", arr6)
arr7=np.sum(arr2)
print("sum of the array:", arr7)
a=np.array([[1, 2], [3, 4]])
b=np.array([[5, 6], [7, 8]])    
c=np.dot(a, b)
print("dot product of a and b:", c)
arr8=arr2.size
print("size of the array:", arr8)
arr9=arr2.shape     
print("shape of the array:", arr9)
arr10=arr2.reshape(5, 1) 
print("reshaped array:", arr10) 
arr11=arr2.flatten()
print("flattened array:", arr11)   
name=input("Enter your name: ")
print("Hello, " + name + "!")