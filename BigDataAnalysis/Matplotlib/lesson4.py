import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 欧洲杯数据分析案例
# 1.将数据集存入一个名为euro12的数据框内。
euro12 = pd.read_csv("Euro2012.csv")
print("euro12: \n", euro12)
print("euro12.shape: \n", euro12.shape)
print("列名信息如下：\n", euro12.columns)

# 2.只选取Goals这一列。
print("euro12.loc[:, 'Goals']: \n", euro12.loc[:, 'Goals'])

# 3.有多少球队参与了2012欧洲杯？
print("euro12.index.unique().shape: \n", euro12.index.unique().shape)

# 4.该数据集中一共有多少列(columns)?
print("该数据集的列数:\n", euro12.shape)
print("euro12.isnull().sum(): \n", euro12.isnull().sum())

# 查看是否有列全为0的值
euro_arr1 = euro12.values == 0
print("euro_arr1.sum(axis=0)==16: \n", euro_arr1.sum(axis=0) == 16)

# 5.将数据集中的列Team, Yellow Cards和Red Cards单独存为一个名叫discipline的数据框。
discipline = euro12.loc[:, ["Team", 'Yellow Cards', 'Red Cards']]
print("discipline: \n", discipline)

# 6.对数据框discipline按照先Red Cards再Yellow Cards进行排序。
discipline.sort_values(['Red Cards', 'Yellow Cards'], ascending=False)

# 7.计算每个球队拿到的黄牌数的平均值。
discipline.groupby('Team')['Yellow Cards'].agg("mean")

# 8.找到进球数Goals超过6的球队数据。

print("euro12.loc[euro12['Goals'] > 6, 'Team']: \n", euro12.loc[euro12["Goals"] > 6, 'Team'])

# 分步完成：
euro12_arr2 = euro12['Goals'] > 6
print("euro12.loc[euro12_arr2,'Team']: \n", euro12.loc[euro12_arr2, 'Team'])


# 9.选取以字母G开头的球队数据。
print("euro12.loc[euro12[\"Team\"].str[:1] == \"G\", \"Team\"]: \n",
      euro12.loc[euro12["Team"].str[:1] == "G", "Team"])

# 10.选取前7列。
print("euro12.iloc[:, :7].shape: \n", euro12.iloc[:, :7].shape)

# 11.选取除了最后3列之外的全部列。
print("euro12.iloc[:, :-3]: \n", euro12.iloc[:, :-3])

# 12.找到英格兰(England)、意大利(Italy)和俄罗斯(Russia)的射正率(ShootingAccuracy)。
euro12_arr3 = np.array(['England', 'Italy', 'Russia'])
euro12_df3 = euro12.set_index("Team")
print("euro12_df3: \n", euro12_df3)
euro12_df4 = euro12_df3.loc[euro12_arr3, 'Shooting Accuracy']

# 13.用12题中的射正率，绘制一个折线图
plt.rcParams['font.sans-serif'] = 'SimHei'
fig = plt.figure(figsize=(8, 6), dpi=80)    # 添加画布

plt.plot(euro12_df4)

plt.show()

