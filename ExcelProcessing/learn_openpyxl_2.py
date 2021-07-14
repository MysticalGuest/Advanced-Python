import openpyxl


# 这个类用来存储用例的
class Case:
    __slots__ = []  # 特殊的类属性，可以用来限制这个类创建的实例属性添加 可写可不写
    pass


# 读取excel数据的类
class ReadExcel(object):
    def __init__(self, file_name, sheet_name):
        """
        这个是用来初始化读取对象的
        :param file_name: 文件名 ---> str类型
        :param sheet_name: 表单名 ———> str类型
        """
        # 打开文件
        self.wb = openpyxl.load_workbook(file_name)
        # 选择表单
        self.sh = self.wb[sheet_name]

    def read_data_line(self):
        # 按行读取数据转化为列表
        rows_data = list(self.sh.rows)
        # print(rows_data)
        # 获取表单的表头信息
        titles = []
        for title in rows_data[0]:
            titles.append(title.value)
        # print(titles)
        # 定义一个空列表用来存储测试用例
        cases = []
        for case in rows_data[1:]:
            # print(case)
            data = []
            for cell in case:  # 获取一条测试用例数据
                # print(cell.value)
                data.append(cell.value)
                # print(data)
                # 判断该单元格是否为字符串，如果是字符串类型则需要使用eval();如果不是字符串类型则不需要使用eval()
                # isinstance(object, classinfo),如果对象的类型与参数二的类型（classinfo）相同则返回 True，否则返回 False
                # if isinstance(cell.value, str):
                #     data.append(eval(cell.value))
                # else:
                #     data.append(cell.value)
                # 将该条数据存放至cases中
                # print(dict(list(zip(titles,data))))
                case_data = dict(list(zip(titles, data)))
                cases.append(case_data)
        return cases


if __name__ == '__main__':
    r = ReadExcel('courses.xlsx', 'Sheet')
    data1 = r.read_data_line()
    print(data1)

