import numpy as np
import pandas as pd

# 接lesson10
# 5.重叠合并--combine_first()
dict1 = {"id": list(np.arange(1, 6, 1)),
         'system': ['win10', 'win7', np.nan, 'win8', np.nan],
         'cup': ['i7', np.nan, 'i5', np.nan, np.nan]}

dict2 = {"id": list(np.arange(1, 6, 1)),
         'system': ['win10', np.nan, 'win7', 'win8', "win10"],
         'cup': [np.nan, "i3", 'i5', "i7", "i7"]}

df9 = pd.DataFrame(dict1)
df10 = pd.DataFrame(dict2)
df11 = df9.combine_first(df10)
print("重叠合并之后的结果:\n", df11)

# 重叠合并2--合并是按照行索引进行的互补
dict3 = {"0": [np.nan, np.nan, np.nan], "1": [3.0, 4.5, 7.8], "2": [5.0, np.nan, np.nan]}
dict4 = {"0": [43, 56], "1": [np.nan, 7.8], "2": [6, 5.5]}
df12 = pd.DataFrame(dict3)
df13 = pd.DataFrame(dict4, index=[0, 2])

df12.combine_first(df13)
print("df12：\n", df12)

# 数据拆分
df1 = pd.read_excel('超市营业额.xlsx')
df1.loc[:, ['工号', '姓名', '交易额']].groupby("姓名")['交易额'].agg(np.mean).round(2)
print("df1：\n", df1)

