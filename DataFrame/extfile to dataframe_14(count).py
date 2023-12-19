#count() :

#  newdfname=olddfname.groupby('colname') ['colname'].count()

import numpy as np
import pandas as pd
df=pd.read_csv('/Users/macbook/Downloads/customer1.txt',sep=',',header=None)# sep is used in seperation of each data ..depends on file
df.columns=['id','fname','lname','age','prof','loc'] #adds the column name


#1. Each profession count and sort based on count in descending order :

df1=df.groupby('prof') ['prof'].count() \
      .sort_values(ascending=False)
print(df1)
print("*"*100)

#2.India working,each prof count  [count descending order]:

df2=df.loc[df['loc']=='india'] \
      .groupby('prof') ['prof'].count() \
      .sort_values(ascending=False)
print(df2)

#First assignment :
# 5. full data : we can find in which location etavum highest aalukal work cheyunnath a..avide work cheyunaavrde full data
# collect cheyuka