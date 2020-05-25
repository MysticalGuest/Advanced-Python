# slice
li = [1, 2, 3, 4, 5, 6, 7]
print(li[2:-1])

# stepper
print(li[0:5:2])

# Slice Defaults
print(li[2:])
print(li[:-2])

# Modify, Append Elements
li.append(8)
print("li after append", li)

li += [9]
print("li after plus", li)

# Delete Elements
del li[4]
print("li after delete", li)


