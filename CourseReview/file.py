f = open("text.txt", 'r')

# for line in f:
#     print(line, end='')
first = f.readlines()
print(f)
print(type(first))
print(first)

f.close()

f = open("text.txt", 'a')
f.write("wewe")

f.close()

