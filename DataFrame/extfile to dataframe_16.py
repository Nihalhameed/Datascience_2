#convert the file to dataframe and create patent and subpatent columns as column name is not mentioned in file


import numpy as np
import pandas as pd
df=pd.read_csv('/Users/macbook/Downloads/patent',header=None,sep=' ')

df.columns=['patent','subpatent']
print(df)

print("*"*100)

#Count of subpatent corresponding to each patent is to be calculated [count descending order]

df1=df.groupby('patent') ['patent'].count() \
      .sort_values(ascending=False)
print(df1)