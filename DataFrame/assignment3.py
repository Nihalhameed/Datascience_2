import numpy as np
import pandas as pd
df=pd.read_csv('/Users/macbook/Downloads/heart_missing.csv')
print(df.isna().sum())

x=df['cp'].mode()[0]
# print(x)
df['cp'].fillna(x,inplace=True)

y=df['fbs'].mode()[0]
# print(y)
df['fbs'].fillna(y,inplace=True)

z=df['restecg'].mode()[0]
# print(z)
df['restecg'].fillna(z,inplace=True)

w=df['oldpeak'].mode()[0]
# print(w)
df['oldpeak'].fillna(w,inplace=True)

df.dropna(inplace=True,ignore_index=True)
print(df)
print(df.isna().sum())

#Cient gives a file :

#missing value find
#clean data
#find duplicates
#drop

#how to store this file after performing this operations and save it in computer local machine anywhere

#syntax :
df.to_csv(



