import pandas as pd
import matplotlib.pyplot as plt


# 探索酒类消费数据
# 1.将数据框命名为drinks
drinks = pd.read_csv("drinks.csv")
print("数据框的形状:\n", drinks.shape)
print("drinks: \n", drinks)

# 2.哪个大陆(continent)平均消耗的啤酒(beer)更多？
drinks.loc[:, ["beer_servings", "continent"]].groupby('continent').mean().round(2).idxmax()

# 3.打印出每个大陆(continent)的红酒消耗(wine_servings)的描述性统计值。

drinks_df2 = drinks.loc[:, ["wine_servings", "continent"]].groupby('continent').describe().round(2)
print("drinks_df2.shape: \n", drinks_df2.shape)
print("drinks_df2.columns: \n", drinks_df2.columns)
drinks_df3 = drinks_df2.iloc[:, 1]   # 每个大陆消费红酒的均值

fig3 = plt.figure(figsize=(10, 6))
# 第1个图
ax1 = fig3.add_subplot(221)
ax1.pie(drinks_df3.values, labels=drinks_df3.index, autopct="%1.1f%%", explode=[0.1, 0.1, 0, 0, 0])

# 4.打印出每个大陆每种酒类别的消耗平均值。
drinks_df4 = drinks.groupby("continent").mean().round()
print("drinks_df4: \n", drinks_df4)

# 第2个图
x = drinks_df4.index
ax2 = fig3.add_subplot(222)
ax2.plot(x, drinks_df4.iloc[:, 0], 'r-.D',
         x, drinks_df4.iloc[:, 1], "g--H",
         x, drinks_df4.iloc[:, 2], "y-.d")
plt.legend(['beer', 'spirit', 'wine'])

# 5.打印出每个大陆每种酒类别的消耗中位数。
print("drinks.groupby(\"continent\").median().round(): \n", drinks.groupby("continent").median().round())

# 6.打印出每个大陆对spirit饮品消耗的平均值，最大值和最小值。
drinks_df5 = drinks.groupby("continent")['spirit_servings'].agg(["mean", "max", 'median']).round()

# x1 = drinks_df5.index
print("drinks_df5: \n", drinks_df5)
print("drinks_df5.index: \n", drinks_df5.index)

# 7.绘制以上（第6题）数据的图形（折线图）
ax3 = fig3.add_subplot(212)
ax3.plot(drinks_df5.index, drinks_df5.iloc[:, 0])
# plt.legend(['beer','spirit','wine'])
plt.show()

