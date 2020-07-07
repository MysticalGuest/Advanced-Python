# 北京卫健委数据爬取
import requests
import re

url = "http://wjw.beijing.gov.cn/xwzx_20031/wnxw/202007/t20200706_1939095.html"

Headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Mobile Safari/537.36'}

res = requests.get(url, headers=Headers)

print("状态码： ", res.status_code)

# 得到所需要的网页的内容
Content = res.text

print("Content: \n", Content)

Patt = '<div class="view TRS_UEDITOR trs_paper_default trs_web"><p>(.*?)</p></div>'
MatchRes = re.search(Patt, Content, re.M | re.I)

# 得到每日的疫情数据信息
Info = MatchRes.group(1)

print("Info: \n", Info)


def SearchNum(Info, Patt):
    # 在Info中使用模板Patt来查找数据
    res = re.search(Patt, Info)
    if res:
        return res.group(1)
    else:
        return '0'


Confirm = SearchNum(Info, '确诊病例(\d)例')
NoSympot = SearchNum(Info, '无症状感染者(\d)例')
suspect = SearchNum(Info, '疑似病例(\d)例')
Heal = SearchNum(Info, '治愈出院病例(\d)例')
Date = re.search('(\d)月(\d)日', Info)
NowDate = "{}-{}-{}".format(2020, Date.group(1), Date.group(2))

print("NowDate: \n", NowDate)

today = {'date': NowDate, 'confirm': Confirm, 'suspect': suspect, 'heal': Heal, 'noSympot': NoSympot}

print("today: \n", today)


def GetInfo(url):
    #  得到指定日期的各项数据
    res = requests.get(url, headers=Headers)
    if res.status_code == 200:
        Content = res.text

        Patt = '<div class="view TRS_UEDITOR trs_paper_default trs_web"><p>(.*?)</p></div>'
        MatchRes = re.search(Patt, Content, re.M | re.I)
        if MatchRes:
            Info = MatchRes.group(1)

            Confirm = SearchNum(Info, '确诊病例(\d)例')
            NoSympot = SearchNum(Info, '无症状感染者(\d)例')
            suspect = SearchNum(Info, '疑似病例(\d)例')
            Heal = SearchNum(Info, '治愈出院病例(\d)例')
            Date = re.search('(\d)月(\d)日', Info)
            NowDate = "{}-{}-{}".format(2020, Date.group(1), Date.group(2))

            today = {'date': NowDate, 'confirm': Confirm, 'suspect': suspect, 'heal': Heal, 'noSympot': NoSympot}
            return today
        else:
            return {}
    else:
        return {}


d1 = GetInfo("http://wjw.beijing.gov.cn/xwzx_20031/wnxw/202007/t20200706_1939095.html")

print("d1: \n", d1)

d2 = GetInfo("http://wjw.beijing.gov.cn/xwzx_20031/wnxw/202007/t20200705_1938961.html")

print("d2: \n", d2)