"""
10 minutes to pandas tutorial
https://pandas.pydata.org/pandas-docs/stable/10min.html#min
7/8/2017
"""
# Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as pyplot

"""
Object Creation
"""
# Series
print("Example Series")
s = pd.Series([1,3,5,np.nan,6,8])
print(s)
print("\n")

# Dataframe
print("Example Date Range")
dates = pd.date_range('20130101',periods=6)
print(dates)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print("Example DataFrame")
print(df)
print("DataFrame through passing dict")
df2= pd.DataFrame({ 'A' : 1.,
                    'B' : pd.Timestamp('20130102'),
                    'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D' : np.array([3] * 4, dtype='int32'),
                    'E' : pd.Categorical(["test","train","test","train"]),
                    'F' : 'foo'})
print(df2)
print(df2.dtypes)
print("\n")

# Viewing the DataFrame
print("\nVIEWING DATA\n")
print("df.head()")
print(df.head())
print("df.head(3)")
print(df.head(3))
print("df.index")
print(df.index)
print("df.columns")
print(df.columns)
print("df.values")
print(df.values)
print("df.describe()")
print(df.describe())
print("df.T")
print(df.T)
print("df.sort_index(axis=1,ascending=False)")
print(df.sort_index(axis=1,ascending=False))
print("df.sort_values(by='B')")
print(df.sort_values(by='B'))
print("\n")

# Selection
print("\nSELECTION\n")
print("Getting")
print("df['A'] (same as df.A, returns a series)")
print(df['A'])
print("df[0:3]")
print(df[0:3])
print(df['20130102':'20130104'])
print("df['20130102':'20130104']")
print("\nSelection by Label")
print("df.loc[dates[0]]")
print(df.loc[dates[0]])
print("df.loc[:,['A','B']]")
print(df.loc[:,['A','B']])
print("df.loc['20130102':'20130104',['A','B']]")
print(df.loc['20130102':'20130104',['A','B']])
print("df.loc['20130102',['A','B']]")
print(df.loc['20130102',['A','B']])
print("df.loc[dates[0],'A']")
print(df.loc[dates[0],'A'])
print("df.at[dates[0],'A'] --- fast, same as prior")
print(df.at[dates[0],'A'])
print("\n")

# Selection by Position
print("\nSelection by Position")
print()
