import pandas as pd
import matplotlib.pyplot as plt


#Here we can see  a graph of  our  datas:
df=pd.read_json('jsonfileSample.json')
print(df)
df.plot(x='firstName',y='age')
plt.show()







































