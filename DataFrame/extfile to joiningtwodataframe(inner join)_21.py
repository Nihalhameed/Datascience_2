#student file
#results file

import numpy as np
import pandas as pd

df1=pd.read_csv('/Users/macbook/Downloads/student',header=None)
df2=pd.read_csv('/Users/macbook/Downloads/results',header=None)

df1.columns=['name','rollno']
df2.columns=['rollno','result']

print(df1)
print(df2)

print("*"*100)

#1. pass ayavarude >> collect name,rollno,result

df3=pd.merge(df1,df2,on='rollno',how='inner') \
      .loc[df2['result']=='pass'] [['name','rollno','result']]
print(df3)