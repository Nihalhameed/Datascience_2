#convert nested dictionary to dataframe :

#Creating a nested dictionary : >> key is passed with all the values and key acts as column name here
import numpy as np
import pandas as pd

dic={'id':[101,102,103,104,105],
     'fname':['nih','arun','anu','vipin','sanjay'],
      'lname':['k','s','d','k','m'],
      'age':[22,23,25,27,30],
      'marks':[50,50,45,40,45]
     }
df=pd.DataFrame(dic)
print(df)

print()

print(df.shape)

#Note : In a nested dictionary its key value act as column name. So dont need to mention column name

print(df.head(3))

print()

print(df.tail(2))

print()

print(df.dtypes)

# id        int64
# fname    object
# lname    object
# age       int64
# marks     int64

#How to add new column to a dataframe in dictionary :

df['location']=['tvm','tvm','ekm','malprm','thrissur']
print(df)

