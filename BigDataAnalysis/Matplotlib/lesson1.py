# matplotlib绘图模块
# 导入库
import matplotlib.pyplot as plt
import numpy as np

# 设置参数
plt.rcParams['font.sans-serif'] = 'SimHei'  # 正常显示汉字
plt.rcParams['axes.unicode_minus'] = False  # 正常显示符号
# 1.获取数据
data = np.arange(0, np.pi * 4, 0.01)
# print(data)

# 2.绘图
# 2-1  绘制画布
plt.figure(figsize=(12, 6), dpi=80)

# 2-2绘图
plt.plot(data, np.sin(data), c="orange", linewidth=5, alpha=0.5, linestyle="--")
plt.plot(data, np.cos(data), c="#3344aa", linewidth=5, alpha=0.5, linestyle=":")

# 3.添加元素
# 3-1标题:
plt.title("三角函数图")  # 图形标题
plt.xlabel("x轴")  # x轴标题
plt.ylabel("y轴")  # y轴标题

# 3-2 轴线上的刻度范围
plt.xlim((0, np.pi * 4 + 1))
plt.ylim((-1, 1))

# 3-3轴线上的刻度取值
plt.xticks([x for x in range(0, 15, 2)])
# plt.yticks(列表）

# 3-4图例
plt.legend(["sin", "cos"], loc=3)

# 2-3保存图像
plt.savefig(r"test.jpg")

# 2-4显示图像
plt.show()

# 案例：有一个饭店，它每月的营业额如:

# 1.获取数据
money = [5.7,  2.8,  5.9, 7.0,  9.0,  20.5,  10.8,  18.4, 7.5,  8.0, 10.2,  30.0]
print(len(money))
# 用红色点划线绘制营业额曲线。
month = list(range(1, 13))

# 2.绘图
# 2-1  绘制画布
plt.figure(figsize=(12, 6), dpi=80)

# 2-2绘图
s_arr = np.array(money)
plt.plot(month, money, c="red", linewidth=3, alpha=0.5, linestyle="-.")  # 绘制折线
plt.scatter(month, money, c="blue", marker="v", s=s_arr * 10)  # 绘制数据点,s用来绘制点的大小

# 给图形上加数据点的值
for i in range(len(money)):
    plt.annotate(xy=(month[i], money[i] + 2), s=str(money[i]))

# 3.添加元素
# 3-1标题:
plt.title("全年营业额趋势图")  # 图形标题
plt.xlabel("月份")  # x轴标题
plt.ylabel("营业额")  # y轴标题

# 3-2 轴线上的刻度范围
plt.xlim((1, 12))
plt.ylim((0, max(money)))

# 3-3轴线上的刻度取值
plt.xticks([x for x in range(0, 14, 1)])
plt.yticks(list(np.linspace(0, max(money) + 3, 5)))

# 3-4图例
plt.legend(["营业额"], loc=3)

# 2-3保存图像
plt.savefig(r"营业额.jpg")

# 2-4显示图像
plt.show()


list(np.linspace(0, max(money), 5))
# 案例：某商场开业之后，有很多顾客反映，商场内有些地方手机信号比较差（打不开微信和支付宝，无法支付）。于是，商场工作人员就对商场进行了手机信号测试，具体如下：
# 例如：在某1个点（x，y），测试手机信号的值为（sig_value),从而产生了以下的数据
# x的取值范围是：0-150
# y的取值范围是：0-30
# sig_value的取值范围是：0-100
# 注意：测试商场的30个点（也就是生成30个数据）

# 要求：1.绘制信号点到图形上（用散点图绘制）
#       2.信号>=70用绿色三角表示
#         信号在40-70之间用蓝色三角表示
#         信号小于40用红色三角表示
#       3.三角的大小用信号值的大小表示

# 生成数据
np.random.seed(40)
x_value = np.random.randint(0, 150, size=(50,))
y_value = np.random.randint(0, 30, size=(50,))
sig_value = np.random.randint(0, 100, size=(50,))
print(sig_value)
# 2.绘图
# 2-1  绘制画布
plt.figure(figsize=(12, 6), dpi=80)

# 2-2绘图

for i in range(len(sig_value)):
    if sig_value[i] < 40:
        c_value = "red"
    elif sig_value[i] < 70:
        c_value = "blue"
    else:
        c_value = "green"

    plt.scatter(x_value[i], y_value[i], c=c_value, marker="v", s=sig_value[i])  # 绘制数据点,s用来绘制点的大小

# 给图形上加数据点的值
for i in range(len(sig_value)):
    plt.annotate(xy=(x_value[i], y_value[i] + 1), s=str(sig_value[i]))

# 3.添加元素
# 3-1标题:
plt.title("商场信号图")  # 图形标题
plt.xlabel("长度")  # x轴标题
plt.ylabel("宽度")  # y轴标题

# 3-2 轴线上的刻度范围
plt.xlim((0, 150))
plt.ylim((0, 30))

# 3-3轴线上的刻度取值
plt.xticks([x for x in range(0, 150, 20)])
plt.yticks([x for x in range(0, 30, 5)])

# 3-4图例
# plt.legend(["营业额"],loc=3)

# 2-3保存图像
plt.savefig(r"信号图.jpg")

# 2-4显示图像
plt.show()

