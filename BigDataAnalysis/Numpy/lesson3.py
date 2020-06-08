# 1.文本文件的保存和加载
# 1-1  保存
import numpy as np

np.random.seed(10)
save_arr1 = np.random.randint(10, 100, size=[20, 3])
print("创建的数组", "-" * 30, "\n", save_arr1)
np.savetxt(r"arr1.txt", save_arr1, fmt="%d", delimiter=",")

# 1-2 读文件
load_arr1 = np.loadtxt(r"arr1.txt", delimiter=",", dtype="int8")
print("加载的数组", "-" * 30, "\n", load_arr1)

# 2：numpy案例--鸢尾花花萼长度数据的统计分析

load_csv_data = np.loadtxt(r"iris_sepal_length.csv", delimiter=",")
# 2-1查看数据属性
print("数组的形状", "-" * 30, "\n", load_csv_data.shape)
print("数组的类型", "-" * 30, "\n", load_csv_data.dtype)
print("数组的维度", "-" * 30, "\n", load_csv_data.ndim)

# 2-2对数据进行排序
load_csv_data.sort()
print("数组的排序结果", "-" * 30, "\n", load_csv_data)

# 2-3去除重复值
load_csv_data1 = np.unique(load_csv_data)
print("数组的去重结果", "-" * 30, "\n", load_csv_data1)
# 2-4去重后，花萼长度的和
print("数组去重后的和值", "-" * 30, "\n", np.sum(load_csv_data1))
print("数组没有去重后的和值", "-" * 30, "\n", np.sum(load_csv_data))
# 2-5花萼的均值，标准差，方差，最大值，最小值
print("数组没有去重后的均值", "-" * 30, "\n", np.mean(load_csv_data))
print("数组没有去重后的标准差值", "-" * 30, "\n", np.std(load_csv_data))
print("数组没有去重后的方差值", "-" * 30, "\n", np.var(load_csv_data))
print("数组没有去重后的最小值", "-" * 30, "\n", np.min(load_csv_data))
print("数组没有去重后的最大值", "-" * 30, "\n", np.max(load_csv_data))

# 3：生成一个国际象棋棋盘（即8X8的数组），用0代表黑色方块，用1代表白色方块

arr_qi = np.ones((8, 8))

print("arr_qi: ", arr_qi)
# 生成数字棋盘
for i in range(8):
    for j in range(8):
        if (i + j) % 2 != 0:
            arr_qi[i, j] = 0  # 找到元素改变值
print(arr_qi)

# 生成图像棋盘
for x in range(8):
    for y in range(8):
        if arr_qi[x, y] == 0:
            print("@", end="  ")  # @代替黑方块
        else:
            print("*", end="  ")  # *代替白方块
    print()

# 生成数字棋盘
arr2 = np.eye(2)
arr3 = np.concatenate((arr2, arr2, arr2, arr2), axis=1)
arr4 = np.concatenate((arr3, arr3, arr3, arr3))
# 生成图像棋盘
for i in range(8):
    for j in range(8):
        if arr4[i, j] == 0:
            print("@", end="  ")
        else:
            print("*", end="  ")
    print()

