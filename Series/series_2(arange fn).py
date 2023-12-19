# read 1 to 20 elements  with series

# import numpy as np
# import pandas as pd
#
# a=pd.Series([i for i in range (1,21)])
# print(a)

#or

import numpy as np
import pandas as pd

a=np.arange(1,21) #arange function is located in numpy library not in pandas
b=pd.Series(a)
print(a)