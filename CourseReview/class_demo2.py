class Staff:
    def __init__(self, p_position, p_name, p_pay):
        self._position = p_position
        self.name = p_name
        self.pay = p_pay
        print('Creating Staff object')

    def __str__(self):
        return ('Position = %s, Name = %s, Pay = %d' %
                (self._position, self.name, self.pay))

    def calculate_pay(self):
        prompt = '\nEnter number of hours worked for %s: ' % self.name
        hours = input(prompt)
        prompt2 = '\nEnter the hourly rate for %s in yuan: ' % self.name
        hourly_rate = input(prompt2)
        self.pay = int(hours) * int(hourly_rate)
        return self

    @property  # 这个修饰符将position方法改变为属性
    def position(self):
        print('Getter method')
        return self._position

    @position.setter  # 这个修饰符的作用是；
    # 当属性position发生改变时，position方法被调用
    def position(self, value):
        # 该方法会对输入的新值进行测试
        if value == 'Manager' or value == 'Basic':
            self._position = value
        else:
            print('Position is invalid.No chages made.')


s = Staff("Basic", 'Juan', 0)
print(s.name)
print(s.position)  # 会调用position方法获取值
s.position = "CEO"  # 使用position属性更新_position的值时，应该使用position()方法更新值
# s.calculate_pay()
# print(s.pay)
print(s)

