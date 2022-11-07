import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(0,20).reshape(5,4),index=['rows1','rows2','rows3','rows4','rows5'],columns=['columns1','columns2','columns3','columns4'])
# print(df.info())

# print(df.describe())
# print(df[['columns1','columns2','columns1']])
# print(df['columns1'])
# print(df.loc[['rows1','rows2']])
# print(df.head())
# print(df.iloc[2:4,0:2])
# print(df.iloc[2:4,0:3])
# print(df.iloc[2:,1:])
# print(df.iloc[:,1:])
# print(df.iloc[:,1:].values)
# print(df.isnull().sum())

# df = pd.DataFrame([[1,np.nan,3],[1,2,3]],index=['rows1','rows2'],columns=['columns1','columns2','columns3'])
# print(df)
# print(df.isnull().sum())
# print(df.isnull())
# print(df['columns3'].value_counts())
# print(df['columns2'].unique())
print(df[df['columns2']>2])