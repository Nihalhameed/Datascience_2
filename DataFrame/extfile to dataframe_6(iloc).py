#customer file
#collect only this columns : fname,lname,age,prof

import numpy as np
import pandas as pd

df=pd.read_csv('/Users/macbook/Downloads/customer1.txt',sep=',',header=None)
df.columns=['id','fname','lname','age','prof','loc'] #gives column name

# df1=df[['fname','lname','age','prof']]
# print(df1)




#2. fname,lname,age,loc of 50 employees

# df1=df[['fname','lname','age','loc']].head(50)
# print(df1)

#3. last 10 employees  fname,lname,age,prof

# df1=df[['fname','lname','age','loc']].tail(10)
# print(df1)

#Important :
#    To collect particlar rows(in-between)  : use iloc()

# df1=df.iloc[2]  #index number is passsed with iloc
# print(df1)

df1=df.iloc[2:9] #index= 2 to 8
print(df1)

print("*"*100)

df1=df.iloc[2:40:3]  #index 2 to 40 with step 3
print(df1)


