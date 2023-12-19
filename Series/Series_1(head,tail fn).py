#Important : While importing Pandas before that import numpy as well

#Series :

# In output, each element in list is printed followed by their index value.


import numpy as np
import pandas as pd
a=pd.Series([1,2,3,4,5,6,7,8,9])
print(a)


print()
#Output : each value  in list is printed followed by their index value.

#type function :

print(type(a)) #<class 'pandas.core.series.Series'>

#head()
#tail()

print()

#Functioning of head() : columns needed is collected

#head() - first 5 elements in Series is printed

print(a.head()) # 5 elements default printed

print(a.head(3)) # 3 is the desired no. of elements to get as output > first 3 elements printed

#Functioning of tail() : columns needed is collected

print(a.tail()) # Last 5 elements is  printed as default

print(a.tail(3)) #3 is the desired no of elements to get as output > last 3 elements is printed



