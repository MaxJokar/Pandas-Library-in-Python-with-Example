#series are  one dimention !!!

import pandas as pd 

# print(pd.__version__)

# data=[12,23,21,23,4,5,78,98,78]
#our list data  exchanged to a series , index near data
#till 64bit can expand :Terminal
#0    12
# 1    23
# 2    21
# 3    23
# 4     4
# 5     5
# 6    78
# 7    98
# 8    78
# dtype: int64

# ser=pd.Series(data)
# print(ser[5])





#a    12     
# b    23     
# c    21     
# d    23     
# e     4     
# f     5     
# dtype: int64

#when a data is  exchanging to a series we can use index
# data=[12,23,21,23,4,5]
# ser=pd.Series(data,index=['a','b','c','d','e','f'])
# print(ser['d'])  #Terminal:23




#Dictionaries have index and no need for indexing!!!
# Dictionaries from key value for  their index is used
#exchange to a series and print the series
# Red      100
# Blue     200
# Green    300

data={
    "Red":100,
    "Blue":200,
    "Green":300,
    
}

ser=pd.Series(data)
print(ser)
print(ser["Green"])  #300
print(ser[2]) #300







































































































