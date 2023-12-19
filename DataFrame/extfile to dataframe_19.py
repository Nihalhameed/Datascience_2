import numpy as np
import pandas as pd

df=pd.read_csv('/Users/macbook/Downloads/customer5.txt',header=None)
df.columns=['id','fname','lname','age','prof','loc','sal']
print(df)
print("*"*100)

#Another method to find count() :
#1.Each profession count :

df1=df['prof'].value_counts()
print(df1)

