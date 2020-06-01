#  练习1：输入任意的一段文字(包含：汉字，英文大写字母，英文小写字母，其它字符）。
#     要求：将四类字符分别保存到四个列表中；

word = "今天天气真好，有30摄氏度心情不错，Very Happy！"

lower_case = []
capital = []
han_zi = []
qi_ta = []
for i in word:
    if i >= "a" and i <= "z":
        lower_case += i
    elif i >= "A" and i <= "Z":
        capital += i
    elif ord(i) >= 0x4e00 & ord(i) <= 0x9fa5:
        han_zi += i
    else:
        qi_ta += i
print("汉字：{}\n英文小写：{}\n英文大写:{}\n其它：{}".format(han_zi, lower_case, capital, qi_ta))


"""练习2：输入一个字符串，输出加密后的字符串。
要求：每个字符的编码和下一个字符的编码相减，用这个差的绝对值作为加密编码；加密编码对应的字符作为当前位置上的加密结果。
（注意：最后1个字符和第1个字符进行运算）
            “有间谍”
"""

"""
ord()函数，ord('c'),return 99
以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值;
如果所给的 Unicode 字符超出了你的 Python 定义范围，则会引发一个 TypeError 的异常.
"""
# abs() 函数返回数字的绝对值
# chr() 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符
word2 = "输入一个字符串"
sic = ""
for j in range(len(word2)):
    if j == (len(word2) - 1):
        print(word2[j])
        sic += chr(abs(ord(word2[j]) - ord(word2[0])))
    else:
        print(word2[j])
        sic += chr(abs(ord(word2[j]) - ord(word2[j + 1])))
print(sic)

# 二、列表方法的使用
# 1.元素的添加方法
# 1-1 append：向列表的末尾追加一个元素
print("请输入姓名，输入0时退出输入")
name_list = []
while True:
    name = input("请输入姓名：")
    if name == "0":
        break
    else:
        name_list.insert(0, name)
print(name_list)