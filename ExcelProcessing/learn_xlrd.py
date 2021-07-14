import xlrd

data = xlrd.open_workbook("grade.xls")

table = data.sheets()[0]          # 通过索引顺序获取
# 通过索引顺序获取
# table = data.sheet_by_index(sheet_index))
# 通过名称获取
# table = data.sheet_by_name(sheet_name)
# 以上三个函数都会返回一个xlrd.sheet.Sheet()对象
# print(table)

# 返回book中所有工作表的名字
names = data.sheet_names()
print(names)
# 检查某个sheet是否导入完毕
# data.sheet_loaded(sheet_name or index)

# 获取该sheet中的有效行数
nrows = table.nrows
print(nrows)
# 返回由该行中所有的单元格对象组成的列表
for i in range(nrows):
    print(table.row(i))

# 返回由该列中所有的单元格对象组成的列表
print()
print(table.row_slice(1))

# 返回由该行中所有单元格的数据类型组成的列表
print(table.row_types(1, start_colx=0, end_colx=None))

# 返回由该行中所有单元格的数据组成的列表
print(table.row_values(1, start_colx=0, end_colx=None))

# 返回该列的有效单元格长度
print(table.row_len(0))
