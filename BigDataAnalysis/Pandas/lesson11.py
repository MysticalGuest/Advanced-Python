import pandas as pd
import numpy as np


'''超市：五个柜台，五个营业员。
   张三有事要外出，李四就需要顶替张三经营柜台，此时李四就经营2个柜台
   1.要求：找出那些营业员在某个时间段，同时负责多个柜台。
   2.例如：2019-3-6 9：00-14：00  李四负责两个柜台，
       重复的值一定有：日期，时段，姓名，工号   (找出这4个值重复的信息)
       不重复的值有：柜台，交易额
'''
df_excel = pd.read_excel('超市营业额.xlsx')
# 1.首先从df_excel种提取四个重复信息
df_excel_v1 = df_excel.loc[:, ["工号", "姓名", '日期', '时段']]
# 2.查看哪些值重复
df_excel_v2 = df_excel_v1[df_excel_v1.duplicated()]

# 3.显示每个人究竟经营那些柜台
for i in df_excel_v2.values:
    print(df_excel[(df_excel.工号 == i[0]) &
                   (df_excel.日期 == i[2]) &
                   (df_excel.时段 == i[3])])

# 4.缺失值
# 4-1 检测缺失值
bool_v1 = df_excel["交易额"].isnull()
print("df_excel[bool_v1]: \n", df_excel[bool_v1])      # 显示除缺失的数据

# 4-1 检测不是缺失值的
bool_v2 = df_excel['交易额'].notnull()
print("df_excel.shape: \n", df_excel.shape)
df_excel_v3 = df_excel[bool_v2]
print("df_excel_v3.shape: \n", df_excel_v3.shape)

# 4-1 检测缺失值的个数
print("df_excel.isnull().sum(): \n", df_excel.isnull().sum())

df_detail = pd.read_csv("meal_order_detail2.csv")
print("缺失值统计:\n", df_detail.isnull().sum())
print("df_detail.shape: \n", df_detail.shape)

# 4-4 fillna填充缺失值
df_excel.isnull().sum()
fill_v1 = df_excel.loc[:, '交易额'].median()
print(fill_v1)
fill_v2 = df_excel.loc[:, '交易额'].mean()
print(fill_v2)
df_excel1 = df_excel.fillna(fill_v1)
df_excel1.isnull().sum()

# 4-5 dropna删除缺失值
print("原数据信息：\n", df_excel.shape)
print("删除后的数据信息：\n", df_excel.dropna().shape)
print("使用all参数后的数据信息\n", df_excel.dropna(how="all").shape)

df_detail.isnull().sum()
print("原数据的信息：\n", df_detail.shape)
print("删除缺失值后的信息：\n", df_detail.dropna(axis=1, how="all").shape)
df_detail_v1 = df_detail.dropna(axis=1, how="all")

# 问题:将列值全为0的的列，替换我nan值。
print("df_detail_v1[df_detail_v1.values == 0].shape: \n", df_detail_v1[df_detail_v1.values == 0].shape)

df_excel['交易额'].describe()

print("df_excel['交易'].loc[df_excel['交易额']<200]: \n", df_excel["交易额"].loc[df_excel['交易额'] < 200])

print("np.array([2,3,4,5])[[False,False,True,True]]: \n", np.array([2, 3, 4, 5])[[False, False, True, True]])

df_detail_v1.loc[:, np.sum(df_detail_v1.values == 0, axis=0) != 0] = np.nan
print("df_detail_v1: \n", df_detail_v1)

df_detail_v1.dropna(axis=1)
print("df_detail_v1: \n", df_detail_v1)

# 1.处理遗留问题
# 检测缺失值
detail1 = pd.read_csv("meal_order_detail1.csv", sep=",", encoding="utf-8")
detail1.isnull().sum()
detail1_v1 = detail1.dropna(how="all", axis=1)      # 删除全部为空的列

# 将df中全部为0 的值，设置nan，然后删除
arr_v1 = (detail1_v1.values == 0).sum(axis=0)     # 把全部为0的列进行计数
shape_v1 = detail1_v1.shape       # 查看形状shape
print(shape_v1)
arr_bool1 = (arr_v1 == shape_v1[0])             # 把arr_v1的值转换为逻辑值

# 找到对应列修改为nan，将为nan的列删除
detail1_v1.loc[:, arr_bool1] = np.nan        # 用逻辑值找到对应列后，修改为np.nan
detail1_v2 = detail1_v1.dropna(how="all", axis=1)     # 将为nan的列删除

# 按会员号emp_id分组，然后计算
detail1_v2.groupby("emp_id")['amounts', "counts"].agg(sum)
detail1_v2["total"] = detail1_v2["amounts"]*detail1_v2['counts']
print("detail1_v2: \n", detail1_v2)
detail1_v2.groupby("emp_id")['total', "counts"].agg(sum)

# 绘制一个透视表
print("detail1_v2: \n", detail1_v2)
# 每个会员，所下订单的金额之和
detail_v3 = detail1_v2.pivot_table(index="emp_id", columns="order_id", values="amounts", aggfunc="sum").head(10)
detail_v3.fillna(0).agg(sum, axis=1)
print("detail1_v3: \n", detail_v3)

