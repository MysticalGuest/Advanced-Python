# 饼图子图的绘制
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
plt.rcParams['font.sans-serif'] = 'SimHei'  # 正常显示汉字
plt.rcParams['axes.unicode_minus'] = False  # 正常显示符号
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
data = dic_course
# {'数据结构': {'优秀': 7, '及格': 18, '不及格': 5},
#  '线性代数': {'优秀': 9, '及格': 14, '不及格': 7},
#  '计算机编程': {'优秀': 9, '及格': 14, '不及格': 7},
#  '英语': {'优秀': 7, '及格': 20, '不及格': 3}}


# 3.绘制画布
p = plt.figure(figsize=(12, 12), dpi=80)  # 先绘制大画布
course_name_list = list(dic_course.keys())
# 划分子图1
# def my_label(pct,aa):
#     absolute = int(pct/100.*np.sum(aa))
#     return "{:.1f}%\n({:d})".format(pct,absolute)
for k in range(4):
    ax1 = p.add_subplot(2, 2, k + 1)  # 划分子图1，是2行2列图形中的第1个图
    value_dict = dic_course[course_name_list[k]]
    print(value_dict)

    data_pie = list(value_dict.values())  # 饼图的数据
    label_pie = list(value_dict.keys())  # 饼图的标签

    # 绘制图形的
    #     lambda x:my_label(x,data_pie)
    plt.pie(data_pie,
            labels=label_pie,
            autopct="%.1f%%",
            explode=[0.04 for x in range(3)],
            radius=1,
            labeldistance=1.3, pctdistance=1.1)
    print("data_pie: \n", data_pie)
    plt.xlabel(course_name_list[k])  # 添加图形x轴标题的

# #显示画布
plt.savefig(r'饼图子图绘制1.jpg')
plt.show()

