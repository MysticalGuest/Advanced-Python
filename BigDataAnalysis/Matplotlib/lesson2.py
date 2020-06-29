import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df_Chip1 = pd.read_csv("Chipotle.tsv", sep="\t")

print("原数据是:\n", df_Chip1)

# 探索Chipotle快餐数据

# 1.将数据集存入一个名为chipo的数据框内
chipo = pd.read_csv("Chipotle.tsv", sep="\t")

# 2.查看前10行内容
print("数据集的前10行：\n", chipo.head(10))
print("数据集的前11行：\n", chipo.loc[:10, :])

# 3.数据集中有多少个列(columns)？
print("数据集中列的个数：%d列\n" % chipo.shape[1])

# 4.打印出全部的列名称
print("数据集中列名称：\n", chipo.columns)

# 5.数据集的索引是怎样的？
print("数据集中的行索引:\n", chipo.index)

# 6.被下单数最多商品(item)是什么?
# 统计出每一种商品的数量
chipo_df1 = chipo.loc[:, ['quantity', 'item_name']].groupby("item_name").agg(sum)
print("chipo_df1: \n", chipo_df1)

# 找出数量最多的商品名
print("chipo_df1.loc[chipo_df1['quantity'] == np.max(chipo_df1['quantity']), :]: \n",
      chipo_df1.loc[chipo_df1['quantity'] == np.max(chipo_df1['quantity']), :])      # 方法1
chipo_df2 = chipo_df1.sort_values('quantity', ascending=False).head(15)      # 方法2

print("chipo_df2: \n", chipo_df2)

# 绘制图形
plt.rcParams['font.sans-serif'] = 'SimHei'
# figsize:指定figure的宽和高，单位为英寸
# 1英寸等于2.5cm,A4纸是 21*30cm的纸张
# dpi参数指定绘图对象的分辨率，即每英寸多少个像素，默认为80
fig = plt.figure(figsize=(10, 5), dpi=80)    # 添加画布

# 绘制第1个图形
ax1 = fig.add_subplot(211)
plt.xticks(rotation=45)     # x轴标记旋转45度
x = np.arange(0, 15, 1)
y = chipo_df2.values[:, 0]

p1, = ax1.plot(chipo_df2.index, chipo_df2.values, 'r-.D')
# 绘制图形上的点
for i in (range(len(x))):
    ax1.annotate(xy=(x[i], y[i]+3), s=y[i], fontsize=14)

plt.show()    # 显示

