import pandas as pd
import matplotlib.pyplot as plt


data_v1 = pd.read_excel("超市营业额.xlsx")
print("data_v1: \n", data_v1)
# 数据透视表
data_piv1 = data_v1.pivot_table(values="交易额", index="日期", columns="柜台", aggfunc="mean").round(2)
# 绘制散点图
print("data_piv1: \n", data_piv1)
print("data_piv1.index: \n", data_piv1.index)
print("data_piv1.values: \n", data_piv1.values)
print("data_piv1.columns: \n", data_piv1.columns)

data_piv1.sort_index()

plt.rcParams['font.sans-serif'] = 'SimHei'
fig = plt.figure(figsize=(15, 6), dpi=80)
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)
# x = data_piv1.index
x_list = []
[x_list.append(i[6:]) for i in data_piv1.index]
print("x_list: ", x_list)
x = x_list
print("x: ", x)
y = data_piv1.values
ax1.plot(x, y[:, 0], 'r--^',
         x, y[:, 1], 'b-.D',
         x, y[:, 2], 'g-.D',
         x, y[:, 3], 'y-.D')

ax2.scatter(x, y[:, 0])
ax2.scatter(x, y[:, 1])
plt.legend(data_piv1.columns, loc='upper left')
plt.show()

data_piv2 = pd.crosstab(data_v1["姓名"], data_v1["日期"], data_v1['交易额'], aggfunc="sum")
print("data_piv2: \n", data_piv2)

