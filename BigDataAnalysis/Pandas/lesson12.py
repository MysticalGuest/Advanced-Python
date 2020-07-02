import numpy as np
import pandas as pd
# 异常值处理方法1--拉依达准则函数
import warnings


warnings.filterwarnings('ignore')


def out_range(data):
    arr_bool = (data.mean() - 3 * data.std() > data) | (data.mean() + 3 * data.std() < data)  # 确定了异常值的布尔值

    index = np.arange(data.shape[0])[arr_bool]
    out_v1 = data.iloc[index]
    return out_v1


detail1 = pd.read_csv("meal_order_detail1.csv", sep=",", encoding="utf-8")
detail1_v2 = detail1.dropna(how="all", axis=1)

data1 = detail1_v2['amounts']
out_v2 = out_range(data1)
print(out_v2)
print(out_v2.shape)
print(out_v2.max())
print(out_v2.min())

data2 = detail1_v2['counts']     # 销售个数

out_v3 = out_range(data2)
print(out_v2)
print(out_v3.shape)    # 共62个异常值
print(out_v3.max())    # 最大异常值10
print(out_v3.min())    # 最小的异常值是3

# 处理方法：将大于范围的异常值，修改取值范围的上限值
data2[data2 > (data2.mean()+3*data2.std())] = (data2.mean()+3*data2.std())
data3 = data2
(data3 > 5).sum()

# 处理方法：将大于范围的异常值，修改取值范围的下限值
data2[data2 > (data2.mean()+3*data2.std())] = (data2.mean()+3*data2.std())
data3 = data2
(data3 > 5).sum()

# 上面函数的分布操作
data2 = detail1_v2['counts']
min_v1 = data2.mean()-3*data2.std()       # 0.0719245104270092    范围最小值
max_v2 = data2.mean()+3*data2.std()      # 2.073612301017749    范围最大值


(data2 < min_v1).sum()       # 统计小于最小值的个数
(data2 > max_v2).sum()       # 统计大于最大值的个数
data2[data2 > max_v2] = max_v2      # 将异常值进行处理
(data2 > 3).sum()        # 验证处理结果


# 处理异常值的第2中方法
def out_range1(data):
    QL = data.quantile(0.25)  # 下四分位
    QU = data.quantile(0.75)  # 上四分位
    IQR = QU - QL  # 四分位间距

    data.loc[data > (QU + 1.5 * IQR)] = QU
    data.loc[data < (QL - 1.5 * IQR)] = QL
    return data


# data4 = detail1_v2['amounts']
data4 = out_range1(data1)
print("data4: \n", data4)

detail1_v2['amounts'].describe()

print("data4.quantile(0.25): \n", data4.quantile(0.25))
print("data4.quantile(0.75): \n", data4.quantile(0.75))

