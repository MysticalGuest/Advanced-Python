# 1.创建Series对象
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
pandas库的Series对象用来表示一维数据结构，跟数组类似，但多了一些额外的功能；
它的内部结构很简单，由两个相互关联的数组组成(index和values)，
其中主数组用来存放数据，主数组的每一个元素都有一个与之相关联的标签，这些标签存储在一个Index的数组中
"""

# 1-1  方法1用数组创建
seri_v1 = pd.Series(np.arange(1, 20, 5))
print("seri_v1的原始数据".ljust(30, "="))
print(seri_v1)
seri_v1[2] = -13
print(seri_v1)

# 1-2  方法2用字典创建
seri_v2 = pd.Series({"语文": 90, "数学": 80, "英语": 78,
                     "数据分析": 97, "物理": 90, "化学": 89})
print("seri_v2的原始数据".ljust(30, "="))
print(seri_v2)
print(type(seri_v2))

# 1-3  Series 操作
print("seri_v1的数据求绝对值".ljust(30, "="))
print(abs(seri_v1))

print("seri_v1的索引加字符'a'".ljust(30, "="))
print(seri_v1.add_prefix("a"))

print("seri_v2的索引加姓名'_张三'".ljust(30, "="))
print(seri_v2.add_suffix("_张三"))

print("测试张三的各课成绩是否在80到100之间".ljust(30, "="))
print(seri_v2.between(80, 100))

print("查看各课成绩在90分以上的信息".ljust(30, "*"))     #用逻辑表达式取值
print(seri_v2[seri_v2 >= 90])

print("取Seri_v2中最小的2个值".ljust(30, "*"))
print(seri_v2.nsmallest(2))

print("取Seri_v2中最大的2个值".ljust(30, "*"))
print(seri_v2.nlargest(2))

lambda x:x+3    # lambda表达式，也叫临时函数


def add_def(x):
    return x*3


print("用函数处理Seri_v2中所有值".ljust(30, "*"))
print(seri_v2.apply(add_def))

print("用Seri_v2值绘制折线图".ljust(30,"*"))

plt.rcParams['font.sans-serif'] = 'SimHei'

plt.plot(seri_v2)
for i in range(len(seri_v2)):
    plt.annotate(xy=(i, seri_v2[i]),  # 箭头的终点坐标
                 s=seri_v2[i],     # 显示的值
                 arrowprops=dict(arrowstyle="->"),    # 箭头样式
                 xytext=(i, seri_v2[i]+2))   # 箭头的起点坐标
plt.show()

