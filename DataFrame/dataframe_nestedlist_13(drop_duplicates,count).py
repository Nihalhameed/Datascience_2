import numpy as np
import pandas as pd
lst=[[101,'logan','h',23,'python','tvm',25000],
     [102,'alan','h',25,'bigdata','ekm',15000],
     [103,'salman','k',22,'python','malappuram',25000],
     [104,'niha','k',35,'bigdata','tvm',12000],
     [105,'tom','holland',25,'bigdata','kottayam',22000],
     [106,'nihal','l',23,'python','tvm',25000],
     [106,'nihal','l',23,'python','tvm',25000]]

df=pd.DataFrame(lst)
df.columns=['id','fname','lname','age','prof','loc','salary'] #column names is defined


#drop_duplicates() :
#       Removes duplicate rows from a dataframe

#Syntax :
#    newdfname=olddfname.drop_duplicates()

df1=df.drop_duplicates()
print(df1)
print("*"*100)

#Normal functions in pandas we studied :

#1. head()
#2. tail()
#3. dtypes()
#4. isna().sum()
#5. fillna()
#6. describe()
#7. iloc
#8. loc
#9. sort_values
#10. drop_duplicates
#11.
#12.

#Evaluating Functions in Pandas :

#1. count()
#2. max()
#3. min()
#4. sum()
#5. Mean()

#1. count () function :

#   1. Row count() :
#       When a dataset is given it is converted to dataframe, from the df need to find how many rows are present.


print(df.count())#counts the no: of rows for each elements in dataframe

print("*"*100)

# id        7
# fname     7
# lname     7
# age       7
# prof      7
# loc       7
# salary    7

#Syntax of count() :

#   newdfname=olddfname.groupby('colname') ['colname'].count()

#Note : for whichever column we need to find the count,
#then we have to group by that particular column's name itself


#1. Each profession's count:

df2=df.groupby('prof') ['prof'].count()
print(df2)
print("*"*100)

#or

#Another method to find count() :


df2a=df['prof'].value_counts()
print(df1)
print("*"*100)

#2. Ech age group count :

df3=df.groupby('age') ['age'].count()
print(df3)
print("*"*100)

#3. Each age group count and based on count here age should be sorted :
#in ascending order :


df4=df.groupby('age') ['age'].count() \
      .sort_values() #no columns
print(df4)


#in descending order :

df4=df.groupby('age') ['age'].count() \
      .sort_values(ascending=False) #no columns
print(df4)

