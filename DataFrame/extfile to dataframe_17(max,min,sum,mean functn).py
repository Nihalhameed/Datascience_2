#2. max function () :

# Collect the maximum value

#Syntax :

#  newdfnam=olddfname.groupby('colname') ['colname'].max()

#Note: grouping column and selecting column is differenT
#Note2 : in count()- only a single columns is used.. while in max() we need two columns to be considered

import numpy as np
import pandas as pd

df=pd.read_csv('/Users/macbook/Downloads/Temperature',header=None,sep=' ')
df.columns=['year','temperature']
print(df)

print("*"*100)


#1.For each year maximum temeperature is to be found [maximum temp desc order]:

df1=df.groupby('year') ['temperature'].max() \
      .sort_values(ascending=False)
print(df1)

print("*"*100)

#3. max function () :

#Syntax :

#  newdfname=olddfname.groupby('colname') ['colname'].min()

#1.For each year minimum temeperature is to be found []:

df2=df.groupby('year') ['temperature'].min()
print(df2)

print("*"*100)

#4. sum function () :

#Syntax :

 #newdfname=olddfname.groupby('colname') ['colname'].sum()

#1. For each year,caalculate total temperature :

df3=df.groupby('year') ['temperature'].sum()
print(df3)

print("*"*100)

#5. mean function (average) :
#Syntax :

 #newdfname=olddfname.groupby('colname') ['colname'].mean()

#1. For each year,caalculate average  temperature

df4=df.groupby('year') ['temperature'].mean()
print(df4)


