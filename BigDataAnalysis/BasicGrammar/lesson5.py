# 1.函数传参
# 1-1位置传参


def add_def(a, b):
    print("函数中a={}和b={}".format(a, b))
    return a + b


# c = add_def(10,20)
# print(c)

# 1-2默认值参数
def add_def1(a, d, b=20):
    print("函数中a={}和b={}".format(a, b))
    return a + b + d


c = add_def1(10, 30, 40)
print(c)


# 1-3关键字传参
def add_def2(a, d, b=20):
    print("函数中a={}和b={}".format(a, b))
    return a + b + d


c = add_def2(d=10, a=30, b=40)
print(c)


# 1-4可变长度传参--星号元组传参
def add_def3(a, b, *args):
    print("函数中a={}和b={}".format(a, b))
    print("函数中args={}".format(args))
    # l_args = [x for x in args]
    return a + b, sum(args)


# c = add_def3(10,20,30,40,50,60,70,70)
print(c)


# 1-5可变长度传参--双星号关键字传参
def add_def4(a, b, **kwargs):
    print("函数中a={}和b={}".format(a, b))
    print("函数中kwargs={}".format(kwargs))
    # l_args = [x for x in args]
    return a + b, sum(kwargs.values())


# c = add_def4(10,20,x=30,y=40,z=50,w=60,s=70,h=70)
# print(c)

# 1-6混合传参
def add_def5(a, b, d=50, *args, **kwargs):
    print("函数中a={}和b={}".format(a, b))
    print("函数中kwargs={}".format(kwargs))
    l_args = [x for x in args]
    print(d)
    print(l_args)
    print(kwargs)

    return a + b, sum(kwargs.values())


c = add_def5(10, 20, 30, 40, 506, 80, x=30, y=40, z=50, w=60, s=70, h=70)
print(c)

# 2.lambda表达式
# 2-1  排序方法sort
l2 = [12, 345, 6789, 100, 32, 97]

l2.sort()  # 按数字大小排序，方法
l2
l2.sort(key=lambda x: str(x))  # 把数字转换为字符串后，排序
l2

# 2-2 最大值函数
max(l2)
max(l2, key=lambda x: str(x)[1])

# 2-3 像使用普通函数一样使用
chu_def = lambda x, y: x / y
print(chu_def(12, 3))

# 3.标准库的使用--系统库sys的使用
import sys

print(sys.platform)  # 系统平台
# print(sys.exit("我退出了"))      #退出应用程序
print(sys.getdefaultencoding())  # 获取当前系统编码

# 标准库--系统平台库platform
import platform

print(platform.platform())  # 系统版本号
print(platform.system())  # 系统类型
print(platform.uname())

# 标准库--数学库math
import math

print(math.fmod(17, 3))  # 求余数
print(math.pow(3, 4))  # x的y次方
print(math.pi)  # pi的值
# help(math)


# 标准库--随机库random
import random  # 随机库

print(random.random())  # 返回0到1之间的1个随机浮点数
print(random.randint(10, 100))  # 返回10到100直接的一个随机整数
print(random.choice([2, 3, 4, 5, 6, 7]))  # 返回列表中的一个随机数

l3 = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(l3)  # 将列表打乱顺序
l3

random.sample(l3, 3)  # 从列表中，获取指定个数的值，从l3中获取3个值

# 标准库：时间库time
import time  # 时间库

print(time.time())  # 获取时间戳
print(time.localtime(time.time()))  # 关键字时间
print(type(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))))  # 格式化输出时间
time.sleep(3)
print(time.ctime())


# 斗地主游戏发牌
# print(chr(0x2665))    红桃
# print(chr(0x2663))    梅花
# print(chr(0x2660))    黑桃
# print(type(chr(0x25c6)))    方框
# 函数1：生成牌函数
def get_puke():
    l1 = [str(x) for x in range(2, 11)]
    l2 = ["A", "J", "Q", "K"]
    l3 = ["大王", '小王']
    l4 = [chr(0x2665), chr(0x2663), chr(0x2660), chr(0x25c6)]
    puke = []
    for i in l4:
        for j in (l1 + l2):
            puke.append(i + j)
    puke.extend(l3)  # extend没有返回值。
    return puke


# 函数2：发牌函数
def out_puke(puke):
    import random
    random.shuffle(puke)
    person1 = puke[0:17:1]  # 0-16
    person2 = puke[17:34:1]  # 17-33
    person3 = puke[34:51:1]  # 34-51
    bottom = puke[51:]
    return (person1, person2, person3, bottom)


# 函数3：游戏规则
def rule_puke():
    pass


# 函数4：整理牌

# 主函数
def main():
    puke = get_puke()
    print(len(puke))
    ok_puke = out_puke(puke)
    print(ok_puke[0])
    return ok_puke[0]


# 入口
if __name__ == "__main__":
    per1 = main()
per1

per1.sort()
print(per1)

# 文件操作
# 方法1：open
f1 = open("test1.txt", 'a')
while True:
    name = input("请输入姓名")

    if name == "0":
        break
    score = input("请输入成绩")
    f1.writelines({name: score})
f1.close()

# 用raadline读取文件
f2 = open('test1.txt', 'r')
# f2.read(8)
import time

while True:
    str1 = f2.readline()
    if not str1:
        break

    time.sleep(0.3)
    print(str1)
f2.close()

# 用in方法读取文件
f3 = open('test1.txt', 'r')
# f2.read(8)
for i in f3:
    print(i)
f3.close()

# 关于csv文件的操作
from csv import writer, reader
from random import randint
from datetime import date, timedelta

with open("test2.csv", "w", newline="") as fp:
    wr = writer(fp)
    # 写入表头
    wr.writerow(["日期", "销量"])  # 写入列标题
    start_date = date(2020, 5, 1)
    for i in range(100):
        amount = 500 + i * 5 + random.randint(50, 100)
        wr.writerow([str(start_date), amount])  # 写入数据
        start_date = start_date + timedelta(days=1)

with open("test2.csv", 'r') as pf1:
    for line in reader(pf1):  # 按行读取文件数据
        print(line)

# 写入字典数据到csv中
from csv import writer, reader

l1 = [{"name": "aaa", "age": 34}, {"name": "bbb", "age": 34}]
with open("test3.csv", 'w', newline="") as pf2:
    wt = writer(pf2)
    wt.writerow(["name", 'age'])  # 写入列标题
    for i in l1:
        wt.writerow(i.values())  # 写入字典的值

