# 北京卫健委数据爬取
import requests
'''
requests是使用Apache2 licensed 许可证的HTTP库。
Request
  支持HTTP连接保持和连接池，
  支持使用cookie保持会话，
  支持文件上传，
  支持自动响应内容的编码，
  支持国际化的URL和POST数据自动编码。
在python内置模块的基础上进行了高度的封装，从而使得python进行网络请求时，变得人性化，
使用Requests可以轻而易举的完成浏览器可有的任何操作。
requests会自动实现持久连接keep-alive。
'''
import re
'''
re模块是python独有的匹配字符串的模块，该模块中提供的很多功能是基于正则表达式实现的。
'''

url = "http://wjw.beijing.gov.cn/xwzx_20031/wnxw/202007/t20200706_1939095.html"

Headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Mobile Safari/537.36'}

'''
完整api接口：requests.get(url,params=params,headers=headers)
* url为基准的url地址，不包含查询参数
* 该方法会自动对params字典编码,然后和url拼接
一、简介的请求
requests.get('https://github.com/MysticalGuest')    # 最基本的不带参数的get请求
更多其他请求：
  requests.get(url)                                 # GET请求
  requests.post(url)                                # POST请求
  requests.put(url)                                 # PUT请求
  requests.delete(url)                              # DELETE请求
  requests.head(url)                                # HEAD请求
  requests.options(url)                             # OPTIONS请求
二、为url传递参数
查询参数-params是什么？
1.参数类型
  字典,字典中键值对作为查询参数，值为None的键不会被添加到url中
2.使用方法
  比如我们要访问百度，查询python，出现的url如下：
https://www.baidu.com/s?tn=59044660_hao_pg&isource=infinity&iname=baidu&itype=web&ie=utf-8&wd=python
get请求的形式：
geturl = https://www.baidu.com/s?
params = {
  'tn': '59044660_hao_pg',
  'isource': 'infinity',
  'iname': 'baidu',
  'itype': 'web',
  'ie': 'utf-8',
  'wd': 'python'
}
# 自动对params进行编码,然后自动和url进行拼接,去发请求
r = requests.get(url, params=params, headers=headers)
三、响应的内容
r.encoding                     #获取当前的编码
r.encoding = 'utf-8'           #设置编码
r.text                         #以encoding解析返回内容。字符串方式的响应体，会自动根据响应头部的字符编码进行解码。
r.content                      #以字节形式（二进制）返回。字节方式的响应体，会自动为你解码 gzip 和 deflate 压缩。
r.headers                      #以字典对象存储服务器响应头，但是这个字典比较特殊，字典键不区分大小写，若键不存在则返回None
r.status_code                  #响应状态码
r.raw                          #返回原始响应体，也就是 urllib 的 response 对象，使用 r.raw.read()   
r.ok                           # 查看r.ok的布尔值便可以知道是否登陆成功
#*特殊方法*#
r.json()                       #Requests中内置的JSON解码器，以json形式返回,前提返回的内容确保是json格式的，不然解析出错会抛异常
r.raise_for_status()           #失败请求(非200响应)抛出异常
'''
# 无参get请求
res = requests.get(url, headers=Headers)
print("状态码： ", res.status_code)

Content = res.text
print("Content: \n", Content)

Patt = '<div class="view TRS_UEDITOR trs_paper_default trs_web"><p>(.*?)</p></div>'
'''
re.search(pattern，string，flags = 0)
* pattern : 正则中的模式字符串。
* string : 要被查找替换的原始字符串。
* flags : 标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。
方法扫描整个字符串，并返回第一个成功的匹配。如果匹配失败，则返回None。
group(num) 或 groups() 匹配对象函数来获取匹配表达式。

re.I(re.IGNORECASE)
使匹配对大小写不敏感，执行不区分大小写的匹配；类似的表达式也[A-Z]将匹配小写字母。
re.M(re.MULTILINE)
多行匹配，影响 ^ 和 $
'''
MatchRes = re.search(Patt, Content, re.M | re.I)
# 得到每日的疫情数据信息
Info = MatchRes.group(1)
# Info = MatchRes.groups()
print("Info: \n", Info)


def SearchNum(info, patt):
    # 在info中使用模板patt来查找数据
    r = re.search(patt, info)
    if r:
        return r.group(1)
    else:
        return '0'


Confirm = SearchNum(Info, r'确诊病例(\d)例')
No_asymptomatic = SearchNum(Info, r'无症状感染者(\d)例')
Suspect = SearchNum(Info, r'疑似病例(\d)例')
Heal = SearchNum(Info, r'治愈出院病例(\d)例')
print("Confirm: {}, No Asymptomatic: {} ,Suspect: {}, Heal: {}".format(Confirm, No_asymptomatic, Suspect, Heal))

Date = re.search(r'(\d)月(\d)日', Info)
print("Date: ", Date.groups())

NowDate = "{}-{}-{}".format(2020, Date.group(1), Date.group(2))
print("NowDate: \n", NowDate)

today = {'date': NowDate, 'confirm': Confirm, 'suspect': Suspect, 'heal': Heal, 'No Asymptomatic': No_asymptomatic}
print("today: \n", today)


def GetInfo(def_url):
    #  得到指定日期的各项数据
    r = requests.get(def_url, headers=Headers)
    if r.status_code == 200:
        text = r.text

        patt = '<div class="view TRS_UEDITOR trs_paper_default trs_web"><p>(.*?)</p></div>'
        match_res = re.search(patt, text, re.M | re.I)
        if match_res:
            info = match_res.group(1)

            confirm = SearchNum(info, r'确诊病例(\d)例')
            no_asymptomatic = SearchNum(info, r'无症状感染者(\d)例')
            suspect = SearchNum(info, r'疑似病例(\d)例')
            heal = SearchNum(info, r'治愈出院病例(\d)例')
            date = re.search(r'(\d)月(\d)日', info)
            now_date = "{}-{}-{}".format(2020, date.group(1), date.group(2))

            def_today = {'date': now_date, 'confirm': confirm, 'suspect': suspect, 'heal': heal,
                         'no_asymptomatic': no_asymptomatic}
            return def_today
        else:
            return {}
    else:
        return {}


d1 = GetInfo("http://wjw.beijing.gov.cn/xwzx_20031/wnxw/202007/t20200706_1939095.html")
print("d1: \n", d1)

d2 = GetInfo("http://wjw.beijing.gov.cn/xwzx_20031/wnxw/202007/t20200705_1938961.html")
print("d2: \n", d2)
