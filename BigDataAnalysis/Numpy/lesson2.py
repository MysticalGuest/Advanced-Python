# 2.数组的操作
import numpy as np

arr_fun = np.arange(1, 16, 1)
arr_fun1 = arr_fun.reshape((3, 5))
print("*" * 50)
print("二维数组3行5列 \n", arr_fun1)

print("用索引访问", "*" * 30)
print(arr_fun1[0, 1])  # 返回2

print(arr_fun1[2, 4])  # 返回15

print(arr_fun[4])  # 访问1维数组的方法

print("arr_fun1[:, 1]\n", arr_fun1[:, 1])  # 返回第2列的值

print("arr_fun1[1, :]\n", arr_fun1[1, :])  # 返回第2行的值
print(arr_fun1[0:2, 1:4])
print(arr_fun1[0:2, 2:5])

print(arr_fun1[:, (1, 3)])  # 返回2，4两列的值

print(arr_fun1[(True, False, True), :])  # 用逻辑值，来取值

print("=" * 50)
print(arr_fun1[arr_fun1[:, 4] > 8, :])  # 先找出第3列中大于5的行，再从结果中返回前3列。

# 数组操作在实际中的应用 --输入姓名，年龄，班级值到三个列表中name_list,age_list,class_list中，形成1个大列表info_list
info_list = []
name_list, age_list, class_list = [], [], []
while True:
    name = input("输入姓名")
    if name == "0":
        break
    age = input("输入年龄")
    class_v = input("输入班级")
    name_list.append(name)
    age_list.append(age)
    class_list.append(class_v)

info_list.append(name_list)
info_list.append(age_list)
info_list.append(class_list)
print("info_list: ", info_list)

arr_info = np.array(info_list)
print("arr_info: ", arr_info)

info_list = [['aaa', 'bbb', 'ccc', 'ddd', 'eee'], ['23', '25', '28', '26', '27'], ['计算机', '计算机', '英语', '数学', '数学']]
arr_info = np.array(info_list)

arr_info[:, arr_info[2, :] == "计算机"]

# 数据类型转换
arr_type = arr_info[1, :]  # 提取出年龄行信息

np.int8(arr_type)
np.float16(arr_type)

arr_info[:, np.int8(arr_info[1, :]) > 25]  # 索引年龄大于25的信息

print(arr_info[1, :])

np.str_(34)

# 用bool值提取数据
arr_bool = np.eye(4)
arr_bool1 = np.array(arr_bool, dtype=np.bool)  # 生成布尔值数组

print("布尔值数组：\n", arr_bool1)
np.random.seed(5)
arr_eye = np.random.randint(1, 10, size=[4, 4])  # 用布尔值提取元素
print("需要提取值的数组:\n", arr_eye)
print("提取结果如下：\n", arr_eye[arr_bool1])

print("arr_eye: \n", arr_eye)

print("arr_bool: \n", arr_bool)

# 数组的操作--展平，合并，分隔
# 二维数组变为1维数组--展平
print("二维数组:\n", arr_eye)
print("一维数组：\n", arr_eye.ravel())  # 数组展平为1维数组
print("一维数组:\n", arr_eye.reshape(16))

print("一维数组:\n", arr_eye.flatten("F"))  # 纵向展平

# 数组的合并--多个数组并成1个数组
print("横向合并：\n", np.concatenate((arr_eye, arr_eye), axis=1))  # axia为1的时候，是横向合并
print("纵向合并：\n", np.concatenate((arr_eye, arr_eye), axis=0))  # axia为1的时候，是横向合并

# 数组的拆分--多个数组并成1个数组
print("横向拆分：\n", np.split(arr_eye, 2, axis=1))
print("纵向拆分：\n", np.split(arr_eye, 2, axis=0))
arr1 = np.split(arr_eye, 2, axis=0)  # 拆分后会形成包含多个数组的列表
print(type(arr1))
print(arr1[0])
# print(arr2)


