# 列表解析
l1 = [number for number in range(1, 6)]
print("l1", l1)

l2 = [number-1 for number in l1]
print("l2", l2)

l3 = [number * number + 1 for number in l2]
print("l3", l3)

l4 = [number for number in l1 if number % 2 == 1]
print("l4 " + str(l4))

rows = range(1, 4)
cols = range(1, 3)
cells = [[row, col] for row in rows for col in cols]
print("cells", cells)

rows1 = range(1, 13)
cols1 = range(1, 7)
cells1 = [[row, col] for row in rows1 if row % 3 == 0
          for col in cols1 if col % 2 == 0]
print("cells1", cells1)

# p377

