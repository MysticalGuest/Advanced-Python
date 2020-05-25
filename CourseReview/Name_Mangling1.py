class Test:
    def __init__(self):
        self.__num = 10


t = Test()
# print(t.__num)   #报错
print(t._Test__num)  #打印10
print("My dog's name is " + str(t._Test__num) + ".")


class Test:
    var01 = "我是类变量"

    def __init__(self):
        self.var02 = "我是实例变量"

    def myfunction(self):
        var03 = "我是局部变量"
        print(var03)


print(Test.var01)
t = Test()
print(t.var02)
t.myfunction()

