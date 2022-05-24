import pandas as pd 


df=pd.read_csv('country_classification.csv')
# print(df.to_string())


#   country_code                                        country_label
# 0                           AD                                              Andorra
# 1                           AE                                 United Arab Emirates
# 2                           AF                                          Afghanistan
# 3                           AG                                  Antigua and Barbuda
# 4                           AI                                             Anguilla
# 5                           AL                                              Albania
# 6                           AM                                              Armenia
# 7                           AO                                               Angola
# 8                           AQ                                           Antarctica

#to delete the  records with NULL  data is used 
# new_df=df.dropna()
# print(new_df.to_string())


#to replace the  NULL data we can use the Below code:put 100 insted of NULL

new_df=df.fillna(100)
print(new_df.to_string())










 























