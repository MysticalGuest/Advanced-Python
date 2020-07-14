import requests         # 加载网络请求库
import json             # 加载json数据分析
import pandas as pd     # 加载数据分析库
import time


'''
Covid-19疫情数据爬取

1.准备  
2.实时数据爬取  
  （1）国内实时数据爬取  
  （2）国外实时数据爬取  
3.历史数据爬取  
  （1）国内历史数据爬取  
  （2）国外历史数据爬取 
'''
# 1.准备
# 构造浏览器头信息
Headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Mobile Safari/537.36'}

# 所有的数据接口：list-total
AllUrl = "https://c.m.163.com/ug/api/wuhan/app/data/list-total?t=318816974928"

# 分地区数据接口：list-by-area-code，得到的是历史数据
ProvUrl = 'https://c.m.163.com/ug/api/wuhan/app/data/list-by-area-code?areaCode=610000'

# 2.实时数据爬取
# (1)国内实时数据爬取
res = requests.get(AllUrl, headers=Headers)

'''
返回的json数据格式：
|键名称|  说明|
|--|--|
|code|操作代码|
|data|返回的数据集|
|msg|操作状态|
|reqId|顺序号|
|timestamp|时间戳|

data项的结构：
|键名称|说明|
|--|--|
|areaTree|全世界每个国家的实时数据 |
|chinaDayList|中国历史数据 |
|chinaTotal| 中国实时数据 |
|lastUpdateTime| 国内数据更新时间 |
|overseaLastUpdateTime| 世界数据更新时间 |
'''

# 取回返回的所有数据
reqDict = json.loads(res.text)
AllData = reqDict['data']
# 得到全世界每个国家的实时数据
AllToday = AllData['areaTree']
# print("AllToday: \n", AllToday)
# 每个国家的实时数据是一个字典
ChinaData = AllToday[2]

'''
|键名称|说明|
|--|--|
|id|国家代码|
|name|国家名称|
|today|当天实时数据|
|total|历史累计数据|
|extData|扩展数据|
|children|数据子集|
|lastUpdateTime|更新时间 |
'''

print(ChinaData.keys())

# 得到国家代码信息对照表
ContryInfo = {}
ContryInfoName = {}
for item in AllToday:
    ContryInfo[item['id']] = item['name']
    ContryInfoName[item['name']] = item['id']


print("ContryInfo: \n", ContryInfo)
print("ContryInfoName: \n", ContryInfoName)



print("AllToday[1]: \n", AllToday[1])

today = pd.DataFrame([AllToday[1]['today']])
today.columns = ['today_'+i for i in today.columns]
print("today: \n", today)

total = pd.DataFrame([AllToday[1]['total']])
total.columns = ['total_'+i for i in total.columns]
print("total: \n", total)

contrydata = pd.concat([today, total], axis=1)
print("contrydata: \n", contrydata)


# (2)国外实时数据爬取
# 将每个国家的实时数据的提取
# data :是数据集，是列表，但是这个列表表示的是一个国家的信息
# info_list:是要处理数据项的名称
def get_data(data, info_list):
    info = pd.DataFrame([data])[info_list]

    today = pd.DataFrame([data['today']])
    today.columns = ['today_' + i for i in today.columns]

    total = pd.DataFrame([data['total']])
    total.columns = ['total_' + i for i in total.columns]

    return pd.concat([info, today, total], axis=1)


d = get_data(AllToday[2], ['id', 'name', 'lastUpdateTime'])
print("d: \n", d)
    
save_data(d,"中国实时数据")
# 保存各省的实时数据
# 取出各省的实时数据，这个实时数据在children子数据项下

AllProvData = AllToday[2]['children']

ProvData = get_data_all(AllProvData,['id','name','lastUpdateTime'])

save_data(ProvData,"各省实时数据")

# (2)国外实时数据爬取
# 1.取出指定国家的实时数据

# 构造国家信息代码表
ContryInfoNo = {}

for i in range(len(AllToday)):
    ContryInfoNo[AllToday[i]['name']] = i
cn = '波兰'
xh = ContryInfoNo[cn]

d = get_data(AllToday[xh], ['id','name','lastUpdateTime'])
print("d: \n", d)


