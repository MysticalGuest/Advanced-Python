# 探索1960 - 2014美国犯罪数据
# 1.	将数据框命名为crime。
import pandas as pd
import numpy as np
crime = pd.read_csv("US_Crime_Rates_1960_2014.csv")
print("数据的形状\n",crime.shape)

# 2.	每一列(column)的数据类型是什么样的？
print("每列的数据类型\n",crime.dtypes)
# 3.	将Year的数据类型转换为datetime64。
crime['Year'] = pd.to_datetime(crime['Year'],format="%Y")
# 4.	将列Year设置为数据框的索引。
crime = crime.set_index('Year')
crime.drop('Unnamed: 0',axis=1,inplace=True)
# 5.	删除名为Total的列。
crime.drop('Total',axis=1,inplace=True)
# 6.	按照Year（每十年）对数据框进行分组并求和。
crime.resample("10YS").sum()
# 7.	何时是美国历史上生存最危险的年代？
(crime['Population'].diff()[1:]/crime['Population'].values[:-1]).idxmin()

(crime['Population'].diff()[1:]/crime['Population'].values[:-1])*100
#将次数据绘图

#差分函数diff(periods=n)  periods设置跨度
np.random.seed(10)
data = pd.Series(index = pd.date_range(start="20200601",periods=14,freq="D"),
                 data = np.random.randint(100,1000,14))

data.diff(periods=7)