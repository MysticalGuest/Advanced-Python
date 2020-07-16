import requests
import json  # json的分析处理模块
import pandas as pd


# 函数1：请求网页，并将信息转换为字典
def page_def(url1):
    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Mobile Safari/537.36'}
    url = url1
    res = requests.get(url, headers=headers)  # 请求网页的命令
    print(res.status_code)  # 返回状态码
    data = json.loads(res.text)  # 转换为字典
    return data  # 字典数据


# 函数2：解析元素
def element_def(data, ele_v1):
    # perday = data['data']
    # AllData = perday['list']
    if ele_v1 == "children":
        area_v1 = data['data']['areaTree']
        name_dic = {}
        for i in range(len(area_v1)):  # 判断那些国家有children
            if area_v1[i]['children']:
                name_dic[data['data']['areaTree'][i]['name']] = i
        sel_name = input("请选择您要实时数据的国家：{}".format(name_dic.keys()))
        all_data = data['data']['areaTree'][name_dic[sel_name]]['children']
        # perday = data['data']
        # AllData = perday['list']
        return all_data, sel_name
    else:
        all_data = data['data'][ele_v1]
        return all_data


# 函数3：转换为dataframe形式的数据
def dataFrame_def(AllData, info_data):
    alldata = pd.DataFrame(AllData)[info_data]

    today_data = pd.DataFrame([item['today'] for item in AllData])  # 当天的数据
    today_data.columns = ['当日_' + c for c in today_data.columns]

    total_data = pd.DataFrame([item['total'] for item in AllData])  # 总的数据
    total_data.columns = ['累计_' + c for c in total_data.columns]

    if info_data[0] != "name":
        date_data = pd.DataFrame(AllData)['date']
    else:
        # id_data = pd.DataFrame(AllData)["id"]
        date_data = pd.DataFrame(AllData)["name"]
    #  date_data = pd.concat([id_data,name_data],axis=1)
    #  date_data = pd.DataFrame(AllData)['date']
    NewData = pd.concat([date_data, today_data, total_data], axis=1)  # 将today，total，info进行合并
    return NewData


# 采集历史数据
def hist_def():
    print("请输入您的选择".center(40, "="))
    print("您要采集什么历史数据：\n1.全国历史数据  \n2.中国各省 \n3.全球各国 \n0.退出  \n")
    sel_v2 = input("请输入您的选择：")
    if sel_v2 == "1":  # 中国历史数据
        use_url = "https://c.m.163.com/ug/api/wuhan/app/data/list-total?t=318920407501"
        ele_v1 = 'chinaDayList'
        sel_v3 = "中国"

    elif sel_v2 == "2":  # 中国各省历史数据
        sel_v3 = input("请输入您要获取的省份名称：")
        # 需要解决一个省名和省号对应关系的字典
        id_name_dic = {"湖北": 420000, "陕西": 610000}
        use_url = "https://c.m.163.com/ug/api/wuhan/app/data/list-by-area-code?areaCode={}&t=1594602042681 ".format(
            id_name_dic[sel_v3])
        ele_v1 = 'list'

    elif sel_v2 == "3":  # 全球各国历史数据
        use_url = "https://c.m.163.com/ug/api/wuhan/app/data/list-by-area-code?areaCode={}&t=1594602038577".format(66)
        ele_v1 = 'list'
        sel_v3 = "某国"

    page_data = page_def(use_url)  # 请求网页
    all_data = element_def(page_data, ele_v1)  # 解析元素
    df_data = dataFrame_def(all_data, ['date', 'today', 'total'])  # 转换为df
    df_data.to_csv("{}_hist_data.csv".format(sel_v3), encoding='gbk')
    return df_data


# 采集实时数据
def real_def():
    use_url = "https://c.m.163.com/ug/api/wuhan/app/data/list-total?t=318920407501"
    print("请输入您的选择".center(40, "="))
    print("您要采集什么实时数据：\n1.全球的实时数据\n2.各国州/省\n")
    sel_v2 = input('请输入您的选择：')
    if sel_v2 == "1":  # 全球各国的实时数据
        ele_v1 = 'areaTree'
        sel_v3 = "全球"
    elif sel_v2 == "2":  # 中国各省的实时数据
        ele_v1 = 'children'
        sel_v3 = '各国州-省'
    else:
        print("没有您要的数据")

    page_data = page_def(use_url)  # 请求网页
    all_data = element_def(page_data, ele_v1)  # 解析元素
    # print(all_data)
    if len(all_data) == 1:

        df_data = dataFrame_def(all_data, ['name', 'today', 'total'])  # 转换为df
    # df_data.to_csv("{}_real_data.csv".format(sel_v3),encoding='gbk')
    else:
        df_data = dataFrame_def(all_data[0], ['name', 'today', 'total'])  # 转换为df
    # df_data.to_csv("{}_real_data.csv".format(all_data[1]),encoding='gbk')
    return df_data


def main():
    print("请输入您的选择".center(40, "="))
    print("您要采集的数据是：\n1.历史数据  \n2.实时数据 \n0.退出  \n")
    sel_v1 = input("请输入您的选择：")
    if sel_v1 == "1":
        page_data = hist_def()

    elif sel_v1 == "2":
        page_data = real_def()

    elif sel_v1 == "0":
        import sys
        sys.exit("我先走了")
    else:
        print("没有您的选择")

    return page_data


if __name__ == "__main__":
    page_data = main()
page_data
