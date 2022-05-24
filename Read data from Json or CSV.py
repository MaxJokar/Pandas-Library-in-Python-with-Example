#How to use datas from other files , server (jason)..
import pandas as pd 
#to read CSV  we  use  read_csv function:
#Termina:7077  2013  ...  ANZSIC06 groups C111, C112, C113, C114, C115, ...
# 37078  2013  ...  ANZSIC06 groups C111, C112, C113, C114, C115, ...
# 37079  2013  ...  ANZSIC06 groups C111, C112, C113, C114, C115, ...
# [37080 rows x 10 columns]
#it shows the first fifth line and fifth last one :
# df=pd.read_csv('country_classification.csv')
# print(df)



#To see all we should  to_string:

# df=pd.read_csv('country_classification.csv')
# print(df.to_string())


# df=pd.read_csv('Report.csv')
# print(df[['Year']])

#Year    2020
# Name: 0, dtype: int64
# print(df[['Year']].iloc[0])



 




#    Year  ...                             Industry_code_ANZSIC06
# 0  2020  ...  ANZSIC06 divisions A-S (excluding classes K633...
# 1  2020  ...  ANZSIC06 divisions A-S (excluding classes K633...
# 2  2020  ...  ANZSIC06 divisions A-S (excluding classes K633...

# [3 rows x 10 columns]
#        Year  ...                             Industry_code_ANZSIC06
# 37077  2013  ...  ANZSIC06 groups C111, C112, C113, C114, C115, ...
# 37078  2013  ...  ANZSIC06 groups C111, C112, C113, C114, C115, ...
# 37079  2013  ...  ANZSIC06 groups C111, C112, C113, C114, C115, ...

#Head , Tail:
# df=pd.read_csv('country_classification.csv')
# print(df.head(3))
# print(df.tail(3))





#To know what our DataFrame has: .info
# RangeIndex: 258 entries, 0 to 257
# Data columns (total 2 columns):
#  #   Column         Non-Null Count  Dtype 
# ---  ------         --------------  ----- 
#  0   country_code   257 non-null    object
#  1   country_label  258 non-null    object
# dtypes: object(2)
# memory usage: 4.2+ KB
# None


# df=pd.read_csv('country_classification.csv')
#To understand what our DataFram has or included:
# print(df.info())









#RENAME:To rename the LABEL of  Comumn 
                #   country_code                                      country_label
# 0                           AD                                            Andorra
# 1                           AE                               United Arab Emirates
# 2                           AF                                        Afghanistan
# 3                           AG                                Antigua and Barbuda
# 4                           AI                                           Anguilla
# ..                         ...                                                ...
# 253              TOT (OMT CIF)  Total goods - cost including insurance and fre...
# 254              TOT (OMT FOB)                        Total goods - free on board
# 255              TOT (OMT VFD)                       Total goods - value for duty
# 256            TOT (BoP basis)            Total goods - Balance of Payments basis
# 257  BoP conceptual adjustment          Balance of Payments conceptual adjustment

# [258 rows x 2 columns]
# RENAMEPandaS RENAMEPandaS RENAMEPandaS RENAMEPandaS RENAMEPandaS RENAMEPandaS RENAMEPandaS RENAMEPandaS RENAMEPandaS RENAMEPandaS
#                    cOunTRycOdE                                        laBElCouTry
# 0                           AD                                            Andorra
# 1                           AE                               United Arab Emirates
# 2                           AF                                        Afghanistan
# 3                           AG                                Antigua and Barbuda
# 4                           AI                                           Anguilla
# ..                         ...                                                ...
# 253              TOT (OMT CIF)  Total goods - cost including insurance and fre...
# 254              TOT (OMT FOB)                        Total goods - free on board
# 255              TOT (OMT VFD)                       Total goods - value for duty
# 256            TOT (BoP basis)            Total goods - Balance of Payments basis


# df=pd.read_csv('country_classification.csv')
# print(df)
# print(10*'RENAMEPandaS ')
# df=pd.read_csv('country_classification.csv')
# new_df=df.rename(columns={'country_code':'cOunTRycOdE','country_label':'laBElCouTry'})
# print(new_df)




#Rename:
#OPTIONS: index: determines the  Labels(Row Numbers), Columns:determines the Columns and inplace!
#If you want to  reWrite of  df:inplace=True=>works on all DataFrame and is False as Default
#inplace means  execute on its output result:
#                   cOunTRycOdE                                        laBElCouTry
# 0                           AD                                            Andorra
# 1                           AE                               United Arab Emirates
# 2                           AF                                        Afghanistan
# 3                           AG                                Antigua and Barbuda
# 4                           AI                                           Anguilla
# ..                         ...                                                ...
# 253              TOT (OMT CIF)  Total goods - cost including insurance and fre...
# 254              TOT (OMT FOB)                        Total goods - free on board
# 255              TOT (OMT VFD)                       Total goods - value for duty
# 256            TOT (BoP basis)            Total goods - Balance of Payments basis
# 257  BoP conceptual adjustment          Balance of Payments conceptual adjustment

