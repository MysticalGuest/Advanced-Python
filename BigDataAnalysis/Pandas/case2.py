# 探索风速数据
import pandas as pd
import datetime


# 1.	将数据作存储并且设置前三列为合适的索引。

wind = pd.read_csv("wind.csv",sep="\s+",parse_dates=[[0,1,2]])

wind

wind.columns
wind.dtypes
values_df = wind.iloc[:,:3].values
date_list = []
# for i in range(values_df.shape[0]):
#     date_list.append(date_df(int("19"+str(values_df[i,0])),values_df[i,1],values_df[i,2]))

wind['date_v'] = date_list

wind.insert(1,"date_v1",date_list)

wind
#方法1
# def date_df(y,m,d):
#     date1 = datetime.date(y,m,d)
#     return pd.to_datetime(date1)

# values_df = wind.iloc[:,:3].values
# date_list = []
# for i in range(values_df.shape[0]):
#     date_list.append(date_df(int("19"+str(values_df[i,0])),values_df[i,1],values_df[i,2]))

# wind.insert(3,"date_v1",date_list)

#方法2
def  data_df2(x):
    if x.year >2000:
        year_v = x.year-100
    else:
        year_v = x.year
    date_v2 = pd.to_datetime(datetime.date(year_v,x.month,x.day))
    return date_v2
# 2.	2061年？我们真的有这一年的数据？创建一个函数并用它去修复这个bug。
wind['Yr_Mo_Dy'] = wind['Yr_Mo_Dy'].agg(data_df2)
wind.dtypes

# 3.	将日期设为索引，注意数据类型，应该是datetime64[ns]。
wind = wind.set_index('Yr_Mo_Dy')
# 4.	对应每一个location，一共有多少数据值缺失？
wind.isnull().sum()
# 5.	对应每一个location，一共有多少完整的数据值？
wind.notnull().sum()
# 6.	对于全体数据，计算风速的平均值。
wind.mean(axis=1)
# 7.	创建一个名为loc_stats的数据框去计算并存储每个location的风速最小值，最大值，平均值和标准差。
loc_stats = wind.agg(["min","max","mean"])

# 8.	创建一个名为day_stats的数据框去计算并存储所有location的风速最小值，最大值，平均值和标准差。
day_stats = wind.T.agg(["min","max","mean"]).T

# 9.	对于每一个location，计算一月份的平均风速。
wind_df3 = wind[wind.index.month == 1]
wind_df3.groupby([wind_df3.index.year,wind_df3.index.month]).mean().round(2)
# 10.	对于数据记录按照年为频率取样。

wind.asfreq("YS")
# 11.	对于数据记录按照月为频率取样。
wind.asfreq("20D")

