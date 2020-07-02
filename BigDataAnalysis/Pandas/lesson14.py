# 分析一个公司中，员工的年龄和工资的关系
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(45)
dict_data = {"年龄": list(np.random.randint(18, 60, 40)),
             "工资": list(np.random.randint(4000, 30000, 40))}

df_data = pd.DataFrame(dict_data)
print("df_data: \n", df_data)

# 给以上数据绘图
fig = plt.figure(figsize=(10, 10), dpi=100)

ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
ax1.plot(df_data.index, df_data["年龄"])
ax2.plot(df_data.index, df_data["工资"], "r-.")
plt.plot(df_data.index, df_data["年龄"])
plt.plot(df_data.index, df_data["工资"], "r-.")
plt.show()


# 写离差标准化函数
def min_max_scale(data):
    data = (data-data.min())/(data.max()-data.min())
    return data


# 标准差标准化
def stand_scale(data):
    data = (data-data.mean())/data.std()
    return data


# 小数定准标准化
def decimal_scale(data):
    data = data/10**np.ceil(np.log10(data.abs().max()))
    return data


df_data = pd.DataFrame(dict_data)

df_data['年龄'] = decimal_scale(df_data['年龄'])
df_data['工资'] = decimal_scale(df_data['工资'])

fig2 = plt.figure(figsize=(10, 10), dpi=100)

ax1 = fig2.add_subplot(221)
ax2 = fig2.add_subplot(222)
ax3 = fig2.add_subplot(212)
ax1.plot(df_data.index, df_data["年龄"])
ax2.plot(df_data.index, df_data["工资"], "r-.")
ax3.plot(df_data.index, df_data["年龄"], "b--",
         df_data["工资"], "r-.", alpha=0.8)
plt.show()

# 离散化连续型数据
data5 = df_data['年龄']
# 方法1：等宽法
df_data['年龄'] = pd.cut(data5, 4, labels=['青年', '中年', '老年', '领导'])
df_data.groupby("年龄").describe()


# 方法2：等频法划分
def same_cut(data, k):
    w = data.quantile(np.arange(0, 1+1.0/k, 1.0/k))
    data = pd.cut(data, w)
    return data


results = same_cut(data5, 5).value_counts()
print(results)

print("10**0.2: \n", 10**0.2)

