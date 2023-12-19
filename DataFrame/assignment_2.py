#oid,date,custo,id,quantity,product_category,,product,state,country,typeofpayment

import numpy as np
import pandas as pd

df=pd.read_csv('/Users/macbook/Downloads/txn.txt',header=None)
df.columns=['oid','date','customid','quantity','category','product','state','country','paymethod']
print(df)

print("*"*100)

print(df.isna().sum()) #output : no missing values

# oid            0
# date           0
# customid       0
# quantity       0
# category       0
# product        0
# state          0
# country        0
# paymentmode    0

#1.Find row count :

print(df.count())
print("*"*100)

#2. jan month oid,cusno,category,product,state

df1=df.loc[(df['date']>='01-01-2011')&(df['date']<='01-31-2011')] \
        [['oid','customid','category','product','state']]
print(df1)
print("*"*100)

#2A. Row count:

print(df1.count())
print("*"*100)


#3. July Month oid,cusno,category,product,state

df2=df.loc[(df['date']>='07-01-2011')&(df['date']<='07-31-2011')] \
       [['oid','customid','category','product','state']]
print(df2)
print("*"*100)

#3A. Row count  :

print(df2.count())
print("*"*100)

#4. Each category [count desc sort] :
df3=df.groupby('category') ['category'].count() \
      .sort_values(ascending=False)
print(df3)

print("*"*100)

#5.category full details :

df4=df.loc[df['category']=='Outdoor Recreation']
print(df4)
print("*"*100)

#6. Each paymethod count :

df5=df.groupby('paymethod') ['paymethod'].count()
print(df5)
print("*"*100)

#7.  jan-july month purchase total count [include]
df6=df.loc[(df['date']>='01-01-2011')&(df['date']<='07-31-2011')] \
      .groupby('date') ['quantity'].count().sum()
print(df6)
print("*"*100)

#8. Each category total amount(quantity)

df7=df.groupby('category') ['quantity'].sum()
print(df7)
print("*"*100)

#9.Each category maximum amount (quantity)

df8=df.groupby('category') ['quantity'].max()
print(df8)
print("*"*100)

#10.Each category avg amount

df9=df.groupby('category') ['quantity'].mean()
print(df9)
print("*"*100)

#11. total amount(quantity) by cash and credit card

df10=df.groupby('paymethod') ['quantity'].sum()
print(df10)
print("*"*100)

#12.Indoor games ,total amount(quantity)
df11=df.loc[df['category']=='Indoor Games'] \
       .groupby('category') ['quantity'].sum()
print(df11)
print("*"*100)

#13. Each state count :

df12=df.groupby('state') ['state'].count()
print(df12)







