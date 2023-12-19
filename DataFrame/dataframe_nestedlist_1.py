#Convert Nested list to dataframe :

#id,fname,lname,age,prof,location,salary

import pandas as pd

#7 employee details :

lst=[[101,'nihal','h',23,'python','tvm',25000],
     [102,'alan','h',22,'bigdata','ekm',15000],
     [103,'Salman','k',21,'python','malappuram',25000],
     [104,'niha','k',35,'python','tvm',12000],
     [105,'tom','holland',25,'bigdata','kottayam',22000],
     [106,'nihal','l',23,'python','tvm',25000],
     [107,'noufal','m',27,'bigdata','ekm',21000]]

df=pd.DataFrame(lst,columns=(['id','fname','lname','age','prof','location','salary'])) #column names is defined
print(df)

print("*"*100)



#From given dataframe print first 3 rows and last one row :
print(df.head(3))

print()

print(df.tail(1)) #prints the last row

print("*"*100)

#Datatype check :


print(df.dtypes)

print("*"*100)

#output :
# id           int64
# fname       object (object is the datatype instead of string)
# lname       object
# age          int64
# location    object
# salary       int64

#Describe() function :

print(df.describe()) #by default from the dataframe it reads only integer-format columns

#                id        age        salary
# count    7.000000   7.000000      7.000000
# mean   104.000000  25.142857  20714.285714
# std      2.160247   4.775932   5250.850271
# min    101.000000  21.000000  12000.000000
# 25%    102.500000  22.500000  18000.000000
# 50%    104.000000  23.000000  22000.000000
# 75%    105.500000  26.000000  25000.000000
# max    107.000000  35.000000  25000.000000

#To read  'object' columns in the dataframe :

print(df.describe(include='O')) #capital O used

#         fname lname    prof location
# count       7     7       7        7
# unique      6     5       2        4  (unique- prints the count of unique elements without repetition)
# top     nihal     h  python      tvm  (top - most repeated value or word is shown and its count is determined by top)
# freq        2     2       4        3  (freq - shows the frequency count of 'top')

print("*"*100)


print(df.describe(include='all')) #All columns are printed including integer type and object >>dtypes

print("*"*100)

print(df.columns) # just the column name is printed

print("*"*100)

print(df.info()) #collects all the information od the dataframe

print("*"*100)

 #How to add a new column to a dataframe in list :
#
# df['Gender']=['M','M','M','F','M','M','M']
# print(df)

#1. How to change(Rename) a column name :


#Syntax :

#newdataframefname=olddataframename.rename(columns={'oldcolname':'newcolname'})


df1=df.rename(columns={'fname':'first_name'})
print(df1)

print("*"*100)


#2. Collecting only needed columns :

#Syntax :

#newdfname=olddfname[['colnames']]

#fname,lname,age,prof >>> collect this columns

df1=df[['fname','lname','age','prof']]
print(df1)

print("*"*100)


