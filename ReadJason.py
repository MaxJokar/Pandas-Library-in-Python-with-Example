# Pandas is a  library for  precess  of  datas  or analyse the data
import pandas as pd 


#read and  convert to  dataFrame:
# ople
# 0   {'firstName': 'Joe', 'lastName': 'Jackson', 'gender': 'male', 'age': 28, 'number': '7349282382'}
# 1   {'firstName': 'James', 'lastName': 'Smith', 'gender': 'male', 'age': 32, 'number': '5678568567'}
# 2  {'firstName': 'Emily', 'lastName': 'Jones', 'gender': 'female', 'age': 24, 'number': '456754675'}


df=pd.read_json('jsonfileSample.json')
print(df.to_string())































