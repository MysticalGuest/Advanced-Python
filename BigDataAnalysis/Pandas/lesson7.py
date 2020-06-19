# 7.处理与时间有关的数据
# 7-1创建日期时间
import pandas as pd
import numpy as np


time_v1 = pd.date_range(start="20200501", end="20200601", freq="3D")
print("创建间隔时间为3天的日期数据：\n", time_v1)

time_v2 = pd.date_range(start="20200501010101", periods=12, freq="2H")
print("创建间隔时间为2小时的时间数据：\n", time_v2)

time_v3 = pd.date_range(start="20100101", periods=8, freq="Y")
print("创建间隔时间为1年的日期数据：\n", time_v3)

time_v4 = pd.date_range(start="20100101", periods=8, freq="YS")
print("创建间隔时间为1年的日期数据：\n", time_v4)

time_v5 = pd.date_range(start="20100101", periods=6, freq="2M")
print("创建间隔时间为2月的日期数据：\n", time_v5)

time_v6 = pd.date_range(start="20100101", periods=6, freq="2MS")
print("创建间隔时间为2月的日期数据：\n", time_v6)

# 7-2日期时间的操作

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

np.random.seed(40)   # 给定随机数的随机种子
data_v1 = pd.DataFrame(data=np.random.randint(10, 200, size=(24, 3)),
                       index=pd.date_range(start="20200501", periods=24, freq="H"),
                       columns=["西北大学", "外国语大学", "政法大学"])
print("创建的以时间为索引的DataFrame\n", data_v1)

data_v2 = data_v1.resample("5H")
print("每5个小时取样的结果平均值\n", data_v2.mean())

data_v1.index = data_v1.index+pd.Timedelta("2D")
print("添加2天后data_v1的值\n", data_v1)

data_v1.index = data_v1.index+pd.Timedelta(weeks=2)
print("添加2天后data_v1的值\n", data_v1)

# 7-3提取日期时间中的年，月，日，或返回星期名等
time_v7 = pd.date_range(start="20200501", end="20200601", freq="D")
print("list(time_v7.weekday): \n", list(time_v7.weekday))  # 0代表星期一
print(time_v7.weekday_name)
time_v8 = pd.date_range(start="19990101", periods=30, freq="Y")
print(time_v8.is_leap_year)
print("time_v8: \n", time_v8)


# 7-4将字符串日期转换为日期时间
data_str = "20200601"
data_stamp = pd.Timestamp("20200601")
print("data_stamp.to_pydatetime(): \n", data_stamp.to_pydatetime())
data_style = pd.to_datetime(data_stamp)
print(type(data_style))

# 7-5实操与时间相关数据的练习
data_v1 = pd.read_excel("超市营业额.xlsx")
print("data_v1: ", data_v1)

# 查看数据属性
print("数据值\n", data_v1.values)
print("数据列名\n", data_v1.columns)
print("数据形状\n", data_v1.shape)
print("数据各列的类型\n", data_v1.dtypes)

# 转换日期相关数据为日期格式
data_v1['日期'] = pd.to_datetime(data_v1["日期"])
print("转换日期格式之后的类型为\n", data_v1.dtypes)

# 要计算每7天的营业额之和
data_v2 = data_v1.resample("7D", on="日期").sum()["交易额"]   # 显示的时间是采样周期的开始时间
print("使用采样周期的开始时间：\n", data_v2)

data_v3 = data_v1.resample("7D", on="日期", label="right").sum()["交易额"]   # 显示的时间是采样周期的开始时间
print("使用采样周期的结束时间：\n", data_v3)

data_v4 = data_v1.resample("7D", on="日期", label="right").mean()["交易额"].round(2)   # 显示的时间是采样周期的开始时间
print("使用采样周期的结束时间：\n", data_v4)

# 将日期转换为星期名称的形式
data_v1['日期'] = pd.to_datetime(data_v1['日期'])   # 转换为日期时间格式
week_v1 = [x.day_name for x in data_v1['日期']]   # 遍历出每个日期的星期名
data_v1['日期'] = week_v1      # 赋值星期名到日期列
print("data_v1: \n", data_v1)

