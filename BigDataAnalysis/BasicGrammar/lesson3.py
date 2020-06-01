# 类型转换函数2
print(list(), tuple(), dict(), set())  # 每种类型的空值表示方法

s = {4, 6, 7, 8}
l_data = list(s)  # 转换为列表
print("转换为列表: ", l_data)

t_data = tuple(s)  # 转换为元组
print("转换为元组: ", t_data)

d_data = dict(name="曹晓龙", age=24, sex="man")  # 转换为字典
print("转换为字典: ", d_data)

l_data2 = l_data * 2
print("l_data2 = l_data * 2: ", l_data2)

s_data = set(l_data2)  # 转换为集合
print("转换为集合: ", s_data)

# 类型转换函数3：eval（）
print("3+4+5")  # 字符串，原样输出
print(eval("3+4+5"))  # 通过eval，将字符串转换为它原来的功能：求和

print(eval("0o345"))

# 最大值，最小值
data = [3, 18, 188]
print(max(data))  # 返回最大值

print(max(data, key=str))  # 使用str将data中的值，转换为字符串后，再进行比较

data2 = ['aa', 'bbb', 'ccc', 'aaaa']
print(max(data2, key=len))  # 使用len将data2中的值，求出其长度，然后比较长度的大小

# 元素数量，求和函数
print(len(data))
print(sum(data))

# 排序函数
print(sorted(data))  # 升序排序
print(sorted(data, reverse=True, key=str))  # 逆序排序

print(range(1, 10, 1))  # 生成range对象

print(list(range(1, 10, 1)))  # 将range对象转换为列表
print(tuple(range(1, 10, 1)))  # 转换为元组
print(set(range(1, 10, 1)))  # 转换为集合

# zip()函数的使用
# 声明数据
name = ['曹操', '刘备', '诸葛亮', '李世民']
tel = ["11111", '222222', '333333', '444444']

# 转换为zip对象
data = zip(name, tel)
print(data)

# 用for循环将zip对象迭代出来
list_value = list()
for item in data:
    list_value = list_value + [item]
print(list_value)

# 将迭代出来的列表转换为字典
dict_value = dict(list_value)
print(dict_value)

# zip()函数的练习
# 1.获取需要转换为字典的数据
pro_name = ["陕西", "山西", "北京"]
pro_code = ["6100", "4100", "1000"]

# 2.用zip函数转换为元组
name_code = zip(pro_name, pro_code)

# 3.用for循环迭代出zip中的内容,放到列表list_value
list_value = []
for item in name_code:
    list_value = list_value + [item]

# 4.将包含元组对象的列表list_value，转换为字典dict_value
dict_value = dict(list_value)
print(dict_value)
dict(zip(pro_name, pro_code))

# zip（）的特点
pro_name = ["陕西", "山西", "北京"]
pro_code = ["6100", "4100", "1000"]
zip_data = zip(pro_name, pro_code)
list_value1 = list(zip_data)  # 第1次取zip的值，是有值的。
print(list_value1)

tuple_values = tuple(zip_data)  # 第2次取zip的值，zip就是空的
print(tuple_values)

# enumerate()
list_value2 = ["陕西", "山西", "北京"]
print(list(enumerate(list_value2, start=1)))

# map()
map_list = [13, 24, 45, 356, 67]
print(list(map(str, map_list)))

map_list2 = list(map(str, map_list))
print(list(map(len, map_list2)))

# 访问列表对象
# 方法1：索引方法
data2 = list(range(1, 30, 2))
print(data2)

print(type(data2[1]))  # 正向索引

print(data2[-1])  # 逆向索引

# print(data2[20])      #索引超出范围，有IndexError索引溢出错误

# 方法2：切片方法
print(data2[::])  # 三个参数全部省略

print(data2[3:])  # 从第4个元素开始取，取到末尾

print(data2[1::2])  # 从第2个元素开始取，取到末尾，只取索引下标为奇数的值。

print(data2[-4:])  # 取最后的4个元素

print(data2[-1::-1])  # 逆向输出列表

data3 = data2[3:]
data2[6:7] = [30]  # 替换列表中第7个元素为30
print(data2)
data2[2:2] = [40, 50]  # 在第2和第3个元素之间，插入两个值
print(data2)
data2[1:4] = []  # 删除第2到第4个元素

print(data2)

for i in range(1, 10):
    for j in range(1, i + 1):
        print("{}*{}={}".format(j, i, j * i), end='\t')
    print()

