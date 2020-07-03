# 探索风速数据
import pandas as pd
import datetime

wind1 = pd.read_csv("wind.csv", sep="\\s+")

print("wind1: \n", wind1)
values_df1 = wind1.iloc[:, :3].values
print("values_df1: \n", values_df1)


# 方法1
def date_df(y, m, d):
    date1 = datetime.date(y, m, d)
    return pd.to_datetime(date1)


date_list = []
for i in range(values_df1.shape[0]):
    date_list.append(date_df(int("19"+str(values_df1[i, 0])), values_df1[i, 1], values_df1[i, 2]))

wind1.insert(3, "date_v1", date_list)

wind1['date_v'] = date_list

wind1.insert(1, "date_v2", date_list)

print("wind1: \n", wind1)


# 1.将数据作存储并且设置前三列为合适的索引。
wind2 = pd.read_csv("wind.csv", sep="\\s+", parse_dates=[[0, 1, 2]])

print("wind: \n", wind2)

print("wind.columns: ", wind2.columns)
print("wind.dtypes: ", wind2.dtypes)
values_df = wind2.iloc[:, :3].values
print("values_df: \n", values_df)


# 方法2
def data_df2(x):
    if x.year > 2000:
        year_v = x.year-100
    else:
        year_v = x.year
    date_v2 = pd.to_datetime(datetime.date(year_v, x.month, x.day))
    return date_v2


# 2.	2061年？我们真的有这一年的数据？创建一个函数并用它去修复这个bug。
wind2['Yr_Mo_Dy'] = wind2['Yr_Mo_Dy'].agg(data_df2)
print("wind2.dtypes): \n", wind2.dtypes)

# 3.	将日期设为索引，注意数据类型，应该是datetime64[ns]。
wind2 = wind2.set_index('Yr_Mo_Dy')
# 4.	对应每一个location，一共有多少数据值缺失？
wind2.isnull().sum()
# 5.	对应每一个location，一共有多少完整的数据值？
wind2.notnull().sum()
# 6.	对于全体数据，计算风速的平均值。
wind2.mean(axis=1)
# 7.	创建一个名为loc_stats的数据框去计算并存储每个location的风速最小值，最大值，平均值和标准差。
loc_stats = wind2.agg(["min", "max", "mean"])

# 8.	创建一个名为day_stats的数据框去计算并存储所有location的风速最小值，最大值，平均值和标准差。
day_stats = wind2.T.agg(["min", "max", "mean"]).T

# 9.	对于每一个location，计算一月份的平均风速。
wind_df3 = wind2[wind2.index.month == 1]
wind_df3.groupby([wind_df3.index.year, wind_df3.index.month]).mean().round(2)
# 10.	对于数据记录按照年为频率取样。

wind2.asfreq("YS")
# 11.	对于数据记录按照月为频率取样。
wind2.asfreq("20D")

