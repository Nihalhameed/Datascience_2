#customer file :
import numpy as np
import pandas as pd
df=pd.read_csv('/Users/macbook/Downloads/customer1.txt',header=None)
df.columns=['id','fname','lname','age','prof','loc']
#print(df.isna().sum())
# id       0
# fname    0
# lname    0
# age      0
# prof     0
# loc      1

#filling the missing values :

df1=df.fillna(100)
print(df1.isna().sum())

print("*"*100)

#1. Find Row count :

print(df1.count())

print("*"*100)

#2.Remove duplicates rows and find total row count :

df2=df1.drop_duplicates()
print(df2.count())
print("*"*100)

#3. Age maximum 10 fname,lname,prof,loc

df3=df1.sort_values(by='age',ascending=False) \
    [['fname','lname','prof','loc']].head(10)
print(df3)
print("*"*100)

#4.  Age minimum 5 employees fname,lname,prof,loc

df4=df1.sort_values(by='age') \
    [['fname','lname','prof','loc']].head(5)
print(df4)
print("*"*100)

#5. Each location count [count desc order]

df5=df1.groupby('loc') ['loc'].count() \
       .sort_values(ascending=False)
print(df5)
print("*"*100)

#6. Full data of highest people in which location , read the full data of people in that location :
#Here it is autralia ,full data collect :


df6=df1.loc[df['loc']=='australia']
print(df6)
print("*"*100)

#7.Each age group count [age desc order]

df7=df1.groupby('age') ['age'].count() \
       .sort_values(ascending=False)
print(df7)
print("*"*100)

#8.Each profession count [count desc order]

df8=df1.groupby('prof') ['prof'].count() \
       .sort_values(ascending=False)
print(df8)
print("*"*100)

#9. India work :
df9=df1.loc[df['loc']=='india']
print(df9)
#9A. Row count :

print(df9a.count())
print("*"*100)

#9B. Each profession count [count desc order]

df9b=df9.groupby('prof') ['prof'].count() \
        .sort_values(ascending=False)
print(df9b)
print("*"*100)

#9C.Age mxm 3 employees fname,lname,age,prof

df9c=df9.sort_values(by='age',ascending=False) \
         [['fname','lname','age','prof']].head(3)
print(df9c)
print("*"*100)

#9D. Age minimum 3 employees fname,lname,age,prof

df9d=df9.sort_values(by='age') [['fname','lname','age','prof']].head(3)
print(df12)
print("*"*100)

#9E. age above 40 full data

df13=df9.loc[df['age']>40].sort_values(by='age') #sorted age for easily checking the value of age
print(df13)
print("*"*100)

#9F. age range 30 to 40 [profession count]

df14=df9.loc[(df['age']>=30)&(df['age']<=40)] \
        .groupby('prof') ['prof'].count()
print(df14)
print("*"*100)

#10. US work :
df15=df1.loc[df['loc']=='us']
print(df15)

#10A. Row count

print(df15.count())
print("*"*100)

#10B.  Each age group count

df16=df15.groupby('age') ['age'].count()
print(df16)
print("*"*100)

#10C. Each profession count [count desc]

df17=df15.groupby('prof') ['prof'].count() \
         .sort_values(ascending=False)
print(df17)
print("*"*100)

#10D. Civil engineer dept and age above 30

df18=df15.loc[(df['prof']=='Civil engineer')&(df['age']>30)]
print(df18)