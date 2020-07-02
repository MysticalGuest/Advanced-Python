import pandas as pd


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

