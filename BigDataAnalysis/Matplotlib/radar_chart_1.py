# 雷达图的绘制
import matplotlib.pyplot as plt
import numpy as np


plt.rcParams['font.sans-serif'] = 'SimHei'    # 正常显示汉字
plt.rcParams['axes.unicode_minus'] = False    # 正常显示符号

p = plt.figure(figsize=(13, 6), dpi=80)

courses = ['英语', '语文', '数学']
scores = [60, 90, 30]
ax1 = p.add_subplot(121)

# 绘制到折线图上
ax1.plot(courses, scores)

# 绘制到雷达图
ax2 = p.add_subplot(122, projection="polar")     #
# ax2.plot(courses,scores)
data_len = len(scores)
# 将圆分成n等份
arr1_len = np.linspace(0,     # 第1个数据
                       2*np.pi,    # 最后1个数据
                       data_len,    # 数据个数
                       endpoint=False)   # 不包含终点

scores.append(scores[0])
arr1_len = np.append(arr1_len,arr1_len[0])  # 线条闭合
# 绘制标签
plt.thetagrids(arr1_len*180/np.pi, courses)

# 绘制图形的填充色
plt.fill(arr1_len, scores, facecolor='b', alpha=0.5)
plt.fill(arr1_len, [50, 30, 80, 70], facecolor='y', alpha=0.5)
# 绘制图形
ax2.plot(arr1_len, scores, 'rv--')
ax2.plot(arr1_len, [50, 30, 80, 70], 'gv--')

# 绘制图例和显示图形
plt.legend(['张三',"李四"])
plt.show()

