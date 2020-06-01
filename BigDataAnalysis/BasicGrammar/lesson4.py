# 二、列表方法的使用
# 1.元素的添加方法
# 1-1 append：向列表的末尾追加一个元素
name_list = ['X', 'M', 'J']
print("请输入姓名，输入0时退出输入")
name_list2 = []
while True:
    name = input("请输入姓名：")
    if name == "0":
        break
    else:
        name_list2.insert(0, name)
print(name_list2)

# 1-3两个列表的链接
name_list.extend(name_list2)
print("连接后：", name_list)

# 2.列表元素的删除
# 2-1 pop   pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
l2 = [1, 2, 3, 4, 5]
# del_list = []
l2_len = len(l2)
# for i in range(l2_len):
#     del_list.append(l2.pop(-1))

del_list = [l2.pop(-1) for i in range(l2_len)]
print(del_list)
print("删除后：", l2)

# 3.列表的其它方法
# 3-1 index  count
l3 = [1, 2, 2, 2, 2, 3, 4, 4, 5, 5, 5, 9, 66, 6, 7, 9, 7, 8, 8, 0, 0, 0]

ele_value = []  # 元素列表
loc_value = []  # 位置列表
cou_value = []  # 元素个数
for i in l3:
    if i in ele_value:
        continue
    else:
        ele_value.append(i)
        loc_value.append(l3.index(i))
        cou_value.append(l3.count(i))   # count() 方法返回具有指定值的元素数量

print("元素列表：{}\n对应的位置列表：{}".format(ele_value, loc_value))

"""
zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表
"""
zip_list = zip(ele_value, loc_value, cou_value)

print("zip对象：", zip(ele_value, loc_value, cou_value))
print("zip：", zip_list)
print(list(zip_list))

# 4排序和逆序    list.sort( key=None, reverse=False)
l4 = [1, 2, 4, 5, 66, 7, 8]
l4.sort(key=str)
print("(key=str): ", str)
print("l4.sort(key=str): ", l4)
l4.reverse()
print("l4.reverse(): ", l4)
l4.sort()
print("l4.sort(): ", l4)

# 输出100之间能被3和5整除的数:for方法
l5 = []
for i in range(1, 101, 1):
    if i % 3 == 0 and i % 5 == 0:
        l5.append(i)
print(l5)

# 列表推导式方法
l6 = [str(i) for i in range(1, 101, 1) if i % 3 == 0 and i % 5 == 0]
print(l6)

data = ["{} * {} = {}".format(x, y, x * y) for x in range(1, 10, 1) for y in range(1, x, 1)]
print(data)

# 字典的操作：点菜程序
menu_dic = {"凉菜": {"拍黄瓜": "10元", "火山飘雪": "12元"},
            "素菜": {'红烧茄子': "20元", "土豆丝": "21元"},
            "荤菜": {"红烧猪蹄": "25元", "土豆烧牛腩": "30元"}}

# menu_dic.keys()
# menu_dic.values()
# menu_dic.items()
# menu_dic.get("素菜")
# 第1层选择
print("请输入您的操作选择：\n1.点菜 \n2.修改菜单 0.退出")
while True:
    sel_val1 = input("请输入您的操作选择：")
    if sel_val1 == "1":

        # 第2层选择
        print("请选择您要的种类：\n1.凉菜   \n2.素材  \n3.荤菜 \n0.退出")
        print("=" * 40)
        while True:

            # 第3层选择
            sel_val = input("请输入您的选择：")
            if sel_val == "1":
                print((menu_dic.get("凉菜").values()))
            elif sel_val == "2":
                print(menu_dic.get("素菜").keys())
            elif sel_val == "3":
                print(menu_dic.get("荤菜"))
            elif sel_val == "0":
                print("谢谢您的光临！")
                break
            else:
                print("没有您选择菜品")

    elif sel_val1 == "2":
        # 第2层选择
        print("请输入你要进行的操作：\n1.添加或修改  \n2.删除")

        while True:
            # 第3层选择
            sel_val2 = input("请输入您的操作")
            put_key = input("请输入您要修改的菜名")
            put_valu = input("请输入您要修改的价格")
            if sel_val2 == "1":
                menu_dic.get("凉菜")[put_key] = put_valu
            elif sel_val2 == "2":
                pass
                # 学生自己完成
            elif sel_val2 == "0":
                print("欢迎您光临！")
                break
            else:
                print("请重新选择")
        print(menu_dic)
    elif sel_val1 == "0":
        break
    else:
        print("请重新选择")

