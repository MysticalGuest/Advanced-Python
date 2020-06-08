# numpy数值计算库的使用
# 1数组的创建
# 1-1创建方法1   np.array()
import numpy as np

l1 = [x for x in range(1, 16)]
print("l1: ", l1)

'''
list完全不同，它的每个元素其实是一个地址的引用，这个地址又指向了另一个元素，这些元素的在内存里不一定是连续的。
所以list其实是只能塞进地址的“数组”，而且由于地址不用连续，每当我想加入新元素，我只用把这个元素的地址添加进list。
'''
l2 = [1, 2, 3, 4, 5]
print("l2[0]: ", l2[0])

'''
一个numpy array 是内存中一个连续块，并且array里的元素都是同一类（例如整数）。
所以一旦确定了一个array，它的内存就确定了，那么每个元素（整数）的内存大小都确定了（4 bytes）。
'''
arr1 = np.array(l1)  # 创建1维数组
print("arr1: ", arr1)
print("arr1: ", arr1[2])

l2 = ["曹操", 24]
arr2 = np.array(l2)  # 24将会被强制转换维字符型，因为数组中的数据类型只能有一种
print("arr2: ", arr2)

l3 = [[2, 3, 4, 5], [5, 6, 7, 8], [9, 7, 5, 3]]
arr3 = np.array(l3)  # 创建一个二维数组
print("多维数组是arr3的值: {}".format(l3))

print("-" * 50)
print("arr3数组的维数：{}  \narr3数组的尺寸：{}  \narr3数组的元素个数：{} \narr3数组的类型：{}"
      .format(arr3.ndim, arr3.shape, arr3.size, arr3.dtype))

# 1-2查看数组属性
print("-" * 50)
print("arr1数组的维数：{}  \narr1数组的尺寸：{}  \narr1数组的元素个数：{} \narr1数组的类型：{}"
      .format(arr1.ndim, arr1.shape, arr1.size, arr1.dtype))

print("arr3: ", arr3)

# 1-2创建数组的方法2   使用函数创建
print("使用arange函数创建数组：\n", np.arange(1, 10, 2))

# np.linspace主要用来创建等差数列，1到10间50个数
print("使用linspace函数创建数组：\n", np.linspace(1, 10, 50))

print("使用zeors函数创建数组：\n"), np.zeros((3, 4))

print("使用eye函数创建数组：\n", np.eye(3))

print("使用ones函数创建数组：\n", np.ones((4, 3)))

# 改变数组维度的两种方法
arr4 = np.arange(1, 16, 1)
print("arr4: ", arr4)
# 改变维度方法1：
arr5 = arr4.reshape((3, 5))
print("arr5: ", arr3)
# 改变维度方法2：
arr5.shape = 5, 3
print("arr5: ", arr3)

# 1-3创建数组的方法3：随机数创建
print("-" * 50)
print(np.random.random(100).reshape(20, 5))
print("-" * 50)
print(np.random.rand(10, 5))   # 生成符合均匀分布的随机数
print("-" * 50)
print(np.random.randn(10, 5))    # 生成符合正态分布的随机数

print("-" * 50)
np.random.seed(5)  # 生成确定随机数生成的随机种子
print("生成给定范围的随机数：\n", np.random.randint(10, 100, size=(10, 10)))

