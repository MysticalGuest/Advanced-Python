# 绘制三维图形--子图
import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif'] = 'SimHei'    # 正常显示汉字
plt.rcParams['axes.unicode_minus'] = False    # 正常显示符号

# 声明要绘制三维图形

fig = plt.figure(figsize=(15, 15), dpi=80)

# 绘制三维折线图
ax1 = plt.subplot(231, projection='3d')

test_data = np.linspace(-4 * np.pi, 4 * np.pi, 100)  # 测试数据

z = np.linspace(-4, 4, 100) * 0.3
r = z ** 4 + 1
x = r * np.sin(test_data)
y = r * np.cos(test_data)
ax1.plot(x, y, z, 'rv--')

# 绘制三维柱状图
ax2 = plt.subplot(232, projection='3d')

x = np.random.randint(20, 80, size=(10))
y = np.random.randint(0, 50, size=(10))
z = np.random.randint(10, 90, size=(10))

ax2.bar3d(x, y, z, dx=1, dy=1, dz=z, color='r')  # 绘制三维柱形图

ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('z')

# 绘制三维柱状图
ax3 = plt.subplot(233, projection='3d')

# 生成数据
# np.random.seed(40)
x = np.random.randint(0, 150, size=(50,))
y = np.random.randint(0, 30, size=(50,))
z = np.random.randint(0, 100, size=(50,))
print(z)
for i in range(len(z)):
    c_value = 'r'
    if z[i] < 40:
        c_value = "r"
    elif z[i] < 70:
        c_value = "b"
    else:
        c_value = "g"
    ax3.scatter(x[i], y[i], z[i], c=c_value, marker="*", s=z[i])  # 绘制三维柱形图

ax3.set_xlabel('x')
ax3.set_ylabel('y')
ax3.set_zlabel('z')

ax4 = plt.subplot(212)
np.random.seed(40)
x_value = np.random.randint(0, 150, size=(50,))
y_value = np.random.randint(0, 30, size=(50,))
sig_value = np.random.randint(0, 100, size=(50,))
print(sig_value)
# 2.绘图
# 2-1  绘制画布
# plt.figure(figsize=(12,6),dpi = 80)

# 2-2绘图

for i in range(len(sig_value)):
    if sig_value[i] < 40:
        c_value = "red"
    elif sig_value[i] < 70:
        c_value = "blue"
    else:
        c_value = "green"

    ax4.scatter(x_value[i], y_value[i], c=c_value, marker="*", s=sig_value[i])  # 绘制数据点,s用来绘制点的大小

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

plt.savefig(r"三维-子图.jpg")
plt.show()

