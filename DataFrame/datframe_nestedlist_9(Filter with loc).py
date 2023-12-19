import numpy as np
import pandas as pd
lst=[[101,'nihal','h',23,'python','tvm',25000],
     [102,'alan','h',22,'bigdata','ekm',15000],
     [103,'Salman','k',21,'python','malappuram',25000],
     [104,'niha','k',35,'bigdata','tvm',12000],
     [105,'tom','holland',25,'bigdata','kottayam',22000],
     [106,'nihal','l',23,'python','tvm',25000],
     [107,'noufal','m',27,'bigdata','ekm',21000]]

df=pd.DataFrame(lst,columns=(['id','fname','lname','age','prof','location','salary'])) #column names is defined
print(df)

print("*"*100)

#Filter  : Using function >> loc
 # Collects only information/data based on condition

#Syntax :

#1. loc with #one condition :

#   newdataframename=olddataframename.loc[olddf['colname']condition]

#collect full details of people whose age>27

df1=df.loc[df['age']>27]
print(df1)


print("*"*100)

#age==25 , collect their fname,lname,age,salary (collect these columns)

df1=df.loc[df['age']==25] [['fname','lname','age','salary']] #
print(df1)

print("*"*100)

#bigdata working profession, collect their full details


df1=df.loc[df['prof']=='bigdata']
print(df1)

print("*"*100)

#2. loc with more than one condition :



#Syntax :

# newdfname=oldfname.loc[(olddf['colname']codition1)&(olddf['colname']conditon2)]

#1. age baove 27 and prof bigdata

df1=df.loc[(df['age']>27)&(df['prof']=='bigdata')]

print(df1)

print("*"*100)

#2. salary above 15000 and prof python if both these condtion satisfy then. collect details : fname,lname,age,loc

df1=df.loc[(df['salary']>15000)&(df['prof']=='python')] [['fname','lname','age','location']]
print(df1)

