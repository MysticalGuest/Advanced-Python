# 以下是整数类型的书写方式
print("十进制数值的写法:", 234)
print("八进制数值的写法:", 0o234)
print("十六进制数值的写法:", 0x234)
print("二进制数值的写法:", 0b010101)


# 复数的书写方式--了解即可
c = 3+4j
print("复数的写法", c)
print("复数的实部", c.real)
print("复数的虚部", c.imag)
print("复数的模", abs(c))

# Python中各种容器对象的书写方式
x_list = [1, 2, 3, 4, 5]  # 列表的书写方式
print("列表的书写方式", x_list)

x_tuple = (1, 2, 3, 4, 5)  # 元组的书写方式
print("列表的书写方式", x_tuple)

x_dict = {"西红柿鸡蛋": "20元", "凉拌黄瓜": "12元"}  # 字典的书写方式
print("字典的书写方式", x_dict)

x_set = {'a', 'b', 'c', 'd', 'd', 'c'}  # 集合的书写方式
print("集合的书写方式", x_set)

# 字符串的书写方式
x_str1 = '这是字符串的书写方式：用单引号括住'
x_str2 = "这是字符串的书写方式：\
用双引号括住"
x_str3 = '''
学习就怕满，懒，难
心里有了满，懒，难，不看不钻就不前。
心里去掉满，懒，难，边学边干，蚂蚁也能爬泰山。
'''
print(x_str1)
print(x_str2)
print(x_str3)

# 转义字符的书写
print("转义字符回车的书写：\n就是用斜杆+字符组成转义字符")
print("转义字符制表符的书写：\n姓名\t性别\t年龄\t\n曹晓龙\t男\t25")

# 让转义字符符号斜杆“\”原样输出的方法:在字符串前加“r”即可
print("让'\\'原样输出", r"C:\Users\kitty-peter\Desktop")

# 运算符和表达式
# 1.加号运算
print("整数加法:", 3 + 4)
name = "曹晓龙"
print("字符串加法\n:", "我的名字是：" + name)
print("列表的加法：", [1, 2, 3] + ['a', 'b', 'c'])
print("元组的加法：", (1, 2, 3) + ('a', 'b', 'c'))
# 不能进行加法操作
# print("字典的加法：",{'a':1,'b':2}+{"c":3,"d":4})
# print("集合的加法：",{1,2,3,4}+{1,2,3,5})

# 2.减号运算
print("数值的加法：", 5 - 4)
print("集合的加法：", {1, 2, 3, 4} - {1, 2, 3, 5})  # 计算集合的差集

# 3.乘法运算
print("字符的乘法：", "一定记得写报告" * 3)
print("数值的乘法:", 4.5 * 3)
print("列表的乘法：", ['I love you'] * 3)
print("元组的乘法：", ('重要的事情说3遍',) * 3)  # 元组中只有1个值时，必须在后面跟上逗号，否则就认为它的值为字符串

# 4.除和整除运算//
print("除运算：", 23 / 4)
print("整除运算：", 23 // 4)

# 5.求余运算
print("求余运算：", 17 % 4)

# 6.幂运算
print("幂运算：", 3 ** 5)

# 基本的输入输出命令
# 1.输入命令
name = input("请输入您的姓名：")
age = input("请输入您的年龄：")

print("您输入的姓名是", name, sep='：', end="\t")
print("您输入的年龄是", age, sep="：")

for i in range(10):
    print(i, end="\t")

for name in ['曹操', '刘备', '诸葛孔明']:
    print(name, end="\t")

# 九九乘法表
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    for j in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        # print(i,"*",j,"=",i*j,end="  ")
        # print("%d*%d=%d"%(i,j,i*j),end="  ")      #%格式输出
        print("{}*{}={}".format(i, j, i * j), end="  ")
    print()

name = "jone"
age = 23
print("我的名字是：%s;我的年龄是：%d" % (name, age))
print("我的名字时：{1};我的年龄时：{0}".format(age, name))

r = input("请输入半径：")
print(int(r) * 3)

print(r"C:\Users\kitty-peter\Desktop")
