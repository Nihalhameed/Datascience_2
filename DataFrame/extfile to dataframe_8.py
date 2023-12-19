#dataframe
#1. age equal to 22 >> fname,lname,age,phoneno

#2. age above 22 full data

#3. chennai loc fname,lname,age,phoneno

#4.chennai work and age above 23 fname,lname,age,phoneno

import numpy as np
import pandas as pd
df=pd.read_csv('/Users/macbook/Downloads/sample4.txt')
df.columns=['id','fname','lname','age','phoneno','loc']
print(df)

print()

#1.

df1=df.loc[df['age']==22] [['fname','lname','age','phoneno']]
print(df1)
print()

#2.

df1=df.loc[df['age']>22]
print(df1)
print()

#3.
df1=df.loc[df['loc']=='Chennai'] [['fname','lname','age','phoneno']]
print(df1)
print()

#4.
df1=df.loc[(df['loc']=='Chennai')&(df['age']>23)] [['fname','lname','age','phoneno']]
print(df1)
