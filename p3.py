import pandas as pd



#Mean:average;  Median:Bigger middle element;  Mode:the most repetitive element  

# data={
#     'name':['Jack','John','Max','Philip'],
#     'age':[50,60,42,6]
# }

# df=pd.DataFrame(data)
# print(df)

#     name  age
# 0    Jack   50
# 1    John   60
# 2     Max   42
# 3  Philip    6



data={
    'name':['Jack','John','Max','Philip','Dany'],
    'age':[10,20,30,40,50]
}

df=pd.DataFrame(data)
print(df)
print(10*'mean')
print(df[['age']].mean())
print(10*'median')
print(df[['age']].median())
print(10*'mode')
print(df[['age']].mode())






