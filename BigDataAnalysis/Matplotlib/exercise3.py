
# 动画绘图--animation
# 案例：动画绘制1-12月中，各种品牌的销量的折线图
from matplotlib import animation  # 动画绘图库
import matplotlib.pyplot as plt
import numpy as np

# from IPython.display import HTML  # HTML中显示动画

np.random.seed(12)
# 男装：30-60
arr_nan = np.random.randint(30, 60, size=(12,))
# 女装：20-85
arr_nv = np.random.randint(20, 85, size=(12,))
# 餐饮：30-75
arr_can = np.random.randint(30, 75, size=(12,))
# 化妆品：80-140
arr_hua = np.random.randint(80, 140, size=(12,))
# 首饰：70-150
arr_shou = np.random.randint(70, 150, size=(12,))
# 月份：1-12
arr_month = np.arange(1, 13, 1)

arr_total = list(np.array([arr_nan, arr_nv, arr_can, arr_hua, arr_shou]))
print("arr_total: ", arr_total)
fig = plt.figure(figsize=(8, 6), dpi=80)  # 定义绘图画布
# 这些是作为单个整数编码的子绘图网格参数。
# 例如，“111”表示“1×1网格，第一子图”，“234”表示“2×3网格，第四子图”
ax1 = fig.add_subplot(111)


def update(num):  # 要执行的函数
    ax1.clear()  # 清除之前绘制的内容
    print("num: ", num)
    print("arr_total[num]: ", arr_total[num])
    ax1.pie(arr_total[num], explode=[0.2 for x in range(12)], labels=arr_month)
    return ax1,


ani = animation.FuncAnimation(fig=fig,
                              func=update,
                              frames=np.arange(5),
                              interval=500,  # 这里的frames在调用update函数是会将frames作为实参传递给“n”
                              blit=True, repeat=False)

# animation中的frames是，要执行函数多少次。一般是一个可迭代对象，将参数依次给了函数，
plt.show()

# HTML(ani.to_jshtml())


arr_total = np.array([arr_nan, arr_nv, arr_can, arr_hua, arr_shou])
l1 = list(arr_total)
print("l1[1]", l1[1])

