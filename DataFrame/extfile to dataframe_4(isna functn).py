#To read an external file to make it to a dataframe :

import numpy as np
import pandas as pd
df=pd.read_csv('/Users/macbook/Downloads/movies_cleaned_pandas.csv',sep=',',header=None)
df.columns=['id','name','year','rating','duration'] #correct format of column names as of file should be given to get output
print(df)

print("*"*100)

#isna().sum() : To calculate the total missing values in a dataframe :

#Whenever we get a dataframe we need to calculate the total missing values :

print(df.isna().sum())

# id          0 (count of missing value)
# name        0
# year        0
# rating      0
# duration    0

