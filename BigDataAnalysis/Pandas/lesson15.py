# 异常值处理方法1--拉依达准则函数
import warnings
import pandas as pd

warnings.filterwarnings('ignore')


def out_range(data):
    arr_bool = (data.mean() - 3 * data.std() > data) | (data.mean() + 3 * data.std() < data)  # 确定了异常值的布尔值

    index = np.arange(data.shape[0])[arr_bool]
    out_v1 = data.iloc[index]
    return out_v1


# 处理异常值的第2中方法
def out_range1(data):
    QL = data.quantile(0.25)  # 下四分位
    QU = data.quantile(0.75)  # 上四分位
    IQR = QU - QL  # 四分位间距

    data.loc[data > (QU + 1.5 * IQR)] = QU
    data.loc[data < (QL - 1.5 * IQR)] = QL
    return data


df_excel = pd.read_excel("超市营业额.xlsx")

print('处理之前的最大值是：\n', df_excel['交易额'].max())
print('处理之前的最小值是：\n', df_excel['交易额'].min())
data_v3 = df_excel['交易额']
data_v4 = out_range1(data_v3)
print('函数2处理之前的最大值是：\n', data_v4.max())
print('函数2处理之前的最小值是：\n', data_v4.min())

# 方法2处理异常值
import numpy as np


def out_range(data):
    arr_bool = (data.mean() - 3 * data.std() > data) | (data.mean() + 3 * data.std() < data)  # 确定了异常值的布尔值

    index = np.arange(data.shape[0])[arr_bool]
    out_v1 = data.iloc[index]
    return out_v1


df_excel = pd.read_excel("超市营业额.xlsx")
data_v3 = df_excel['交易额']
out_v2 = out_range(data_v3)
print(out_v2)
print('函数1处理之前的最大值是：\n', data_v4.max())
print('函数1处理之前的最小值是：\n', data_v4.min())
data_v3.mean() - 3 * data_v3.std()
data_v3.mean() + 3 * data_v3.std()

# 方法2：分布处理异常值
min_bool2 = data_v3.mean()-3*data_v3.std()
max_bool2 = data_v3.mean()+3*data_v3.std()
bool_v2 = (data_v3 < min_bool2) | (data_v3 > max_bool2)
print("data_v3[bool_v2]: \n", data_v3[bool_v2])

