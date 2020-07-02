import pandas as pd


# 3.数据清洗
# 3-1  重复值的检测和处理
detail1 = pd.read_csv("meal_order_detail1.csv", sep=",", encoding="utf-8")
print("detail1: \n", detail1)

print("detail1['dishes_name'].describe(): \n", detail1['dishes_name'].describe())

# 去重方法1：分组方法
list(detail1.groupby('dishes_name', sort=False)['dishes_name'].describe().index)

# 去重方法2：列表方法


def del_rep(list1):
    list2 = []   # 存放去重后的结果
    for i in list1:
        if i not in list2:
            list2.append(i)
    return list2


name_list = list(detail1['dishes_name'])
print("len(name_list): ", len(name_list))
resu_list = del_rep(name_list)
print("len(resu_list): ", len(resu_list))
print("列表去重后的结果\n", resu_list)

# 去重方法3：集合方法
resu_list2 = set(name_list)
print("集合去重后的结果\n", resu_list2)

# 去重方法4：pandas方法
print(type(detail1['dishes_name'].drop_duplicates()))     # 去重之后得到的是一个Series，把对应的索引也取出了。
index1 = detail1['dishes_name'].drop_duplicates(keep='first').index    # 得到取出结果的索引index
print(detail1.loc[index1, :].shape)     # 用索引取df的所有值

# 去食堂吃饭，10个人都要了烤肉   ：只出现烤肉一条信息
# 取每个订单中的烤肉
# 有10条烤肉信息

# 3-2


def put_data_def(file_name):
    pd.set_option('display.unicode.ambiguous_as_wide', True)
    pd.set_option('display.unicode.east_asian_width', True)
    print("1.csv文件 \n 2.excel文件\n")
    type_v1 = input("请输入您要打开的文件类型：")
    if type_v1 == "1":
        df_csv = pd.read_csv("{}.csv".format(file_name, sep=","))
        return df_csv
    elif type_v1 == "2":
        df_excel = pd.read_excel("{}.xlsx".format(file_name))
        return df_excel


df_excel = put_data_def("超市营业额")
print("原始数据：\n", df_excel)
print("原来数据的形状：\n", df_excel.shape)
print("删除重复值后的形状：\n", df_excel.drop_duplicates().shape)
# 找出重复值是哪一行
print("重复的一行", df_excel[df_excel.duplicated() == True])


