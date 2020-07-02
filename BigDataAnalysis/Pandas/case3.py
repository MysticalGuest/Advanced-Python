# 探索Apple公司股价数据
import matplotlib.pyplot as plt
import pandas as pd


# 1.	读取数据并存为一个名叫apple的数据框。
apple = pd.read_csv('appl_1980_2014.csv')
apple.shape
apple
# 2.	查看每一列的数据类型。
apple.dtypes
# 3.	将Date这个列转换为datetime类型。
apple['Date'] = pd.to_datetime(apple['Date'])
# 4.	将Date设置为索引。
apple = apple.set_index('Date',)
# 5.	有重复的日期吗？
apple.index.unique().shape == apple.index.shape
# 6.	将index设置为升序。
apple = apple.sort_index()
# 7.	找到每个月的最后一个交易日(businessday)。
date_df5 = apple.groupby([apple.index.year,apple.index.month]).agg(lambda x:x.index.max())
date_df5.iloc[:,0]
# 8.	数据集中最早的日期和最晚的日期相差多少天？
(apple.index.max()-apple.index.min()).days
# 9.	在数据中一共有多少个月？
date_df5.shape
# 10.	按照时间顺序可视化Adj Close值。
data_x = apple.index
data_y = apple.loc[:"Adj Close"]

apple

apple.index.unique().shape

apple.index.shape


data_x = apple.index
data_y = apple.loc[:,['Open','Close',"Adj Close"]].values
plt.figure(figsize=(13,10))
plt.plot(data_x,data_y[:,2],"r--",
        data_x,data_y[:,1],"b-.",
        data_x,data_y[:,0],"y-."
        )
plt.show()

