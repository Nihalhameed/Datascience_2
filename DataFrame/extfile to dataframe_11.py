#Standard method :
#        Hierarchy order for using the functions >> loc,sort,colnames head/tail

import numpy as np
import pandas as pd
df=pd.read_csv('/Users/macbook/Downloads/sample4.txt',header=None)
df.columns=['id','fname','lname','age','phoneno','loc']
print(df)
print("*"*100)

#1. Age maximum ulla 2 employee..avarude fname,lname,age,phoneno collect aaku
#2. Age minimum ulla 1 employee..fname,lname,age,loc
#3.Chennai work cheyunna employeesil ninnum,age maximum ulla 1 employee..fname,lname,age

#1.
df1=df.sort_values(by='age',ascending=False) [['fname','lname','age','phoneno']].head(2)
print(df1)

print("*"*100)

#2.
df1=df.sort_values(by='age') [['fname','lname','age','loc']].head(1)
print(df1)
print("*"*100)


#3.

df2=df.loc[df['loc']=='Chennai'].sort_values(by='age',ascending=False) [['fname','lname','age']].head(1)
print(df2)

print("*"*100)

#Note :
#To break the above single large query to multiple queries (for each functions to be performed): use '\'


df3=df.loc[df['loc']=='Chennai'] \
      .sort_values(by='age',ascending=False) \
       [['fname','lname','age']].head(1)
print(df3)

