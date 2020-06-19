# 5.DataFrame的操作
import pandas as pd
import numpy as np


# 5-1 查看DataFrame的基础属性
df_v3 = pd.read_csv("meal_order_detail1.csv", sep=",", encoding="utf-8")
df_v5 = pd.read_excel("超市营业额2.xlsx", sheet_name=1)

print("df_v5的值属性：values".ljust(30, "="), "\n")
print(df_v5.values)   # 返回的是一个数组

print("df_v5的列名：columns".ljust(30, "="), "\n")
print(df_v5.columns)

print("df_v5的行索引：index".ljust(30, "="), "\n")
print(df_v5.index)

print("df_v5的各列的类型：dtypes".ljust(30, "="), "\n")
print(df_v5.dtypes)

print("df_v3的形状：shape".ljust(30, "="), "\n")
print(df_v3.shape)     # 返回的是一个元组

# ['工号', '姓名', '日期', '时段', '交易额', '柜台'],

# 5-2 查数据--方式1：直接用列名查找
print("用字典方式访问df_v5的数据".ljust(30, "="), "\n")
print(df_v5['姓名'])     # 用列名方式
print(df_v5.姓名)       # 把列名当作属性来访问，不建议使用

print("取df_v5中姓名的前n行".ljust(30, "="), "\n")
print(df_v5["姓名"][:5])   # 把姓名取出后，相当于一个Series，然后可以用操作数组的方式进行操作

print("取df_v5中多列的前n行".ljust(30, "="), "\n")
print(df_v5[["姓名", "交易额"]][:5])   # 把姓名取出后，相当于一个Series，然后可以用操作数组的方式进行操作

print("取df_v5中所有列的前n行".ljust(30, "="), "\n")
print(df_v5[:][:5])   # 把姓名取出后，相当于一个Series，然后可以用操作数组的方式进行操作


print("取df_v5中所有列的前n行".ljust(30, "="), "\n")
print(df_v5[:].head(6))   # 把姓名取出后，相当于一个Series，然后可以用操作数组的方式进行操作


print("取df_v5中所有列的后n行".ljust(30, "="), "\n")
print(df_v5[:].tail(6))   # 把姓名取出后，相当于一个Series，然后可以用操作数组的方式进行操作


# ['工号', '姓名', '日期', '时段', '交易额', '柜台'],
# 5-3 第2中访问方式--用方法操作loc
print("用loc取df_v5中的姓名值".ljust(30, "="), "\n")

print(df_v5.loc[:, "姓名"])

print("用loc取df_v5中的姓名值".ljust(30, "="), "\n")

print(df_v5.loc[:, ["姓名", "交易额", '柜台']].head())

info_df1 = df_v5.loc[:, ["姓名", "交易额", '柜台']]
print("用loc取df_v5中交易额大于1400的信息".ljust(30, "="), "\n")
info_bool = info_df1["交易额"] > 1400    # 交易额大于1400的逻辑值
# 用逻辑值取数据
print(info_df1.loc[info_bool, :])

# 5-4 第2中访问方式--用方法操作iloc
print("用iloc取df_v5中的姓名值".ljust(30, "="), "\n")
# ['工号', '姓名', '日期', '时段', '交易额', '柜台'],
print(df_v5.iloc[:, 1:4])

info_df1 = df_v5.loc[:, ["姓名", "交易额", '柜台']]
print(info_df1)
print(info_df1.loc[info_df1["交易额"] > 1400, :])


df_index = df_v5.set_index(np.arange(1, 9, 1))
print(df_index.iloc[1:5, :])

# 查找数据方法loc和iloc的区别
print("原始数据为：", df_v5)
# 区别1：区间有区别
print("用loc取的值\n", df_v5.loc[1:5, ['姓名', '日期', '交易额']])   # loc切片时，左闭，右闭
print("用iloc取的值:\n", df_v5.iloc[1:5, [1, 2, 4]])    # iloc切片时，左闭，右开

# 区别2：loc用的索引本身，而iloc用的是索引位置

df_v6 = df_v5.set_index(np.arange(2, 10, 1))
print("修改索引后的数据:\n", df_v6)
print("用loc取的值\n", df_v6.loc[2:5, ['姓名', '日期', '交易额']])   # loc切片时，左闭，右闭
print("用iloc取的值:\n", df_v6.iloc[2:5, [1, 2, 4]])    # iloc切片时，左闭，右开

# 条件取值
print("df_v5.loc[df_v5['交易额']>1400, :]: \n", df_v5.loc[df_v5['交易额'] > 1400, :])
print("df_v5.iloc[(df_v5['交易额']>1400).values, :]: \n", df_v5.iloc[(df_v5['交易额'] > 1400).values, :])

# 2.改数据
df_v5.loc[df_v5['交易额'] > 1400, '交易额'] = df_v5.loc[df_v5['交易额'] > 1400, '交易额']-100

# 3.增加列
df_v5['记录员'] = "李宇春"

# 4.柜台为化妆品的记录员，修改为“王源”
df_v5.loc[df_v5.柜台 == "化妆品", "记录员"] = "王源"
print("df_v5: ", df_v5)

# 5.指定位置插入列
df_v5.insert(2, '性别', ["女" for x in range(8)])
print("df_v5: ", df_v5)

# 6.插入行
row_dict = dict(工号=1008, 姓名="刘德华", 性别="男", 日期=None, 时段=None, 交易额=1234, 柜台="食品", 记录员="王源")
df_v5.append(row_dict, ignore_index=True)

df_v5.loc[2] = [1010, '孙九', '女', '2019-04-01', '14：00-21：00', 1333, '蔬菜水果', '李宇春']
print("df_v5: \n", df_v5)

# 7.删除列/行

df_v7 = df_v5.drop("性别", axis=1, inplace=False)   # 删除列
df_v8 = df_v5.drop(4, axis=0, inplace=False)      # 删除行
print("df_v8: \n", df_v8)

