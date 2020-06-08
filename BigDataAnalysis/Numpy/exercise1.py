import numpy as np

load_csv_data = np.loadtxt("iris_sepal_length.csv", delimiter=",");

print("数组的形状", '-'*30, "\n", load_csv_data.shape)
print("数组的类型", '-'*30, "\n", load_csv_data.dtype)
print("数组的纬度", '-'*30, "\n", load_csv_data.ndim)

print(load_csv_data)
# 对数据进行排序
load_csv_data.sort()
print(load_csv_data)

# 去除重复值
data = list(set(load_csv_data))
print(data)

print("列表元素之和: ", sum(data))

print("均值: ", sum(data)/len(data))
print("均值: ", np.mean(data))
print("最大值: ", max(data))
print("最小值: ", min(data))
print("方差: ", np.var(data))
print("标准差: ", np.std(data, ddof=1))

