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
print("\nSelect via position of passed ints")
print("df.iloc[3]")
print(df.iloc[3])
print("\nSelect by interger slices")
print("df.iloc[3:5,0:2]")
print(df.iloc[3:5,0:2])
print("\nSelect by lists of integer position locations")
print("df.iloc[[1,2,4,],[0,2]]")
print(df.iloc[[1,2,4],[0,2]])
print("\nSlicing rows explicitly")
print("df.iloc[1:3,:]")
print(df.iloc[1:3,:])
print("\nSlicing columnns explicitly")
print("df.iloc[:,1:3]")
print(df.iloc[:,1:3])
print("\nFor getting a value explicitly")
print("df.iloc[1,1]")
print(df.iloc[1,1])
print("\nFor getting fast access to a scalar (equiv to prior)")
print("df.iat[1,1]")
print(df.iat[1,1])
print("\n")

# Boolean Indexing
print("\nBoolean Indexing")
print("Use single column's values to select data")
print("df[df.A > 0]")
print(df[df.A>0])
print("\nSelect values where boolean condition met")
print("df[df>0]")
print(df[df>0])
print("\nUse isin() to filter")
df2=df.copy()
df2['E']=['one','one','two','three','four','three']
print("df2")
print(df2)
print("df2[df2['E'].isin(['two,'four'])]")
print(df2[df2['E'].isin(['two','four'])])
print("\n")

#Setting
print("\nSetting")
print("\nSetting a new column aligns data by indexes")
print("s1=pd.Series([1,2,3,4,5,6],index=pd.date_range('20130102',periods=6))")
s1=pd.Series([1,2,3,4,5,6],index=pd.date_range('20130102',periods=6))
print("s1")
print(s1)
df['F']=s1
print("df['F']=s1")
print("df")
print(df)
print("\nSet values by label")
print("df.at[dates[0],'A']=0")
df.at[dates[0],'A']=0
print(df)
print("\nSet values by position")
print("df.iat[0,1]=0")
df.iat[0,1]=0
print(df)
print("\nSet by assigining with numpy array")
print("df.loc[:,'D'] = np.array([5] * len(df))")
df.loc[:,'D'] = np.array([5] * len(df))
print(df)
print("\nA where operation")
print("df3 = df.copy()")
df3 = df.copy()
print("df3[df3>0]=-df3")
df3[df3>0]=-df3
print("df3")
df3
print("\n")

#Missing Data