# 2.列出所有国家的实时数据
# 将每个国家的实时数据的提取
# data :是数据集，是列表，列表中的每个元素都是一个国家的数据
# info_list:是要处理数据项的名称
def get_data_all(data, info_list):
    info = pd.DataFrame(data)[info_list]

    today = pd.DataFrame([i['today'] for i in data])
    today.columns = ['today_' + i for i in today.columns]

    total = pd.DataFrame([i['total'] for i in data])
    total.columns = ['total_' + i for i in total.columns]

    return pd.concat([info, today, total], axis=1)


d = get_data_all(AllToday, ['id', 'name', 'lastUpdateTime'])
print("d: \n", d)


# 保存数据到文件
# data:保存有数据的Pandas表
# name:数据文件的说明
def save_data(data,name):
    # 生成文件名
    filename = name +'_'+time.strftime('%Y-%m_%d',time.localtime(time.time()))+".csv"
    data.to_csv(filename,sep=",",encoding="utf-8-sig")
    print("文件保存完毕.")


save_data(d, "全球实时数据")

# 3.历史数据爬取
# （1）国内历史数据爬取
# 全国历史数据的爬取从chinaDayList数据项中取得

ChinaList = AllData['chinaDayList']   # 取出中国的所有的历史数据

# 取出每天的日期
dateList = pd.DataFrame([i['date'] for i in ChinaList])

# 取出全国所有数据中每天的实时数据，放到Pandas表中
ChinaList_today = pd.DataFrame([i['today'] for i in ChinaList])
ChinaList_today.columns = ['today_'+i for i in ChinaList_today.columns]

# 取出全国所有数据中每天的累计数据，放到Pandas表中
ChinaList_total = pd.DataFrame([i['total'] for i in ChinaList])
ChinaList_total.columns = ['today_'+i for i in ChinaList_total.columns]

#合并数据
ChinaListData = pd.concat([dateList,ChinaList_today,ChinaList_total],axis=1)
ChinaListData

save_data(ChinaListData,"全国历史数据")

# 保存各省的历史数据

Url= ProvUrl.format('420000')

req = requests.get(Url,headers=Headers)


ProvData = json.loads(req.text)['data']['list']

type(ProvData)

# 取出指定code的省份的历史数据
def get_prov_data(code):
    Url= ProvUrl.format(code)
    req = requests.get(Url,headers=Headers)
    if req.status_code == 200:
        ProvData = json.loads(req.text)['data']['list']

        provList = pd.DataFrame([i['date'] for i in ProvData])

        # 取出每天的实时数据，放到Pandas表中
        ProvList_today = pd.DataFrame([i['today'] for i in ProvData])
        ProvList_today.columns = ['today_'+i for i in ProvList_today.columns]

        # 取出每天的累计数据，放到Pandas表中
        ProvList_total = pd.DataFrame([i['total'] for i in ProvData])
        ProvList_total.columns = ['today_'+i for i in ProvList_total.columns]

        #合并数据
        provListData = pd.concat([provList,ProvList_today,ProvList_total],axis=1)
        return provListData
    else:
        print("网页访问不成功。")


prov = get_prov_data('420000')
save_data(prov, "湖北历史数据")


# 构造省份代码表，用省名称查找相应的行政代码

ProvInfo = AllData['areaTree'][2]['children']   # 取出了所有省份信息
ProvInfoNo = {}

for i in range(len(ProvInfo)):
    ProvInfoNo[ProvInfo[i]['name']] = ProvInfo[i]['id']

ProvInfoNo

n = '广东'
code = ProvInfoNo[n]
prov = get_prov_data(code)
save_data(prov, n + "历史数据")

# 遍历所有省份的历史数据
for key in ProvInfoNo.keys():
    code = ProvInfoNo[key]
    prov = get_prov_data(code)
    save_data(prov, n + "历史数据")

    time.sleep(10)  # 延迟

# （2）国外历史数据爬取

n = '意大利'
code = ContryInfoName[n]

prov = get_prov_data(code)
save_data(prov, n + "历史数据")

# 遍历所有国家的历史数据
for key in ContryInfoName.keys():
    code = ContryInfoName[key]
    prov = get_prov_data(code)
    save_data(prov, key + "历史数据")

    time.sleep(10)  # 延迟



