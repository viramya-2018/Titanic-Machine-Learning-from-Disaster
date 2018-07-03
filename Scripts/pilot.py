import numpy as np
import csv  
import pandas as pd

arr = []
arr.append([1,2])
arr.append([1,2])
arr.append([1,2])

print arr[0][0]

a = pd.DataFrame(data=arr,columns=['c','d'])
a.to_csv("ppp.csv", header=None)
print a