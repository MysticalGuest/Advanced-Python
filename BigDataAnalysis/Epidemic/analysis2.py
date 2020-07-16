import pandas as pd
import matplotlib.pyplot as plt


# 全球实时数据分析
def read_def(file_name):
    file = open(file_name, encoding="gbk")    # 解决文件名中，有中文文字的方法
    data = pd.read_csv(file)
    return data


read_data = read_def("全球_real_data.csv")
read_data.isnull().sum()
# read_data.shape
read_data.fillna(0)
new_df = read_data.set_index("id")
new_df = new_df.iloc[:, 1:]
new_df = new_df.fillna(0)
# 找出最大的前n个信息
print("new_df.loc[new_df['当日_confirm'].nlargest(10).index]: \n", new_df.loc[new_df["当日_confirm"].nlargest(10).index])
new_df.sort_values('累计_dead', ascending=False).head(10)    # 找出最大的前n个信息的方法2

# 找出最小的前n个信息
print("new_df.loc[new_df['累计_confirm'].nsmallest(10).index]: \n",
      new_df.loc[new_df["累计_confirm"].nsmallest(10).index])
# new_df.nlargest(2)

# 描述性统计
new_df.loc[:, ['当日_confirm', "累计_confirm", "累计_dead", "累计_heal"]].describe().round(2)

new_df["死亡率"] = (new_df['累计_dead']/new_df['累计_confirm']).agg(lambda i: format(i, '.2f'))  # 计算死亡率

# 找出最大的前n个死亡率信息的
print("new_df.sort_values('死亡率', ascending=False).head(20).loc[:, ['name', '累计_confirm', '累计_dead', '死亡率']]:\n",
      new_df.sort_values('死亡率', ascending=False).head(20).loc[:, ['name', "累计_confirm", "累计_dead", '死亡率']])

new_df['当日_storeConfirm'] = new_df["累计_confirm"] - new_df['累计_dead']-new_df['累计_heal']
# 找出最大的前n个死亡率信息的
new_df2 = new_df.sort_values('死亡率', ascending=False).head(20).loc[:, ['name', "累计_confirm", "累计_dead", '死亡率']]

new_df2 = new_df2.sort_values('name')

fig = plt.figure(figsize=(8, 6), dpi=80)

plt.rcParams['font.sans-serif'] = 'SimHei'
x = new_df2['name']
y = new_df2['累计_confirm']
y1 = new_df2['死亡率']
plt.plot(x, y)
plt.xticks(rotation=30)
plt.show()
