# % matplotlib notebook
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation  # 动画绘图库
# from IPython.display import HTML  # HTML中显示动画

fig = plt.figure(figsize=(8, 6), dpi=60)
ax1 = fig.add_subplot(111)
x = list(np.arange(1, 4))
y = [[2, 6, 5], [4, 7, 8], [9, 8, 3], [2, 3, 5]]


def update(num):
    ax1.clear()
    color_v = "rbyg"
    ax1.barh(x, y[num], color=color_v[num])
    return ax1,


ani = animation.FuncAnimation(fig, update,
                              frames=np.arange(4),
                              interval=500,  # 这里的frames在调用update函数是会将frames作为实参传递给“n”
                              blit=True, repeat=True)
plt.show()

x = np.arange(1, 13)
y = np.random.randint(10, 30, 12)
print("x: ", x)
print("y: ", y)

color_v = "rby"
print(type(color_v[1]))

