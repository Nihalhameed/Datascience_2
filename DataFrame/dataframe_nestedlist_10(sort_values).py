import numpy as np
import pandas as pd
lst=[[101,'nihal','h',23,'python','tvm',25000],
     [102,'alan','h',22,'bigdata','ekm',15000],
     [103,'salman','k',21,'python','malappuram',25000],
     [104,'niha','k',35,'bigdata','tvm',12000],
     [105,'tom','holland',25,'bigdata','kottayam',22000],
     [106,'nihal','l',23,'python','tvm',25000],
     [107,'noufal','m',27,'bigdata','ekm',21000]]

df=pd.DataFrame(lst)
df.columns=['id','fname','lname','age','prof','loc','salary'] #column names is defined
print(df)

print('*'*100)

#Very important function :

#sort () : >> sorts in ascending or descending order
# >> sorts the given data by using a columnname

#Syntax :

   #newdfname=olddfname.sort_values(by='columnname')

#1. sort by age in acending order

# df1=df.sort_values(by='age')
# print(df1) #index number is also shown in ascending order along with the data
#
# print('*'*100)

#     id   fname    lname  age     prof         loc  salary
# 2  103  Salman        k   21   python  malappuram   25000
# 1  102    alan        h   22  bigdata         ekm   15000
# 0  101   nihal        h   23   python         tvm   25000
# 5  106   nihal        l   23   python         tvm   25000
# 4  105     tom  holland   25  bigdata    kottayam   22000
# 6  107  noufal        m   27  bigdata         ekm   21000
# 3  104    niha        k   35  bigdata         tvm   12000

#2. sort by age in descending order :

# df1=df.sort_values(by='age',ascending=False)
# print(df1)
#
# print("*"*100)

#3. sort by salary in descending order :

# df1=df.sort_values(by='salary')
# print(df1)

# print("*"*100)

#Note : Here 'age' and 'salary' was integer based columns > it can be sorted
#Similarly 'object'(string) data can also be sorted :
        #1. For ascending order : A to Z
        #2. For descending order : Z to A

#4. sort by fname in ascending order :
df1=df.sort_values(by='fname')
print(df1)

print("*"*100)

