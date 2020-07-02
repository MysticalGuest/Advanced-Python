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

# 是否使用Unicode东亚宽度来计算显示文本的宽度。 启用它可能会影响性能（默认：False）[默认：False] [当前：True]
pd.set_option('display.unicode.ambiguous_as_wide', True)
# pd.set_option('display.unicode.east_asian_width', True)

df1 = pd.read_excel('超市营业额.xlsx')
print("打开的第1个数据：\n", df1)

# sheet_name对应Excel中的Sheet标签，一个excel可能有不止一个sheet
# sheet_name参数可以接收的有：str，int，list或None，默认0
# 指定读取第一个位置的sheet
df2 = pd.read_excel("超市营业额.xlsx", sheet_name=1)
print("打开的第2个数据：\n", df2)

# 1.合并数据命令1-concate()
df3 = pd.concat([df1, df2], axis=0, ignore_index=True)
print("使用concate合并的数据，将df1和df2合并:\n", df3)

# 2.合并数据命令2-append()
df6 = df1.loc[df1['日期'] == "2019-03-01", :]     # 提取出2019年3月1日的数据，和2019年4月1日的数据合并
print("df6：\n", df6)
df4 = df6.append(df2, ignore_index=True)   # ignore_index的作用是忽略原来的索引。
print("使用append合并的数据：\n", df4)

# 3.合并数据命令3-merge()
df5 = pd.read_excel("超市营业额.xlsx", sheet_name=2)
print("df5：\n", df5)

df7 = pd.merge(df3, df5, on="工号", how="left")
print("df7：\n", df7)

# 4.合并数据命令4-join
df8 = df3.set_index("工号").join(df5.set_index("工号"), lsuffix="_x", rsuffix="_y")
print("df8：\n", df8)

# 5.重叠合并--combine_first()


# 补充知识点：设置索引
df7 = pd.merge(df3, df5, how="left")
df9 = df7.set_index('柜台')
print("df9：\n", df9)
# 重置索引
df9.reset_index()
print("df9：\n", df9)