dic1 = {'拍黄瓜': '20元', '火山飘雪': '12元'}
dic2 = {'拍黄瓜': '30元', '火山飘雪': '12元', '红烧茄子': '20元'}
dic1.update(dic2)
print("dic1: ", dic1)

# 集合的操作
set1 = {1, 2, 3, 4, 5, 6, 6, 5, 4, 6, 7}
print(set1)
set2 = {1, 9, 8, 0, 2}
print(set2)

set1.update(set2)
print(set1)
set1.remove(0)

# 字符串的操作
# 1.编码和解码
s1 = "我好饿！"
print(s1.encode("utf-8"))  # 1个汉字3个字节码
print(s1.encode("gbk"))  # 1个汉字2个字节码 GB-2312，CP936

print(b'\xe6\x88\x91\xe5\xa5\xbd'.decode("utf-8"))

# 2.索引和个数
s2 = "风声雨声读书声，家事国事天下事"
s2.count("声")
s2.index("声")

# 3.替换
# 3-1  replace
s3 = "风声雨声读书声，家事国事天下事"
s4 = s3.replace("声", '点').replace("事", "理")
print(s3, "\n", s4)

# 3-2  maketrans和translate
table = "".maketrans("1234567890", "abcdefghij")
table2 = "".maketrans("我你它们", "好坏美丑")
print("tel:13488279155".translate(table))
print("我们是它们".translate(table2))

print("4.排版".ljust(40, "="))
print("我要靠左".ljust(30) + "结束")
print("我要靠右".rjust(30) + "结束")
print("我要居中".center(30) + "结束")

print("5.字符串的拆分".ljust(40, "="))
soc_s = "曹晓龙|28|男|计算机#刘备|28|男|计算机#曹操|28|男|计算机#李宇春|28|男|计算机"
soc_list = soc_s.split("#")
data = [i.split("|") for i in soc_list]
print(data)

print("5.字符串的连接".ljust(40, "="))
l3 = [12, 34, 56, 98, 76]
"|".join([str(x) for x in l3])

print("6.清除字符串两边的内容".ljust(40, "="))
s5 = "     ###这是我今天的作业###      "
s5.strip(" ").strip("#")  # 先删除空格，再删除井号

print("7.英文字母大小写方法".ljust(40, "="))
s6 = "i AM  from  china. i AM  from  china!"
print(s6.lower())
print(s6.upper())

# 功能：录入成绩，并判断等级
print("程序控制语句1：分支结构".ljust(40, "="))
print("成绩的等级判断".ljust(40, "="))
print("0-60  不及格\n60-75  及格    \n75-90   良好   \n90-100  优秀")


# 录入信息函数
def input_def():
    # 输入阶段
    print("=".ljust(30, "="))
    stu_id = input("请输入学号")
    if stu_id == "-1":
        return ((stu_id))
    stu_name = input("请输入姓名")
    stu_score = float(input("请输入成绩："))
    return (stu_id, stu_name, stu_score)


def rank_def(stu_score):
    stu_rank = ""
    # 判断等级

    if stu_score < 60:
        stu_rank = "不及格"

    elif stu_score < 75:
        stu_rank = "及格"

    elif stu_score < 90:
        stu_rank = "良好"

    elif stu_score < 100:
        stu_rank = "优秀"

    else:
        print("您的成绩不正常！")
    print("您的成绩是：{},等级是：{}".format(stu_score, stu_rank))
    return stu_rank


# def info_def(info_value):
#     stu_info = {}  # 最外层字典
#     # 形成字典的代码
#     info_value["姓名"] = stu_name
#     info_value["成绩"] = stu_score
#     info_value["等级"] = stu_rank
#     stu_info[stu_id] = info_value
#     print(stu_info)


def main():
    print("请输入您的信息：\n 学号输入'-1'的时候退出")
    info_value = {}
    while True:
        info_list = [input_def()]  # 录入函数
        print(info_list)
        if info_list[0] == "-1":
            break
        stu_rank = rank_def(info_list[0][2])  # 判断等级函数
        print(stu_rank)
        # 由学生来完成，形成字典的函数
        # info_def(info_list.append(stu_rank))  #形成字典函数
    print(info_list)


if __name__ == "__main__":
    main()
# {"1001":{"姓名":"刘德华","成绩":70,"等级":'及格'}，1002":{"姓名":"刘德华","成绩":70,"等级":'及格'}}

