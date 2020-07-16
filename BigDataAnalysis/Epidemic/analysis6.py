import numpy as np


'''
功能说明：数据分析
作者：
时间：
版本：数据分析_v1.1

'''


# 标准化函数（小数定标标准化）
def decimal_scale(data):
    data = data/10**np.ceil(np.log10(data.max()))
    return data


# 绘图函数
def matplot_def(mat_data):
    import matplotlib.pyplot as plt
    plt.rcParams['font.sans-serif'] = 'SimHei'
    fig = plt.figure(figsize=(8, 6), dpi=60)
    values1 = mat_data.values
    # values2 = decimal_scale(values1[:,1:])
    for i in range(mat_data.shape[1] - 1):
        y = decimal_scale(values1[:, i + 1])
        plt.plot(values1[:, 0], y)
    for j in range(mat_data.shape[0]):  # 将数据值，绘制到图表上
        plt.annotate(xy=(j, decimal_scale(values1[:, 1])[j]), s=values1[:, 1][j])
    plt.xticks(rotation=30)
    plt.legend(['当日确诊', '境外输入', '累计确诊', '累计死亡', '累计治愈'])
    plt.show()


# 函数1：
def group_def():
    pass


# 函数2：描述性统计
def describe_def():
    pass


# 函数3：查找数据
def find_def(read_df):
    find_v1 = ''
    new_df1 = read_df.loc[:, ['id', 'name', '当日_confirm', '当日_dead', '当日_heal',
                              '当日_input', '累计_confirm', '累计_dead', '累计_heal',
                              '累计_input', '累计_newConfirm', '累计_newDead', '累计_newHeal', ]]
    # 查询累计确诊累计_confirm大于m的数据
    print("请输入您要查找数据的方式：1.累计确诊2.当日确诊")
    sel_v2 = input("请输入您的选择")
    if sel_v2 == "1":
        m = input("请输入您要查找的最少累计确诊数量")
        find_v1 = new_df1.loc[new_df1['累计_confirm'] > int(m), ['name', '当日_confirm',
                                                               '当日_input', '累计_confirm',
                                                               '累计_dead', '累计_heal']]
    # 查询当日确诊当日_confirm大于m的数据
    elif sel_v2 == "2":
        m = input("请输入您要查找的最少累计确诊数量")
        find_v1 = new_df1.loc[new_df1['当日_confirm'] > int(m), ['name', '当日_confirm',
                                                               '当日_input', '累计_confirm',
                                                               '累计_dead', '累计_heal']]
    matplot_def(find_v1)
    return find_v1


# 功能函数：打开文件
def read_def(file_name):
    import pandas as pd
    file = open(file_name, encoding="gbk")  # 解决文件名中，有中文文字的方法
    read_data = pd.read_csv(file)
    return read_data


# 主函数
def main():
    print("数据分析".center(40, "="))
    print("您可以打开的数据有：\n中国_real_data.csv\n全球_real_data.csv\n中国_hist_data.csv")
    sel_file = input("请输入要读取的数据文件名:")
    read_df = read_def(sel_file)
    anlyse_result = ''
    sel_v1 = input("请输入您的分析选择:\n1.查找数据\n2.描述性统计\n3.分组聚合")
    if sel_v1 == "1":
        anlyse_result = find_def(read_df)
    elif sel_v1 == "2":
        anlyse_result = describe_def()
    elif sel_v1 == "3":
        anlyse_result = group_def()
    return anlyse_result


if __name__ == "__main__":
    result = main()
    print("result: ", result)