# DataFrame:several dimentions !TWO  dimension 
#they have  column number/name and  index(row number)

import pandas as pd 

#Terminal:
#     0==>number of  column:
# 0  23
# 1  45
# 2  56
# 3  45
# 4  78
# 5  89
# data=[23,45,56,45,78,89]
# df=pd.DataFrame(data)
# print(df)





#          0
# jack    23
# john    45
# max     56
# rose    45
# philip  78
# dany    89
# data=[23,45,56,45,78,89]
# df=pd.DataFrame(data,index=['jack','john','max','rose','philip','dany'])
# print(df)






#       Age
# jack     23
# john     45
# max      56
# rose     45
# philip   78
# dany     89


# data=[23,45,56,45,78,89]
# df=pd.DataFrame(data,index=['jack','john','max','rose','philip','dany'],columns=['Age'])
# print(df)




#   color  Grade
# 0    Red    100
# 1  Green    130
# 2   Blue    250

# data={
#     'color':["Red","Green","Blue"],
#     'Grade':[100,130,250]
    
# }
# df=pd.DataFrame(data)
# print(df)






#dont use column when we have keys  they work as  columns 
#index:A,B,C
#    color  Grade  Price
# A    Red    100   1000
# B  Green    130   2000
# C   Blue    250   3000

# data={
#     'color':["Red","Green","Blue"],
#     'Grade':[100,130,250],
#     'Price':[1000,2000,3000]
    
# }
# df=pd.DataFrame(data,index=["A","B","C"])
# print(df)







#   color  Grade  Price
# 0    Red    100   1000
# 1  Green    130   2000
# 2   Blue    250   3000
#print(df.loc[0]):
# color     Red
# Grade     100
# Price    1000
# Name: 0, dtype: object=>key value is object here


# data={
#     'color':["Red","Green","Blue"],
#     'Grade':[100,130,250],
#     'Price':[1000,2000,3000]
    
# }
# df=pd.DataFrame(data)
# print(df)
# print(df.loc[0])
# print()
# print(df.loc[0]['Grade']) #100



 




# color     Red
# Grade     100
# Price    1000
# Name: 0, dtype: object


# data={
#     'color':["Red","Green","Blue"],
#     'Grade':[100,130,250],
#     'Price':[1000,2000,3000]
    
# }
# df=pd.DataFrame(data)

# print(df.loc[0])






#Conclusion:
#From loc for ROW NUMBER ,for columns name of  Columns needed

# data={
#     'color':["Red","Green","Blue"],
#     'Grade':[100,130,250],
#     'Price':[1000,2000,3000]
    
# }
# df=pd.DataFrame(data)

# color     Red
# Grade     100
# Price    1000
# Name: 0, dtype: object

# print(df.loc[0])
# print()

# 0      Red
# 1    Green
# 2     Blue
# Name: color, dtype: object

# print(df['color'])






# color     Red
# Grade     100
# Price    1000
# Name: 0, dtype: object
 
# data={
#     'color':["Red","Green","Blue"],
#     'Grade':[100,130,250],
#     'Price':[1000,2000,3000]
    
# }
# df=pd.DataFrame(data)


#   color
# 0    Red
# 1  Green
# 2   Blue
# print(df[['color']])




#   color  Price
# 0    Red   1000
# 1  Green   2000
# 2   Blue   3000

# print(df[['color','Price']])









#from loc we use for ROWs, for column Name of them:


# color    Green
# Price     2000
# Name: 1, dtype: object

# data={
#     'color':["Red","Green","Blue"],
#     'Grade':[100,130,250],
#     'Price':[1000,2000,3000]
    
# }
# df=pd.DataFrame(data)
# print(df[['color','Price']].loc[1])




#index Location:
#iloc  brings the ROW number
# color     Red
# Grade     100
# Price    1000

# data={
#     'color':["Red","Green","Blue"],
#     'Grade':[100,130,250],
#     'Price':[1000,2000,3000]
    
# }
# df=pd.DataFrame(data)
# print(df.iloc[0])















