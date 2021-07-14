import openpyxl


class MyReadExcel(object):
    # def __init__(self, file_name):
    #     self.wb = openpyxl.load_workbook(file_name)

    def __init__(self, file_name, sheet_name):
        self.wb = openpyxl.load_workbook(file_name)
        self.sh = self.wb[sheet_name]

    def read_data(self):
        row_data = list(self.sh.rows)[1:]
        one_data = []
        all_data = []
        symbol = 0
        for data in row_data:
            # 数据处理
            for elem in data:
                if symbol % 6 == 0:  # 学号
                    one_data.append(str(elem.value))
                elif symbol % 6 == 2:  # 成绩
                    one_data.append(float(elem.value))
                else:
                    one_data.append(elem.value)
                symbol += 1
            all_data.append(one_data)
            one_data = []
            # print(data.value, end=",")
        return all_data


if __name__ == '__main__':
    r = MyReadExcel('grade.xlsx', 'sheet1')
    data1 = r.read_data()
    for data in data1:
        print(data)

