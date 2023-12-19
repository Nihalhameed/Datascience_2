#custome file contains >> id,name,age,loc,salary

#orde file contains >> orderid,purchase_date,id,amount

import numpy as np
import pandas as pd
df1=pd.read_csv('/Users/macbook/Downloads/custom.txt',header=None)
df2=pd.read_csv('/Users/macbook/Downloads/order.txt',header=None)

df1.columns=['id','name','age','loc','salary']
df2.columns=['orderid','date','id','amount']
print(df1)
print(df2)

print("*"*100)
#1. Salary maximum ulla 1 employee>> name,age,loc,date,amount
#2. Latest date ulla employee>> collect name,age,date,amount

#1.
df3=pd.merge(df1,df2,on='id',how='inner') \
      .sort_values(by='salary',ascending=False) [['name','age','date','amount']].head(1)
print(df3)

print("*"*100)

#2.

df4=pd.merge(df1,df2,on='id',how='inner') \
      .sort_values(by='date',ascending=False) [['name','age','date','amount']].head(1)
print(df4)

#order id,date,customerid,product quantity,product_category,state,country,typeofpayment