"""
练习1：进制转换计算程序
   要求：
    1.输入1个需要转换的十进制数字x
    2.再输入一个需要转换成的进制编号 y
        当输入y为2时，将x转换为二进制
        当输入y为8时，将x转换为八进制
        当输入y为16时，将x转换为十六进制
"""


# 进制转换代码
for i in [1, 2, 3, 4, 5]:
    shi_num = int(input('请输入十进制数字'))
    print("2:十到二的转换\n8:十到八的转换\n16:十到十六的转换")     # 提示语句
    code_num = input("请输入转换成的进制编号")

    res_num = ""    # 存放转换后的结果
    if code_num == '2':
        res_num = str(bin(shi_num))
    elif code_num == '8':
        res_num = str(oct(shi_num))
    elif code_num == '16':
        res_num = str(hex(shi_num))
    else:
        print("您输入的进制编号不存在")
        continue
    print("您输入的数字：{}；转换为{}进制的结果是：{}".format(shi_num, code_num, res_num))

# 进制转换代码
while True:
    print("\n\n" + "-" * 30)
    print("2:十到二的转换\n8:十到八的转换\n16:十到十六的转换\n0:结束程序")  # 提示语句
    print("-" * 30)
    code_num = input("请输入转换成的进制编号")

    if code_num == '0':  # 当输入0时，退出程序
        break
    shi_num = int(input('请输入十进制数字'))
    res_num = ""  # 存放转换后的结果

    # 开始进制转换
    if code_num == '2':
        res_num = str(bin(shi_num))
    elif code_num == '8':
        res_num = str(oct(shi_num))
    elif code_num == '16':
        res_num = str(hex(shi_num))
    else:
        print("您输入的进制编号不存在")
        continue
    print("您输入的数字：{}；转换为{}进制的结果是：{}".format(shi_num, code_num, res_num))

''' 练习2：进行汉字编码转换
要求:1.输入1段汉字x_str2，将其转换为unicode编码，放到列表x_list3中
'''
str_value = input("请输入您要转换编码的字符串：")

# 将字符串转换为编码
x_list3 = []
for i in str_value:
    x_list3 = x_list3 + [ord(i)]
print("将字符串转换为编码的结果:", x_list3)

# 将编码转换为字符串
x_str3 = ""
for j in x_list3:
    x_str3 = x_str3 + chr(j)
print("将编码转换为字符串的结果：", x_str3)

