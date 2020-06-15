# 案例：绘制正弦和余弦曲线，把两个子图的图例显示在一起，并显示于子图之外。
import matplotlib.pyplot as plt
import numpy as np


x = np.arange(0, 2*np.pi, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

fig = plt.figure(figsize=(8, 8), dpi=80)
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
pic1, = ax1.plot(x, y1, 'r--')     # 将绘制的图形赋予变量pic1，但后面的逗号一定要有，表面它是元组

pic2, = ax2.plot(x, y2, 'b-.')

# 图例的设置
plt.legend([pic1,pic2], ['sin',"cos"], loc="upper right", bbox_to_anchor=(1, 2.5))
plt.show()

