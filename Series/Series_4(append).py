#join
#_.append ()

import numpy as np
import pandas as pd
s1=pd.Series([4,5,6,7,1])
s2=pd.Series([5,7,6,5,4])

s3=s1._append(s2)
print(s3)

# 0    4
# 1    5
# 2    6
# 3    7
# 4    1
# 0    5
# 1    7
# 2    6
# 3    5
# 4    4
#Here index of elements in s2 starts again from 0 ..i.e index is not in correct order, fro that use  the below method :

s3=s1._append(s2,ignore_index=True)
print(s3)

# 0    4
# 1    5
# 2    6
# 3    7
# 4    1
# 5    5
# 6    7
# 7    6
# 8    5
# 9    4


