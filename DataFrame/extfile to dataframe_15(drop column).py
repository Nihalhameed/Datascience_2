#How to drop a column from a dataframe :

#Syntax :

#   newdfname=olddfname.drop(['colname'],axis=1)

# Standard usage : axis=1 : for columns & axis=0 for rows

import numpy as np
import pandas as pd

df=pd.read_csv('/Users/macbook/Downloads/customer1.txt',header=None)
df.columns=['id','fname','lname','age','prof','loc']

#   newdfname=olddfname.drop(['colname'],axis=1)

df1=df.drop(['loc'],axis=1)
print(df1)
#output : loc column is dropped or removed


#2. How to change(Rename) a column name :


#Syntax :

#newdataframefname=olddataframename.rename(columns={'oldcolname':'newcolname'})

# df1=df.rename(columns={'fname':'first_name'})
# print(df1)
#
# print("*"*100)