# 数组的四则运算
x = np.arange(1, 11)
print("x:", x)
np.random.seed(5)
y = np.random.randint(1, 20, size=10)
print("y:", y)

# 数组的比较运算
print("x<y: ", x < y)
print("x>y: ", x > y)
print("np.all(x == y): ", np.all(x == y))   # 所有的都相等的时候，才返回True
print("np.all(x == y): ", np.any(x == y))   # 只要有1个相等的就返回True

x1 = x.reshape((2, 5))
y1 = y.reshape((5, 2))
print("x1: ", x1)
print("y1: ", y1)
# 广播机制--纵向广播（从上向下）
arr1 = np.array([1, 2, 3, 4, 5])
print("arr1: ", arr1)
print("纵向广播: \n", x1 + arr1)

# 广播机制--横向广播(从左向右)
y2 = arr1.reshape((5, 1))
np.random.seed(5)
arr2 = np.random.randint(1, 19, size=[5, 4])
print("arr2\n", arr2)

print("横向广播: ", y2 + arr2)

# 数组常用的统计函数
arr3 = np.arange(20).reshape(4, 5)
print("arr3: ", arr3)

# 函数操作1：
print("数组所有数据的和", np.sum(arr3))
print("数组中每1列的值的和", np.sum(arr3, axis=0))
print('数组中每1行的值的和', np.sum(arr3, axis=1))  # 使用numpy中的函数
print("数组中每1行的值的和", arr3.sum(axis=1))  # 使用的是数组的方法

print("数组中每行的最大值", np.max(arr3, axis=1))  # 求最大值
print("返回数组中最大值的索引下标", np.argmax(arr3, axis=1))  # 返回下标

# 不聚合函数--会产生中间结果
print("求数组的累计和", np.cumsum(arr3, axis=0))
print("求数组的累计积", np.cumprod(arr3[1:, :], axis=1))

# 一维数组的排序
np.random.seed(10)
arr5 = np.random.randint(10, 100, size=(8,))
np.sort(arr5)
# arr5.sort()
print("arr5: ", arr5)

# 二维数组的排序
# 数组的排序
np.random.seed(10)
arr6 = np.random.randint(10, 100, size=(4, 3))
print("用函数排序", np.sort(arr6, axis=0))
# arr5.sort()
print(arr6.sort(axis=0))
print("arr6: ", arr6)

# 返回索引下标的排序
# 数组的排序
np.random.seed(10)
arr7 = np.random.randint(10, 100, size=(5,))
print("arr7: ", arr7)
np.argsort(arr7)  # 返回索引下标的排序
# arr5.sort()


# 数组去重
info_list = [['aaa', 'bbb', 'ccc', 'ddd', 'eee'], ['23', '25', '28', '26', '27'], ['计算机', '计算机', '英语', '数学', '数学']]
arr_info = np.array(info_list)
print("arr_info", arr_info)
# 方法1：使用函数
# np.unique(arr_info[2, :])
print("去重后arr_info", np.unique(arr_info))

# 方法2：使用python中的集合去重
print("去重后arr_info", (set(arr_info[2, :])))

# 数据重复
arr8 = np.array([1, 2, 3])
arr9 = np.tile(arr8, 3)
print("arr8: ", arr8)
print("arr9: ", arr9)

arr6.repeat(3, axis=0)  # 纵向重复
print("纵向重复arr6: ", arr6)

# 数组的存储
np.random.seed(20)
save_arr1 = np.random.randint(10, 100, size=[10, 10])
save_arr2 = np.random.randint(10, 100, size=[20, 20])
print("-" * 50)
print(save_arr1)
print("-" * 50)
print(save_arr2)

np.save("arr_file", arr1)  # 单数组保存
np.savez("arr_file1", arr1=save_arr1, arr2=save_arr2)  # 多数组保存

load_file1 = np.load("arr_file1.npz")
print("-" * 50)
print(load_file1["arr1"])

print("-" * 50)
print(load_file1["arr2"])

