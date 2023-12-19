import numpy as np
import pandas as pd

df=pd.read_csv('/Users/macbook/Downloads/customer1.txt',header=None)
df.columns=['id','fname','lname','age','prof','loc']
print(df)

print("*"*100)

#1. India work..fname,lname,age,prof

df1=df.loc[df['loc']=='india'] [['fname','lname','age','prof']]
print(df1)

print("*"*100)

#2. Uk working and age above 50..fname,lname,age,prof
df2=df.loc[(df['loc']=='uk')&(df['age']>50)] [['fname','lname','age','prof']]
print(df2)
print("*"*100)

#3.Age maximum ulla 5 employees..fname,lname,age,prof

df3=df.sort_values(by='age',ascending=False) [['fname','lname','age','prof']].head() #head by default takes 5 values
print(df3)
print("*"*100)

#4.Age minimum ulla 3 employe..fname,lname,age,loc
df4=df.sort_values(by='age') [['fname','lname','age','loc']].head(3)
print(df4)
print("*"*100)
#5.Teacher prof..fname,lname,age

df5=df.loc[df['prof']=='Teacher'] [['fname','lname','age']]
print(df5)
print("*"*100)

#6. india working and prof Dancer..fname,lname,age

df6=df.loc[(df['loc']=='india')&(df['prof']=='Dancer')] [['fname','lname','age']]
print(df6)
print("*"*100)

#7.india working,age maximum ulla 3 employees..fname,lname,age,prof

df7=df.loc[df['loc']=='india'].sort_values(by='age',ascending=False) [['fname','lname','age','prof']].head(3)
print(df7)
print("*"*100)

#8.india work and prof Dancer,age minimum 1 employee..fname,lname,age

df8=df.loc[(df['loc']=='india')&(df['prof']=='Dancer')] \
      .sort_values(by='age') \
       [['fname','lname','age']].head(1)
print(df8)
print("*"*100)

#9.US work,age minimum ulla 5 employee..ful data

df9=df.loc[df['loc']=='us'].sort_values(by='age').head()
print(df9)
print("*"*100)

#10. Pilot prof,age minimum ulla 1 employee..fname,lname,age,loc

df10=df.loc[df['prof']=='Pilot'].sort_values(by='age') [['fname','lname','age','loc']].head(1)
print(df10)
print("*"*100)

#11.age range 25 to 40..fname,lname,age,prof

df11=df.loc[(df['age']>=25)&(df['age']<=40)].sort_values(by='age') [['fname','lname','age','prof']]
print(df11)