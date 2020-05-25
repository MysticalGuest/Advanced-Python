di = {"oct": 12, "nov": 8, "dec": '2'}
dic = {"s": di, "d": "er"}
print("dic", dic)
print(di)
print(di["oct"])
print(di["dec"])
for d in di:
    print("d:", d)
    print(di[d])

for item in di.items():
    print("item:", type(item))
    print("item:", item)
    print("item[0], item[1]:", item[0], item[1])

for month, temp in di.items():
    print(month, end=' ')
    print(temp)

# 请注意，键名未加引号
di1 = dict(oct=1, nov=2)
print(di1)

di2 = dict()
di2["as"] = 12
print(di2)
print("a", 'd', 'w')
print("a", 'd', 'w', end='')
print("a", 'd', 'w', sep='')
print('\'Hello\', she said.')
print("\\")

print(range(0, 5, 2))
print(range(5))
for i in range(0, 5, 2):
    print(i, end=' ')
print()
for i in range(5, 0, -1):
    print(i, end=' ')
print()
for i in range(5, 0, -2):
    print(i, end=' ')
print()
x = 0
while x < 5:
    print(x, end=' ')
    x += 1
print()
x = 0
while x < 5:
    print(x, end=' ')
    if x == 2:
        break
    x += 1
print()
x = 0
while x < 5:
    x += 1
    if x == 2:
        continue
    print(x, end=' ')



