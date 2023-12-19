#Joining :

#     Combining two dataframes is called joining
#     (condition : two dataframes should have common field,using this common field joining is performed)

# 4 types of joining :

#1. Inner joining (Important)
#2. Left outer joining
#3. Right outer joining
#4. Full outer joining

#1. Create dic1 > need to collect id,fname,lname,age >5 employee details

#2.Create dic2> need to collect id,prof,salary,loc >5 employee details



dic1={'id':[1,2,3,4,5],
      'fname':['nihal','noufal','christo','hemanth','karun'],
      'lname':['h','h','k','b','j'],
      'age':[20,21,22,24,25]}
dic2={'id':[3,4,5,6,7],
      'prof':['python','bigdata','bigdata','python','python'],
      'salary':['15000','20000','25000','21000','140000'],
      'loc':['tvm','ekm','kottayam','ekm','thrissur']}

import numpy as np
import pandas as pd

df1=pd.DataFrame(dic1)
df2=pd.DataFrame(dic2)

print(df1)
print(df2)
print("*"*100)

#1. Inner joining : While joining two dataframes having common field ..their data should match and
  #                thus the matched element data is collected from both the dataframes.

#Syntax :

#  newdfname=pd.merge(df1,df2,on='colname',how='inner')

df3=pd.merge(df1,df2,on='id',how='inner')
print(df3) #'id' equal aayitullavrude matched elementsinte (3,4,5) full-data collect aakkum

print("*"*100)
#1a. id equal aayavarude >> collect fname,lname,prof,salary

df4=pd.merge(df1,df2,on='id',how='inner') [['fname','lname','prof','salary']]
print(df4) #id equal ayitulavarude matched elementsinte selected-column data collect aakkum
print("*"*100)

#1b. id equal,age maximum ulla 2 employee >>collect fname,lname,age,prof,salary

df5=pd.merge(df1,df2,on='id',how='inner') \
      .sort_values(by='age',ascending=False) \
      [['fname','lname','age','prof','salary']].head(2)
print(df5)
print("*"*100)

#1C. From the joined data,Big data profession work cheyunnavarude,age maximum ulla 1 employee >>
#    collect fname,lname,age,prof,salary

df6=pd.merge(df1,df2,on='id',how='inner') \
      .loc[df2['prof']=='bigdata'] \
      .sort_values(by='age',ascending=False) \
      [['fname','lname','age','prof','salary']].head(1)
print(df6)
print("*"*100)

#1d. Salary minimum ulla 1 employee >> collect fname,lname,age,prof,salary

df7=pd.merge(df1,df2,on='id',how='inner') \
      .sort_values(by='salary') \
      [['fname','lname','age','prof','salary']].head(1)
print(df7)
