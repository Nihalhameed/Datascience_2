#Data set in an external file :

#data set collected will be stored as :
   #( text,csv,XML,JSON) file formats
   #JSON : Javascript Object Notation
   #XML : Extensible Markup Language


#To read an external file to make it to a dataframe :

# import numpy as np
# import pandas as pd
# df=pd.read_csv('/Users/macbook/Downloads/customer1.txt',sep=',')# sep is used in seperation using comma or space of each data ..depends on file
# print(df) #the external file is converted to a dataframe

#header_Tag :
 #Along with data if column name is mentioned , then that file contains a header tag
 #If column name is not present along with the data ,then that file has no header tag


#if there is no header tag >> mention header=None

# import numpy as np
# import pandas as pd
# df=pd.read_csv('/Users/macbook/Downloads/customer1.txt',sep=',',header=None)# sep is used in seperation of each data ..depends on file
# print(df) # When header=None is passed proper order of data is collected

#this file has no header tags i.e is no columns

import numpy as np
import pandas as pd
df=pd.read_csv('/Users/macbook/Downloads/customer1.txt',sep=',',header=None)# sep is used in seperation of each data ..depends on file
#To define column names :
df.columns=['id','fname','lname','age','prof','loc'] #adds the column name
print(df)

#seperation : sep need not be used for the above file..since its already having comma seperated values.
# (by default takes comma)

print("*"*100)

#1. To get the total number of missing values :
# isna().sum() function :

print(df.isna().sum())

# id       0
# fname    0
# lname    0
# age      0
# prof     0
# loc      1 (there is 1 missing value in loc)

print("*"*100)

#id=2 ,fname =3 , lname=1 , age=0, prof=2, loc=3

#2. Filling the missing values :
#fillna() function :

#Create a new datframe :

df1=df.fillna('india') #df1 is new dataframe >>  fills with india in every columns
print(df1)
print(df1.isna().sum())

# id       0
# fname    0
# lname    0
# age      0
# prof     0
# loc      0








