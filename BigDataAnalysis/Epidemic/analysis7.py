import numpy as np


def decimal_scale(data):
    data = data / 10 ** np.ceil(np.log10(data.max()))
    return data

decimal_scale(result.values[:, 1:])


def matplot_def(mat_data):
    import matplotlib.pyplot as plt
    plt.rcParams['font.sans-serif'] = 'SimHei'
    fig = plt.figure(figsize=(8, 6), dpi=60)
    values1 = mat_data.values
    #     values2 = decimal_scale(values1[:,1:])
    for i in range(mat_data.shape[1] - 1):
        y = decimal_scale(values1[:, i + 1])
        plt.plot(values1[:, 0], y)

    for j in range(mat_data.shape[0]):  # 将数据值，绘制到图表上
        plt.annotate(xy=(j, decimal_scale(values1[:, 1])[j]), s=values1[:, 1][j])

    plt.legend(['当日确诊', '境外输入', '累计确诊', '累计死亡', '累计治愈'])
    plt.show()

matplot_def(result)
result


def decimal_scale(data):
    data = data/10**np.ceil(np.log10(data.max()))
    return data
result
decimal_scale(result.values[:,1:])

import pandas as pd
file_name = open("中国_real_data.csv")
pd.read_csv(file_name)

area_url = "https://c.m.163.com/ug/api/wuhan/app/data/list-by-area-code?areaCode={}".format(42000)

# 测试代码1--输入省份名来拼接url
id_name_dic = {"湖北": 420000, "陕西": 610000}
sel_v3 = '湖北'
# id_name_dic['湖北']
use_url = "https://c.m.163.com/ug/api/wuhan/app/data/\
list-by-area-code?areaCode={}&t=1594602042681 ".format(id_name_dic[sel_v3])
print(use_url)


# 测试代码2--那些国家有州/省的实时数据

# 函数1：请求网页，并将信息转换为字典
def page_def(url1):
    import requests
    import json  # json的分析处理模块
    Headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

    url = url1
    res = requests.get(url, headers=Headers)  # 请求网页的命令
    print(res.status_code)  # 返回状态码
    data = json.loads(res.text)  # 转换为字典
    return data  # 字典数据


use_url = "https://c.m.163.com/ug/api/wuhan/app/data/list-total?t=318920407501"
data = page_def(use_url)
area_v1 = data['data']['areaTree']
name_dic = {}
for i in range(len(area_v1)):  # 判断那些国家有children
    if area_v1[i]['children']:
        name_dic[data['data']['areaTree'][i]['name']] = i
print(name_dic)