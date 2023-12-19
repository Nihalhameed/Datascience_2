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

#2. Left outer joining :

#It prints all the row from left dataframe + data of
#matched value from right dataframe or
#null(in right df) incase of no  matching element in the two dataframe

#Syntax :

df3=pd.merge(df1,df2,on='id',how='left') #how = left >>for left outer join
print(df3)
print("*"*100)

#    id    fname lname  age     prof salary       loc
# 0   1    nihal     h   20      NaN    NaN       NaN
# 1   2   noufal     h   21      NaN    NaN       NaN
# 2   3  christo     k   22   python  15000       tvm
# 3   4  hemanth     b   24  bigdata  20000       ekm
# 4   5    karun     j   25  bigdata  25000  kottayam

#3. Right outer joining :
#........................

#It prints all the row from right dataframe + data of
#matched value from left dataframe or
#null(in left df) incase of no  matching element in the two dataframe

df4=pd.merge(df1,df2,on='id',how='right') #how = right >>for right outer join
print(df4)
print("*"*100)

#    id    fname lname   age     prof  salary       loc
# 0   3  christo     k  22.0   python   15000       tvm
# 1   4  hemanth     b  24.0  bigdata   20000       ekm
# 2   5    karun     j  25.0  bigdata   25000  kottayam
# 3   6      NaN   NaN   NaN   python   21000       ekm
# 4   7      NaN   NaN   NaN   python  140000  thrissur

#4. Full outer joining :

# Its a combination of left outer joining + right outer joining

df5=pd.merge(df1,df2,on='id',how='outer') #how = outer for full outer join
print(df5)
print("*"*100)


#QUESTION :

#Age maximum ulla 1 employee >>fname,lname,age,prof salary

df6=pd.merge(df1,df2,on='id',how='outer') \
      .sort_values(by='age',ascending=False) \
       [['fname','lname','age','prof','salary']].head(1)
print(df6)