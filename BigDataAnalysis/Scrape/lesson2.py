# 网易疫情数据爬取
import requests
import json
import pandas as pd

# url = "https://wp.m.163.com/163/page/news/virus_report/index.html?_nw_=1&_anw_=1"
url = "https://c.m.163.com/ug/api/wuhan/app/data/list-by-area-code?areaCode=420000&t=1594002847773"

Headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Mobile Safari/537.36'}

res = requests.get(url, headers=Headers)

print("状态码： ", res.status_code)

print("", res.content)

data = json.loads(res.text)

print(type(data))

print(data.keys())

perday = data['data']
print(perday)

AllData = perday['list']
print(len(AllData))

print(AllData[1])

alldata = pd.DataFrame(AllData)[['date', 'today', 'total']]

print(alldata)

today_data = pd.DataFrame([item['today'] for item in AllData])
today_data.columns = ['当日_' + c for c in today_data.columns]

print(today_data)

total_data = pd.DataFrame([item['total'] for item in AllData])
total_data.columns = ['累计_' + c for c in total_data.columns]

print(total_data)

date_data = pd.DataFrame(AllData)['date']
print(date_data)

NewData = pd.concat([date_data, today_data, total_data], axis=1)

print(NewData)


def GetProvData(Url):
    res = requests.get(Url, headers=Headers)
    if res.status_code == 200:
        d = json.loads(res.text)
        perday = d['data']['list']
        return perday
    else:
        return []


pd.DataFrame(GetProvData(url))

# 获取全国数据
url = 'https://c.m.163.com/ug/api/wuhan/app/data/list-total?t=318800576081'

res = requests.get(url, headers=Headers)

print(res.status_code)

AllData = json.loads(res.text)

AllData = AllData['data']

# 取出所有国家的数据
AreaTreeData = AllData['areaTree']

# 查找中国的数据
for i in range(len(AreaTreeData)):
    if AreaTreeData[i]['name'] == '中国':
        print("i=", i)

# 取出中国的每个省份的行政编码并保存到字典中
ProvData = AreaTreeData[2]['children']

ProvDict = {}
for item in ProvData:
    ProvDict[item['id']] = item['name']

print(ProvDict)

print(AllData['chinaDayList'])

ChinaDayList = AllData['chinaDayList']

# 得到全国历史各日的疫情数据信息
Date_List = pd.DataFrame([c['date'] for c in ChinaDayList])
today_List = pd.DataFrame([c['today'] for c in ChinaDayList])
total_List = pd.DataFrame([c['total'] for c in ChinaDayList])

today_List.columns = ['当日_' + c for c in today_List.columns]
total_List.columns = ['累计_' + c for c in total_List.columns]

ChinaInfo = pd.concat([Date_List, today_List, total_List], axis=1)

ChinaInfo.head(20)

# 给出当日全国各省份的疫数据信息，放到字典中
ProvDay = {}
for prov in AreaTreeData[2]['children']:
    id = prov['id']
    name = prov['name']
    today = prov['today']
    total = prov['total']
    ProvDay[id] = {'name': name, 'today': today, 'total': total}

print(ProvDay)

p = pd.DataFrame(ProvDay)

print(p)

