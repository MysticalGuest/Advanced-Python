import pandas as pd


dian_df = pd.read_csv("data_etr.csv",parse_dates=['DATA_DATE'])

# 用户用电量统计分析
# data.csv为用户用电量数据,数据中有编号为1-200的200位电力用户，DATA_DATE表示时间，如2015/1/1表示2015年1月1日，KWH为用电量。
# 1.	将数据进行转置，转置后行为用户编号、列为日期、值为用户每日用电量。
dian_df1 = pd.pivot_table(dian_df,index="CONS_NO",columns="DATA_DATE",values="KWH")
# 2.	对数据中的异常数据进行识别并处理。

# 3.	统计每个用户用电数据的基本统计量，包括：最大值、最小值、均值、中位数、和、方差、偏度、峰度。
# 4.	每个用户用电数据按日差分，并求取差分结果的基本统计量，统计量同3。
# 5.	求取每个用户的5%分位数。
# 6.	每个用户按周求和并差分（一周7天，年度分开），并求取差分结果的基本统计量，统计量同3。
# 7.	统计每个用户的日用电量在其最大值0.9倍以上的次数。
# 8.	求取每个用户日为最大值/最小值的索引月份，若最大值/最小值存在于多个月份中，则输出含有最大值/最小值最多的那个月份。如1号用户的最小值为0，12个月每个月都有0，则看哪个月的0最多。
# 9.	求取每个用户七八月电量和与三四月电量和的比值，最大值的比值，最小值的比值，均值（日均电量）的比值。
# 10.	合并上述特征。

dian_df1

