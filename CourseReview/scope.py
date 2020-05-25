message1 = "Global"

def my_function():
    message2 = "Local"
    print(message1)
    print(message2)


my_function()
try:
    print(message2)
except Exception as e:
    print(e)


def some(a, b, c=1, d=2, f=3):
    print(a, b, c, d, f)


some(9, 0)
some(9, 0, 8)
try:
    some(9, 0, 8, 7, 6, 5)
except Exception as e:
    print(e)


def add(*num):
    sum = 0
    print(type(num))
    print(num)
    for i in num:
        sum += 1
    print(sum)


add(2)
add(1, 2, 3, 4, 5, 6, 7, 8, 9)


def print_member_age(**age):
    for i, j in age.items():
        print('Name = ', i, ', Age = ', j, sep='')
# Note use of sep=''.


print_member_age(bo=12, cd=23)

