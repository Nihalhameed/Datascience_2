import numpy as np
import pandas as pd

df=pd.read_csv('/Users/macbook/Downloads/customer5.txt',header=None)
df.columns=['id','fname','lname','age','prof','loc','sal']
print(df)

#1. Each profession >> maximum salary [salary desc]

df1=df.groupby('prof') ['sal'].max() \
      .sort_values(ascending=False)
print(df1)

print("*"*100)

#2. Each profession >> total salary [salary desc]

df2=df.groupby('prof') ['sal'].sum() \
      .sort_values(ascending=False)
print(df2)
print("*"*100)

#3. Each country >> min salary [salary asc]

df3=df.groupby('loc') ['sal'].min() \
      .sort_values()
print(df3)
print("*"*100)

#4. Each age group >> max salary [salary desc]

df4=df.groupby('age') ['sal'].max() \
      .sort_values(ascending=False)
print(df4)
print("*"*100)

#5. Each profession >> average salary

df5=df.groupby('prof') ['sal'].mean()
print(df5)
print("*"*100)

#6. Each profession >> max age

df6=df.groupby('prof') ['age'].max()
print(df6)
print("*"*100)

#7. Each country >> min age

df7=df.groupby('loc') ['age'].min()
print(df7)

