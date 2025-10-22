import pandas as pd

df = pd.read_csv('data/amazon.csv')

'''
#####   General information about the data set   ######

print(df.shape)   # Number of rows and columns (R, C)
print(df.columns) # Columns names
print(df.info())  # data types
print(df.head(5)) # First five rows 


#####   Look for missing values/duplicates   ######

print(df.isnull().sum())        # missing values per column
print(df.duplicated().sum())    # Number of duplicated rows

'''

print(df.describe(include='all'))

print(df['category'].value_counts().head(10))       # Top categories
print(df['rating'].value_counts().sort_index())     # Rating distribution
print(df[['discounted_price', 'actual_price']].head(10))  # Check price format