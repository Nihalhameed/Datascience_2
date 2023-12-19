#convert file to dataframe
#columns name
#total number of missing value
#fill

#convert file to dataframe:

import numpy as np
import pandas as pd

df=pd.read_csv('/Users/macbook/Downloads/missing_data1.csv',sep=',') #the file has header tags = column name (so no need to define col name)
print(df.columns) #columns names are shown as output

print("*"*100)

print(df.isna().sum())

# Duration    0
# Date        1
# Pulse       0
# Maxpulse    0
# Calories    2

print("*"*100)

df1=df.fillna(100) #full integer values is present in columns so 100 is given
print(df1)
print(df1.isna().sum())

# Duration    0
# Date        0
# Pulse       0
# Maxpulse    0
# Calories    0

