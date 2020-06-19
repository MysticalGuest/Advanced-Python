# 6.描述性统计
# 6-1使用numpy函数
import numpy as np
import pandas as pd

df_v5 = pd.read_excel("超市营业额2.xlsx", sheet_name=1)

des_v1 = df_v5.loc[:, '交易额']
print("用numpy函数统计和值如下:\n", np.sum(des_v1))
print("用numpy函数统计\n最大值:{}\n方差:{:.2f}\n标准差:{:.2f}\n均值:{:.2f}\n\n"
      .format(np.max(des_v1), np.var(des_v1), np.std(des_v1), np.mean(des_v1)))

# 6-2使用pandas的方法
des_v2 = df_v5.loc[:,'交易额']
print("用pandas的方法进行统计:\n最大值:{}\n方差:{:.2f}\n标准差:{:.2f}\n均值:{:.2f}\n\n"
      .format(des_v2.max(), des_v2.var(), des_v2.std(), des_v2.mean()))

# 6-3使用pandas的描述性统计函数
print("des_v2.describe(): ", des_v2.describe())    # 使用函数

# 对非数值数据进行出现的次数统计
df_v5["柜台"].value_counts()

# 统计一共有多个种类,出现次数最多的种类,最多的次数是多少?
# 将数据类型转换位category类型,然后进行统计
df_v5["柜台"] = df_v5['柜台'].astype("category")
print("df_v5[\"柜台\"].describe(): ", df_v5["柜台"].describe())

print("df_v5.dtypes: ", df_v5.dtypes)

print("df_v5[\"柜台\"].value_counts(): \n", df_v5["柜台"].value_counts())

