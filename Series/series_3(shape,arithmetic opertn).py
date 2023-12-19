#To print total elements or to get the size :

#1D

import numpy as np
import pandas as pd
a=pd.Series([4,1,3,4,5])
b=pd.Series([4,3,2,1,1])

print(a.shape) #(5,)  >> order of 1*5
print(a.size) # total number of elements is displayed

#Shape should be same : Size of elements must be equal to get output


#Addition of two series :
#Syntax :

c=a.add(b)
print(c)

#output :
# 0    8
# 1    4
# 2    5
# 3    5
# 4    6

#Note :
#if shape is not same : #NaN (Not a Number) will be the output value which is the missing value

#Subtraction :

d=a.sub(b)
print(d)

#Multiplication :
e=a.mul(b)
print(e)

#Division :
f=a.div(b)
print(f)

