import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters


# 数据分析--分组聚合
# 功能函数：打开文件
def read_def(file_name):
    file = open(file_name, encoding="gbk")    # 解决文件名中，有中文文字的方法
    data = pd.read_csv(file)
    return data


read_data = read_def("中国_hist_data.csv")

# 将日期date转换为日期时间格式
read_data["date"] = pd.to_datetime(read_data["date"])

# 查看数据类型
print("read_data.dtypes: ", read_data.dtypes)
read_data = read_data.set_index('date')    # 将日期设置为索引

new_df = read_data.iloc[:, [1, 2, 3, 4, 7, 8, 9, 10, 11, 13]]

new_df.isnull().sum()    # 测试是否有Nan值

time_10D_df = new_df.resample('10D').sum()   # 每10天间隔取样

register_matplotlib_converters()
x = time_10D_df.index
y = time_10D_df.values
plt.plot(x, y[:, 0])
plt.show()


# 将索引转换为星期形式
# new_df.index = new_df.index.weekday_name
print("new_df: ", new_df)

# 按星期进行分类汇总
time_weekday_df = new_df.groupby(new_df.index).max()
x = time_weekday_df.index
y = time_weekday_df.values
# plt.plot(x,y[:,0])
# plt.show()
new_df.loc[new_df.iloc[:,0] ==new_df.iloc[:,0].max(),:]

# 按每天进行分组--将索引转换为天的形式
new_df.index = new_df.index.day
time_day_df = new_df.groupby(new_df.index).sum()
x = time_day_df.index
y = time_day_df.values
fig = plt.figure(figsize=(10,8),dpi=80)
plt.xticks([x for x in range(32)])
plt.plot(x, y[:, 0])
plt.show()
