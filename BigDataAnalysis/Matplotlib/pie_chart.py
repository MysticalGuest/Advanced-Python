# 饼图的绘制
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']    # 正常显示汉字
plt.rcParams['font.family'] = 'SimHei'
# plt.rcParams['figure.figsize'] = (5.0, 5.0)

data_pie = np.array([1, 58, 40, 50, 89, 141])
print("data_pie", data_pie)

name_list = ['男装', "女装", "餐饮", "化妆品", "首饰"]


# 每个标签占多大，会自动去算百分比
sizes = [60, 30, 10]

# 将某部分爆炸出来， 使用括号，将第一块分割出来，数值的大小是分割出来的与其他两块的间隙
# explode=[0.04 for x in range(5)]

plt.pie(data_pie[1:],
        labels=name_list,
        autopct="%.1f",
        explode=[0.04 for x in range(5)],
        radius=1,
        shadow=True,
        labeldistance=1.3,
        pctdistance=1.1,)
# labeldistance，文本的位置离远点有多远，1.3指1.3倍半径的位置
# autopct，圆里面的文本格式，%3.1f%%表示小数有三位，整数有一位的浮点数
# shadow，饼是否有阴影
# startangle，起始角度，0，表示从0开始逆时针转，为第一块。一般选择从90度开始比较好看
# pctdistance，百分比的text离圆心的距离
# patches, l_texts, p_texts，为了得到饼图的返回值，p_texts饼图内部文本的，l_texts饼图外label的文本

plt.show()

