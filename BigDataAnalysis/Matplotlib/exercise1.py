import matplotlib.pyplot as plt
import numpy as np


# 案例：某班级中有四门课程的成绩如下（30个学生):
# 数据结构：50-95
# 线性代数：45-95
# 计算机编程：50-100
# 英语：40-100
# 要求：绘制饼图显示每门课程中成绩优，及格，不及格的占比
# 优秀（成绩大于85）
# 及格（60-85）
# 不及格（小于60）

# 1.生成数据
score = dict(数据结构=np.random.randint(50, 95, size=(30,)),
             线性代数=np.random.randint(50, 95, size=(30,)),
             计算机编程=np.random.randint(50, 95, size=(30,)),
             英语=np.random.randint(50, 95, size=(30,)))
print("score: \n", score)

# 2.统计每门优秀，及格，不及格的个数
dic_course = {}  # 用来存放最后的每个课程的级别个数

for key in score.keys():  # 提取字典的键
    dic_type = {}  # 用来存放每个级别的字典
    y = 0  # 优秀的个数
    b = 0  # 不及格的个数
    j = 0  # 及格的个数

    for i in score[key]:
        if i >= 85:
            y += 1
        elif i >= 60:
            j += 1
        else:
            b += 1
    # 存放于字典中
    dic_type["优秀"] = y
    dic_type['及格'] = j
    dic_type["不及格"] = b

    # 把个数字典添加到总字典中
    dic_course[key] = dic_type

print("dic_course: /n", dic_course)  # 统计每种类型的个数结束


def my_label(pct):
    return "{:.1f}%".format(pct)


plt.pie([1, 2, 4], autopct=my_label)
plt.show()

