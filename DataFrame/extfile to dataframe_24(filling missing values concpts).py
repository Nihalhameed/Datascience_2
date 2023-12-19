import numpy as np
import pandas as pd
df=pd.read_csv('/Users/macbook/Downloads/missing_data1.csv')
print(df)

print("*"*100)

# print(df.isna().sum())
# Duration    0
# Date        1
# Pulse       0
# Maxpulse    0
# Calories    2

#Missing values in df :

#18 index  >> Calories
#22 index >>Date
#28 >> Calories

#fillna() :

#1. filling missing values by creating new dataframe :

# df1=df.fillna(150)
# print(df1)

#2. filling missing values without creating new dataframe (imp):

# df.fillna(150,inplace=True)
# print(df.isna().sum())

# Duration    0
# Date        0
# Pulse       0
# Maxpulse    0
# Calories    0

#3. filling missing values in a selected column (by creating new df):
#eg :
#Calories >> fill missing value

# df1=df['Calories'].fillna(150)
# print(df1) # output prints only thee column of 'Calories'

#So,
#filling missing values in a selected column (correct way(imp)) :

#Note : (inplace=True) is used when a dataframe is edited without creating a new dataframe.

# df['Calories'].fillna(130,inplace=True)
# print(df) #output fills with 130 to only in Calories column having a missing value before
# print("*"*100)
#eg 2:

#Date >> fill the missing values :

# df['Date'].fillna('2023/12/21',inplace=True)
# print(df)
# print("*"*100)

#Important Note : In pandas we cannot fill the missing values in our own manner :

#We can only fill missing values  by :

#mean()- filling with average value
#median() -filling with middle value
#mode()- filling with most repeated value
# Note:
#( Use object to find missing values for objects and use annyone mean,mode,median for int values


#Example : Calories >> fill with mean()

# a=df['Calories'].mean() #calculate the average value and stores it to 'a'
# print(a)
#
# df['Calories'].fillna(a,inplace=True)
# print(df)

#2. calories >> median() :

# a=df['Calories'].median() #calculate the middle value and stores it to 'a'
# print(a)
#
# df['Calories'].fillna(a,inplace=True)
# print(df)

#3. calories >> mode() :

# a=df['Calories'].mode()[0] #calculate the repeated value and stores it to 'a' ,index 0 is also passed
# print(a)
#
# df['Calories'].fillna(a,inplace=True)
# print(df)
print("*"*100)

#Important note : Mostly missing values are filled using mode()

#dropna() fucntion : Wherever there is missing values that rows are dropped completely.
#..........

# df.dropna(inplace=True,ignore_index=True) #ignore_index removes unwanted rows and re-orders the elements in index number
# print(df) #index 0 to 28, before it was 0 to 31
#
# print(df.isna().sum())

#date :1
#calories :2

#For deleting  a particular column having missing value:

#For date column :

# df.dropna(subset=['Date'],inplace=True,ignore_index=True)
# print(df)

#For calories column :

# df.dropna(subset=['Calories'],inplace=True)
# print(df)

#How to handle wrong format data:

#example :

#Height(cm) Weight(kg)

#110     40
#160     65
#180     70
#140     55
#120     50
#380     78
#170     400


#1. From the data 7th index data has a wrong value in 'duration' which is 450 :

#df.loc[7,'Duration']=45
#print(df)

#2. Duration in 7th index >> replace it with mode()

# a=df['Duration'].mode()[0]
# df.loc[7,'Duration']=a
# print(df) #450 to 60

#3. Calories above 400 varunna  (full data collect)is in wrong format enn assume cheyuka and then for that above 400 data
#Calories ===> fill it with mean()

a=df['Calories'].mean()
for i in df.index:
    if df.loc[i,'Calories']>400:
        if df.loc[i,'Calories']=a
print(a)
