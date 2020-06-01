# 关系运算符
print(34 > 43)  # False
print(3 + 4 > 4 + 3)  # False
print("9" > "10")  # True
print([1, 2, 3, 4] > [2, 2, 3, 4])  # False

# 成员测试运算符

x_list1 = []  # 声明1个空列表
for i in range(5):
    x_name = input("请输入姓名：")  # 请输入1个值
    if x_name in x_list1:  # 成员判断，如果之前已经存在，就继续输入，不添加，否则就添加
        print("您输入的用户名{},已经被占用,请重新输入".format(x_name))
        continue
    else:
        x_list1 = x_list1 + [x_name]  # 列表和列表向加
    print(x_list1)

# 集合运算符
a = {2, 3, 4, 5, 6}
b = {3, 4, 5, 7, 9}
print(a | b)  # 并集
print(a & b)  # 交集
print(a - b)  # a和b的差
print(a ^ b)  # 对称差集：去掉2个集合的公共部分，返回2个集合的剩余元素

# 逻辑运算
# 1.逻辑与运算（and)
print(1 and 0)
print(1 and 2)
print(0 and 1)

# 2.逻辑或运算（or)
print(1 or 0)
print(1 and 2)
print(0 or 1)

# 3.逻辑非运算（not）
print(not (3 > 4))

print(dir(__builtins__))

# 类型转换
s1 = "2222"
i1 = int(s1)
f1 = float(s1)
print("字符类型到整数类型：", i1, type(i1))
print("字符类型到浮点类型：", f1, type(f1))

print("十进制到二进制", bin(18))
print("十进制到八进制", oct(18))
print("十进制到十六进制", hex(13))

print("汉字'曹'的编码", ord("曹"))
print("汉字'中'的编码", ord('中'))
print("编码转换为字符", chr(26362), chr(20014))

s2 = "我喜欢你"
l2 = []
for i in s2:
    l2 = l2 + [ord(i)]
print(l2)

for j in l2:
    print(chr(j))

