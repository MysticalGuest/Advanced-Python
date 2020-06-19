# 8.分组聚合
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data_v1 = pd.read_excel("超市营业额.xlsx")

data_group1 = data_v1.groupby(by="姓名")
print("分组后得到的分组对象\n", data_group1)

print("分组中每一组的大小\n", data_group1.size()) # 使用size方法

print("查看每个分组中的前5个值\n", data_group1.head(4))  # 查看分组的前n个值

# 8-1 对分组进行聚合
print("查看每一组交易额之和\n,", data_group1["交易额"].sum())
print("查看每一组交易额均值\n,", data_group1["交易额"].mean().round(2))

data_group2 = data_v1.groupby(by="日期")
data_group2.size()
print("一周中每天的交易额分析：", data_group2["交易额"].sum())

# 8-2  使用agg方法进行聚合数据:多个函数作用于1个数据
print(data_group2['交易额'].agg([np.sum, np.mean, np.median]))

# 8-3 练习1，统计各柜台的交易额平均值，和值，标准差
data_group3 = data_v1.groupby(by="柜台")
print("各柜台的数据信息:\n", data_group3['交易额'].agg([np.sum, np.mean, np.std]).round(2))
data_v6 = data_group3['交易额'].agg([np.sum, np.mean, np.std]).round(2)
print("data_v6: ", data_v6)
print("data_v6.values: ", data_v6.values)
print("data_v6.index: ", data_v6.index)
print("data_v6.columns: ", data_v6.columns)

# 8-4 练习2，统计一周中每天各柜台的均值，和值，标准差
print("一周中每天各柜台的均值\n", data_v1.groupby(by=["日期", '柜台'])['交易额'].mean())

plt.rcParams['font.sans-serif'] = 'SimHei'
ax1 = plt.subplot(221)
ax2 = plt.subplot(222)
ax3 = plt.subplot(212)
ax1.plot(data_v6.index, data_v6['sum'])
ax2.plot(data_v6.index, data_v6['mean'])
ax3.plot(data_v6.index, data_v6['std'])
plt.show()

print("data_v6.sort_index(ascending=False): \n", data_v6.sort_index(ascending=False))

print("data_v6.sort_values(by=\"sum\", ascending=False, inplace=False): \n",
      data_v6.sort_values(by="sum", ascending=False, inplace=False))

print("data_v1.sort_values(by=['日期', '柜台']): \n", data_v1.sort_values(by=['日期', '柜台']))

