class Staff:
    def __init__(self, p_position, p_name, p_pay):
        self.position = p_position
        self.name = p_name
        self.pay = p_pay
        print('Creating Staff object')

    def __str__(self):
        return ('Position = %s, Name = %s, Pay = %d' %
                (self.position, self.name, self.pay))

    def calculate_pay(self):
        prompt = '\nEnter number of hours worked for %s: ' % self.name
        hours = input(prompt)
        prompt2 = '\nEnter the hourly rate for %s in yuan: ' % self.name
        hourly_rate = input(prompt2)
        self.pay = int(hours) * int(hourly_rate)
        return self


s = Staff("Basic", 'Juan', 0)
print(s.name)
print(s.position)
s.calculate_pay()
print(s.pay)
print(s)

