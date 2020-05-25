def change(x):
    x = 3


def change2(x):
    x[0] = 100


y = 1
change(y)
print(y)

w = [1, 2, 3]
change2(w)
print(w)