# df=pd.read_csv('country_classification.csv')
# df.rename(columns={'country_code':'cOunTRycOdE','country_label':'laBElCouTry'},inplace=True)
# print(df)




  
#DROP:to delete something from our DataFrame:
#                   country_code                                      country_label
# 1                           AE                               United Arab Emirates
# 3                           AG                                Antigua and Barbuda
# 4                           AI                                           Anguilla
# 5                           AL                                            Albania
# 6                           AM                                            Armenia
# ..                         ...                                                ...
# 253              TOT (OMT CIF)  Total goods - cost including insurance and fre...
# 254              TOT (OMT FOB)                        Total goods - free on board
# 255              TOT (OMT VFD)                       Total goods - value for duty
# 256            TOT (BoP basis)            Total goods - Balance of Payments basis
# 257  BoP conceptual adjustment          Balance of Payments conceptual adjustment


# df=pd.read_csv('country_classification.csv')
# df.drop([0,2],inplace=True) #NOw we dont have  the  0 and the 2  Row!
# print(df)
 
  
  
  
  
  
#Drop Columns:
#                                     country_label
# 0                                              Andorra
# 1                                 United Arab Emirates
# 2                                          Afghanistan
# 3                                  Antigua and Barbuda
# 4                                             Anguilla
# ..                                                 ...
# 253  Total goods - cost including insurance and fre...
# 254                        Total goods - free on board
# 255                       Total goods - value for duty
# 256            Total goods - Balance of Payments basis
# 257          Balance of Payments conceptual adjustment
  
  
  
# df=pd.read_csv('country_classification.csv')
# df.drop(columns=['country_code'],inplace=True) #NOw we dont have  the  0 and the 2  Row!
# print(df)
 
  
  
  

#sum min max
#                            country_label
# 0                                              Andorra
# 1                                 United Arab Emirates
# 2                                          Afghanistan
# 3                                  Antigua and Barbuda
# 4                                             Anguilla
# ..                                                 ...
# 253  Total goods - cost including insurance and fre...
# 254                        Total goods - free on board
# 255                       Total goods - value for duty
# 256            Total goods - Balance of Payments basis
# 257          Balance of Payments conceptual adjustment
  
  
# df=pd.read_csv('country_classification.csv')
# print(df[['country_label']])
  
  
  
  
#sum of  Column 'country_label' is inTermina :
# country_label    AndorraUnited Arab EmiratesAfghanistanAntigua ...
# dtype: object
  
# df=pd.read_csv('country_classification.csv')
# print(df[['country_label']].sum())            #SUM of   a  Column
# print(df[['country_label']].min())           #Brings the minimum number in the list
# print(df[['country_label']].max()) 





#Groupby: 
#    Code  Name  Age
# 0     1  Jack   90
# 1     2  Andy   45
# 2     1  Jack   90
# 3     1   Max   80
# 4     2  Jack   90
# 5     1   Max   70
# data=[
#     [1,'Jack',90],
#     [2,'Andy',45],
#     [1,'Jack',90],
#     [1,'Max',80],
#     [2,'Jack',90],
#     [1,'Max',70]
# ]

# df=pd.DataFrame(data,columns=['Code','Name','Age'])
# print(df)






#   Code  Name  Age
# 0     1  Jack   90
# 1     2  Andy   45
# 2     1  Jack   90
# 3     1   Max   80
# 4     2  Jack   90
# 5     1   Max   70
# sum of  agesum of  agesum of  agesum of  agesum of  agesum of  agesum of  agesum of  agesum of  agesum of  age
# Age    465
# dtype: int64
  
# data=[
#     [1,'Jack',90],
#     [2,'Andy',45],
#     [1,'Jack',90],
#     [1,'Max',80],
#     [2,'Jack',90],
#     [1,'Max',70]
# ]

# df=pd.DataFrame(data,columns=['Code','Name','Age'])
# print(df)
# print(10*'sum of  age')
# print(df[['Age']].sum())

  
  
  
  
  
  
  
  
  
  
  
  
#Group by : we want to add sum of  the same codes together using groupBy
#    Code  Name  Age
# 0     1  Jack    2
# 1     2  Andy    4
# 2     1  Jack    9
# 3     2   Max    8
# 4     2  Jack    3
# 5     1   Max    6
# sum of  age--sum of  age--sum of  age--sum of  age--sum of  age--
# Age    32
# dtype: int64

#       Age
# Code
# 1      17
# 2      15 
  
  
  
# data=[
#     [1,'Jack',2],
#     [2,'Andy',4],
#     [1,'Jack',9],
#     [2,'Max',8],
#     [2,'Jack',3],
#     [1,'Max',6]
# ]

# df=pd.DataFrame(data,columns=['Code','Name','Age'])
# print(df)
# print(5*'sum of  age--')
# print(df[['Age']].sum())
# print()
# print(df.groupby(['Code']).sum('Age')) #make group the same code then add the age for each
# print()
# print()

#      Code  Age
# Name
# Andy     2    4
# Jack     4   14
# Max      3   14
# print(df.groupby(['Name']).sum('Age'))
  
  
  
  
  
  
  
  

#AXES: shows the Columns  Names
#[RangeIndex(start=0, stop=258, step=1), Index(['country_code', 'country_label'], dtype='object')]
# df=pd.read_csv('country_classification.csv')
# print(df.axes)

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  













