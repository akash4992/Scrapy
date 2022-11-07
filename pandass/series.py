import pandas as pd
import numpy as np
# s = pd.Series([1,2,3,4,5,np.nan,6,7,8])
# print(s)
d = pd.date_range('20200301',periods=10)
# print(d)
# df = pd.DataFrame(np.random.randn(10,4),index=d,columns=['A','B','C','D'])
# print(df)
# df = pd.DataFrame({
#     'A':[1,2,3,4],
#     'B':pd.Timestamp('20200301'),
#     'C':pd.Series(1,index=list(range(4)),dtype='float32'),
#     'D':np.array([5]*4,dtype='int32'),
#     'E':pd.Categorical(['True','False','True','False']),
#     'F':'Edureka'})
# print(df.head())
# print(df.tail())
# print(df.index)
# print(df.columns)
# print(df.to_numpy())
# print(df.describe())
# print(df.sort_index(axis=1,ascending=False))
# print(df.sort_values('C'))
# print(df[0:3])
# data = df.loc[:,['B','C']]
# # print(data)
# data = df[df['A']>0]
# print(df.isnull)
# data = df.isnull().count()
# data = df.dropna()
# data = df.fillna(value=2)

# print(data)
# df2 = df.reindex(index=d[0:4],columns=list(df.columns)+['G'])
# data = df2.loc[d[0]:d[1],'F']=1
# print(data)
# data = df.mean(1)
# print(data)
# s = pd.Series([1,2,3,np.nan,4,5,6,7,8,9],index=d).shift(2)
# data = df.sub(s,axis='index')
# print(data)
# data = df.apply(np.cumsum)
# print(data)
# data = df.apply(lambda x: x.max() - x.min())
# print(data)
# print(s.value_counts)
s  = pd.Series(['Python','Jupiter','np.nan','Edureka','Football','World'])
# print(s.str.lower())
# print(s.str.upper())

df = pd.DataFrame(np.random.randn(10,4))
# print(df)
df2 = [df[:3],df[3:7],df[7:]]
# print(df2)
data = pd.concat(df2)
# print(data)
left = pd.DataFrame({'A':[1,2],'B':[3,4]})
right = pd.DataFrame({'A':[1,2],'D':[5,6]})
data = pd.merge(left,right,on='A')
# print(data)
# data= df.groupby(2).sum()
data= df.groupby([2,3]).sum()
# print(data)

my_touple = list(zip(*[[1,2,3,4,5,17,18,19],[11,12,13,6,7,8,9,10]]))
index = pd.MultiIndex.from_tuples(my_touple,names=['First','Second'])
print(index)

df = pd.DataFrame(np.random.randn(8,2),index=index,columns=['A','B'])
print(df) 