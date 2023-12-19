import numpy as np
import pandas as pd

df=pd.read_csv('/Users/macbook/Downloads/customer1.txt',sep=',',header=None)
df.columns=['id','fname','lname','age','prof','loc']
print(df)

print("*"*100)

# x is the input and y is the output
#x should take all columns , delete loc-last column
#y -delete all columns other than loc

x=df.iloc[:,:-1] # full rows > : , :-1 >> deletes last column
print(x)
y=df.iloc[:,-1]  #full rows > : , -1 (gets only the last column)
print(y)


